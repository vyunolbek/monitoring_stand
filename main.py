import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
import os
import json
import difflib
import numpy as np
import cv2
import easyocr

class ImageEditor:
    def __init__(self, root, save_path):
        self.root = root
        self.root.title("Image Editor")

        self.save_path = save_path

        # Создаем холст для рисования
        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Создаем кнопку для загрузки изображения
        self.load_button = tk.Button(root, text="Выбрать изображение", command=self.load_image)
        self.load_button.pack(side=tk.TOP)

        # Создаем кнопку для сохранения координат квадратиков
        self.save_button = tk.Button(root, text="Сохранить координаты", command=self.save_coordinates)
        self.save_button.pack(side=tk.TOP)

        # Список для хранения данных о квадратиках (координаты, класс)
        self.rectangles_data = []

        # Переменные для хранения текущего изображения и его пути
        self.image_path = None
        self.original_image = None
        self.displayed_image = None
        self.ratio = None

        # Привязываем обработчики к событиям мыши
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

        self.check_button = tk.Button(root, text="Проверить", command=self.check_text)
        self.check_button.pack(side=tk.TOP)

        # Создаем кнопку для загрузки координат
        self.load_coords_button = tk.Button(root, text="Загрузить координаты", command=self.load_coordinates_for_check)
        self.load_coords_button.pack(side=tk.TOP)

        # Создаем кнопку для загрузки изображения для проверки
        self.load_image_button = tk.Button(root, text="Загрузить изображение", command=self.load_image_for_check)
        self.load_image_button.pack(side=tk.TOP)

        self.reader = easyocr.Reader(['en'])

    def load_coordinates_for_check(self):
        # Загрузить JSON с координатами для проверки
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                self.rectangles_data = json.load(f)
                print(self.rectangles_data)
            # Очистить холст и отрисовать изображение с координатами
            self.display_image()
            self.draw_saved_rectangles()

    def load_image_for_check(self):
        # Загрузить изображение для проверки
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.image_path = file_path
            self.original_image = Image.open(file_path)
            self.resize_image()
            self.display_image()
            self.draw_saved_rectangles()

    def check_text(self):
        # Проверяем текст на квадратах с использованием Tesseract OCR
        if self.image_path:
            for data in self.rectangles_data:
                coordinates = data["coordinates"]
                # region = self.original_image.crop(coordinates)
                region = np.array(self.original_image)[coordinates[1]:coordinates[1] + (coordinates[3] - coordinates[1]), coordinates[0]:coordinates[0] + (coordinates[2] - coordinates[0])]
                print(region)
                region = cv2.cvtColor(region, cv2.COLOR_BGR2RGB)
                #text = pytesseract.image_to_string(region, lang='eng')
                class_name = data["class"]
                cv2.imwrite(f'{coordinates}.png', region)

                if class_name == 'p':
                    avg_color_per_row = np.average(region, axis=0)
                    avg_color = np.average(avg_color_per_row, axis=0)
                    dist = np.linalg.norm(avg_color - data['color'])
                    percent = dist / np.sqrt(255 ** 2 + 255 ** 2 + 255 ** 2)
                    print(percent)
                    if percent < 0.08:
                        color = 'green'
                    else:
                        color = 'red'

                if class_name != 'p':
                    # Рисуем прямоугольник с соответствующим цветом
                    if difflib.SequenceMatcher(None, text, class_name).ratio() <= 0.5:
                        region = cv2.rotate(region, cv2.ROTATE_180)
                        text = self.reader.readtext(region)[0][1]
                        if difflib.SequenceMatcher(None, text, class_name).ratio() > 0.5:
                            color = 'green'
                        else:
                            color = 'red'
                    elif difflib.SequenceMatcher(None, text, class_name).ratio() > 0.5:
                        color = 'green'
                    else:
                        color = 'red'

                self.canvas.create_rectangle([i * self.ratio for i in coordinates], outline=color, width=2, tags="checked_rectangles")

                # Добавляем текст с классом
                self.canvas.create_text(
                    coordinates[0] * self.ratio, coordinates[1] * self.ratio, anchor=tk.SW, text=f"Class: {class_name}", fill=color, font=("Arial", 8)
                )

    def load_image(self):
        # Открываем диалоговое окно выбора файла
        file_path = filedialog.askopenfilename(filetypes=[("Изображения", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

        if file_path:
            # Загружаем изображение и обновляем холст
            self.image_path = file_path
            self.original_image = Image.open(file_path)
            self.resize_image()
            self.display_image()

            # Рисуем сохраненные квадратики
            self.draw_saved_rectangles()

    def resize_image(self):
        # Изменяем размер изображения для отображения его на холсте
        width, height = self.root.winfo_width(), self.root.winfo_height() - 120

        if width > 0 and height > 0:
            self.ratio = min(width / self.original_image.width, height / self.original_image.height)
            new_width = int(self.original_image.width * self.ratio)
            new_height = int(self.original_image.height * self.ratio)
            self.displayed_image = self.original_image.resize((new_width, new_height), Image.LANCZOS)

    def display_image(self):
        # Очищаем холст
        self.canvas.delete("all")

        # Преобразуем изображение в формат Tkinter
        tk_image = ImageTk.PhotoImage(self.displayed_image)

        # Отображаем изображение на холсте
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image, tags="image")
        self.canvas.image = tk_image

    def on_mouse_click(self, event):
        # Начинаем рисование при клике
        self.start_x, self.start_y = event.x, event.y

    def on_mouse_drag(self, event):
        # Рисуем временный прямоугольник при перемещении мыши (пока кнопка мыши нажата)
        self.canvas.delete("temp_rectangle")
        self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y, outline="red", width=2, tags="temp_rectangle"
        )

    def on_mouse_release(self, event):
        # Завершаем рисование при отпускании кнопки мыши
        end_x, end_y = event.x, event.y

        # Ограничиваем координаты
        start_x = max(0, min(self.start_x, self.displayed_image.width))
        start_y = max(0, min(self.start_y, self.displayed_image.height))
        end_x = max(0, min(end_x, self.displayed_image.width))
        end_y = max(0, min(end_y, self.displayed_image.height))

        # Пересчитываем координаты относительно исходного изображения
        ratio = self.original_image.width / self.displayed_image.width
        start_x = int(start_x * ratio)
        start_y = int(start_y * ratio)
        end_x = int(end_x * ratio)
        end_y = int(end_y * ratio)

        # Окно для ввода класса
        class_name = simpledialog.askstring("Input", "Enter class name for the rectangle:")

        if class_name != 'p':
            # Рисуем окончательный прямоугольник на исходном изображении
            self.canvas.create_rectangle(start_x / ratio, start_y / ratio, end_x / ratio, end_y / ratio, outline="red", width=2, tags="rectangles")

            # Добавляем данные о прямоугольнике в список
            self.rectangles_data.append({"coordinates": (start_x, start_y, end_x, end_y), "class": class_name})

            # Удаляем временный прямоугольник
            self.canvas.delete("temp_rectangle")

        elif class_name == 'p':
            region = np.array(self.original_image)[start_y:start_y + (end_y - start_y), start_x:start_x + (end_x - start_x)]
            region = cv2.cvtColor(region, cv2.COLOR_BGR2RGB)
            cv2.imwrite(f'test.png', region)

            avg_color_per_row = np.average(region, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            
            self.canvas.create_rectangle(start_x / ratio, start_y / ratio, end_x / ratio, end_y / ratio, outline="red", width=2, tags="rectangles")

            # Добавляем данные о прямоугольнике в список
            self.rectangles_data.append({"coordinates": (start_x, start_y, end_x, end_y), "class": class_name, "color": avg_color.tolist()})

            # Удаляем временный прямоугольник
            self.canvas.delete("temp_rectangle")

    def draw_saved_rectangles(self):
        # Рисуем сохраненные квадратики на холсте
        
        ratio = self.original_image.width / self.displayed_image.width

        for data in self.rectangles_data:
            coordinates = data['coordinates']
            class_name = data["class"]
            self.canvas.create_rectangle([i / ratio for i in data["coordinates"]], outline="red", width=2, tags="rectangles")
            self.canvas.create_text(
                coordinates[0] / ratio, coordinates[1] / ratio, anchor=tk.SW, text=f"Class: {class_name}", fill="red", font=("Arial", 8)
            )

    def save_coordinates(self):
        # Выводим координаты и классы в консоль (вы можете изменить эту часть для сохранения в файл и т.д.)
        print("Координаты квадратиков:")
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)

        with open(os.path.join(self.save_path, 'coords.json'), 'w') as f:
            json.dump(self.rectangles_data, f)
            for data in self.rectangles_data:
                print("Coordinates:", data["coordinates"])
                print("Class:", data["class"])
                print()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditor(root, './saved')
    root.geometry("800x600")
    root.mainloop()

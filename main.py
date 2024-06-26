from tkinter import *
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import json
import difflib
import numpy as np
import cv2
import pytesseract

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=21,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d ! "
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

class ImageEditor:
    def __init__(self, root, save_path):
        self.root = root
        self.root.title("Image Editor")
        self.save_path = save_path

        # Создаем холст для рисования
        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Список для хранения данных о квадратиках (координаты, класс)
        self.rectangles_data = []

        # Переменные для хранения текущего изображения и его пути
        self.image_path = None
        self.original_image = None
        self.displayed_image = None
        self.wratio = float
        self.hratio = float

        # Привязываем обработчики к событиям мыши
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

        self.check_button = tk.Button(root, text="Проверить", command=self.check_text)
        self.check_button.pack(side=tk.TOP)

        # Создаем кнопку для сохранения координат квадратиков
        self.save_button = tk.Button(root, text="Сохранить координаты", command=self.save_coordinates)
        self.save_button.pack(side=tk.TOP)

        # Создаем кнопку для загрузки координат
        self.load_coords_button = tk.Button(root, text="Загрузить координаты", command=self.load_coordinates_for_check)
        self.load_coords_button.pack(side=tk.TOP)

        self.load_coords_button = tk.Button(root, text="Очистить координаты", command=self.clear_coords)
        self.load_coords_button.pack(side=tk.TOP)

        # Создаем кнопку для загрузки изображения для проверки
        self.load_image_button = tk.Button(root, text="Загрузить изображение", command=self.load_image_for_check)
        self.load_image_button.pack(side=tk.TOP)

        self.load_image_button = tk.Button(root, text="Включить видео", command=self.get_cap)
        self.load_image_button.pack(side=tk.TOP)

        self.cap = cv2.VideoCapture(0)

        self.load_image_button = tk.Button(root, text="Выключить видео", command=self.stop_cap)
        self.load_image_button.pack(side=tk.TOP)

        self.json_combobox = ttk.Combobox(root)
        self.json_combobox.pack(side=tk.TOP)
        self.json_combobox.bind("<Button-1>", self.load_json_files)
        self.json_combobox.bind("<<ComboboxSelected>>", self.on_json_selected)

        self.video = True

        self.is_file = False
    
    def load_json_files(self, event):
        # Получаем список JSON файлов из указанной папки
        json_files = [f for f in os.listdir(self.save_path) if f.endswith('.json')]
        self.json_combobox['values'] = json_files

    def on_json_selected(self, event):
        # Обработчик выбора JSON файла из выпадающего списка
        selected_file = self.json_combobox.get()
        file_path = os.path.join(self.save_path, selected_file)
        with open(file_path, 'r') as f:
            self.rectangles_data = json.load(f)
            print(self.rectangles_data)
        self.display_image()
        self.draw_saved_rectangles()

    def is_clicked(self):
        self.changes += 1

    def clear_coords(self):
        self.rectangles_data.clear()
        self.canvas.delete('all')
        self.display_image()
        self.draw_saved_rectangles()

    def get_cap(self):
        self.is_file = False
        self.video = True
        while True and self.video:
            _, frame = self.cap.read()
            if _:
                frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                self.original_image = frame
                self.resize_image()
                self.display_image()

                # Рисуем сохраненные квадратики
                self.draw_saved_rectangles()
                self.root.update()
            else:
                break
    
    def stop_cap(self):
        self.video = False

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
        self.is_file = True
        # Загрузить изображение для проверки
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            self.original_image = Image.open(file_path)
            self.resize_image()
            self.display_image()
            self.draw_saved_rectangles()

    def check_text(self):
        # Проверяем текст на квадратах с использованием Tesseract OCR
        if self.image_path or type(self.original_image) == np.ndarray or type(self.original_image) == Image.Image:
            self.canvas.delete("checked_rectangles")
            for j, data in enumerate(self.rectangles_data):
                coordinates = list(map(int, data["coordinates"]))
                region = np.array(self.original_image)[coordinates[1]:coordinates[1] + (coordinates[3] - coordinates[1]), coordinates[0]:coordinates[0] + (coordinates[2] - coordinates[0])]
                region = cv2.cvtColor(region, cv2.COLOR_BGR2RGB)
                cv2.imwrite('region.png', region)
                class_name = data["class"]

                if class_name == 'None':
                    continue

                if class_name.split(' ')[0] == 'p':
                    avg_color_per_row = np.average(region, axis=0)
                    avg_color = np.average(avg_color_per_row, axis=0)
                    print(data)
                    for i in data['color']:
                        dist = np.linalg.norm(avg_color - i)
                        percent = dist / np.sqrt(255 ** 2 + 255 ** 2 + 255 ** 2)
                        if percent < 0.08:
                            color = 'green'
                            break
                        else:
                            color = 'red'

                if class_name != 'p':
                    region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
                    ret, thresh = cv2.threshold(region, 127, 255, cv2.THRESH_BINARY)
                    kernel = np.ones((3, 3), np.uint8)
                    region = cv2.erode(thresh, kernel, iterations=1)
                    text = pytesseract.image_to_string(Image.fromarray(region))
                    # Рисуем прямоугольник с соответствующим цветом
                    if len(text) != 0:
                        for i in class_name.split("|"):
                            if difflib.SequenceMatcher(None, text, i).ratio() <= 0.5:
                                region = cv2.rotate(region, cv2.ROTATE_180)
                                text = pytesseract.image_to_string(Image.fromarray(region))
                                if difflib.SequenceMatcher(None, text, i).ratio() > 0.5:
                                    color = 'green'
                                    break
                                else:
                                    color = 'red'
                            elif difflib.SequenceMatcher(None, text, i).ratio() > 0.5:
                                color = 'green'
                                break
                            else:
                                color = 'red'
                        else:
                            color = 'red'

                self.canvas.delete("red")
                self.rectangles_data[j]['status'] = color
                self.canvas.create_rectangle([coordinates[0] / self.wratio, coordinates[1] / self.hratio, coordinates[2] / self.wratio, coordinates[3] / self.hratio], outline=self.rectangles_data[j]['status'], width=4, tags="checked_rectangles")
                # Добавляем текст с классом
                self.canvas.create_text(
                    coordinates[0] / self.wratio, coordinates[1] / self.hratio, anchor=tk.SW, text=f"Class: {class_name}", fill=self.rectangles_data[j]['status'], font=("Arial", 8)
                )

    def load_image(self):
        # Открываем диалоговое окно выбора файла
        file_path = filedialog.askopenfilename(filetypes=[("Изображения", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.is_file = True
            # Загружаем изображение и обновляем холст
            self.image_path = file_path
            self.original_image = Image.open(file_path)
            self.resize_image()
            self.display_image()

            # Рисуем сохраненные квадратики
            self.draw_saved_rectangles()

    def resize_image(self):
        # Изменяем размер изображения для отображения его на холсте
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()

        if width > 0 and height > 0:
            self.wratio = self.original_image.width / width
            self.hratio = self.original_image.height / height
            self.displayed_image = self.original_image.resize((width, height), Image.LANCZOS)

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
        if not self.is_file:
            self.rectangles_data.append({"coordinates": (self.start_x * self.wratio, self.start_y * self.hratio, event.x * self.wratio, event.y * self.hratio), "class": "None", 'status': 'red', "displayed_image": [self.displayed_image.width, self.displayed_image.height]})
        else:
            pass

    def on_mouse_drag(self, event):
        if self.is_file:
            self.canvas.delete('temp_rectangle')
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline='red', width=2, tags='temp_rectangle')
        else:
            self.rectangles_data.pop()
            self.rectangles_data.append({"coordinates": (self.start_x * self.wratio, self.start_y * self.hratio, event.x * self.wratio, event.y * self.hratio), "class": "None", 'status': 'red', "displayed_image": [self.displayed_image.width, self.displayed_image.height]})

    def on_mouse_release(self, event):
        if not self.is_file:
            self.rectangles_data.pop()
        # Завершаем рисование при отпускании кнопки мыши
        end_x, end_y = event.x, event.y

        # Ограничиваем координаты
        start_x = max(0, min(self.start_x, self.canvas.winfo_width()))
        start_y = max(0, min(self.start_y, self.canvas.winfo_height()))
        end_x = max(0, min(end_x, self.canvas.winfo_width()))
        end_y = max(0, min(end_y, self.canvas.winfo_height()))

        # Пересчитываем координаты относительно исходного изображения
        start_x = int(start_x * self.wratio)
        start_y = int(start_y * self.hratio)
        end_x = int(end_x * self.wratio)
        end_y = int(end_y * self.hratio)

        # Окно для ввода класса
        class_name = simpledialog.askstring("Input", "Enter class name for the rectangle:")
        if type(class_name) == type(None):
            self.canvas.delete('temp_rectangle')
            self.rectangles_data.pop()
            self.draw_saved_rectangles()
            pass
        elif class_name.split(' ')[0] != 'p':

            # Рисуем окончательный прямоугольник на исходном изображении
            # self.canvas.create_rectangle(start_x / ratio, start_y / ratio, end_x / ratio, end_y / ratio, outline="red", width=2, tags=["rectangles", "red"])

            # Добавляем данные о прямоугольнике в список

            self.rectangles_data.append({"coordinates": (start_x, start_y, end_x, end_y), "class": class_name, 'status': 'red', "displayed_image": [self.displayed_image.width, self.displayed_image.height]})
            # Удаляем временный прямоугольник
            self.canvas.delete("temp_rectangle")
            self.canvas.delete("temp_rectangles")
            self.draw_saved_rectangles()

        elif class_name.split(' ')[0] == 'p':
            colors = []
            count_of_colors = class_name.split(' ')[-1]
            print(count_of_colors)
            self.stop_cap()
            for _ in range(int(count_of_colors)):
                f, frame = self.cap.read()
                frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                self.original_image = frame
                self.resize_image()
                self.display_image()
                self.draw_saved_rectangles()
                self.root.update()

                region = np.array(self.original_image)[start_y:start_y + (end_y - start_y), start_x:start_x + (end_x - start_x)]

                region = cv2.cvtColor(region, cv2.COLOR_BGR2RGB)

                avg_color_per_row = np.average(region, axis=0)
                avg_color = np.average(avg_color_per_row, axis=0)
                colors.append(avg_color.tolist())
                if _ != int(count_of_colors) - 1:
                    messagebox.askyesno('Подтверждение', 'Поменяли?')
            
            # self.canvas.create_rectangle(start_x / ratio, start_y / ratio, end_x / ratio, end_y / ratio, outline="red", width=2, tags=["rectangles", "red"])
            self.rectangles_data.append({"coordinates": (start_x, start_y, end_x, end_y), "class": class_name, "color": colors, "status": "red", "displayed_image": [self.displayed_image.width, self.displayed_image.height]})

            self.get_cap()
            # Добавляем данные о прямоугольнике в список

            # Удаляем временный прямоугольник
            self.canvas.delete("temp_rectangle")
            self.canvas.delete("temp_rectangles")
        
            self.draw_saved_rectangles()
        
        elif class_name != 'p':

            # Рисуем окончательный прямоугольник на исходном изображении
            # self.canvas.create_rectangle(start_x / ratio, start_y / ratio, end_x / ratio, end_y / ratio, outline="red", width=2, tags=["rectangles", "red"])

            # Добавляем данные о прямоугольнике в список

            self.rectangles_data.append({"coordinates": (start_x, start_y, end_x, end_y), "class": class_name, 'status': 'red', "displayed_image": [self.displayed_image.width, self.displayed_image.height]})
            # Удаляем временный прямоугольник
            self.canvas.delete("temp_rectangle")
            self.canvas.delete("temp_rectangles")
            self.draw_saved_rectangles()

    def draw_saved_rectangles(self):
        # Рисуем сохраненные квадратики на холсте

        for j, data in enumerate(self.rectangles_data):
            coordinates = list(data['coordinates'])
            class_name = data["class"]
            color = self.rectangles_data[j]['status']
            if class_name == 'None' and color == 'red':
                self.canvas.create_rectangle([coordinates[0] / self.wratio, coordinates[1] / self.hratio, coordinates[2] / self.wratio, coordinates[3] / self.hratio], outline=color, width=2, tags=["temp_rectangles", "red"])
                continue
            elif color == 'red':
                self.canvas.create_rectangle([coordinates[0] / self.wratio, coordinates[1] / self.hratio, coordinates[2] / self.wratio, coordinates[3] / self.hratio], outline=color, width=2, tags=["rectangles", 'red'])
                #self.canvas.create_rectangle([coordinates[0], coordinates[2], coordinates[1], coordinates[3]], outline=color, width=2, tags=["rectangles", 'red'])
                self.canvas.create_text(
                coordinates[0] / self.wratio, coordinates[1] / self.hratio, anchor=tk.SW, text=f"Class: {class_name}", fill=color, font=("Arial", 8)
                )
            else:
                self.canvas.create_rectangle([coordinates[0] / self.wratio, coordinates[1] / self.hratio, coordinates[2] / self.wratio, coordinates[3] / self.hratio], outline=color, width=4, tags=["rectangles", 'green'])
                self.canvas.create_text(
                    coordinates[0] / self.wratio, coordinates[1] / self.hratio, anchor=tk.SW, text=f"Class: {class_name}", fill=color, font=("Arial", 8)
                )

    def save_coordinates(self):
        # Выводим координаты и классы в консоль (вы можете изменить эту часть для сохранения в файл и т.д.)
        file_name = simpledialog.askstring("Input", "Enter the preset name:")
        print("Координаты квадратиков:")
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)
        
        for i, data in enumerate(self.rectangles_data):
            if data['class'] == 'None':
                self.rectangles_data.pop(i)

        with open(os.path.join(self.save_path, f'{file_name}.json'), 'w') as f:
            json.dump(self.rectangles_data, f)
            for data in self.rectangles_data:
                print("Coordinates:", data["coordinates"])
                print("Class:", data["class"])
                print()

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    app = ImageEditor(root, './saved')
    root.mainloop()

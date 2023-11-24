import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")

        # Создаем холст для рисования
        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Создаем кнопку для загрузки изображения
        self.load_button = tk.Button(root, text="Выбрать изображение", command=self.load_image)
        self.load_button.pack(side=tk.TOP)

        # Создаем кнопку для сохранения координат квадратиков
        self.save_button = tk.Button(root, text="Сохранить координаты", command=self.save_coordinates)
        self.save_button.pack(side=tk.TOP)

        # Список для хранения координат квадратиков
        self.coordinates = []

        # Переменные для хранения текущего изображения и его пути
        self.image_path = None
        self.original_image = None
        self.displayed_image = None

        # Привязываем обработчики к событиям мыши
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

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
        width, height = self.root.winfo_width(), self.root.winfo_height()

        if width > 0 and height > 0:
            ratio_w = width / self.original_image.width
            ratio_h = height / self.original_image.height
            new_width = int(self.original_image.width * ratio_w)
            new_height = int(self.original_image.height * ratio_h)
            self.displayed_image = self.original_image.resize((new_width, new_height), Image.ANTIALIAS)

    def display_image(self):
        # Очищаем холст
        self.canvas.delete("all")

        # Преобразуем изображение в формат Tkinter
        tk_image = ImageTk.PhotoImage(self.displayed_image)

        # Отображаем изображение на холсте
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image = tk_image

    def on_mouse_click(self, event):
        # Начинаем рисование при клике
        self.start_x, self.start_y = event.x, event.y

    def on_mouse_drag(self, event):
        # Рисуем временный прямоугольник при перемещении мыши (пока кнопка мыши нажата)
        self.canvas.delete("temp_rectangle")
        self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="red", width=2, tags="temp_rectangle")

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

        # Рисуем окончательный прямоугольник на исходном изображении
        self.canvas.create_rectangle(start_x, start_y, end_x, end_y, outline="red", width=2)

        # Добавляем координаты в список
        self.coordinates.append((start_x, start_y, end_x, end_y))

    def draw_saved_rectangles(self):
        # Рисуем сохраненные квадратики на холсте
        for coord in self.coordinates:
            self.canvas.create_rectangle(coord, outline="red", width=2)

    def save_coordinates(self):
        # Выводим координаты в консоль (вы можете изменить эту часть для сохранения в файл и т.д.)
        print("Координаты квадратиков:")
        for coord in self.coordinates:
            print(coord)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditor(root)
    root.geometry("800x600")
    root.mainloop()

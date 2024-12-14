# Модуль для работы с графическим интерфейсом
# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox

class FileRenamerApp:
    def __init__(self, master, rename_callback):
        """Инициализация интерфейса приложения"""
        self.master = master
        self.master.title("File Renamer")  # Устанавливаем заголовок окна
        self.master.geometry("600x300")  # Устанавливаем размеры окна
        self.rename_callback = rename_callback  # Колбэк для обработки переименования файлов

        # Переменная для хранения пути к папке
        self.folder_path = tk.StringVar()

        # Элементы интерфейса для выбора папки
        tk.Label(master, text="Выберите папку:").pack(anchor='w', padx=10, pady=5)  # Надпись для выбора папки
        self.folder_entry = tk.Entry(master, textvariable=self.folder_path, width=50)  # Поле для отображения пути к папке
        self.folder_entry.pack(anchor='w', padx=10)
        tk.Button(master, text="Обзор", command=self.browse_folder).pack(anchor='w', padx=10, pady=5)  # Кнопка "Обзор" для вызова диалога выбора папки

        # Элементы интерфейса для ввода маски-шаблона
        tk.Label(master, text="Введите маску-шаблон имени файлов:").pack(anchor='w', padx=10, pady=5)  # Надпись для маски
        self.mask_entry = tk.Entry(master, width=50)  # Поле для ввода маски
        self.mask_entry.pack(anchor='w', padx=10)

        # Поля для ввода начального и конечного числа
        tk.Label(master, text="Введите начальное число:").pack(anchor='w', padx=10, pady=5)  # Надпись для начального числа
        self.start_number_entry = tk.Entry(master, width=20)  # Поле для ввода начального числа
        self.start_number_entry.pack(anchor='w', padx=10)

        tk.Label(master, text="Введите конечное число:").pack(anchor='w', padx=10, pady=5)  # Надпись для конечного числа
        self.end_number_entry = tk.Entry(master, width=20)  # Поле для ввода конечного числа
        self.end_number_entry.pack(anchor='w', padx=10)

        # Кнопка для запуска процесса переименования
        tk.Button(master, text="Переименовать", command=self.rename_files).pack(anchor='w', padx=10, pady=10)  # Кнопка "Переименовать"

    def browse_folder(self):
        """Открывает диалоговое окно для выбора папки и сохраняет путь"""
        folder_selected = filedialog.askdirectory()  # Показываем диалог выбора папки
        if folder_selected:  # Если папка выбрана, сохраняем её путь
            self.folder_path.set(folder_selected)

    def rename_files(self):
        """Передает введенные данные в колбэк для переименования файлов"""
        folder = self.folder_path.get()  # Получаем путь к папке
        mask = self.mask_entry.get()  # Получаем введенную маску
        start_number = self.start_number_entry.get()  # Получаем начальное число
        end_number = self.end_number_entry.get()  # Получаем конечное число
        self.rename_callback(folder, mask, start_number, end_number)  # Вызываем колбэк с переданными данными
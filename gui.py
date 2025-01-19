# gui.py

"""
gui.py - Модуль, содержащий описание пользовательского интерфейса программы.
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip
from config import NUMBER_PLACEHOLDER, NAME_FILE_PLACEHOLDER

class FileRenamerApp:
    """
    Класс, отвечающий за создание пользовательского интерфейса приложения.
    """
    def __init__(self, master, rename_callback):
        """
        Инициализация интерфейса приложения.
        
        :param master: Главное окно приложения
        :param rename_callback: Колбэк для обработки данных
        """
        # Сохраняем ссылку на главное окно и колбэк
        self.master = master
        self.rename_callback = rename_callback

        # Устанавливаем заголовок окна и его размеры
        self.master.title("File Renamer")
        self.master.geometry("600x400")

        # Увеличиваем шрифт для всех элементов интерфейса
        self.master.option_add("*Font", "Helvetica 14")

        # Переменная для хранения пути к выбранной папке
        self.folder_path = tk.StringVar()

        # Создаем элементы интерфейса для выбора папки
        tk.Label(master, text="Выберите папку:").pack(anchor='w', padx=10, pady=5)
        self.folder_entry = tk.Entry(master, textvariable=self.folder_path, width=50)
        self.folder_entry.pack(anchor='w', padx=10)
        tk.Button(master, text="Обзор", command=self.browse_folder).pack(anchor='w', padx=10, pady=5)

        # Создаем элементы для ввода маски-шаблона
        tk.Label(master, text=f"Введите маску-шаблон имени файлов (например, {NUMBER_PLACEHOLDER}.{NAME_FILE_PLACEHOLDER}.txt):").pack(anchor='w', padx=10, pady=5)
        self.mask_entry = tk.Entry(master, width=50)
        self.mask_entry.pack(anchor='w', padx=10)
        tk.Button(master, text="Вставить из буфера обмена", command=self.paste_mask).pack(anchor='w', padx=10, pady=5)

        # Создаем поля для ввода начального и конечного чисел
        tk.Label(master, text="Введите начальное число:").pack(anchor='w', padx=10, pady=5)
        self.start_number_entry = tk.Entry(master, width=20)
        self.start_number_entry.pack(anchor='w', padx=10)

        tk.Label(master, text="Введите конечное число:").pack(anchor='w', padx=10, pady=5)
        self.end_number_entry = tk.Entry(master, width=20)
        self.end_number_entry.pack(anchor='w', padx=10)

        # Создаем кнопку для запуска процесса переименования
        tk.Button(master, text="Переименовать", command=self.rename_files).pack(anchor='w', padx=10, pady=10)

    # Метод для открытия диалогового окна и выбора папки
    def browse_folder(self):
        """
        Открывает диалоговое окно для выбора папки и сохраняет путь.
        """
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    # Метод для вставки текста из буфера обмена в поле маски
    def paste_mask(self):
        """
        Вставляет текст из буфера обмена в поле маски.
        """
        self.mask_entry.delete(0, tk.END)
        self.mask_entry.insert(0, pyperclip.paste())

    # Метод для передачи введенных данных в колбэк переименования
    def rename_files(self):
        """
        Передает введенные данные в колбэк для переименования файлов.
        """
        folder = self.folder_path.get()
        mask = self.mask_entry.get()
        start_number = self.start_number_entry.get()
        end_number = self.end_number_entry.get()
        self.rename_callback(folder, mask, start_number, end_number)
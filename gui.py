# gui.py

"""
gui.py - Модуль, содержащий описание пользовательского интерфейса программы.
"""
import tkinter as tk
from tkinter import filedialog, messagebox

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
        self.master = master
        self.master.title("File Renamer")
        self.master.geometry("600x400")
        self.rename_callback = rename_callback

        # Переменная для хранения пути к папке
        self.folder_path = tk.StringVar()

        # Элементы интерфейса для выбора папки
        tk.Label(master, text="Выберите папку:").pack(anchor='w', padx=10, pady=5)
        self.folder_entry = tk.Entry(master, textvariable=self.folder_path, width=50)
        self.folder_entry.pack(anchor='w', padx=10)
        tk.Button(master, text="Обзор", command=self.browse_folder).pack(anchor='w', padx=10, pady=5)

        # Элементы интерфейса для ввода маски-шаблона
        tk.Label(master, text="Введите маску-шаблон имени файлов:").pack(anchor='w', padx=10, pady=5)
        self.mask_entry = tk.Entry(master, width=50)
        self.mask_entry.pack(anchor='w', padx=10)

        # Поля для ввода начального и конечного числа
        tk.Label(master, text="Введите начальное число:").pack(anchor='w', padx=10, pady=5)
        self.start_number_entry = tk.Entry(master, width=20)
        self.start_number_entry.pack(anchor='w', padx=10)

        tk.Label(master, text="Введите конечное число:").pack(anchor='w', padx=10, pady=5)
        self.end_number_entry = tk.Entry(master, width=20)
        self.end_number_entry.pack(anchor='w', padx=10)

        # Кнопка для запуска процесса переименования
        tk.Button(master, text="Переименовать", command=self.rename_files).pack(anchor='w', padx=10, pady=10)

    def browse_folder(self):
        """
        Открывает диалоговое окно для выбора папки и сохраняет путь.
        """
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    def rename_files(self):
        """
        Передает введенные данные в колбэк для переименования файлов.
        """
        folder = self.folder_path.get()
        mask = self.mask_entry.get()
        start_number = self.start_number_entry.get()
        end_number = self.end_number_entry.get()
        self.rename_callback(folder, mask, start_number, end_number)
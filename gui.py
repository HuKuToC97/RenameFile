# Модуль для работы с графическим интерфейсом
# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox

class FileRenamerApp:
    def __init__(self, master, rename_callback):
        """Инициализация интерфейса приложения"""
        self.master = master
        # Устанавливаем заголовок окна
        self.master.title("File Renamer") 
        # Устанавливаем размеры окна 
        self.master.geometry("600x300")  
        # Колбэк для обработки переименования файлов
        self.rename_callback = rename_callback  

        # Переменная для хранения пути к папке
        self.folder_path = tk.StringVar()

        # Элементы интерфейса для выбора папки
        # Надпись для выбора папки
        tk.Label(master, text="Выберите папку:").pack(anchor='w', padx=10, pady=5)  
        # Поле для отображения пути к папке
        self.folder_entry = tk.Entry(master, textvariable=self.folder_path, width=50)  
        self.folder_entry.pack(anchor='w', padx=10)
        # Кнопка "Обзор" для вызова диалога выбора папки
        tk.Button(master, text="Обзор", command=self.browse_folder).pack(anchor='w', padx=10, pady=5)  

        # Элементы интерфейса для ввода маски-шаблона
        # Надпись для маски
        tk.Label(master, text="Введите маску-шаблон имени файлов:").pack(anchor='w', padx=10, pady=5)  
        # Поле для ввода маски
        self.mask_entry = tk.Entry(master, width=50)  
        self.mask_entry.pack(anchor='w', padx=10)

        # Поля для ввода начального и конечного числа
        # Надпись для начального числа
        tk.Label(master, text="Введите начальное число:").pack(anchor='w', padx=10, pady=5)  
        # Поле для ввода начального числа
        self.start_number_entry = tk.Entry(master, width=20)  
        self.start_number_entry.pack(anchor='w', padx=10)

        # Надпись для конечного числа
        tk.Label(master, text="Введите конечное число:").pack(anchor='w', padx=10, pady=5)  
        # Поле для ввода конечного числа
        self.end_number_entry = tk.Entry(master, width=20)  
        self.end_number_entry.pack(anchor='w', padx=10)

        # Кнопка для запуска процесса переименования
        tk.Button(master, text="Переименовать", command=self.rename_files).pack(anchor='w', padx=10, pady=10)  # Кнопка "Переименовать"

    def browse_folder(self):
        """Открывает диалоговое окно для выбора папки и сохраняет путь"""
        # Показываем диалог выбора папки
        folder_selected = filedialog.askdirectory()  
        # Если папка выбрана, сохраняем её путь
        if folder_selected:  
            self.folder_path.set(folder_selected)

    def rename_files(self):
        """Передает введенные данные в колбэк для переименования файлов"""
        # Получаем путь к папке
        folder = self.folder_path.get()  
        # Получаем введенную маску
        mask = self.mask_entry.get()  
        # Получаем начальное число
        start_number = self.start_number_entry.get()  
        # Получаем конечное число
        end_number = self.end_number_entry.get()  
        # Вызываем колбэк с переданными данными
        self.rename_callback(folder, mask, start_number, end_number)  
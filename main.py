# main.py

"""
main.py - Основной модуль программы. 
Содержит настройку логирования и управление основным окном приложения.
"""
import tkinter as tk
from gui import FileRenamerApp
from renamer import process_rename
from validators import validate_inputs
from config import APP_TITLE, APP_SIZE, NUMBER_PLACEHOLDER, NAME_FILE_PLACEHOLDER
from tkinter import messagebox
import logging

# Настройка логирования: задаем файл для логов, уровень логирования, форматирование и кодировку
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Функция-колбэк для обработки данных из интерфейса и запуска логики переименования
def rename_callback(folder, mask, start, end):
    """
    Колбэк для обработки данных и запуска переименования файлов.
    
    :param folder: Путь к папке
    :param mask: Маска для поиска файлов
    :param start: Начальное число
    :param end: Конечное число
    """
    try:
        # Проверяем входные данные на корректность
        start, end = validate_inputs(folder, mask, start, end)
        # Логируем начало переименования с указанием папки и шаблона
        logging.info(f"Начало переименования в папке {folder} с шаблоном {mask}")
        # Запускаем процесс переименования
        process_rename(folder, mask, start, end)
        # Показываем сообщение об успешном завершении процесса
        messagebox.showinfo("Успех", "Файлы успешно переименованы!")
        # Логируем успешное завершение
        logging.info("Переименование завершено успешно.")
    except Exception as e:
        # Показываем сообщение об ошибке, если что-то пошло не так
        messagebox.showerror("Ошибка", str(e))
        # Логируем текст ошибки
        logging.error(f"Ошибка переименования: {e}")

# Точка входа в программу
if __name__ == "__main__":
    # Создаем главное окно приложения
    root = tk.Tk()
    # Устанавливаем заголовок окна и размеры
    root.title(APP_TITLE)
    root.geometry(APP_SIZE)
    # Инициализируем интерфейс приложения с передачей колбэка
    app = FileRenamerApp(root, rename_callback)
    # Запускаем основной цикл обработки событий интерфейса
    root.mainloop()
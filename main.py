# main.py
import tkinter as tk
from gui import FileRenamerApp
from renamer import process_rename
from validators import validate_inputs
from config import APP_TITLE, APP_SIZE
from tkinter import messagebox
import logging

# Настройка логирования
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def rename_callback(folder, mask, start, end):
    """Колбэк для обработки данных и запуска переименования файлов"""
    try:
        # Проверяем входные данные
        start, end = validate_inputs(folder, mask, start, end)
        logging.info(f"Начало переименования в папке {folder} с шаблоном {mask}")
        # Запускаем переименование
        process_rename(folder, mask, start, end)
        # Показываем сообщение об успехе
        messagebox.showinfo("Успех", "Файлы успешно переименованы!")
        logging.info("Переименование завершено успешно.")
    except Exception as e:
        # Показываем сообщение об ошибке
        messagebox.showerror("Ошибка", str(e))
        logging.error(f"Ошибка переименования: {e}")

if __name__ == "__main__":
    # Создаем главное окно приложения
    root = tk.Tk()
    # Устанавливаем заголовок и размеры
    root.title(APP_TITLE)
    root.geometry(APP_SIZE)
    # Инициализируем приложение
    app = FileRenamerApp(root, rename_callback)
    # Запускаем цикл обработки событий
    root.mainloop()
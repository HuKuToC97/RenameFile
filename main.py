# Точка входа в приложение
# main.py
import tkinter as tk
from gui import FileRenamerApp
from renamer import process_rename
from validators import validate_inputs
from tkinter import messagebox

def rename_callback(folder, mask, start, end):
    """Колбэк для обработки данных и запуска переименования файлов"""
    try:
        start, end = validate_inputs(folder, mask, start, end)  # Проверяем входные данные
        process_rename(folder, mask, start, end)  # Запускаем переименование
        messagebox.showinfo("Успех", "Файлы успешно переименованы!")  # Показываем сообщение об успехе
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))  # Показываем сообщение об ошибке

if __name__ == "__main__":
    root = tk.Tk()  # Создаем главное окно приложения
    app = FileRenamerApp(root, rename_callback)  # Инициализируем приложение
    root.mainloop()  # Запускаем цикл обработки событий

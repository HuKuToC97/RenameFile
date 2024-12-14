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
        # Проверяем входные данные
        start, end = validate_inputs(folder, mask, start, end)  
        # Запускаем переименование
        process_rename(folder, mask, start, end)  
        # Показываем сообщение об успехе
        messagebox.showinfo("Успех", "Файлы успешно переименованы!")  
    except Exception as e:
        # Показываем сообщение об ошибке
        messagebox.showerror("Ошибка", str(e))  

if __name__ == "__main__":
    # Создаем главное окно приложения
    root = tk.Tk()  
    # Инициализируем приложение
    app = FileRenamerApp(root, rename_callback)
    # Запускаем цикл обработки событий  
    root.mainloop()  

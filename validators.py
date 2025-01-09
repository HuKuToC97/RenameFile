# validators.py
import os

def validate_inputs(folder, mask, start, end):
    """Проверка корректности входных данных"""
    if not os.path.exists(folder):
        raise ValueError("Указанный путь не существует.")
    if not mask or '#' not in mask:
        raise ValueError("Маска должна содержать символ '#'.")
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        raise ValueError("Поля для чисел должны содержать только целые числа.")
    return start, end
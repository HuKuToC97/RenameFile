# validators.py

"""
validators.py - Модуль для проверки корректности входных данных.
"""
import os

def validate_inputs(folder, mask, start, end):
    """
    Проверка корректности входных данных.

    :param folder: Путь к папке
    :param mask: Маска для поиска файлов
    :param start: Начальное число
    :param end: Конечное число
    :return: Проверенные и преобразованные значения start и end
    """
    if not os.path.exists(folder):
        raise ValueError("Указанный путь не существует.")
    if not mask or '{number}' not in mask:
        raise ValueError("Маска должна содержать символ '{number}'.")
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        raise ValueError("Поля для чисел должны содержать только целые числа.")
    return start, end
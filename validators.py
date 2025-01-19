# validators.py

"""
validators.py - Модуль для проверки корректности входных данных.
"""
import os
from config import NUMBER_PLACEHOLDER

def validate_inputs(folder, mask, start, end):
    """
    Проверка корректности входных данных.

    :param folder: Путь к папке
    :param mask: Маска для поиска файлов
    :param start: Начальное число
    :param end: Конечное число
    :return: Проверенные и преобразованные значения start и end
    """
    # Проверяем существование указанного пути
    if not os.path.exists(folder):
        raise ValueError("Указанный путь не существует.")
    # Проверяем, что маска содержит обязательный плейсхолдер
    if not mask or NUMBER_PLACEHOLDER not in mask:
        raise ValueError(f"Маска должна содержать символ '{NUMBER_PLACEHOLDER}'.")
    # Проверяем, что начальное и конечное числа являются целыми числами
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        raise ValueError("Поля для чисел должны содержать только целые числа.")
    # Возвращаем проверенные значения
    return start, end
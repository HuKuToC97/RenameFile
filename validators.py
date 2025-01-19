# validators.py
"""
validators.py - Модуль для проверки корректности входных данных.
"""
import os
from config import NUMBER_PLACEHOLDER

def validate_inputs(folder, mask, start_number, replace_number):
    """
    Проверка корректности входных данных.

    :param folder: Путь к папке
    :param mask: Маска для поиска файлов
    :param start_number: Число, с которого начать переименование
    :param replace_number: Число, на которое заменить значение
    :return: Проверенные и преобразованные значения start_number и replace_number
    """
    # Проверяем существование указанного пути
    if not os.path.exists(folder):
        raise ValueError("Указанный путь не существует.")
    # Проверяем, что маска содержит обязательный плейсхолдер
    if not mask or NUMBER_PLACEHOLDER not in mask:
        raise ValueError(f"Маска должна содержать символ '{NUMBER_PLACEHOLDER}'.")
    # Проверяем, что стартовое и заменяющее числа являются целыми числами
    try:
        start_number = int(start_number)
        replace_number = int(replace_number)
    except ValueError:
        raise ValueError("Поля для чисел должны содержать только целые числа.")
    # Возвращаем проверенные значения
    return start_number, replace_number
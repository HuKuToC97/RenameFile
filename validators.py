# Проверка данных (путь, маска, числа)
# validators.py
import os

def validate_inputs(folder, mask, start, end):
    """Валидация входных данных, введенных пользователем"""
    if not os.path.exists(folder):
        raise ValueError("Указанный путь не существует.")  # Проверяем, существует ли папка
    if not mask or '#' not in mask:
        raise ValueError("Маска должна содержать символ '#'.")  # Проверяем, содержит ли маска символ '#'
    try:
        start = int(start)  # Проверяем, что начальное число является целым числом
        end = int(end)  # Проверяем, что конечное число является целым числом
    except ValueError:
        raise ValueError("Поля для чисел должны содержать только целые числа.")  # Если числа некорректны, выбрасываем ошибку
    return start, end  # Возвращаем проверенные данные
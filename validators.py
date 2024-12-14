# Проверка данных (путь, маска, числа)
# validators.py
import os

def validate_inputs(folder, mask, start, end):
    """Валидация входных данных, введенных пользователем"""
    if not os.path.exists(folder):
        # Проверяем, существует ли папка
        raise ValueError("Указанный путь не существует.")  
    if not mask or '#' not in mask:
        # Проверяем, содержит ли маска символ '#'
        raise ValueError("Маска должна содержать символ '#'.")  
    try:
        # Проверяем, что начальное число является целым числом
        start = int(start)  
        # Проверяем, что конечное число является целым числом
        end = int(end)  
    # Если числа некорректны, выбрасываем ошибку
    except ValueError:
        raise ValueError("Поля для чисел должны содержать только целые числа.")  
    # Возвращаем проверенные данные
    return start, end  
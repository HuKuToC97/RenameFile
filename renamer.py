# Логика переименования файлов
# renamer.py
import os
import re

def process_rename(folder, mask, start, end):
    """Основная логика переименования файлов в указанной папке"""
    # Создаем регулярное выражение на основе маски
    # Замена '#' на число и '*' на любое количество символов
    regex_pattern = re.escape(mask).replace('\\#', '(\\d+)').replace('\\*', '.*')  
    # Компилируем регулярное выражение
    regex = re.compile(f"^{regex_pattern}$")  

    # Находим все файлы, которые соответствуют маске
    # Список файлов, соответствующих маске
    files_to_rename = [f for f in os.listdir(folder) if regex.match(f)]  
    # Сортируем файлы по числу в имени
    files_to_rename.sort(key=lambda f: int(regex.match(f).group(1)))  

    # Если файлы не найдены, выбрасываем ошибку
    if not files_to_rename:
        raise FileNotFoundError("Не найдено файлов, соответствующих маске.")  

    # Вычисляем разницу между конечным и начальным числами
    difference = end - start  

    # Переименование файлов
    for filename in files_to_rename:
        # Сравниваем имя файла с регулярным выражением
        match = regex.match(filename)  
        if match:
            # Извлекаем старый номер из имени файла
            old_number = int(match.group(1))  
            # Вычисляем новый номер
            new_number = old_number + difference  
            # Обновляем имя файла
            new_filename = regex.sub(str(new_number), filename, 1)  
            # Переименовываем файл
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))  
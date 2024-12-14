# Логика переименования файлов
# renamer.py
import os
import re

def process_rename(folder, mask, start, end):
    """Основная логика переименования файлов в указанной папке"""
    # Создаем регулярное выражение на основе маски
    regex_pattern = re.escape(mask).replace('\\#', '(\\d+)').replace('\\*', '.*')  # Замена '#' на число и '*' на любое количество символов
    regex = re.compile(f"^{regex_pattern}$")  # Компилируем регулярное выражение

    # Находим все файлы, которые соответствуют маске
    files_to_rename = [f for f in os.listdir(folder) if regex.match(f)]  # Список файлов, соответствующих маске
    files_to_rename.sort(key=lambda f: int(regex.match(f).group(1)))  # Сортируем файлы по числу в имени

    if not files_to_rename:
        raise FileNotFoundError("Не найдено файлов, соответствующих маске.")  # Если файлы не найдены, выбрасываем ошибку

    difference = end - start  # Вычисляем разницу между конечным и начальным числами

    # Переименование файлов
    for filename in files_to_rename:
        match = regex.match(filename)  # Сравниваем имя файла с регулярным выражением
        if match:
            old_number = int(match.group(1))  # Извлекаем старый номер из имени файла
            new_number = old_number + difference  # Вычисляем новый номер
            new_filename = regex.sub(str(new_number), filename, 1)  # Обновляем имя файла
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))  # Переименовываем файл
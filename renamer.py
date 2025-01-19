# renamer.py

"""
renamer.py - Модуль, реализующий логику переименования файлов в папке.
"""
import os
import re
import logging
from config import NUMBER_PLACEHOLDER, NAME_FILE_PLACEHOLDER

def process_rename(folder, mask, start, end):
    """
    Основная логика переименования файлов.

    :param folder: Путь к папке
    :param mask: Маска для поиска файлов
    :param start: Начальное число
    :param end: Конечное число
    """
    # Заменяем плейсхолдеры {number} и {name_file} на соответствующие части регулярного выражения
    regex_pattern = mask.replace(NUMBER_PLACEHOLDER, '(\\d+)').replace(NAME_FILE_PLACEHOLDER, '(.*)')
    logging.info(f"Сгенерированное регулярное выражение: {regex_pattern}")  # Логируем сгенерированное выражение
    regex = re.compile(f"^{regex_pattern}$")
    logging.info(f"Скомпилированное регулярное выражение: {regex}")  # Логируем объект регулярного выражения

    # Собираем список файлов, подходящих под маску
    files_to_rename = [f for f in os.listdir(folder) if regex.match(f)]
    logging.info(f"Файлы, соответствующие маске: {files_to_rename}")  # Логируем найденные файлы

    # Сортируем файлы по числовой части
    files_to_rename.sort(key=lambda f: int(regex.match(f).group(1)))
    logging.info(f"Отсортированные файлы: {files_to_rename}")  # Логируем отсортированные файлы

    # Если файлы не найдены, генерируем ошибку
    if not files_to_rename:
        logging.error("Не найдено файлов, соответствующих маске.")
        raise FileNotFoundError("Не найдено файлов, соответствующих маске.")

    # Вычисляем разницу между начальным и конечным числом
    difference = int(end) - int(start)
    logging.info(f"Разница между начальным и конечным числом: {difference}")  # Логируем вычисленную разницу

    # Проходим по каждому файлу и переименовываем его
    for filename in files_to_rename:
        match = regex.match(filename)
        if match:
            # Извлекаем старый номер и оставшуюся часть имени
            old_number = int(match.group(1))
            name_part = match.group(2)
            logging.info(f"Обработка файла: {filename}, номер: {old_number}, имя: {name_part}")  # Логируем детали файла

            # Вычисляем новый номер
            new_number = old_number + difference
            # Формируем новое имя файла
            new_filename = f"{new_number}.{name_part}"
            # Выполняем переименование
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
            # Логируем информацию о переименовании
            logging.info(f"{filename} -> {new_filename}")
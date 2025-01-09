# renamer.py

"""
renamer.py - Модуль, реализующий логику переименования файлов в папке.
"""
import os
import re
import logging

def process_rename(folder, mask, start, end):
    """
    Основная логика переименования файлов.

    :param folder: Путь к папке
    :param mask: Маска для поиска файлов
    :param start: Начальное число
    :param end: Конечное число
    """
    regex_pattern = re.escape(mask).replace('\{number\}', '(\\d+)').replace('\{name_file\}', '.*')
    regex = re.compile(f"^{regex_pattern}$")

    files_to_rename = [f for f in os.listdir(folder) if regex.match(f)]
    files_to_rename.sort(key=lambda f: int(regex.match(f).group(1)))

    if not files_to_rename:
        logging.error("Не найдено файлов, соответствующих маске.")
        raise FileNotFoundError("Не найдено файлов, соответствующих маске.")

    difference = int(end) - int(start)

    for filename in files_to_rename:
        match = regex.match(filename)
        if match:
            old_number = int(match.group(1))
            name_part = filename[len(match.group(0)):]
            new_number = old_number + difference
            new_filename = f"{new_number}{name_part}"
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
            logging.info(f"{filename} -> {new_filename}")
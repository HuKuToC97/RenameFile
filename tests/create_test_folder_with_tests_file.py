import os

def generate_files(directory, template, count, content=""):
    """
    Создает файлы в указанной директории по заданному шаблону.
    Если директория не существует, выводит предупреждение.

    :param directory: Путь к папке, где нужно создать файлы.
    :param template: Шаблон имени файла, например, "file_{num}.txt".
    :param count: Количество создаваемых файлов.
    :param content: Содержимое, которое будет записано в каждый файл.
    """
    # Проверяем, существует ли указанная директория
    if not os.path.exists(directory):
        # Если директории нет, выводим сообщение об ошибке и прекращаем выполнение функции
        print(f"Ошибка: Папка '{directory}' не существует.")
        return
    
    # Запускаем цикл для создания файлов
    for i in range(1, count + 1):  # Нумерация начинается с 1 и до count включительно
        # Формируем имя файла, подставляя текущий номер (i) в шаблон
        filename = template.format(num=i)
        # Получаем полный путь к файлу, объединяя путь директории и имя файла
        filepath = os.path.join(directory, filename)
        
        # Создаем файл в режиме записи (w), с указанием кодировки utf-8
        with open(filepath, "w", encoding="utf-8") as file:
            # Записываем заданное содержимое в файл
            file.write(content)
        
        # Уведомляем, что файл успешно создан
        print(f"Создан файл: {filepath}")

# Если скрипт запускается как основная программа
if __name__ == "__main__":
    # Пример использования функции generate_files:
    folder_for_create_file = r"F:\УЧЕБА GB\Python\test"  # Укажи путь к папке, где нужно создать файлы
    mask = "{num}.file{num}.txt"  # Шаблон имен файлов с подстановкой номера
    count_files = 10  # Количество файлов для создания
    text_in_created_files = "{num}"  # Текст, который будет записан в каждый файл
    
    # Вызываем функцию для создания файлов
    generate_files(folder_for_create_file, mask, count_files, text_in_created_files)

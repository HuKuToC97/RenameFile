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
    # Проверяем, существует ли директория
    if not os.path.exists(directory):
        print(f"Ошибка: Папка '{directory}' не существует.")
        return
    
    for i in range(1, count + 1):
        filename = template.format(num=i)  # Заменяем {num} на номер файла
        filepath = os.path.join(directory, filename)
        
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)  # Записываем содержимое в файл
        
        print(f"Создан файл: {filepath}")

if __name__ == "__main__":
    # Пример использования
    папка = "test_folder"  # Укажи путь к папке
    шаблон = "file_{num}.txt"  # Шаблон имен файлов
    количество = 10  # Количество файлов
    содержимое = "Тестовое содержимое файла."  # Текст для записи
    
    generate_files(папка, шаблон, количество, содержимое)

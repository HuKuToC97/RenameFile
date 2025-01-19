# tests/test_renamer.py
"""
tests/test_renamer.py - Тесты для модуля renamer.
"""
import unittest
import os
from unittest.mock import patch
from renamer import process_rename
from config import NUMBER_PLACEHOLDER, NAME_FILE_PLACEHOLDER

class TestRenamer(unittest.TestCase):
    # Тест успешного переименования файлов
    @patch("os.listdir")
    @patch("os.rename")
    def test_process_rename_success(self, mock_rename, mock_listdir):
        # Имитируем список файлов в папке
        mock_listdir.return_value = ["1_test.txt", "2_test.txt"]
        # Вызываем функцию переименования
        process_rename("/valid/path", f"{NUMBER_PLACEHOLDER}.{NAME_FILE_PLACEHOLDER}.txt", "1", "3")
        # Проверяем, что переименование было вызвано
        mock_rename.assert_called()

    # Тест на случай отсутствия подходящих файлов
    def test_process_rename_no_files(self):
        with self.assertRaises(FileNotFoundError):
            process_rename("/valid/path", f"{NUMBER_PLACEHOLDER}.{NAME_FILE_PLACEHOLDER}.txt", "1", "3")

# Точка входа для запуска тестов
if __name__ == "__main__":
    unittest.main()
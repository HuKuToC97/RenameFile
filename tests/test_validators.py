# tests/test_validators.py

"""
tests/test_validators.py - Тесты для модуля validators.
"""
import unittest
from validators import validate_inputs
from config import NUMBER_PLACEHOLDER

class TestValidators(unittest.TestCase):
    # Тест на успешную проверку корректных данных
    def test_validate_inputs_success(self):
        self.assertEqual(validate_inputs("/valid/path", f"{NUMBER_PLACEHOLDER}.{NAME_FILE_PLACEHOLDER}.txt", "1", "2"), (1, 2))

    # Тест на случай несуществующего пути
    def test_validate_inputs_invalid_folder(self):
        with self.assertRaises(ValueError):
            validate_inputs("/invalid/path", f"{NUMBER_PLACEHOLDER}.{NAME_FILE_PLACEHOLDER}.txt", "1", "2")

    # Тест на случай отсутствия плейсхолдера в маске
    def test_validate_inputs_invalid_mask(self):
        with self.assertRaises(ValueError):
            validate_inputs("/valid/path", "name_file.txt", "1", "2")

    # Тест на случай некорректных числовых данных
    def test_validate_inputs_invalid_numbers(self):
        with self.assertRaises(ValueError):
            validate_inputs("/valid/path", f"{NUMBER_PLACEHOLDER}.{NAME_FILE_PLACEHOLDER}.txt", "one", "two")

# Точка входа для запуска тестов
if __name__ == "__main__":
    unittest.main()
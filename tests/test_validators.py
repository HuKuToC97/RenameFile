# tests/test_validators.py

"""
tests/test_validators.py - Тесты для модуля validators.
"""
import unittest
from validators import validate_inputs

class TestValidators(unittest.TestCase):
    def test_validate_inputs_success(self):
        self.assertEqual(validate_inputs("/valid/path", "{number}.{name_file}.txt", "1", "2"), (1, 2))

    def test_validate_inputs_invalid_folder(self):
        with self.assertRaises(ValueError):
            validate_inputs("/invalid/path", "{number}.{name_file}.txt", "1", "2")

    def test_validate_inputs_invalid_mask(self):
        with self.assertRaises(ValueError):
            validate_inputs("/valid/path", "name_file.txt", "1", "2")

    def test_validate_inputs_invalid_numbers(self):
        with self.assertRaises(ValueError):
            validate_inputs("/valid/path", "{number}.{name_file}.txt", "one", "two")

if __name__ == "__main__":
    unittest.main()
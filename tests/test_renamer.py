# tests/test_renamer.py

"""
tests/test_renamer.py - Тесты для модуля renamer.
"""
import unittest
import os
from unittest.mock import patch
from renamer import process_rename

class TestRenamer(unittest.TestCase):
    @patch("os.listdir")
    @patch("os.rename")
    def test_process_rename_success(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ["1_test.txt", "2_test.txt"]
        process_rename("/valid/path", "{number}_{name_file}.txt", "1", "3")
        mock_rename.assert_called()

    def test_process_rename_no_files(self):
        with self.assertRaises(FileNotFoundError):
            process_rename("/valid/path", "{number}_{name_file}.txt", "1", "3")

if __name__ == "__main__":
    unittest.main()
import os
import unittest

try:
    # It's local
    from src import DataPath
except:
    # It's a submodule
    from ..src import DataPath


class TestDataPath(unittest.TestCase):
    def test_get_default_data_path(self):
        """Test get default data path"""
        DataPath.get_default_data_path()

        # We're just checking that it doesn't throw an error
        self.assertEqual(
            True,
            True,
            "Get default data path threw a big fat error"
        )

    def test_get_data_path(self):
        """Test get data path"""
        DataPath.get_data_path()

        # We're just checking that it doesn't throw an error
        self.assertEqual(
            True,
            True,
            "Get data path threw a big fat error"
        )

    def test_get_repositories_path(self):
        """Test get repositories path"""
        DataPath.get_repositories_path()

        self.assertEqual(
            True,
            True,
            "Get repositories path threw a big fat error"
        )

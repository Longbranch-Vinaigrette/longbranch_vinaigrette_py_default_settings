import os
import unittest

try:
    # It's local
    from src.app_settings import AppSettings
except:
    # It's a submodule
    from ..src.app_settings import AppSettings


class TestAppSettings(unittest.TestCase):
    def test_app_settings(self):
        """Test app settings"""
        try:
            AppSettings(os.getcwd())
            error = False
        except:
            error = True

        self.assertEqual(
            error,
            False,
            "AppSettings shouldn't throw an error unless, it's being run from an "
            "app which doesn't have settings.json, in that case why are you testing"
            "it without the file."
        )

    def test_not_app_settings(self):
        """It should throw an error"""
        try:
            AppSettings(os.path.expanduser("~"))
            error = False
        except:
            error = True

        self.assertEqual(
            error,
            True,
            "Unless you actually have a repository in your home directory"
            "(You're an f*ing psychopath if you do) this should "
            "throw an error."
        )

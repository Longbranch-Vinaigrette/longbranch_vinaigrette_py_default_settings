"""
This is a utility function for this spec file:
https://github.com/Longbranch-Vinaigrette/longbranch-vinaigrette-standards/blob/main/settings.json.spec.js
"""
import json
import os


class AppSettings:
    def __init__(self, app_path: str):
        settings_path = f"{app_path}{os.path.sep}settings.json"

        try:
            with open(settings_path) as f:
                self.settings = json.load(f)
        except:
            raise Exception("The given app doesn't have a settings.json file")

    def get_devtools_data(self):
        """Just access the data with keys"""
        return self.settings["devtools"]

    def get_settings(self):
        """Get settings"""
        return self.settings

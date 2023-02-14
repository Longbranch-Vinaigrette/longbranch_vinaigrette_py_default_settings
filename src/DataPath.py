"""Where data is located in the data path
and whether local configuration override this"""
import os
import json


def get_override_data_path():
    """Get override data path if it exists, otherwise return None"""
    settings_json_path = f"{os.getcwd()}{os.path.sep}settings.json"
    if os.path.exists(settings_json_path):
        with open(settings_json_path) as f:
            data = json.load(f)
            try:
                override_path = data["longbranchVinaigrette"]["overrideDefaultDataPath"]
                return override_path
            except:
                pass


def get_default_data_path():
    """Default data path"""
    # Data path can be overrided
    override_data_path = get_override_data_path()
    if override_data_path:
        return override_data_path

    cache_folder = f"{os.path.expanduser('~')}{os.path.sep}.cache"
    longbranch_vinaigrette_path = f"{cache_folder}{os.path.sep}longbranch_vinaigrette"

    if os.path.exists(longbranch_vinaigrette_path):
        return longbranch_vinaigrette_path

    # If the user doesn't have a .cache folder at home, just create it
    # - Sigma grindset
    if not os.path.exists(cache_folder):
        os.mkdir(cache_folder)

    if not os.path.exists(longbranch_vinaigrette_path):
        os.mkdir(longbranch_vinaigrette_path)

    return longbranch_vinaigrette_path


def get_repositories_path():
    """Path to repositories

    You're guaranteed that the folder exists, because it will be created if it doesn't.

    Note that repository mirror clones the repositories inside a folder
    with the name of the user(in github)"""
    repositories_path = f"{os.path.expanduser('~')}{os.path.sep}repositories"

    if not os.path.exists(repositories_path):
        os.mkdir(repositories_path)
    if not os.path.isdir(repositories_path):
        # If it's not a dir, create a dir
        os.mkdir(repositories_path)

    return repositories_path

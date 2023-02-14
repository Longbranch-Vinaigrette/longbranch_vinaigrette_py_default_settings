"""Where data is located in the data path
and whether local configuration override this"""
import os
import json

from .app_settings import AppSettings


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


# This depends on the project
def get_override_data_path(app_path: str = os.getcwd()):
    """Get override data path if it exists, otherwise return None"""
    return AppSettings(app_path).get_settings() \
        ["longbranchVinaigrette"]["overrideDefaultDataPath"]


# These are global
def get_default_data_path():
    """Default data path"""
    cache_folder = f"{os.path.expanduser('~')}{os.path.sep}.cache"
    longbranch_vinaigrette_path = f"{cache_folder}{os.path.sep}longbranch_vinaigrette"

    if os.path.exists(longbranch_vinaigrette_path):
        return longbranch_vinaigrette_path

    # If the user doesn't have a .cache folder at home, just create it
    # - Sigma grindset
    if not os.path.exists(cache_folder):
        os.mkdir(cache_folder)
    elif os.path.isdir(cache_folder):
        os.mkdir(cache_folder)

    if not os.path.exists(longbranch_vinaigrette_path):
        os.mkdir(longbranch_vinaigrette_path)
    elif os.path.isdir(longbranch_vinaigrette_path):
        os.mkdir(longbranch_vinaigrette_path)

    return longbranch_vinaigrette_path


def get_data_path():
    """Get data path

    If there's a path override in 'settings.json', return it,
    if not return the global data path,
    this function is preferred over get_default_data path"""
    try:
        # Data path can be overrided
        override_data_path = get_override_data_path()
        if override_data_path:
            return override_data_path
    except:
        # There's no override
        pass

    return get_default_data_path()


def get_default_databases_path():
    """Get default database path"""
    default_data_path = get_default_data_path()
    databases_path = f"{default_data_path}{os.path.sep}dbs"

    if not os.path.exists(databases_path):
        os.mkdir(databases_path)
    elif not os.path.isdir(databases_path):
        os.mkdir(databases_path)

    return databases_path


def get_default_sqlite_path():
    """Get default sqlite db storage path"""
    default_databases_path = get_default_databases_path()
    default_sqlite_path = f"{default_databases_path}{os.path.sep}sqlite"

    if not os.path.exists(default_sqlite_path):
        os.mkdir(default_sqlite_path)
    elif not os.path.isdir(default_sqlite_path):
        os.mkdir(default_sqlite_path)

    return default_sqlite_path


def get_default_sqlite_db_path():
    """Get default sqlite db path"""
    default_sqlite_path = get_default_sqlite_path()
    default_sqlite_db_path = f"{default_sqlite_path}{os.path.sep}default_database.db"
    return default_sqlite_db_path

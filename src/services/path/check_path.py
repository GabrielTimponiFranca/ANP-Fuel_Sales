def _get_resource_path(relative_path=None):
    import os, sys

    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    if relative_path is None:
        return base_path.replace('\\', '/')

    return os.path.join(base_path, relative_path).replace("\\", "/")


def _check_and_create_folder(path):
    import os

    if not os.path.exists(path):
        os.mkdir(path)



def _create_folder():
    PATH = _resource_path()

    folders = ["data", "data/csv", "data/parquet", "data/raw"]

    for folder in folders:
        _check_and_create_folder(os.path.join(PATH, folder))
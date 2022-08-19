from subprocess import call
from services.path.check_path import _get_resource_path

if __name__ == "__main__":

    path = "src/pipeline/__init__.py"

    call(f"python {path}", shell=True)

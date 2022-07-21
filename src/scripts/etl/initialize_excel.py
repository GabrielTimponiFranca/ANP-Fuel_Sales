from contextlib import contextmanager


@contextmanager
def _initialize_excel(file, visible=False):
    """[Função que instancia um objeto Excel em python]
    Args:
        file ([str]): [arquivo qie será instanciado]
        visible ([boolean]): [se desejamos que o excel esteja aberto: True or False]
    Returns:
        ([win32com.gen_py]): [objeto Pywin32 que permite o acesso do Excel via Python]
    """

    import pythoncom
    from pathlib import Path
    from win32com.client import Dispatch
    from contextlib import suppress

    pythoncom.CoInitialize()

    try:
        xl = Dispatch("Excel.Application")

    except AttributeError:

        with suppress(TypeError):
            path_temp = f"C:\\Users\\{LOGIN}\\AppData\\Local\\Temp\\gen_py"

            for f in Path(path_temp):
                Path.unlink(f)

            Path.rmdir(path_temp)

    finally:
        xl = Dispatch("Excel.Application")

    xl.Visible = visible

    yield xl.Workbooks.Open(file)


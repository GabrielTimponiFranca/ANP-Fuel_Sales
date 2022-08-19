def _get_raw_data(url, **kwargs):
    import urllib
    from datetime import datetime
    from services.path.check_path import _get_resource_path

    PATH = _get_resource_path()

    date = datetime.now().strftime("%Y_%m_%d")

    path = f"{PATH}/src/data/raw/raw_{date}.xlsx"

    urllib.request.urlretrieve(url, path)

    kwargs.xcom_push(key="path_raw_file", value=path)

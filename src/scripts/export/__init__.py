def export(df, **kwargs):
    from datetime import datetime
    from ..etl.resource import _resource_path

    PATH = _resource_path()

    date = datetime.now().strftime("%Y_%m_%d")

    path = f"{PATH}/src/data/csv/Dados_{date}"

    df.to_csv(f"{path}.csv", sep=";", index=False)

    df.to_parquet(f"{path}.parquet")

    kwargs.xcom_push(key="path_final_df", value=path)

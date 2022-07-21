import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from scripts.etl.raw_data import _get_raw_data
from scripts.etl import _read_raw_data
from ..path.check_path import _create_folder, _get_resource_path

PATH = _get_resource_path()


default_args = {
    "owner": "Gabriel Timponi França",
    "depends_on_past": False,
    "start_date": days_ago(2),
}

dag = DAG(
    dag_id="raizen_test",
    description="Process of ETL fuel sales excel data",
    default_args=dict(
        owner="Gabriel Timponi França", depends_on_past=False, start_date=days_ago(2)
    ),
)

with dag:
    task_1 = PythonOperator(
        task_id="create_folder_if_not_existe",
        python_callable=_create_folder,
        op_kwargs=dict(
            url="https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/vdpb/vendas-combustiveis-m3.xls/@@download/file/vendas-combustiveis-m3.xlsx"
        ),
    )

    task_2 = PythonOperator(
        task_id="get_raw_file",
        python_callable=_get_raw_data,
    )

    task_3 = PythonOperator(task_id="read_excel_file", python_callable=_read_raw_data)

    task_4 = PythonOperator(task_id="export_data", python_callable=_export)

    task_5 = PythonOperator(task_id="app", python_callable=f"python {PATH}/src/main.py")

[task_1, task_2]
task_2 >> task_3 >> task_4

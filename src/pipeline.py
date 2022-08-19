import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from pendulum import today
from scripts.etl.raw_data import _get_raw_data
from scripts.etl import _read_raw_data
from services.path.check_path import _create_folder, _get_resource_path

PATH = _get_resource_path()


default_args = {
    "owner": "Gabriel Timponi França",
    "depends_on_past": False,
    "start_date": today("UTC").add(days=2),
}

dag = DAG(
    dag_id="raizen_test",
    description="Process of ETL fuel sales excel data",
    default_args=dict(
        owner="Gabriel Timponi França",
        depends_on_past=False,
        start_date=today("UTC").add(days=2),
    ),
)

with dag:
    task_1 = PythonOperator(
        task_id="create_folder_if_not_existe",
        python_callable=_create_folder,
    )

    task_2 = PythonOperator(
        task_id="get_raw_file",
        python_callable=_get_raw_data,
        op_kwargs=dict(
            url="https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/vdpb/vendas-combustiveis-m3.xls/@@download/file/vendas-combustiveis-m3.xlsx"
        ),
    )

    task_3 = PythonOperator(
        task_id="read_excel_file",
        python_callable=_read_raw_data,
        op_kwargs=dict(path_file=kwargs.xcom_pull(key="path_raw_file")),
    )

    task_4 = PythonOperator(
        task_id="export_data",
        python_callable=_export,
        op_kwargs=dict(df=kwargs.xcom_pull(key="df")),
    )

    task_5 = BashOperator(task_id="app", bash_command=f"python {PATH}/main.py")

[task_1, task_2]
task_2 >> task_3 >> task_4

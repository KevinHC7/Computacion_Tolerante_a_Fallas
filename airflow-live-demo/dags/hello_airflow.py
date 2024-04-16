from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
def print_hello():
    return 'Hello Airflow!'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'hello_airflow',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval=timedelta(days=1),
    catchup=False,
)
start = DummyOperator(
    task_id='start',
    dag=dag,
)
hello = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)
start >> hello

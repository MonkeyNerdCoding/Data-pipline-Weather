import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/api-request')

from insert_records import main

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 9, 7),
}

dag = DAG(
    dag_id="weather_api_orchestrator",
    description="Orchestrator DAG for weather data processing",
    schedule=timedelta(minutes=1),
    default_args=default_args,
    catchup=False,
)

with dag:
    task1 = PythonOperator(
        task_id='fetch_and_store_weather_data',
        python_callable=main
    )
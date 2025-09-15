import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount  

sys.path.append('/opt/airflow/api-request')

from insert_records import main

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 9, 7),
}

dag = DAG(
    dag_id="weather_api_orchestrator",
    description="Orchestrator DAG for weather data processing",
    schedule=timedelta(minutes=45),
    default_args=default_args,
    catchup=False,
)

with dag:
    task1 = PythonOperator(
        task_id='fetch_and_store_weather_data',
        python_callable=main
    )

    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='dbt run',
        working_dir='/usr/app/dbt',
        mounts=[
            Mount(source='/home/monkeynerd/repos/weather-data-project/dbt/my_project', target='/usr/app/dbt', type='bind'),
            Mount(source='/home/monkeynerd/repos/weather-data-project/dbt/profiles.yml', target='/root/.dbt/profiles.yml', type='bind')
        ],
        network_mode='weather-data-project_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success',
    )
    task1 >> task2
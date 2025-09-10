# import sys
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta
# from airflow.providers.docker.operators.docker import DockerOperator
# from docker.types import Mount  

# file này đã được chỉnh sửa thành dbt_orchestrator.py
# mục đích: tách riêng phần orchestrator dbt để chạy độc lập, test dễ dàng hơn. Sau khi test xong sẽ gộp lại thành 1 file duy nhất như ban đầu là orchestrator.py

# # sys.path.append('/opt/airflow/api-request')
# # from insert_records import main

# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2025, 9, 7),
# }

# dag = DAG(
#     dag_id="weather_dbt_orchestrator",
#     description="Orchestrator DAG for weather data processing",
#     schedule=timedelta(minutes=1),
#     default_args=default_args,
#     catchup=False,
# )

# with dag:
#     # task1 = PythonOperator(
#     #     task_id='fetch_and_store_weather_data',
#     #     python_callable=main
#     # )

#     # task2 = DockerOperator(
#     #     task_id='transform_data_task',
#     #     image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
#     #     command='run',
#     #     working_dir='/usr/app/dbt',
#     #     mount=[
#     #         mount(source='/home/monkeynerd/repos/weather-data-project/dbt/my_project', target='/usr/app/dbt', type='bind'),
#     #         mount(source='/home/monkeynerd/repos/weather-data-project/dbt/profiles.yml', target='/root/.dbt/profiles.yml', type='bind')
#     #     ],
#     #     network_mode='my-network',
#     #     docker_url='unix://var/run/docker.sock',
#     #     auto_remove='success',
#     # )
#     # task2 = DockerOperator(
#     #     task_id='transform_data_task',
#     #     image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
#     #     command='run',
#     #     working_dir='/usr/app/dbt',
#     #     mounts=[
#     #         Mount(source='/home/monkeynerd/repos/weather-data-project/dbt/my_project', target='/usr/app/dbt', type='bind'),
#     #         Mount(source='/home/monkeynerd/repos/weather-data-project/dbt/profiles.yml', target='/root/.dbt/profiles.yml', type='bind')
#     #     ],
#     #     network_mode='weather-data-project_my-network',
#     #     docker_url='unix://var/run/docker.sock',
#     #     auto_remove='success',
#     # )

# # task2 = DockerOperator(
# #     task_id='transform_data_task',
# #     image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
# #     command='run',
# #     working_dir='/usr/app/dbt',
# #     mounts=[
# #         '/home/monkeynerd/repos/weather-data-project/dbt/my_project:/usr/app/dbt',
# #         '/home/monkeynerd/repos/weather-data-project/dbt/profiles.yml:/root/.dbt/profiles.yml'
# #     ],
# #     network_mode='my-network',
# #     docker_url='unix://var/run/docker.sock',
# #     auto_remove='success',
# # )


# file này đã được chỉnh sửa thành dbt_orchestrator.py
# mục đích: tách riêng phần orchestrator dbt để chạy độc lập, test dễ dàng hơn. Sau khi test xong sẽ gộp lại thành 1 file duy nhất như ban đầu là orchestrator.py
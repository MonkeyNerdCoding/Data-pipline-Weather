CREATE USER superset WITH PASSWORD 'superset';
CREATE DATABASE superset_db OWNER superset;

CREATE USER examples WITH PASSWORD 'examples';
CREATE DATABASE examples_db OWNER examples;

-- Thêm user và database cho airflow
CREATE USER airflow WITH PASSWORD 'airflow';
CREATE DATABASE airflow_db OWNER airflow;

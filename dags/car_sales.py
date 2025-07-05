import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount



HOST_PROJECT_DIR = os.environ.get("HOST_PROJECT_DIR", "/opt/airflow")  # fallback for safety

default_args = {
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    "car_sales_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    generate = BashOperator(
        task_id="generate_data",
        bash_command="python /opt/airflow/scripts/generate_data.py"
    )

    clean = DockerOperator(
        task_id="clean_data",
        image="car-sales-spark",
        api_version="auto",
        auto_remove=True,
        command="spark-submit /app/scripts/clean_data.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mounts=[
            Mount(source=f"{HOST_PROJECT_DIR}/scripts", target="/app/scripts", type="bind"),
            Mount(source=f"{HOST_PROJECT_DIR}/data", target="/opt/bitnami/spark/data", type="bind")
        ],
        mount_tmp_dir=False
    )

    load = BashOperator(
        task_id="load_to_postgres",
        bash_command="python /opt/airflow/scripts/load_to_db.py"
    )

    generate >> clean >> load

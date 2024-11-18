from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Your ETL functions
def pull_data():
    # Your script to pull data
    pass

def transform_data():
    # Your script to transform data
    pass

def insert_data():
    # Your script to insert data into SQLite
    pass

# Define the DAG
dag = DAG(
    'etl_pipeline',
    description='A simple ETL pipeline',
    schedule_interval='@daily',
    start_date=datetime(2024, 11, 1),
    catchup=False,
)

# Define tasks
pull_task = PythonOperator(
    task_id='pull_data',
    python_callable=pull_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

insert_task = PythonOperator(
    task_id='insert_data',
    python_callable=insert_data,
    dag=dag,
)

# Set task dependencies
pull_task >> transform_task >> insert_task

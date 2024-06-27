from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from scripts.fetch_weather_data import fetch_weather_data
from scripts.train_model import train_model
import json

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='A simple weather data pipeline',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 6, 1),
    catchup=False,
)

# Charger la configuration depuis le fichier key.json
config = load_config('/opt/airflow/dags/key.json')
city = config['city']
api_key = config['api_key']
save_path = config['save_path']

fetch_data_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather_data,
    op_kwargs={
        'city': city,
        'api_key': api_key,
        'save_path': save_path
    },
    dag=dag,
)

train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    op_kwargs={'data_path': save_path},
    dag=dag,
)

fetch_data_task >> train_model_task

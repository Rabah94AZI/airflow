from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Ajoutez le chemin vers le script fetch_weather_data.py
sys.path.insert(0, '/opt/airflow/scripts')

from fetch_weather_data import fetch_weather_data, preprocess_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('weather_data_pipeline', default_args=default_args, schedule_interval=timedelta(days=1))

def call_fetch_weather_data():
    city = "Paris"
    api_key = "04021105db5527bbe09d188106e8418e"  # Utilisez votre clé API ici
    save_path = "/path/to/save"  # Remplacez par le chemin de sauvegarde des fichiers
    data = fetch_weather_data(city, api_key, save_path)
    return data

def call_preprocess_data(ti):
    data = ti.xcom_pull(task_ids='fetch_weather_data')
    preprocessed_data = preprocess_data(data)
    # Enregistrez ou traitez les données prétraitées ici
    print(preprocessed_data)

fetch_data = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=call_fetch_weather_data,
    dag=dag,
)

preprocess_data_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=call_preprocess_data,
    provide_context=True,
    dag=dag,
)

fetch_data >> preprocess_data_task

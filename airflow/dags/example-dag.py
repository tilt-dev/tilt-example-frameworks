from datetime import timedelta
from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
import os

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(2),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'tutorial',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='hello_bash',
    bash_command='echo "hello bash" && sleep 5',
    dag=dag,
)

t3 = KubernetesPodOperator(
    task_id="hello_kubernetes",
    name="example-task",
    namespace="airflow",
    image=os.environ.get('IMAGE_TASK'),
    in_cluster=True,
    is_delete_operator_pod=True,
    dag=dag,
  )

t1 >> [t2, t3]

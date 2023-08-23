from airflow.operators.bash import BashOperator
from airflow.models import DAG
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'start_date': datetime(2018, 11, 1)
}

dag = DAG(
    dag_id='hello_airflow',
    default_args=args,
    schedule_interval="@once")

# Bash Operator
cmd = 'echo "Hello, Airflow"'
BashOperator(task_id='t1', bash_command=cmd, dag=dag)

#airflow tasks test hello_airflow t1
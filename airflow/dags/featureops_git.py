from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


with DAG(
    'featureops_git',
    description='featureops git',
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['featureops'],
) as dag:
    
    clone_repo = BashOperator(
        task_id='clone_repo',
        bash_command='git clone <repository URL> <destination folder>',
    )
    
    pull_changes = BashOperator(
        task_id='pull_changes',
        bash_command='cd <destination folder> && git pull',
    )
        

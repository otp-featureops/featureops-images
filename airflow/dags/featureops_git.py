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
        bash_command='if [ ! -d "/opt/airflow/dags/airflow-dags" ]; then cd /opt/airflow/dags && git clone https://jiangxuemichelle:{{ var.value.git_token }}@github.com/otp-featureops/airflow-dags.git; fi',
    )
    
    pull_changes = BashOperator(
        task_id='pull_changes',
        bash_command='cd /opt/airflow/dags/airflow-dags && git pull',
    )

    clone_repo >> pull_changes
        

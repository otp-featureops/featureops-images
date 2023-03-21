#!/bin/bash
echo "Starting Airflow db init..."
airflow db init

echo "Starting Airflow user create..."
airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

echo "Updating Env..."
set -a && . /usr/local/airflow/env.list && set +a && env

echo "Coping Dags..."
cp -r /tmp/dags .

echo "Starting Airflow scheduler..."
airflow scheduler -D
echo "Starting Airflow webserver..."
airflow webserver

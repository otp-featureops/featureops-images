#!/bin/bash
echo "Starting Airflow db init..."
airflow db init

echo "Starting Airflow user create..."
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

echo "Starting Airflow webserver..."
airflow webserver

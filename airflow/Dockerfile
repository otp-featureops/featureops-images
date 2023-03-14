FROM apache/airflow:latest
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN apt-get install git
RUN pip install --no-cache-dir os

COPY --chown=airflow:root /dags /opt/airflow/dags

USER airflow
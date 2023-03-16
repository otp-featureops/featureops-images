FROM apache/airflow:latest
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         build-essential \
         vim \
         git \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
COPY --chown=airflow:root /dags /opt/airflow/dags

USER airflow

COPY env.list /usr/local/airflow/env.list
RUN set -a && . /usr/local/airflow/env.list && set +a && env
COPY startup.sh /startup.sh
RUN pip install databand[airflow,airflow-auto-tracking,postgres]

EXPOSE 8080
CMD ["bash", "/startup.sh"]
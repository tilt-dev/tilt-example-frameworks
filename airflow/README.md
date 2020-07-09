# airflow

## Try it

Start Minikube

```
minikube start
```

Then run:

```
tilt up
```

Tilt will:

1. Install Airflow in your cluster with a Postgres database.

2. Deploy the Airflow sample DAG under [dags](./dags)

3. Connect to the Airflow web UI at http://localhost:8080/

When you make changes to the DAG code, Tilt will live-update the DAGs in place, so
that you can immediately test them with the LocalExecutor.

This is a good setup for iterative development.

## Shout-outs

- Thanks to [astronomer.io)(https://astronomer.io) for their excellent [Airflow
  helm chart](https://github.com/astronomer/airflow-chart).
        
- The example DAG is borrowed from [the official Airflow
  Tutorial](https://airflow.apache.org/docs/stable/tutorial.html).


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

When you make changes to the Task code, Tilt will re-deploy the Airflow server
with the updated image. You can manually kick off new tasks with this image in
the Airflow UI.

This is a good setup for iterative development. You can use this setup with a
local Kubernetes cluster so that you don't need to push/pull images from a
remote registry. No need for a fast network or fiddling with private registry
credentials!

## Shout-outs

- Thanks to [astronomer.io](https://astronomer.io) for their excellent [Airflow
  helm chart](https://github.com/astronomer/airflow-chart).


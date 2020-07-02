# kubedb-postgres

## Try it

Start Minikube with Kubernetes version v1.15.0 (The KubeDB installer doesn't work on higher versions, see https://github.com/kubedb/project/issues/691)

```
minikube start --kubernetes-version=v1.15.0
```

Then run:

```
tilt up
```

Tilt will:

1. Install the kubedb operator in your cluster

2. Deploy a postgres custom resource

3. Configure Tilt to watch the postgres pod and forward ports

Connect to the postgres server with:

```
psql -h localhost -p 5432 -U postgres
```

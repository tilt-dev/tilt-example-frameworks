# kibana

## Try it

Start Minikube with Kubernetes version v1.17.0. 

(Elastic's Persistent Volume Claims don't work correctly on Minikube with Kubernetes v1.18.0, see https://github.com/kubernetes/minikube/issues/8662).

```
minikube start --kubernetes-version=1.17.0
```

Then run:

```
tilt up
```

Tilt will:

1. Install the Elastic Kubernetes Operator

2. Deploy Elasticsearch as a Custom Resource

3. Deploy Kibana as a Custom Resource

4. Serve Kibana at http://localhost:5601/

To browse the Kibana UI, click `kibana-password` in Tilt to get the auto-generated username and password.

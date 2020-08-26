# prometheus

## Try it

Start KIND

```
kind create cluster
```

Then run:

```
tilt up
```

Tilt will:

1. Install the Prometheus Operator

2. Deploy Prometheus

3. Configure Tilt to watch the pod and forward ports

View the prometheus server at: http://localhost:9090/

Note that it is OK if the prometheus server restarts the first time if it can't find the config.
The Prometheus Operator will create the config eventually.

## Shout-outs

- Thanks to everyone who contributed to the [Prometheus
  Operator](https://github.com/prometheus-operator/prometheus-operator), the
  easiest way to configure Prometheus Monitors on Kubernetes!

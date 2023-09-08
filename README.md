```shell
minikube delete --all;
minikube start;
```

```shell
minikube addons enable ingress
```

```shell
kubectl apply -f traefik -R;
kubectl apply -f whoami/whoami.yaml
kubectl apply -f whoami/whoami-service.yaml
kubectl apply -f whoami/whoami-ingress.yaml
kubectl apply -f whoamiv2/whoami.yaml
kubectl apply -f whoamiv2/whoami-service.yaml
kubectl apply -f whoamiv2/whoami-ingress.yaml
```
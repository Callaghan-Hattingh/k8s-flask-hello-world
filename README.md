whoami: [192.168.49.10](http://192.168.49.10 )
whoamiv2: [192.168.49.10](http://192.168.49.10/2 )
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
## Metallb ##
```shell
minikube delete --all;
minikube start;
```

```shell
helm repo add metallb https://metallb.github.io/metallb
helm repo update
helm upgrade --install metallb metallb/metallb --create-namespace --namespace metallb-system --wait
kubectl apply -f metallb.yaml
```
```shell
helm repo add traefik https://traefik.github.io/charts
helm upgrade --install traefik traefik/traefik
```
```shell
kubectl apply -f whoami/whoami.yaml
kubectl apply -f whoami/whoami-service.yaml
kubectl apply -f whoami/whoami-ingress.yaml
kubectl apply -f whoamiv2/whoami.yaml
kubectl apply -f whoamiv2/whoami-service.yaml
kubectl apply -f whoamiv2/whoami-ingress.yaml
```

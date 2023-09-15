whoami: [192.168.49.10](http://192.168.49.10/v1 ).
whoamiv2: [192.168.49.10](http://192.168.49.10/v2 ).
keycloak: [192.168.49.10](http://192.168.49.10/keycloak).

```shell
minikube delete --all;
minikube start;
```

```shell
minikube addons enable ingress
```

```shell
kubectl apply -f traefik -R;
kubectl apply -f whoami/whoami2.yaml
kubectl apply -f whoami/whoami-service2.yaml
kubectl apply -f whoami/whoami-ingress2.yaml
kubectl apply -f whoami2/whoami2.yaml
kubectl apply -f whoami2/whoami-service2.yaml
kubectl apply -f whoami2/whoami-ingress2.yaml
```
## Metallb ##

```shell
minikube delete --all;
minikube start;
helm repo add metallb https://metallb.github.io/metallb
helm repo update
helm upgrade --install metallb metallb/metallb --create-namespace --namespace metallb-system --wait
kubectl apply -f metallb.yaml
helm repo add traefik https://traefik.github.io/charts
helm upgrade --install traefik traefik/traefik
```
```shell
kubectl apply -f whoami/whoami.yaml
kubectl apply -f whoami/whoami-service.yaml
kubectl apply -f whoami/whoami-ingress.yaml
kubectl apply -f whoami2/whoami2.yaml
kubectl apply -f whoami2/whoami-service2.yaml
kubectl apply -f whoami2/whoami-ingress2.yaml
```
```shell
kubectl apply -f keycloak -R -f whoami -R -f whoami2 -R
```
```shell
skaffold dev
```

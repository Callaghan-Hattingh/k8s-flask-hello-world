
whoami: [192.168.49.10](http://192.168.49.10/v1 ).

whoami2: [192.168.49.10](http://192.168.49.10/v2 ).

keycloak: [192.168.49.10](http://192.168.49.10/keycloak).

## Metallb ##

```shell
minikube delete --all;
minikube start;
helm repo add metallb https://metallb.github.io/metallb
helm repo add traefik https://traefik.github.io/charts
helm repo update
helm upgrade --install metallb metallb/metallb --create-namespace --namespace metallb-system --wait --version 0.13.11
helm upgrade --install traefik traefik/traefik --version 24.0.0
```
```shell
cd k8s
skaffold dev
```

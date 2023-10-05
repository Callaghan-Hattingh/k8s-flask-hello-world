
whoami: [192.168.49.10](http://192.168.49.10/v1 ).

whoami2: [192.168.49.10](http://192.168.49.10/v2 ).

keycloak: [192.168.49.10](http://192.168.49.10/keycloak).

## Metallb ##

```shell
minikube delete --all;
minikube start;
helm repo add cloudnative-pg https://cloudnative-pg.io/charts/
#helm repo add grafana https://grafana.github.io/helm-charts
helm repo add metallb https://metallb.github.io/metallb
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add traefik https://traefik.github.io/charts
#helm repo update
helm upgrade --install cloudnative-pg cloudnative-pg/cloudnative-pg --version 0.18.2
helm upgrade --install metallb metallb/metallb --create-namespace --namespace metallb-system --wait --version 0.13.11
helm upgrade --install traefik traefik/traefik --version 24.0.0
#helm upgrade --install prometheus prometheus-community/prometheus --version 25.0.0
#helm upgrade --install grafana grafana/grafana --version 6.60.1
helm upgrade --install prometheus prometheus-community/kube-prometheus-stack --version 51.2.0 --values k8s/monitoring/cnpg-prometheus-values.yaml --reuse-values
```
```shell
cd k8s
skaffold dev
```
```shell
kubectl apply -f \
  https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/main/docs/src/samples/monitoring/grafana-configmap.yaml
```

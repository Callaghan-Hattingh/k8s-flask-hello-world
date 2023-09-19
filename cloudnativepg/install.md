```shell
minikube delete --all;
minikube start;
#minikube addons enable ingress;

kubectl apply -f https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/release-1.20/releases/cnpg-1.20.2.yaml

while true; do
  if [ "$(kubectl get pods --field-selector=status.phase!=Running --all-namespaces --ignore-not-found=true | wc -l)" -ne 0 ]; then
    echo "building"
    sleep 5
  else
    echo "Done"
    break 
  fi
done

sleep 45

kubectl apply -f example-cluster.yaml

kubectl get pods -A

#helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
#
#helm upgrade --install \
#  -f https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/main/docs/src/samples/monitoring/kube-stack-config.yaml \
#  prometheus-community prometheus-community/kube-prometheus-stack
# 
#kubectl apply -f example-podmonitor.yaml
#
#kubectl apply -f \
#  https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/main/docs/src/samples/monitoring/grafana-configmap.yaml
#  
#kubectl port-forward svc/prometheus-community-kube-prometheus 9090

```

```shell
skaffold dev
```

```shell
k get svc

mk ip

```



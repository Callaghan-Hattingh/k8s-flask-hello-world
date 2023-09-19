```shell
minikube delete --all;
minikube start;

kubectl apply -f https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/release-1.20/releases/cnpg-1.20.2.yaml

kubectl apply -f example-cluster.yaml

sleep 10

kubectl get pods -A

```
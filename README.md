```shell
minikube delete
minikube start

kubectl apply -f https://raw.githubusercontent.com/traefik/traefik/v2.9/docs/content/reference/dynamic-configuration/kubernetes-crd-definition-v1.yml
kubectl apply -f https://raw.githubusercontent.com/traefik/traefik/v2.9/docs/content/reference/dynamic-configuration/kubernetes-crd-rbac.yml

kubectl apply -f traefik-deployment.yaml -f traefik-whoami.yaml 
```


```shell
echo `minikube ip`/notls
```
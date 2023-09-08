### Traefik multiple ingress services ###

Setup & config env 

```shell
minikube delete --all
minikube start

kubectl apply -f https://raw.githubusercontent.com/traefik/traefik/v2.9/docs/content/reference/dynamic-configuration/kubernetes-crd-definition-v1.yml
kubectl apply -f https://raw.githubusercontent.com/traefik/traefik/v2.9/docs/content/reference/dynamic-configuration/kubernetes-crd-rbac.yml

kubectl apply -f traefik-deployment.yaml -f traefik-whoami.yaml -f traefik-whoamiv2.yaml
```

To get url of whoami & whoamiv2 address
```shell
echo `minikube ip`/notls;
echo `minikube ip`/notls2;
```
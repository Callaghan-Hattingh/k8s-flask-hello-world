minikube start

docker build -t flask-hello-world .
# pull image into mk
minikube image load flask-hello-world

kubectl apply -f flask-app.yaml

minikube ip
kubectl get svc flask-hello-world



helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install monitoring kube-prometheus-stack

helm show values prometheus-community/kube-prometheus-stack > values.yaml

helm install flask-hello-world flask-helm

# keycloak
minikube addons list
minikube addons enable ingress

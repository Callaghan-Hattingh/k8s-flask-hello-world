minikube start

docker build -t flask-hello-world .

minikube image load flask-hello-world

kubectl apply -f flask-app.yaml

minikube ip
kubectl get svc flask-hello-world

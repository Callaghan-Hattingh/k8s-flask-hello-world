```shell
minikube delete --all;
minikube start;

kubectl apply -f https://raw.githubusercontent.com/keycloak/keycloak-k8s-resources/22.0.3/kubernetes/keycloaks.k8s.keycloak.org-v1.yml
kubectl apply -f https://raw.githubusercontent.com/keycloak/keycloak-k8s-resources/22.0.3/kubernetes/keycloakrealmimports.k8s.keycloak.org-v1.yml

kubectl apply -f https://raw.githubusercontent.com/keycloak/keycloak-k8s-resources/22.0.3/kubernetes/kubernetes.yml

while true; do
  if [ "$(kubectl get pods --field-selector=status.phase!=Running --all-namespaces --ignore-not-found=true | wc -l)" -ne 0 ]; then
    echo "building"
    sleep 5
  else
    echo "Done"
    break 
  fi
done

kubectl apply -f example-postgres.yaml

openssl req -subj '/CN=test.keycloak.org/O=Test Keycloak./C=US' -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem

kubectl create secret tls example-tls-secret --cert certificate.pem --key key.pem

 kubectl create secret generic keycloak-db-secret --from-literal=username=postgres --from-literal=password=testpassword

kubectl apply -f example-kc.yaml

kubectl get keycloaks/example-kc -o go-template='{{range .status.conditions}}CONDITION: {{.type}}{{"\n"}}  STATUS: {{.status}}{{"\n"}}  MESSAGE: {{.message}}{{"\n"}}{{end}}'
```
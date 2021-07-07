# Basic Kubernetes #

## Resources ##

- [ ] [KataCoda - Kubernetes](https://katacoda.com/courses/kubernetes)
- [ ] [Kubernetes 101 (learn Kubernetes in 10 Days)](https://github.com/ajeetraina/kubernetes101)
- [ ] [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [ ] [MiniKube](https://github.com/kubernetes/minikube)

## Launching Single Node Cluster ##

**Uses Minikube**

- Get Version
  - `minikube version`
- Start Cluster
  - `minikube start --wait=false`
- Enable Minikube dashboard
  - `minikube addons enable dashboard`

**Kubectll is used as command line for K8s**
- Get Cluster Details and Health
  - `kubectl cluster-info`
- View Nodes
  - `kubectl get nodes`
- Create Container, get status of deployment, and expose http port
  - `kubectl create deployment first-deployment --image=katacoda/docker-http-server`
  - `kubectl get pods`
  - `kubectl expose deployment first-deployment --port=80 --type=NodePort`

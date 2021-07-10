# Basic Kubernetes #

## Resources ##

- [ ] [KataCoda - Kubernetes](https://katacoda.com/courses/kubernetes)
- [ ] [Kubernetes 101 (learn Kubernetes in 10 Days)](https://github.com/ajeetraina/kubernetes101)
- [ ] [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [ ] [MiniKube](https://github.com/kubernetes/minikube)
- [ ] [Kubernetes Learning Path](https://azure.microsoft.com/mediahandler/files/resourcefiles/kubernetes-learning-path/Kubernetes%20Learning%20Path_Version%202.0.pdf)
- [ ] [Kubernetes Tutorials(Interactive)](https://kubernetes.io/docs/tutorials/)
- [ ] [Kubernetes Lab with KVM](https://medium.com/@nicholas.w.talbot/kubernetes-lab-with-kvm-8ab958cd3c5f)

* * * * *

## Overview ##

Kubernetes is an *Orchestration and Control Plane* for docker images. Similar to docker swarm. 

## Key Terms ##

### **Pods** ###

- Basic unit for running containers inside of Kubernetes
- Provides a way to set environment variables, mount storage, and feed information into a container
- Pods are responsible for running the container and every pod holds at least one container and controls the execution of that container
- when all containers exit the pod dies

### **Replica Sets** ###

- Ensures that a set of identially configured Pods are running at the desired replica count
- Replaces one if one pod dies
- "low-level" type in kubernetes, less referred to than 'Deployments' and DaemonSets

### **Secrets** ###

- Used to store non-public information such as tokens, certs, or passwords
- attached to Pods at runtime
- Base 64 encoded at rest but decoded when attached to a pod
- attached as files or environment variables
- Use add-on encryption for actual encryption (not just encoded) 

### **Deployments** ###

- High level abstraction that controls deploying and maintaining a set of Pods
- Uses a ReplicaSet to keep the Pods running, but offers sophisticated logic for deploying, updating, and scaling a set of Pods
- Support rolling updates and rollbacks
- Rollouts can be paused

### **DaemonSets** ###

- Provide a way to ensure that a copy of a Pod is running on every node in the cluster
- Adjusts as a cluster grows / shrinks, DaemonSet spreads these specific Pods across all the nodes
- One frequent patterns is to install or configure software on each host node

### **Ingresses** ###

- Route traffic to and from the cluster
- declare that traffic ought to be channeled from the outside of the cluster into destinations inside the cluster
- Provide a single SSL endpoint for many applications
- Many different implementations for customization

### **CronJobs** ###

- Provide a method for scheduling execution of Pods
- Used for running periodic tasks like backups, reports, and automated tests
- Use common Cron syntax
- Part of the Batch API for creating short lived non-server tools

### **Custom Resource Definitions (CRD)** ###

- Provide an extension mechanism that cluster operators and developers can use to create own resource type
- Defines a new resource type, tells Kubernetes about it
- Once a new resource type is added, a new instance of that resource may be created
- Common pattern is to create a custom controller that watches for new CRD instances and responds accordingly
  
* * * * *

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

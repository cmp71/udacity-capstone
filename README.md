# udacity-capstone
Udacity Cloud and DevOps Engineer Nano Degree - Capstone project

## Rubric checklist
### Create Github repository with project code. All project code is stored in a GitHub repository and a link to the repository has been provided for reviewers.
This repo.
### Use image repository to store Docker images. The project uses a centralized image repository to manage images built in the project. After a clean build, images are pushed to the repository.
https://hub.docker.com/r/agilealchemy/capstone-nginx/tags
### Execute linting step in code pipeline. Code is checked against a linter as part of a Continuous Integration step (demonstrated w/ two screenshots)
Editing html file to deliberately break it - 
  
![alt text](https://github.com/cmp71/udacity-capstone/blob/master/output/Screenshot%202020-09-20%20222747.png "Breaking the html")

Followed by failing Jenkins pipeline -

![alt-text](https://github.com/cmp71/udacity-capstone/blob/master/output/Screenshot%202020-09-20%20222946.png "Failing pipeline")

Editing html file to fix it - 

![alt-text](https://github.com/cmp71/udacity-capstone/blob/master/output/Screenshot%202020-09-20%20223219.png "Fixing html")

Followed by passing Jenkins pipeline - 

![alt-text](https://github.com/cmp71/udacity-capstone/blob/master/output/Screenshot%202020-09-20%20223344.png "Passing pipeline")

### Build a Docker container in a pipeline. The project takes a Dockerfile and creates a Docker container in the pipeline.
This project uses a simple nginx docker image. The `Dockerfile` is in the root of this repo. This Dockerfile is used to create a new image with the following section of the Jenkinsfile. The new docker image is tagged with the current Jenkins build number:
```groovy
    stage('Build Docker image') {
      steps {
        sh "docker build --tag=capstone-nginx:${BUILD_NUMBER} ."
      }
    }
```
It is then uploaded to Docker Hub with the following section of the Jenkinsfile:
```groovy
    stage('Push Docker image') {
      steps {
        withDockerRegistry([url: "", credentialsId: "dockerhub"]) {
          sh "docker image tag capstone-nginx:${BUILD_NUMBER} agilealchemy/capstone-nginx"
          sh "docker push agilealchemy/capstone-nginx"
        }  
      }
    }
```

### The Docker container is deployed to a Kubernetes cluster. The cluster is deployed with CloudFormation or Ansible. This should be in the source code of the student’s submission.
Kubernetes cluster was deployed to AWS from the CLI using EKSCTL. The command to do so is within [createEKScluster.sh](https://github.com/cmp71/udacity-capstone/blob/master/createEKScluster.sh)

Output of the cluster build script -

![alt-text](https://github.com/cmp71/udacity-capstone/blob/master/output/Screenshot%202020-09-20%20200959.png "Cluster build")

### Use Blue/Green Deployment or a Rolling Deployment successfully. The project performs the correct steps to do a blue/green or a rolling deployment into the environment selected. Student demonstrates the successful completion of chosen deployment methodology with screenshots.
Strategy chosen is Rolling Deployment.

This is achieved via setting `strategy.type` to `RollingUpdate` in [deployment.yaml](https://github.com/cmp71/udacity-capstone/blob/master/deployment.yaml) which is used as in input file to `kubectl apply`.

The rolling update is initiated by running the command `kubectl rollout restart deployment capstone` as part of the pipeline.

Version 1.0 of the website:

![alt-text](https://github.com/cmp71/udacity-capstone/blob/master/output/Screenshot%202020-09-20%20231030.png "Website version 1.0")

Editing website html to version 2.0:

![alt-text](https://github.com/cmp71/udacity-capstone/blob/master/output/Screenshot%202020-09-20%20231635.png "Editing website to version 2.0")

Followed by a successful build and re-deployment to Kubernetes in AWS:

![alt-text](https://github.com/cmp71/udacity-capstone/blob/master/output/Screenshot%202020-09-20%20231845.png "Successful build and re-deploy")

Version 2.0 of the website now running:

![alt-text](https://github.com/cmp71/udacity-capstone/blob/master/output/Screenshot%202020-09-20%20232006.png "Website version 2.0")

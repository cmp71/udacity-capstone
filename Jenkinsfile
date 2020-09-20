#!/usr/bin/groovy

pipeline {
  agent any
  stages {
    stage('Linting') {
      steps {
        sh "make lint"
      }
    }
    stage('Build Docker image') {
      steps {
        sh "docker build --tag=capstone:${BUILD_NUMBER} ."
      }
    }
    stage('Push Docker image') {
      steps {
        withDockerRegistry([url: "", credentialsId: "dockerhub"]) {
          sh "docker image tag capstone:${BUILD_NUMBER} agilealchemy/capstone"
          sh "docker push agilealchemy/capstone"
          sh "docker image prune -f"
        }  
      }
    }
    stage('Deploy to AWS Kubernetes') {
      steps {
        withAWS(region: 'us-west-2', credentials: 'aws') {
          sh "aws eks --region us-west-2 update-kubeconfig --name capstone"
          sh "kubectl config use-context arn:aws:eks:us-west-2:679167268608:cluster/capstone"
          sh "kubectl apply -f deployment.yaml"
          sh "kubectl get nodes"
          sh "kubectl get deployment"
          sh "kubectl get pod -o wide"
          sh "kubectl get service/capstone-service"
        }
      }
    }
  }
}

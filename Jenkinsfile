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
        }  
      }
    }
    stage('Deploy to AWS Kubernetes') {
      steps {
        withAWS(region: 'us-west-2', credentials: 'aws') {
          // sh "aws eks --region us-west-2 update-kubeconfig --name eksctltest"
          // sh "kubectl apply -f deployment.yaml"
        }
      }
    }
  }
}

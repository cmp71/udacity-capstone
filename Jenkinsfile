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
        sh "docker build --tag=capstone ."
      }
    }
    stage('Push Docker image') {
      steps {
        sh "docker image tag capstone agilealchemy/capstone:latest"
        sh "docker push agilealchemy/capstone"
      }
    }
  }
}

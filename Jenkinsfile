pipeline {
  agent any
  stages {
    stage('Prep venv') {
      steps {
        sh "make setup"
      }
    }
    stage('Linting') {
      steps {
        sh "make lint"
      }
    }
  }
}

pipeline {
  agent any
  stages {
    stage('Prep venv') {
      steps {
        sh "make setup"
        sh "make install"
      }
    }
    stage('Linting') {
      steps {
        sh "make lint"
      }
    }
  }
}

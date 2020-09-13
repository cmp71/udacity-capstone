pipeline {
  agent any
  stages {
    stage('Prep venv') {
      steps {
        sh "make setup"
        sh "make install"
        sh "make lint"
      }
    }
  }
}

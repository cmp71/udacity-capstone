pipeline {
    agent any
    stages {
        stage('Create kube config file') {
            steps {
                withAWS(region: 'us-west-2', credentials: 'aws') {
                    sh "aws eks --region us-west-2 update-kubeconfig --name eksctltest"
                }
            }
        }
    }
}
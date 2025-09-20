pipeline {
    agent {label 'vm-test'}
    stages{
        stage('Clean'){
            steps{
                echo 'cleaning workspace'
                // cleanWs()
            }
        }
        stage('Unit Test'){
            steps{
                echo 'Running unit tests'
                // sh 'python3'
            }
        }

    }
}
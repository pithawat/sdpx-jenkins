pipeline {
    agent {label 'vm-test'}
    stages{
        stage('Clean'){
            steps{
                echo 'cleaning workspace'
                sh 'pwd'
            }
        }

        stage('Setup Python'){
            steps{
                echo 'Creating virtual env and install requirements'
                sh 'python3 -m venv venv'
                sh '''
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Unit Test'){
            steps{
                echo 'Running unit tests'
                sh '''
                    python3 -m unittest discover -s . -p "test.py" -v
                '''
            }
        }

    }
}
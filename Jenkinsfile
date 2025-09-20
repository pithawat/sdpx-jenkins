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
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirement.txt
                '''
            }
        }

        stage('Unit Test'){
            steps{
                echo 'Running unit tests'
                sh '''
                    python -m unittest discover -s . -p "test.py" -v
                '''
            }
        }

    }
}
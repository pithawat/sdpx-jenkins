pipeline {
    agent none
    environment{
        IMAGE_NAME = 'flask_api'
        CONTAINER_NAME = 'flask_api_container'
        REGISTRY = 'ghcr.io/pithawat'
        TAG = 'latest'
    }

    stages{
        stage('Clean'){
            agent {label 'vm-test'}
            steps{
                echo 'cleaning workspace'
                sh 'pwd'
            }
        }

        stage('Setup Python'){
            agent {label 'vm-test'}
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
            agent {label 'vm-test'}
            steps{
                echo 'Running unit tests'
                sh '''
                    python3 -m unittest discover -s . -p "test.py" -v
                '''
            }
            post {
                unsuccessful {
                    error("Unit tests failed — skipping image build")
                }
            }
        }

        stage('Create API image'){
            agent {label 'vm-test'}
            steps{
                echo 'create API Image'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Start API Container'){
            agent {label 'vm-test'}
            steps{
                sh '''
                    echo 'running container'
                    docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME
                    sleep 10
                    docker ps
                '''
            }
        }

        stage('clone Robot-test repo'){
            agent {label 'vm-test'}
            steps{
                sh '''
                    rm -rf sdpx-robot_test
                    git clone https://github.com/pithawat/sdpx-robot_test.git
                '''
            }
        }

        stage('Run Robot-test'){
            agent {label 'vm-test'}
            steps{
                sh '''
                    cd sdpx-robot_test
                    . ../venv/bin/activate
                    robot api_test.robot
                '''
            }
        }

        stage('push image to github registry'){
            agent {label 'vm-test'}
            steps{
                withCredentials([usernamePassword(credentialsId: 'ghcr-creds', usernameVariable: 'GH_USER', passwordVariable: 'GH_PAT')]){
                    sh '''
                        echo $GH_PAT | docker login ghcr.io -u $GH_USER --password-stdin
                        docker tag $IMAGE_NAME $REGISTRY/$IMAGE_NAME:$TAG
                        docker push $REGISTRY/$IMAGE_NAME:$TAG
                    '''
                }
            }
            post {
                always {
                    echo 'Cleaning up containers'
                    sh 'docker rm -f $CONTAINER_NAME || true'
                }
            }
        }

        stage('pull image from github'){
            agent {label 'vm-pre_prod'}
            steps{
                withCredentials([usernamePassword(credentialsId: 'ghcr-creds', usernameVariable: 'GH_USER', passwordVariable: 'GH_PAT')]){
                    sh '''
                      echo $GH_PAT | docker login ghcr.io -u $GH_USER --password-stdin
                      docker pull $REGISTRY/$IMAGE_NAME:$TAG

                      docker stop $CONTAINER_NAME || true
                      docker rm $CONTAINER_NAME || true

                      docker run -d --name $CONTAINER_NAME -p 5000:5000 $REGISTRY/$IMAGE_NAME:$TAG
                    '''
                }
            }
        }
    }

}
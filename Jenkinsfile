pipeline {
    agent {label 'vm-test'}

    environment{
        IMAGE_NAME = 'flask_api'
        CONTAINER_NAME = 'flask_api_container'
        REGISTRY = 'ghcr.io/pithawat'
        TAG = 'latest'
    }

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
            post {
                unsuccessful {
                    error("Unit tests failed — skipping image build")
                }
            }
        }

        stage('Create API image'){
            steps{
                echo 'create API Image'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Start API Container'){
            steps{
                sh '''
                    echo 'running container'
                    docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME
                    sleep 5
                '''
            }
        }

        stage('clone Robot-test repo'){
            steps{
                sh '''
                    git clone https://github.com/pithawat/sdpx-robot_test.git
                '''
            }
        }

        stage('Run Robot-test'){
            steps{
                sh '''
                    cd sdpx-robot_test
                    robot api_test.robot
                '''
            }
        }

        // stage('push image to github registry'){
        //     steps{
        //         withCredentials([usernamePassword(credentialsId: 'ghcr-creds', usernameVariable: 'GH_USER', passwordVariable: 'GH_PAT')]){
        //             sh '''
        //                 echo $GH_PAT | docker login ghcr.io -u $GH_USER --password-stdin
        //                 docker tag $IMAGE_NAME $REGISTRY/$IMAGE_NAME:$TAG
        //                 docker push $REGISTRY/$IMAGE_NAME:$TAG
        //             '''
        //         }
        //     }
        // }
    }

    post {
        always {
            echo 'Cleaning up containers'
            sh 'docker rm -f $CONTAINER_NAME || true'
        }
    }
}
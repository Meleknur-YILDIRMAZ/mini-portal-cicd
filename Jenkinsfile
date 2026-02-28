pipeline {
    agent any

    environment {
        IMAGE     = "mini-portal-cicd:latest"
        CONTAINER = "mini-portal-cicd"
        PORT      = "5000"
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Test (inside Docker)") {
            steps {
                sh '''
                    set -eux
                    docker build -t ${IMAGE} .
                    docker run --rm ${IMAGE} pytest -q
                '''
            }
        }

        stage("Deploy (Ubuntu)") {
            steps {
                sh '''
                    set -eux
                    docker rm -f ${CONTAINER} || true
                    docker run -d --name ${CONTAINER} -p ${PORT}:5000 ${IMAGE}
                    docker ps --filter "name=${CONTAINER}"
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}

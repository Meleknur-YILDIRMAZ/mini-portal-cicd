pipeline {
  agent any

  environment {
    IMAGE = "mini-portal-cicd:latest"
    CONTAINER = "mini-portal-cicd"
    PORT = "5000"
  }

  stages {
    stage("Checkout") {
      steps { checkout scm }
    }

    stage("Test") {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt
          pytest -q
        '''
      }
    }

    stage("Build Docker Image") {
      steps {
        sh 'docker build -t $IMAGE .'
      }
    }

    stage("Deploy (Ubuntu Server)") {
      steps {
        sh '''
          docker rm -f $CONTAINER || true
          docker run -d --name $CONTAINER -p 80:$PORT $IMAGE
          sleep 2
          curl -fsS http://127.0.0.1/health
        '''
      }
    }
  }
}
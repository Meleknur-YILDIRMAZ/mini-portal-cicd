pipeline {
  agent any

  environment {
    IMAGE = "mini-portal-cicd:latest"
    CONTAINER = "mini-portal-cicd"
    PORT = "5000"
  }

  stages {

    stage("Checkout") {
      steps {
        checkout scm
      }
    }

    stage("Test") {
      steps {
        bat """
          set PY=C:\\Users\\yildi\\AppData\\Local\\Programs\\Python\\Python314\\python.exe
          "%PY%" -m venv .venv
          call .venv\\Scripts\\activate.bat
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          python -m pytest -q
        """
      }
    }

    stage("Build Docker Image") {
      steps {
        bat """
          docker --version
          docker build -t %IMAGE% .
        """
      }
    }

    stage("Deploy (Windows Local)") {
      steps {
        bat """
          docker rm -f %CONTAINER% 2>NUL
          docker run -d --name %CONTAINER% -p 5000:%PORT% %IMAGE%
        """

        powershell """
          Start-Sleep -Seconds 3
          Invoke-WebRequest -UseBasicParsing http://127.0.0.1:5000/health | Out-Null
          Write-Host "Health check OK"
        """
      }
    }
  }

  post {
    always {
      echo "Pipeline finished."
    }
  }
}

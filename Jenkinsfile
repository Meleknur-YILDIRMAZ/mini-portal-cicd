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

    stage("Test") {
      steps {
        bat """
          python -m venv .venv
          call .venv\\Scripts\\activate.bat
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pytest -q
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
        // NOT: 80 portu Windows'ta bazen izin isteyebilir.
        // O yüzden 5000:5000 daha sorunsuz.
        bat """
          docker rm -f %CONTAINER% 2>NUL
          docker run -d --name %CONTAINER% -p 5000:%PORT% %IMAGE%
        """

        // Health check (PowerShell ile)
        powershell """
          Start-Sleep -Seconds 2
          Invoke-WebRequest -UseBasicParsing http://127.0.0.1:5000/health | Out-Null
          Write-Host "Health check OK ✅"
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

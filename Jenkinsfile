pipeline {
    agent any
    environment {
        PORT = '5055'
        BASE_URL = 'http://127.0.0.1:5055'
        IMAGE_NAME = 'exam-registration:latest'
    }
    stages {
        stage('Run Selenium Tests') {
            steps {
                sh '''
                    set -eu
                    python3 -m pip install -r requirements.txt
                    python3 app.py > flask-test.log 2>&1 &
                    APP_PID=$!
                    trap 'kill "$APP_PID" 2>/dev/null || true' EXIT
                    python3 - <<'PY'
import time, urllib.request
for _ in range(40):
    try:
        with urllib.request.urlopen('http://127.0.0.1:5055/health', timeout=1) as response:
            if response.status == 200:
                break
    except Exception:
        time.sleep(0.5)
else:
    raise SystemExit('Flask failed to start on port 5055')
PY
                    python3 -m pytest tests/ -v
                '''
            }
        }
        stage('Build Docker Image') {
            steps { sh 'docker build -t "$IMAGE_NAME" .' }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl apply -f kubernetes/deployment.yaml
                    kubectl apply -f kubernetes/service.yaml
                    kubectl rollout restart deployment/exam-registration
                    kubectl rollout status deployment/exam-registration --timeout=120s
                '''
            }
        }
    }
    post {
        success { echo 'Tests passed, Docker image built, Kubernetes deployed.' }
        failure { echo 'Pipeline failed. Review the first failed stage.' }
    }
}

# Exam — Flask Registration Selenium CI/CD

GitHub: https://github.com/hibahtaj/testing
Docker Hub username: hibah123 (not used by the local-only pipeline)

## Contents
- Flask registration form with required name/password and success page
- 3 Selenium Chrome tests (headless)
- Jenkins pipeline: install dependencies, start Flask, test, build Docker image, deploy to local Docker Desktop Kubernetes
- Kubernetes Deployment (2 replicas) and Service

## One-time prerequisites
- macOS with Jenkins, Python 3, Chrome, Docker Desktop and kubectl installed
- Docker Desktop running with Kubernetes enabled
- Jenkins user able to run `docker` and `kubectl`
- Jenkins Pipeline job set to Pipeline script from SCM, Git URL https://github.com/hibahtaj/testing.git, branch */main, script path Jenkinsfile
- Port 5055 must be available for Selenium tests
- `kubectl config current-context` should target Docker Desktop Kubernetes
- This pipeline uses a LOCAL Docker image (`imagePullPolicy: Never`); Docker Hub credentials and push are intentionally not required. The Jenkins host and Kubernetes must share the Docker Desktop image store.

## Local run
python3 -m pip install -r requirements.txt
python3 app.py
# Open http://localhost:5055

## Local Selenium tests (second terminal)
python3 -m pytest tests/ -v

## GitHub upload
# In this folder, if replacing the files in an existing local Git repository:
git add .
git commit -m "Fix Selenium CI CD project"
git push origin main

## Kubernetes access after Jenkins deploy
kubectl port-forward service/exam-registration-service 5056:5055
# Open http://localhost:5056

## Important
This is a reconstructed project based on the shared Flask code and Jenkins logs, not a verified exact copy of the GitHub repo. It is not possible to preconfigure Jenkins credentials, Docker Desktop Kubernetes, or the user's local Git credentials from inside a ZIP.

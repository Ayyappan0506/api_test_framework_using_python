pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'
        }
    }

    environment {
        VENV_DIR = "venv"
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python -m venv ${VENV_DIR}
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                pytest -v
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
        success {
            echo "Tests passed ✅"
        }
        failure {
            echo "Tests failed ❌"
        }
    }
}

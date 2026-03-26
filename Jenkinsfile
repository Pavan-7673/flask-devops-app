pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Pavan-7673/flask-devops-app'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app ./python-app'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'
                sh 'docker run -d -p 5002:5000 --name flask-container flask-app'
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'aws s3 ls'
                }
                script {
                    dockerImage = docker.build('matrix-test:latest')
                }
            }
        }
        stage('Save results in out/') {
            steps {
                script {
                    sh 'docker build --output out .'
                }
            }
        }
        stage('Build & Deploy') {
            steps {
                script {
                    echo 'Building and deploying...'
                }
            }
        }

        stage('Pull & Test') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    echo 'Pulling and testing...'
                }
            }
        }
    }
}

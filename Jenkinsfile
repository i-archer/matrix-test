pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        S3_BUCKET = 'pavelnovikau-matrix'
        ECR_REPO = 'pavelnovikau'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                   withCredentials([string(credentialsId: 'AWS_CREDENTIALS', variable: 'AWS_CREDENTIALS')]) {
                        withAWS(region: "${AWS_REGION}", credentials: 'AWS_CREDENTIALS') {
                            sh "aws s3 ls"
                        }
                    }
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

pipeline {
    agent any

    parameters {
        string(name: 'AWS_REGION', defaultValue: 'us-east-1', description: 'AWS Region')
        string(name: 'S3_BUCKET', defaultValue: 'pavelnovikau-matrix', description: 'S3 Bucket Name')
        string(name: 'ECR_REPO', defaultValue: 'pavelnovikau', description: 'ECR Repository Name')
        string(name: 'AWS_CREDENTIALS', defaultValue: 'AWS_SECRETS', description: 'AWS Credentials ID')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build('matrix-test:latest')
                    sh "docker build --output out ."
                }
            }
        }

        stage('Deploy to S3') {
            steps {
                script {
                    withCredentials([string(credentialsId: "${AWS_CREDENTIALS}", variable: 'AWS_CREDENTIALS')]) {
                        sh "aws s3 cp artifact.txt s3://${S3_BUCKET}/"
                    }
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

pipeline {
    agent any

    parameters {
        string(name: 'AWS_REGION', defaultValue: '', description: 'AWS Region')
        string(name: 'S3_BUCKET', defaultValue: '', description: 'S3 Bucket Name')
        string(name: 'ECR_REPO', defaultValue: '', description: 'ECR Repository Name')
        string(name: 'AWS_CREDENTIALS', defaultValue: '', description: 'AWS Credentials ID')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    withCredentials([string(credentialsId: "${AWS_CREDENTIALS}", variable: 'AWS_CREDENTIALS')]) {
                        dockerImage = docker.build('matrix-test:latest')
                        sh "docker build --output out ."
                    }
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

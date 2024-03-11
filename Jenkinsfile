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
                    withCredentials([string(credentialsId: "${AWS_CREDENTIALS_ACCESS_KEY}", variable: 'AWS_ACCESS_KEY_ID'), string(credentialsId: "${AWS_CREDENTIALS_SECRET_KEY}", variable: 'AWS_SECRET_ACCESS_KEY')]) {

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

pipeline {
    agent any

    environment {
        S3_BUCKET = 'pavelnovikau-matrix'
    }

    stages {
        stage('Build & Deploy') {
            steps {
                script {
                    dockerImage = docker.build('pavelnovikau:latest')
                    sh "docker build --output out ."
                }
            }

            steps {
                script {
                    withAWS(credentials: 'AWS_1', region: 'us-east-1') {
                        sh "aws s3 cp out/artifact.txt s3://${S3_BUCKET}/"
                    }
                }
            }

            steps {
                script {
                    withAWS(credentials: 'AWS_1', region: 'us-east-1') {
                        sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 161192472568.dkr.ecr.us-east-1.amazonaws.com"
                        sh "docker tag pavelnovikau:latest 161192472568.dkr.ecr.us-east-1.amazonaws.com/pavelnovikau:latest"
                        sh "docker push 161192472568.dkr.ecr.us-east-1.amazonaws.com/pavelnovikau:latest"
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

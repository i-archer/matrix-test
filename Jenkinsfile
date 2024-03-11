pipeline {
    agent any

    parameters {
        choice(name: 'SELECTED_STAGE', choices: ['Build & Deploy', 'Pull & Test' ], description: 'Select the stage to run')
    }

    environment {
        S3_BUCKET = 'pavelnovikau-matrix'
    }

    stages {
        stage('Build & Deploy') {
            when {
                beforeAgent true
                anyOf {
#                    triggeredBy 'GitHubPushCause'
                    expression { params.SELECTED_STAGE == 'Build & Deploy' }
                }
            }
            steps {
                script {
                    dockerImage = docker.build('pavelnovikau:latest')
                    sh "docker build --output out ."
                }
                script {
                    withAWS(credentials: 'AWS_1', region: 'us-east-1') {
                        sh "aws s3 cp out/artifact.txt s3://${S3_BUCKET}/"
                    }
                }
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
                beforeAgent true
                anyOf {
                    triggeredBy 'TimerTrigger'
                    expression { params.SELECTED_STAGE == 'Pull & Test' }
                }
            }
            steps {
                script {
                    withAWS(credentials: 'AWS_1', region: 'us-east-1') {
                        sh "aws s3 cp s3://${S3_BUCKET}/artifact.txt ."
                        def artifactContent = sh(script: 'cat artifact.txt', returnStdout: true).trim()

                        if (artifactContent.isEmpty()) {
                            error 'The downloaded artifact is empty.'
                        } else {
                            echo "Artifact content: ${artifactContent}"
                        }
                    }
                }
            }
        }
    }
}

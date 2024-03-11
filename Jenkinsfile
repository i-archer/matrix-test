pipeline {
    agent any

    stages {
        stage('Build & Deploy') {
            steps {
                // Clone repository and checkout PR branch
                // Build Docker image
                // Run Python script inside the container
                // Deploy artifact to S3
                // Push Docker image to ECR
            }
        }

        stage('Pull & Test') {
            when {
                anyOf {
                    // Triggered periodically
                    cron('H 0 * * *')
                    // Triggered manually in Jenkins UI
                    expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
                }
            }
            steps {
                // Download the most recent artifact from S3
                // Test whether the artifact is empty
            }
        }
    }
}

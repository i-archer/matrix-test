pipeline {
    agent any

    stages {
        stage('Build & Deploy') {
            steps {
                // Ваши шаги для сборки и развертывания
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
                // Ваши шаги для загрузки и тестирования
                script {
                    echo 'Pulling and testing...'
                }
            }
        }
    }
}

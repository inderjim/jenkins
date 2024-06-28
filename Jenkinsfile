pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/inderjim/jenkins'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building...'
                // Add your build commands here, e.g., sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                sh 'echo Testing...'
                // Add your test commands here, e.g., sh 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deploying...'
                // Add your deploy commands here
            }
        }
    }
}

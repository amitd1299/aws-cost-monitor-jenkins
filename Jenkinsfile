pipeline {
    agent any

    triggers {
        cron('0 9 * * *')
    }

    environment {
        THRESHOLD = '10.0'
        AWS_DEFAULT_REGION = 'us-east-1'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub...'
                checkout scm
            }
        }
        stage('Setup') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip3 install -r requirements.txt --break-system-packages'
            }
        }
        stage('Fetch & Analyze Cost') {
            steps {
                echo 'Fetching AWS Cost data...'
                sh 'python3 cost_checker.py'
            }
        }
        stage('Report') {
            steps {
                echo 'Pipeline completed!'
                echo "Threshold: $THRESHOLD USD"
            }
        }
    }

    post {
        success {
            echo 'Cost check passed!'
        }
        failure {
            echo 'Pipeline failed — check AWS credentials!'
        }
    }
}

pipeline {
    agent any

    stages {

        stage('Install Python and pip') {
            steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip python3-venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'PYTHONPATH=. python3 -m pytest'
            }
        }

    }
}
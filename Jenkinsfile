pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest automated tests...'
                sh 'PYTHONPATH=. pytest'
            }
        }

    }
}
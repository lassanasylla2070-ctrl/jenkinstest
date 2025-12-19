pipeline {
    agent any

    stages {
        stage('Run tests') {
            steps {
                sh '''
                bash -c "source /opt/venv/bin/activate && pytest test_calculs.py"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline terminé avec succès !'
        }
        failure {
            echo 'Pipeline échoué !'
        }
    }
}


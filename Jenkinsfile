pipeline {

    agent any

    environment {
        PYTHON_PATH = 'E:\\Espressif\\python_env\\idf5.5_py3.11_env\\Scripts\\python.exe'
    }

    stages {

        stage('Prepare Environment') {
            steps {
                bat '"%PYTHON_PATH%" --version'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON_PATH%" -m pytest -v --junitxml=test-results.xml'
            }
        }

    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}
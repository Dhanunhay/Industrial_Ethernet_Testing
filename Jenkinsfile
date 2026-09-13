pipeline {

    agent any

    stages {

        stage('Prepare Environment') {
            steps {
                bat '"E:\\Espressif\\python_env\\idf5.5_py3.11_env\\Scripts\\python.exe" --version'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"E:\\Espressif\\python_env\\idf5.5_py3.11_env\\Scripts\\python.exe" -m pytest -v --junitxml=test-results.xml'
            }
        }

    }

    post {

        always {
            junit 'test-results.xml'
        }

    }
}
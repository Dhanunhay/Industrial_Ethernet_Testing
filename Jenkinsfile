pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                bat '"E:\\Espressif\\python_env\\idf5.5_py3.11_env\\Scripts\\python.exe" -m pytest -v'
            }
        }

    }
}
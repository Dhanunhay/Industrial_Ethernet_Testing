pipeline {

    agent any

    environment {
        PYTHON_PATH = 'E:\\Espressif\\python_env\\idf5.5_py3.11_env\\Scripts\\python.exe'
    }

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['ALL', 'ETHERNET', 'NETWORK', 'PROFINET'],
            description: 'Select the test suite to execute'
        )
    }

    stages {

        stage('Prepare Environment') {
            steps {
                bat '"%PYTHON_PATH%" --version'
            }
        }

        stage('Run Tests') {
            steps {
                script {

                    if (params.TEST_SUITE == 'ALL') {
                        bat '"%PYTHON_PATH%" -m pytest -v --junitxml=test-results.xml'
                    }

                    else if (params.TEST_SUITE == 'ETHERNET') {
                        bat '"%PYTHON_PATH%" -m pytest -v test_ethernet.py --junitxml=test-results.xml'
                    }

                    else if (params.TEST_SUITE == 'NETWORK') {
                        bat '"%PYTHON_PATH%" -m pytest -v test_network.py --junitxml=test-results.xml'
                    }

                    else if (params.TEST_SUITE == 'PROFINET') {
                        bat '"%PYTHON_PATH%" -m pytest -v test_profinet.py --junitxml=test-results.xml'
                    }
                }
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}
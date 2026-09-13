pipeline {

    agent any

    environment {
    PYTHON_PATH = 'E:\\Espressif\\python_env\\idf5.5_py3.11_env\\Scripts\\python.exe'

    DEVICE_CREDENTIALS = credentials('industrial-device-credentials')
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

        stage('Run All Tests') {
            when {
                expression {
                    params.TEST_SUITE == 'ALL'
                }
            }

            steps {
                bat '"%PYTHON_PATH%" -m pytest -v --junitxml=test-results.xml'
            }
        }

        stage('Run Ethernet Tests') {
            when {
                expression {
                    params.TEST_SUITE == 'ETHERNET'
                }
            }

            steps {
                bat '"%PYTHON_PATH%" -m pytest -v test_ethernet.py --junitxml=test-results.xml'
            }
        }

        stage('Run Network Tests') {
            when {
                expression {
                    params.TEST_SUITE == 'NETWORK'
                }
            }

            steps {
                bat '"%PYTHON_PATH%" -m pytest -v test_network.py --junitxml=test-results.xml'
            }
        }

        stage('Run PROFINET Tests') {
            when {
                expression {
                    params.TEST_SUITE == 'PROFINET'
                }
            }

            steps {
                bat '"%PYTHON_PATH%" -m pytest -v test_profinet.py --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}
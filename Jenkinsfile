pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository from GitHub
                git url: 'https://github.com/your-username/your-repo.git', branch: 'main'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install necessary dependencies (if any)
                script {
                    if (isUnix()) {
                        sh 'pip install pandas'
                    } else {
                        bat 'pip install pandas'
                    }
                }
            }
        }
        
        stage('Run Script') {
            steps {
                // Execute the Python script
                script {
                    if (isUnix()) {
                        sh 'python compare_csv_files.py'
                    } else {
                        bat 'python compare_csv_files.py'
                    }
                }
            }
        }
    }
}

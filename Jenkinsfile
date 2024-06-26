pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository from GitHub
                git url: 'https://github.com/Aarti2022/Performance.git', branch: 'main'
            }
        }
        
        // stage('Install Dependencies') {
        //     steps {
        //         // Install necessary dependencies (if any)
        //         script {
        //             if (isUnix()) {
        //                 // sh 'pip install pandas'
        //             } else {
        //                 bat 'pip install pandas'
        //             }
        //         }
        //     }
        // }
        
        stage('Run Script') {
            steps {
                // Execute the shell script
                script {
                    if (isUnix()) {
                        sh 'test.sh'
                    } else {
                        bat 'bat.sh'
                    }
                }
            }
        }
    }
}

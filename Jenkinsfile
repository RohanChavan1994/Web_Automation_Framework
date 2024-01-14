pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            environment {
                PATH = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311\\Scripts;C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311;" + "${env.PATH}"
            }
            steps {
                // Run commands using the Python path and pip
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pytest .\\code\\12Jan2024\\test_vwo_ddt_gtp2.py --html=.\\html_report\\report.html --alluredir=allure_reports'

                allure includeProperties: false, jdk: '', results: [[path: 'allure_reports']]
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: false, reportDir: 'html_report', reportFiles: 'report.html', reportName: 'HTML_Report', reportTitles: '', useWrapperFileDirectly: true])
            }
        }
    }

    post {
        always {
            script {
                // Define the paths to be compressed
                def path1 = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Pipeline-Web-Automation\\allure_reports"
                def path2 = "C:\\ProgramData\\Jenkins\\.jenkins\\jobs\\Pipeline-Web-Automation\\htmlreports"

                // Combine paths into a single comma-separated string
                def combinedPaths = "\"${path1}\",\"${path2}\""

                // Compress-Archive using the combined paths
                bat "powershell Compress-Archive -Force -Path ${combinedPaths} -DestinationPath reports.zip"

                // Get the build status
                def buildStatus = currentBuild.result ?: 'SUCCESS'

                // Email notification after the build completes
                emailext subject: "Jenkins Build ${buildStatus}",
                    body: "Your Jenkins build has ${buildStatus.toLowerCase()}. Check the build status!",
                    to: 'jenkinsemailsetup@gmail.com',
                    attachmentsPattern: '**/reports.zip'
            }
        }
    }
}

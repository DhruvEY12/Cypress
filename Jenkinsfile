pipeline {
  agent any
  stages {
    stage('Cypress-Scan') {
      steps {
        sh 'npm ci'
        sh "npx run cypress"
      }
    }
  }
}

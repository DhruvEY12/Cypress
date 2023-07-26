pipeline {
  agent any
  stages {
    stage('Cypress-Scan') {
      steps {
        sh 'npm ci'
        sh "npm run"
        sh "npm run cypress"
      }
    }
  }
}

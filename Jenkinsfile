pipeline {
  agent {
    docker {
      image 'cypress/base:18.14.1'
    }
  }
  stages {
    stage('Cypress-Scan') {
      steps {
        sh 'npm ci'
        sh "npm run test:ci:record"
      }
    }
  }
}

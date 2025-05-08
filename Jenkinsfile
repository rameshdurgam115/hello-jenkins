pipeline {
  agent { label 'slave' }
  environment {
    IMAGE = "rameshdurgam115/hello-jenkins"
  }
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/rameshdurgam115/hello-jenkins.git', branch: 'main'
      }
    }
    stage('Build Image') {
      steps {
        sh "docker build -t \$IMAGE:\${BUILD_NUMBER} ."
      }
    }
    stage('Test') {
      steps {
        sh "docker run --rm \$IMAGE:\${BUILD_NUMBER} pytest -q"
      }
    }
    stage('Push to Registry') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'USER', passwordVariable: 'PASS'
        )]) {
          sh '''
            echo \$PASS | docker login -u \$USER --password-stdin
            docker push \$IMAGE:\${BUILD_NUMBER}
          '''
        }
      }
    }
  }
}

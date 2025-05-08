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

    stage('Build') {
      steps {
        sh "docker build -t ${IMAGE}:${BUILD_NUMBER} ."
      }
    }

    stage('Test') {
      steps {
        sh "docker run --rm ${IMAGE}:${BUILD_NUMBER} pytest -q"
      }
    }
  }

  post {
    always {
      sh 'docker system prune -f'
    }
    success {
      echo "✅ Built image ${IMAGE}:${BUILD_NUMBER} on slave"
    }
    failure {
      echo "❌ Build failed"
    }
  }
}

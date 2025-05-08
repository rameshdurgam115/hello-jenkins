pipeline {
  agent { label 'slave' }

  environment {
    DOCKER_IMAGE = "rameshdurgam115/hello-jenkins"
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'git@github.com:rameshdurgam115/hello-jenkins.git', branch: 'main'
      }
    }

    stage('Build Image') {
      steps {
        sh "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} ."
      }
    }

    stage('Test') {
      steps {
        sh "docker run --rm ${DOCKER_IMAGE}:${BUILD_NUMBER} pytest -q"
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'DOCKER_USER',
          passwordVariable: 'DOCKER_PASS'
        )]) {
          sh '''
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
            docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
          '''
        }
      }
    }
  }

  post {
    always {
      sh 'docker system prune -f'
    }
    success {
      echo "✅ Build #${BUILD_NUMBER} succeeded and image pushed!"
    }
    failure {
      echo "❌ Build #${BUILD_NUMBER} failed."
    }
  }
}

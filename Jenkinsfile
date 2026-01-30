pipeline {
  agent any

  environment {
    VM2_HOST = "192.168.56.104"
    VM2_USER = "lassanavm2"

    APP_NAME = "simple-flask-app"
    CONTAINER_NAME = "simple-flask-app-v2"

    VM2_PORT = "5002"
    CONTAINER_PORT = "5000"

    IMAGE_TAG = "${BUILD_NUMBER}"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
        sh 'ls -la'
      }
    }

    stage('Build Docker image (VM1)') {
      steps {
        sh '''
          echo "Building Docker image..."
          docker build --no-cache -t ${APP_NAME}:${IMAGE_TAG} .
          docker images | head
        '''
      }
    }

    stage('Transfer image to VM2') {
      steps {
        sh '''
          echo "Sending image to VM2..."
          docker save ${APP_NAME}:${IMAGE_TAG} | ssh -o StrictHostKeyChecking=no ${VM2_USER}@${VM2_HOST} "docker load"
        '''
      }
    }

    stage('Deploy on VM2') {
      steps {
        sh '''
          ssh -o StrictHostKeyChecking=no ${VM2_USER}@${VM2_HOST} "

            docker stop ${CONTAINER_NAME} || true
            docker rm -f ${CONTAINER_NAME} || true

            docker run -d \
              --name ${CONTAINER_NAME} \
              -p ${VM2_PORT}:${CONTAINER_PORT} \
              ${APP_NAME}:${IMAGE_TAG}

            docker ps | grep ${CONTAINER_NAME}
          "
        '''
      }
    }
  }

  post {
    always {
      sh 'docker ps || true'
    }
  }
}


pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    env.IMAGE_TAG = sh(
                        script: 'git rev-parse --short=12 HEAD',
                        returnStdout: true
                    ).trim()

                    sh '''
                        docker build \
                            --tag "shoe-lab:$IMAGE_TAG" \
                            --tag "shoe-lab:latest" \
                            .
                    '''
                }
            }
        }

        stage('Push Docker image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        set +x
                        printf '%s' "$DOCKERHUB_TOKEN" | docker login \
                            --username "$DOCKERHUB_USERNAME" \
                            --password-stdin
                        docker tag "shoe-lab:$IMAGE_TAG" "$DOCKERHUB_USERNAME/shoe-lab:$IMAGE_TAG"
                        docker tag "shoe-lab:latest" "$DOCKERHUB_USERNAME/shoe-lab:latest"
                        docker push "$DOCKERHUB_USERNAME/shoe-lab:$IMAGE_TAG"
                        docker push "$DOCKERHUB_USERNAME/shoe-lab:latest"
                    '''
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout >/dev/null 2>&1 || true'
        }
    }
}

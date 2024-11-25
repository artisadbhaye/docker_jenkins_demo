pipeline {
	agent any
	environment {
		GIT_REPOSITORY_URL = 'https://github.com/artisadbhaye/docker_jenkins_demo.git'
		DOCKER_IMAGE_NAME = 'aartisadbhaye1/docker_jenkins_demo'
		IMAGE_TAG = '1.0'
	}
	stages {
		stage('Clone Repository') {
			steps {
				script {
					try {
						git branch: 'main', url: GIT_REPOSITORY_URL
					} catch (Exception e) {
						echo "Failed to clone repo: ${e.message}"
						echo "Failed to clone repo"
					}
				}
			}
		}
		stage('Build Docker Image') {
			steps { 
                                script { 
                                        try { 
                                                docker.build("${DOCKER_IMAGE_NAME}:${IMAGE_TAG}")
                                        } catch (Exception e) { 
                                                echo "Failed to build docker image: ${e.message}"
                                                echo "Failed to build docker image"
                                        }
                                }
                        }

		}
		stage('Push to DockerHub') { 
                        steps {
                                script {
                                        try {
                                                withCredentials([usernamePassword(credentialsId: 'ditiss-docker', usernameVariable: 'aartisadbhaye1', passwordVariable: 'ditiss@123')]) {
							//Explicit login before push
							sh """
							echo "$DOCKER_PASSWORD" | docker login -u $DOCKER_USERNAME --password-stdin
							docker push ${DOCKER_IMAGE_NAME}:${IMAGE_TAG}
							"""
						}
                                        } catch (Exception e) {
                                                echo "Failed to PUSH docker image to registry ${e.message}"
                                                echo "Failed to push docker image"
                                        }
                                }
                        }

                }

	}
}

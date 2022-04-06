pipeline {
    agent any 

    environment {
        IMAGE_NAME = 'ks5490/terraform_spartan_project:JK.' + "$BUILD_NUMBER"
        DOCKER_CRED = 'docker_hub_cred'
    }

    stages {
        stage('Cloning the project from GitHub'){
            steps {
                git branch: 'main', 
                url: "https://github.com/Ks5490/jerkinsss.git"
            }
        }

        stage('Build Docker Image'){
            steps {
                script {
                   DOCKER_IMAGE = docker.build IMAGE_NAME
                }
            }
        }

        stage('Push to Docker Hub'){
            steps{
                script {
                    docker.withRegistry('' , DOCKER_CRED){
                        DOCKER_IMAGE.push()
                    }
                }
            }
        }
    }
}
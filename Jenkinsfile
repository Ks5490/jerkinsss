pipeline {
    agent any 

    environment {
        IMAGE_NAME = 'ks5490/terraform_spartan_project:JK.' + "$BUILD_NUMBER"
        DOCKER_CRED = 'docker_hub_cred'
    }

    stages {
            
        stage('Cloning the project from GitHub'){
            steps {
                checkout([
                    $class: 'GitSCM', branches: [[name: '*/main']],
                    serRemoteConfigs: [[
                        url: 'git@github.com:Ks5490/jerkinsss.git',
                        credentialsId: 'ssh_git_cred'
                    ]]
                ])
            }
        }

        stage('Build Docker Image'){
            steps {
                script {
                   DOCKER_IMAGE = docker.build IMAGE_NAME
                }
            }
        }

        stage('Testing the Code'){
            steps{
                script{
                    sh '''
                        docker run --rm -v $PWD/test-results:/reports --workdir /app $IMAGE_NAME pytest -v --junitxml=/reports/results.xml
                    '''
                }
            }
        

            post{
                always{
                    junitxml testResults: '**/test-results/*.xml'
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

        stage('Removing the docker image'){
            steps{
                sh "docker rmi $IMAGE_NAME"
            }
        }
    }
}
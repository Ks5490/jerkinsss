pipeline {
    agent any 

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
                    docker.Build 'ks5490/terraform_spartan_project:0.6'
                }
            }
        }
    }
}
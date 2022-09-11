pipeline {

    agent any
    environment {
        PATH = "/home/jenkins/.local/bin:${env.PATH}"
        DOCKER_HOST = "unix:///var/run/docker.sock"
        image_id = "${env.BUILD_ID}"
        GIT_REPO_NAME = env.GIT_URL.replaceFirst(/^.*?(?::\/\/.*?\/|:)(.*).git$/, '$1')
        SHORT_COMMIT = "${GIT_COMMIT[0..7]}"
    }

    options { disableConcurrentBuilds() }

    stages {

        stage("Run Setup Script") {
            steps {
                echo "run setup script"
                ansiColor('vga') {
                    sh """
                    python setup.py install
                    """
                }
            }
        }


        stage("run lint tests") {
            steps {
                echo "run all tests"
                ansiColor('vga') {
                    sh """
                    pylint binance/binance.py
                    """
                }
            }
        }
    }

    post {
        success {
            slackSend color: "good", message: "Repo: ${env.GIT_REPO_NAME}\nResult: ${currentBuild.currentResult}\nCommit: ${SHORT_COMMIT}\nBranch: ${env.GIT_BRANCH}\nExecution time: ${currentBuild.durationString.replace(' and counting', '')}\nURL: (<${env.BUILD_URL}|Open>)"
            sh 'docker-compose -f install/docker-compose_jenkins.yml -p $BUILD_ID down --rmi all'
            sh 'docker network prune -f'
        }
        failure { slackSend color: "danger", message: "Repo: ${env.GIT_REPO_NAME}\nResult: ${currentBuild.currentResult}\nCommit: ${SHORT_COMMIT}\nBranch: ${env.GIT_BRANCH}\nExecution time: ${currentBuild.durationString.replace(' and counting', '')}\nURL: (<${env.BUILD_URL}|Open>)"
        }
    }
}

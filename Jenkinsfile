pipeline {
  agent any
  stages {
    stage('Code checkout') {
      steps {
        git(url: 'https://github.com/H4CK3RD33P/Employee-Management-CRUD-Flask', branch: 'docker')
      }
    }

    stage('Test') {
      steps {
        echo 'Starting unittests'
        sh 'export DATABASE_URL=sqlite:///employee.db && pip3 install -r requirements.txt && pip3 install nose && nosetests --with-xunit'
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t h4ck3rd33p/employee-management-flask-app:latest .'
        sh '''echo $USER
'''
      }
    }

  }
}
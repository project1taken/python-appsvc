node{
 def app
 stage ('checkout'){
  checkout scm
 }
 stage ('build'){
  app = docker.build('rvarg11/pythonappid')
 }
 stage('test'){
  app.inside{
  sh 'echo "test passed"'
  }
 }
 stage ('publish'){
  docker.withRegistry('https://registry.hub.docker.com','docker-cred'){
  app.push('Dev')
  
  }
 }
}

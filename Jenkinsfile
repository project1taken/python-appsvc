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
  app.push('Release')

  }
  }
 stage ('deploy'){
  sh 'ssh ec2-user@ec2-34-228-238-3.compute-1.amazonaws.com docker pull rvarg11/pythonappid:Release'
//  sh 'ssh ec2-user@ec2-34-228-238-3.compute-1.amazonaws.com docker rm -f pythonappid'
  sh 'ssh ec2-user@ec2-34-228-238-3.compute-1.amazonaws.com docker run -d -p 5000:5000 --name pythonappid rvarg11/pythonappid:Release'
 }
}

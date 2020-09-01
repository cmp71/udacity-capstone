## High level
* Create Cloudformation to deploy/initialise a kubernetes cluster
  * Could be on AWS Kubernetes as a Service
    * https://docs.aws.amazon.com/eks/index.html
    * https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html
* Find a public docker image with a Hello World python app
* Need a pipeline in Jenkins
  * Re-start Jenkins AWS box
* Look for example of blue/green deployment on AWS Kubernetes
Need to lint the app and the docker image

## Rubric
* Everything in GitHub
* Docker image(s) in a repository
* Linting included in pipeline
  * Screenshots of failure and pass
* Build docker image from Dockerfile via pipeline
* Kubernetes cluster deployed with Cloudformation
  * Cloudformation code in GitHub
* Blue/Green or Rolling Deployment
  * Provide screenshots

#!/bin/bash

read -p "Enter environment ( dev | test | staging | production ): " env
echo "You entered: $env"

project="cloudverse-dev-410808"
cluster="dev"
if [ $env = "dev" ] || [ $env = "test" ]
then
  project="cloudverse-dev-410808"
  cluster="dev"
elif [ $env = "staging" ] 
then
  project="cloudverse-staging"
  cluster="staging"
elif [ $env = "production" ] 
then
  project="cloudverse-production"
  cluster="production"
fi

gcloud config set project $project
gcloud container clusters get-credentials $cluster --region asia-southeast1

kubectl -n $env get pods
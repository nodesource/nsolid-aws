#!/bin/bash

if [[ ! -e ~/.aws/credentials ]]; then
  echo "No credentials present for the AWS CLI"
  exit 1
fi

for file in templates/*.json; do
  echo ""
  echo "Validating $file"
  aws cloudformation validate-template --template-body file://$file
  rc=$?
  echo ""
  if [[ $rc != 0 ]]; then
    exit $rc
  fi
done
echo "Templates are valid. Uploading..."
echo ""

BUCKET="nodesource-public-cloudformation"
aws s3 sync ./templates s3://$BUCKET/nsolid/
echo "Templates Updated"

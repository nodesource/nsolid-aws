#!/bin/bash -e

if [[ ! -e ~/.aws/credentials ]]; then
  echo "No credentials present for the AWS CLI"
  exit 1
fi

BUCKET="nodesource-public-cloudformation"

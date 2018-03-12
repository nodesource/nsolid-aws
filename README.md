![N|Solid](/images/nsolid-aws.png)

# N|Solid on AWS

[Amazon Web Services](https://aws.amazon.com/) (AWS) offers reliable, scalable, and inexpensive cloud computing services. Deploy your [N|Solid](https://nodesource.com/products/nsolid) instances to AWS for cloud access to the only Node.js platform built for mission-critical applications.

## Getting Started

Easily run N|Solid in AWS using our [CloudFormation Templates](templates/). You can find a list of templates and their descriptions in the template's [README.md](/templates/README.md). Once you find a template you want to use, simply click the deploy button.

Follow these steps to use the [CloudFormation](https://aws.amazon.com/cloudformation/) templates in `aws-nsolid`:

1. Find the template you want to run in the `/templates` folder, then click the **Deploy to AWS** button.

2. This will open up CloudFormation in your own account. Click the **Next** button.

3. Fill in the required parameters and change the `Stack Name` if desired. Then click the **Next** button.

4. Adjust any CloudFormation options if desired. Click **Next**.

5. If the template requires IAM capabilities, you will need to check the "I acknowledge that AWS CloudFormation might create IAM resources with custom names." box. Once you are ready, click the **Create** button.

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-quick-start.json)

## AMI List

You can also use our N|Solid AMIs for your own projects. See [AMI-LIST.md](AMI-LIST.md) for a full list of AMI IDs in every region.

# N|Solid CloudFormation Templates


## `nsolid-console-ecs`

**Description**

blah blah blah

_Resources Created_

|           Resource            |
|-------------------------------|
|      ECS Service IAM Role     |
|       ECS Task IAM Role       |
|        Security Group         |
| Classic Elastic Load Balancer |
|      ECS Task Definition      |
|          ECS Service          |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-ecs.json)


## `nsolid-console-ecs-with-cluster`

**Description**

blah blah blah

_Resources Created_

|           Resource            |
|-------------------------------|
|         ECS Cluster           |
|         EC2 Instance          |
|       AutoScaling Group       |
|      Launch Configuration     |
|      ECS Service IAM Role     |
|       ECS Task IAM Role       |
|       2 Security Groups       |
| Classic Elastic Load Balancer |
|      ECS Task Definition      |
|          ECS Service          |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-ecs-with-cluster.json)


## `nsolid-console-elb`

**Description**

blah blah blah

_Resources Created_

|           Resource            |
|-------------------------------|
|         EC2 Instance          |
|       AutoScaling Group       |
|      Launch Configuration     |
|       2 Security Groups       |
| Classic Elastic Load Balancer |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-elb.json)


## `nsolid-console-only`

**Description**

blah blah blah

_Resources Created_

|           Resource            |
|-------------------------------|
|         EC2 Instance          |
|        Security Group         |
|    Elastic IP **(optional)**    |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-only.json)


## `nsolid-console-route53`

**Description**

blah blah blah

_Resources Created_

|           Resource            |
|-------------------------------|
|         EC2 Instance          |
|        Security Group         |
|    Elastic IP **(optional)**    |
|       Route53 A Record        |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-route53.json)

## `nsolid-quick-start`

**Description**

blah blah blah

_Resources Created_

|           Resource            |
|-------------------------------|
|        2 EC2 Instances        |
|       2 Security Groups       |
|         2 Elastic IPs         |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-quick-start.json)


## `nsolid-runtime-only`

**Description**

blah blah blah

_Resources Created_

|           Resource            |
|-------------------------------|
|         EC2 Instance          |
|        Security Group         |
|    Elastic IP _(optional)_    |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-runtime-only.json)

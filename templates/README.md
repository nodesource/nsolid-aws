# N|Solid CloudFormation Templates

_These templates are provided as a way of getting started. Before using them in production please make the necessary security updates._

## `nsolid-console-ecs`

**Description**

Runs N|Solid Console in Amazon Elastic Container Service on an existing cluster. This will create an ECS Service and Task Definition, as well as a Classic Load Balancer. Services and Tasks are given proper IAM privileges to automatically attach to the Load Balancer. After the stack is created, the Outputs tab will have the URL of the Load Balancer. Simply load the URL in your browser to view the console. In your N|Solid Runtime, set the `NSOLID_COMMAND` variable to the URL to send data from your processes.

_Parameters Required_

|      Parameter      |            Description           |
|---------------------|----------------------------------|
|     ClusterName     |   Name of existing ECS Cluster   |
| LoadBalancerSubnets | Subnet IDs for the Load Balancer |
|         VPC         | VPC ID that contains the Subnets |

_Resources Created_

|           Resource            |
|-------------------------------|
|      ECS Service IAM Role     |
|       ECS Task IAM Role       |
|        Security Group         |
|     Classic Load Balancer     |
|      ECS Task Definition      |
|          ECS Service          |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-ecs.json)


## `nsolid-console-ecs-with-cluster`

**Description**

Runs N|Solid Console in Amazon Elastic Container Service on a newly created cluster. This will create an ECS Cluster, Service, and Task Definition, as well as a Classic Load Balancer. The ECS Cluster is setup using an Autoscaling Group for automatic replacement in the event of an instance failure. Services and Tasks are given proper IAM privileges to automatically attach to the Load Balancer. After the stack is created, the Outputs tab will have the URL of the Load Balancer. Simply load the URL in your browser to view the console. In your N|Solid Runtime, set the `NSOLID_COMMAND` variable to the URL to send data from your processes.

_Parameters Required_

|      Parameter      |            Description           |
|---------------------|----------------------------------|
|       SSHKey        |        Amazon EC2 Key Pair       |
|     HostSubnet      |   Subnet to put the ECS Host in  |
| LoadBalancerSubnets | Subnet IDs for the Load Balancer |
|         VPC         | VPC ID that contains the Subnets |

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
|     Classic Load Balancer     |
|      ECS Task Definition      |
|          ECS Service          |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-ecs-with-cluster.json)


## `nsolid-console-elb`

**Description**

Runs N|Solid Console on an EC2 Instance that is behind a Classic Load Balancer. The EC2 Instance is setup using an Autoscaling Group for automatic replacement in the event of an instance failure. The Autoscaling Group is attached to the Load Balancer so instance registration is also automatic. After the stack is created, the Outputs tab will have the URL of the Load Balancer. Simply load the URL in your browser to view the console. In your N|Solid Runtime, set the `NSOLID_COMMAND` variable to the URL to send data from your processes.

_Parameters Required_

|      Parameter      |             Description              |
|---------------------|--------------------------------------|
|       SSHKey        |         Amazon EC2 Key Pair          |
|     ConsoleSubnet   | Subnet ID to run N Solid Console in  |
| LoadBalancerSubnets |   Subnet IDs for the Load Balancer   |
|         VPC         |   VPC ID that contains the Subnets   |

_Resources Created_

|           Resource            |
|-------------------------------|
|         EC2 Instance          |
|       AutoScaling Group       |
|      Launch Configuration     |
|       2 Security Groups       |
|      Classic Load Balancer    |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-elb.json)


## `nsolid-console-nlb`

**Description**

Runs N|Solid Console on an EC2 Instance that is behind a Network Load Balancer. The EC2 Instance is setup using an Autoscaling Group for automatic replacement in the event of an instance failure. The Autoscaling Group is attached to each Target Group based on the port number so instance registration is also automatic. The Target Groups are associated with the Load Balancer via the Listeners. After the stack is created, the Outputs tab will have the URL of the Load Balancer. Simply load the URL in your browser to view the console. In your N|Solid Runtime, set the `NSOLID_COMMAND` variable to the URL to send data from your processes.

_Parameters Required_

|      Parameter      |             Description              |
|---------------------|--------------------------------------|
|       SSHKey        |         Amazon EC2 Key Pair          |
|     ConsoleSubnet   |  Subnet ID to run NSolid Console in  |
| LoadBalancerSubnets |   Subnet IDs for the Load Balancer   |
|         VPC         |   VPC ID that contains the Subnets   |

_Resources Created_

|           Resource            |
|-------------------------------|
|         EC2 Instance          |
|       AutoScaling Group       |
|      Launch Configuration     |
|         Security Group        |
|        4 Target Groups        |
|          4 Listeners          |
|      Network Load Balancer    |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-nlb.json)


## `nsolid-console-only`

Runs N|Solid Console on an EC2 Instance. The EC2 Instance is configured with a Security Group that allows traffic from `0.0.0.0/0` on ports `80`, `9001`, `9002`, `9003`. By default the EC2 Instance does not get a public IP address. If you set the `PublicAccess` parameter to `Enabled`, then the Console server will get an Elastic IP address. After the stack is created, the Outputs tab will have the IP address of the instance. Simply load the IP address in your browser to view the console. In your N|Solid Runtime, set the `NSOLID_COMMAND` variable to the IP address to send data from your processes.

_Parameters Required_

|      Parameter      |                    Description                          |
|---------------------|---------------------------------------------------------|
|    Public Access    | If Enabled, the Console instance will get an Elastic IP |
|       SSHKey        |                Amazon EC2 Key Pair                      |
|     ConsoleSubnet   |         Subnet ID to run NSolid Console in              |  
|      ConsoleVPC     |          VPC ID that contains the Subnets               |

_Resources Created_

|           Resource            |
|-------------------------------|
|         EC2 Instance          |
|        Security Group         |
|    Elastic IP _(optional)_    |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-only.json)


## `nsolid-console-route53`

**Description**

Runs N|Solid Console on an EC2 Instance. The EC2 Instance is configured with a Security Group that allows traffic from `0.0.0.0/0` on ports `22`, `80`, `9001`, `9002`, `9003`. By default the EC2 Instance does not get a public IP address. If you set the `PublicAccess` parameter to `Enabled`, then the Console server will get an Elastic IP address. This will also create a Route53 A Record that points to your EC2 Instance. After the stack is created, the Outputs tab will have the IP address of the instance, as well as the domain name you gave your N|Solid Console server. Simply load the IP address or domain name in your browser to view the console. In your N|Solid Runtime, set the `NSOLID_COMMAND` variable to the IP address or domain name to send data from your processes.

_Parameters Required_

|      Parameter      |                    Description                          |
|---------------------|---------------------------------------------------------|
|    Public Access    | If Enabled, the Console instance will get an Elastic IP |
|       SSHKey        |                Amazon EC2 Key Pair                      |
|     ConsoleSubnet   |         Subnet ID to run NSolid Console in              |  
|      ConsoleVPC     |          VPC ID that contains the Subnets               |
|     Route53Zone     |         Route53 Hosted Zone ID of DNS Record            |
|      ConsoleURL     |           Domain Name for NSolid Console                |

_Resources Created_

|           Resource            |
|-------------------------------|
|         EC2 Instance          |
|        Security Group         |
|    Elastic IP _(optional)_    |
|       Route53 A Record        |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-console-route53.json)

## `nsolid-quick-start`

**Description**

Runs N|Solid Console and N|Solid Runtime on separate EC2 Instances. The EC2 Instances are configured with a Security Group that allows traffic from `0.0.0.0/0` on ports `22`, `80`, `9001`, `9002`, `9003`. Both of the EC2 Instances get Elastic IP addresses. After the stack is created, the Outputs tab will have the IP address of both instances. Simply load the N|Solid Console IP address in your browser to view the console. In your N|Solid Runtime, set the `NSOLID_COMMAND` variable to the N|Solid Console IP address to send data from your processes.

_Parameters Required_

|      Parameter      |                    Description                          |
|---------------------|---------------------------------------------------------|
|       SSHKey        |                Amazon EC2 Key Pair                      |
|     ConsoleSubnet   |         Subnet ID to run NSolid Console in              |  
|      ConsoleVPC     |          VPC ID to run NSolid Console in                |
|     RuntimeSubnet   |         Subnet ID to run NSolid Runtime in              |  
|      RuntimeVPC     |          VPC ID to run NSolid Runtime in                |

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

Runs N|Solid Runtime on an EC2 Instance. The EC2 Instance is configured with a Security Group that allows traffic from `0.0.0.0/0` on port `22`. By default the EC2 Instance does not get a public IP address. If you set the `PublicAccess` parameter to `Enabled`, then the Runtime server will get an Elastic IP address. After the stack is created, the Outputs tab will have the IP address of the instance. Simply SSH to the IP address to configure your application. In your N|Solid Runtime, set the `NSOLID_COMMAND` variable to the URL or IP of your N|Solid Console server to send data from your processes.

_Parameters Required_

|      Parameter      |                    Description                          |
|---------------------|---------------------------------------------------------|
|    Public Access    | If Enabled, the Runtime instance will get an Elastic IP |
|       SSHKey        |                Amazon EC2 Key Pair                      |
|     RuntimeSubnet   |         Subnet ID to run NSolid Runtime in              |  
|      RuntimeVPC     |          VPC ID that contains the Subnets               |

_Resources Created_

|           Resource            |
|-------------------------------|
|         EC2 Instance          |
|        Security Group         |
|    Elastic IP _(optional)_    |

**Deploy**

[![Launch Stack CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=nsolid-console-autoscaling&templateURL=https://s3-us-west-2.amazonaws.com/nodesource-public-cloudformation/nsolid/nsolid-runtime-only.json)

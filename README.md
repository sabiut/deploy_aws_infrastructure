# Deploy aws infrastructure

This is a python boto 3 application that i wrote and use it to deploy AWS instances on a public and private network. It is using an encrypted AMI that i have created. Before running the application you need to set a valid AMI.

When you run the app it will generate a file containing your key pair in the root directory. You can use the key pair to ssh to your EC2 instances

#what the application does
1) create a VPC with a private and public network on diffeent availability Zones
2) Backet
3) setup the gateway
4) Create security group
5) Launched two instance one in public and another in private network

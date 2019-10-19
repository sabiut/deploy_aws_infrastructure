from src.ec2.ec2 import Ec2Services
from src.create_vpc.createvpc import CreateVpc
from src.ec2.other_featurs import Features


class EC2(CreateVpc):
    def createec2(self, create_vpcid):

        # Create and launching Ec2 Instances
        ec2 = Ec2Services(create_vpcid.ec2_client)

        # Create a key pair
        create_key = Features()
        key_pair_name = 'companykeyPair'
        print('Creating  key pair:', key_pair_name, "\n")
        outfile = open('companykeyPair.pem', 'w')
        key_pair = create_key.create_key_pair(key_pair_name)
        KeyPairOut = str(key_pair.key_material)
        print(KeyPairOut)
        outfile.write(KeyPairOut)
        print('Key Pair:', key_pair_name, 'was successfully created \n')


        # Creating a Security Group
        print("Creating Public security group ....")
        pub_security_group_name = 'company-public'
        pub_security_group_description = 'Public Security Group'
        pub_security_group = ec2.new_security_group(pub_security_group_name, pub_security_group_description, create_vpcid.vpc_id)
        print(" Security group:", pub_security_group_name, 'was successfully created \n')
        pub_security_group_id = pub_security_group['GroupId']

        # Add rules to the public security  Group
        print("Adding Security rules....")
        ec2.inbound_rule(pub_security_group_id)
        print('Security rules successfully added to the security group \n')

        # Script to be run on ubuntu server once the EC2 instance have launched
        install_update = """#!/bin/bash
                            sudo su
                            apt update -y
                            apt upgrade -y
                            apt install vsftpd -y
                            apt install apache2 -y"""



        # Ubuntu image to be installed
        amage_id = 'ami-01c5d6e337f97bbff'

        # Launch  our first web server EC2 Instance
        print("Launching the first instance ....")

        ec2.launch_our_ec2_instance(amage_id, key_pair_name, 1, 1, pub_security_group_id, create_vpcid.pub_subnetid, install_update)
        instance_one = 'company-Public-server'
        create_vpcid.vpc.addname_tag(amage_id, instance_one)
        print('The first instance was successfully launch.\n')

        # Create a private security group
        print("Creating private security group....")
        private_sg_name = 'company-private'
        private_sg_description = 'Private Security Group'
        private_sg = ec2.new_security_group(private_sg_name, private_sg_description, create_vpcid.vpc_id)
        print("Private security group was successfully created \n")
        private_sg_id = private_sg['GroupId']

        # Add rule to the newly created security group
        ec2.inbound_rule(private_sg_id)
        print("Rules successfully added to the private group \n")

        # Launch a private EC2 Instance
        print("Launching the second instances ....")
        ec2.launch_our_ec2_instance(amage_id,  key_pair_name, 1, 1, private_sg_id, create_vpcid.private_subnet_id, install_update)
        instance_second = 'company-Private-server'
        create_vpcid.vpc.addname_tag(amage_id, instance_second)
        print('The second instance was launch successfully\n')

        print("--------------------------------------------------------------------")
        print("##Congratulation your Cloud Infrastructure was Successfully Deployed ##")
        print("--------------------------------------------------------------------")


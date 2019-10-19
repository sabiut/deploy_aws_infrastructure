from src.ec2.vpc import VPC
from src.client import Ec2Client

# Create VPC
class CreateVpc:

    ec2_client = Ec2Client().get_client()

    def createvpc(self):
        # Deploy the new vpc
        self.ec2_client = Ec2Client().get_client()
        self.vpc = VPC(self.ec2_client)
        print("Creating VPC...")
        vpc_response = self.vpc.create_new_vpc()
        print(str(vpc_response), "has been created successfully \n")

        # Create VPC name tag
        vpc_name = 'company-VPC'
        self.vpc_id = vpc_response['Vpc']['VpcId']
        print("Adding the VPC name tag...")
        self.vpc.addname_tag(self.vpc_id, vpc_name)
        print("The name tag:", vpc_name, "was added successfully to", self.vpc_id)

        # Add a new internet gateway
        new_igw = self.vpc.create_new_igw()
        igw_id = new_igw['InternetGateway']['InternetGatewayId']
        self.vpc.attach_gateway_to_vpc(self.vpc_id, igw_id)
        print('The Internet Gateway ', igw_id, ' was successfully attached to  ' + self.vpc_id)

        # Create a new public subnet 10/24 for our public web server
        public_subnet = self.vpc.add_new_subnet(self.vpc_id, '10.0.10.0/24', 'us-east-1b')
        public_subnet1 = self.vpc.add_new_subnet(self.vpc_id, '10.0.12.0/24', 'us-east-1a')
        public_subnet2 = self.vpc.add_new_subnet(self.vpc_id, '10.0.13.0/24', 'us-east-1c')
        public_subnet3 = self.vpc.add_new_subnet(self.vpc_id, '10.0.14.0/24', 'us-east-1d')
        self.pub_subnetid = public_subnet['Subnet']['SubnetId']
        self.pub_subnetid1 = public_subnet1['Subnet']['SubnetId']
        self.pub_subnetid2 = public_subnet2['Subnet']['SubnetId']
        self.pub_subnetid3 = public_subnet3['Subnet']['SubnetId']
        print('Public Subnet:', str(public_subnet), "was successfully created \n")

        # Adding name tag to the Public Subnet
        self.vpc.addname_tag(self.pub_subnetid, 'Company-Public-Subnet')
        print("Public subnet name tag was successfully added \n")

        # Creating a routing table
        public_route_table = self.vpc.public_routing_table(self.vpc_id)
        rtb_id = public_route_table['RouteTable']['RouteTableId']
        print('The public routing table was created successfully')

        # Add the gateway to the routing table
        self.vpc.route_igw_torouting_table(rtb_id, igw_id)
        print("Gateway was successfully added to the routing table \n")

        # Associate Public Subnet with Route Table
        print("Associating  subnet with routing table...")
        self.vpc.associate_subnet_to_routingtable(self.pub_subnetid, rtb_id)
        self.vpc.associate_subnet_to_routingtable(self.pub_subnetid1, rtb_id)
        self.vpc.associate_subnet_to_routingtable(self.pub_subnetid2, rtb_id)
        self.vpc.associate_subnet_to_routingtable(self.pub_subnetid3, rtb_id)
        print('Successfully associating subnet', self.pub_subnetid, ' with routing Table ', rtb_id)

        # Auto assign ip address
        self.vpc.auto_assign_ip_addresses(self.pub_subnetid)
        self.vpc.auto_assign_ip_addresses(self.pub_subnetid1)
        self.vpc.auto_assign_ip_addresses(self.pub_subnetid2)
        self.vpc.auto_assign_ip_addresses(self.pub_subnetid3)


        # Create a Private Subnet for our private file server
        print("Creating private subnet...")
        private_subnet = self.vpc.add_new_subnet(self.vpc_id, '10.0.11.0/24', 'us-east-1b')
        self.private_subnet_id = private_subnet['Subnet']['SubnetId']
        print('Private subnet', private_subnet, 'was successfully created')

        # Add name tag to private subnet
        print("Adding private subnet name tag....")
        company_subnet = 'Company Private subnet'
        self.vpc.addname_tag(self.private_subnet_id, company_subnet)
        print("Private subnet name tag was successfully created \n")

        print("-------------------------------------------")
        print(" You have successfully Deployed your VPC")
        print("-------------------------------------------")

        print("Deploying EC2 Instances ..........")

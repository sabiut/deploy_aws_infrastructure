class VPC:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.ec2 """

     # Create a new vps
    def create_new_vpc(self):
        return self._client.create_vpc(
            CidrBlock='10.0.0.0/16',
            AmazonProvidedIpv6CidrBlock = True,
            InstanceTenancy = 'default'

        )

    # Create name tags
    def addname_tag(self, resourceid, resourcename):
        return self._client.create_tags(
            Resources=[resourceid],
            Tags=[{
                'Key': 'Name',
                'Value': resourcename
            }]
        )

    # Add a new internet gateway
    def create_new_igw(self):
        return self._client.create_internet_gateway()

    # Attached the gateway to our VPC
    def attach_gateway_to_vpc(self, vpc_id, igw_id):
        return self._client.attach_internet_gateway(
            InternetGatewayId=igw_id,
            VpcId=vpc_id
        )

    # Creating subnets
    def add_new_subnet(self, vpc_id, cidr_block,zone):
        return self._client.create_subnet(
            VpcId=vpc_id,
            CidrBlock=cidr_block,
            AvailabilityZone=zone,



        )

     # Create a routing table
    def public_routing_table(self, vpc_id):
        return self._client.create_route_table(VpcId=vpc_id)

    # Defining routing rule for in the routing table
    def route_igw_torouting_table(self, rtb_id, igw_id):
        print('Adding route for IGW ' + igw_id + ' to Route Table ' + rtb_id)
        return self._client.create_route(
            RouteTableId=rtb_id,
            GatewayId=igw_id,
            DestinationCidrBlock='0.0.0.0/0'
        )

    # Associate the public subnet to routing table
    def associate_subnet_to_routingtable(self, subnet_id, rtb_id):
        return self._client.associate_route_table(
            SubnetId=subnet_id,
            RouteTableId=rtb_id
        )

    # auto assign public ip address
    def auto_assign_ip_addresses(self, subnet_id):
        return self._client.modify_subnet_attribute(
            SubnetId=subnet_id,
            MapPublicIpOnLaunch={'Value': True}
        )
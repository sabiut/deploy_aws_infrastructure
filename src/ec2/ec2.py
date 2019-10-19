class Ec2Services:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.ec2 """


    # Creating security groups
    def new_security_group(self, group_name, description, vpc_id):
        return self._client.create_security_group(
            GroupName=group_name,
            Description=description,
            VpcId=vpc_id
        )

    # Adding security rules to the group
    def inbound_rule(self, security_group_id):
        self._client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                },

                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }

            ]
        )
    # Launching our EC2 instances
    def launch_our_ec2_instance(self, image_id, key_name, min_count, max_count, security_group_id, subnet_id, user_data):
        return self._client.run_instances(
            ImageId=image_id,
            KeyName=key_name,
            MinCount=min_count,
            MaxCount=max_count,
            InstanceType='t2.micro',
            SecurityGroupIds=[security_group_id],
            SubnetId=subnet_id,
            UserData=user_data,

        )




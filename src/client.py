import boto3

class FindClient:
    def __init__(self, client):
        self.client = boto3.client(client, region_name="us-east-1")

    def get_client(self):
        return self.client


class Ec2Client(FindClient):
    def __init__(self):
        super().__init__('ec2')
import boto3

class Features:
    # Create Bucket
    def create_bucket(self):
        print("creating  Bucket ......")
        bucketname = 'compxhiuytrdsewaq'
        client = boto3.client('s3')
        client.create_bucket(
            ACL='private',
            Bucket=bucketname
        )
        print("Bucket was created successfully")

    # Retrieve the list of existing buckets
    def list_of_bucket(self):
        self.client = boto3.client('s3')
        response = self.client.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'{bucket["Name"]}', '\n')

    # Creating a key pair
    def create_key_pair(self, key_name):
        self.client = boto3.resource('ec2')
        return self.client.create_key_pair(KeyName=key_name)






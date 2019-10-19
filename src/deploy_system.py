from src.create_vpc.createvpc import CreateVpc
from src.create_ec2.createec2 import EC2
from src.ec2.other_featurs import Features


def mainprogram():

    create_bucket = Features()
    create_bucket.create_bucket()
    create_bucket.list_of_bucket()
    create_vpc = CreateVpc()
    create_vpc.createvpc()
    create_ec2 = EC2()
    create_ec2.createec2(create_vpc)


# Deploy the cloud System
if __name__ == '__main__':
    mainprogram()

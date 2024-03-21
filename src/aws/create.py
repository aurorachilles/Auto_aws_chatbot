import boto3
import os
from dotenv import load_dotenv
from src.aws.conf.func import finalize
import time

load_dotenv()

AWS_ID = os.getenv("aws_id")
AWS_KEY = os.getenv("aws_key")
AWS_REGION = os.getenv("aws_region")


def create_ec2(val: list[str]) -> bool:
    conf = finalize(val)
    if not conf:
        return False
    else:
        instance_type, instance_image, storage_type, security_g, min_count, max_count, key_name, instance_name = conf

    try:
        ec2 = boto3.client(instance_type, region_name=AWS_REGION, aws_access_key_id=AWS_ID,
                           aws_secret_access_key=AWS_KEY)
        print("Creating Instance. Please wait...")

        response = ec2.run_instances(
            ImageId=instance_image,
            InstanceType=storage_type,
            SecurityGroupIds=[security_g],
            KeyName=key_name,
            MinCount=int(min_count),
            MaxCount=int(max_count),
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{
                    'Key': 'Name',
                    'Value': instance_name
                }]
            }]
        )

        print("Instance launched successfully!")
        print("Fetching instance information. This may take a few minutes.")
        time.sleep(10)

        public_ip = (ec2.describe_instances(InstanceIds=[response['Instances'][0]['InstanceId']]))['Reservations'][0]['Instances'][0]['PublicIpAddress']
        inst_name = (ec2.describe_instances(InstanceIds=[response['Instances'][0]['InstanceId']]))['Reservations'][0]['Instances'][0]['Tags'][0]['Value']
        inst_id = (ec2.describe_instances(InstanceIds=[response['Instances'][0]['InstanceId']]))['Reservations'][0]['Instances'][0]['InstanceId']

        print("Instance launched at IP: http://",public_ip, "named: ", inst_name, "with ID: ", inst_id)
        return True

    except Exception as e:
        print("Instance creation failed")
        print("Error in boto3 Client")
        print("Error: ", e)
        return False

#
# instance_id = response['Instances'][0]['InstanceId']
# print('Launched EC2 instance with ID:', instance_id)

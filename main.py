
import boto3
#this folder will not be found on github. These are my personal credientials to my AWS account
from credentials import aws_secret_id,aws_secret_key,region


instance_type = 't2.micro'
image_id="ami-03f4878755434977f"
security_group = "sg-0137aa7387b9c41fa"
name_of_instance = "vishal_instance_1"

ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=aws_secret_id, aws_secret_access_key=aws_secret_key)

response = ec2.run_instances(
    ImageId=image_id,
    InstanceType= instance_type,
    SecurityGroupIds=['sg-0137aa7387b9c41fa'],
    KeyName='new_gen',
    MaxCount = 1,
    MinCount = 1,  
    TagSpecifications=[{
        'ResourceType':'instance',
        'Tags':[{
            'Key':'Name',
            'Value':name_of_instance
        }]
    }]
)


instance_id = response['Instances'][0]['InstanceId']
print('Launched EC2 instance with ID:', instance_id)
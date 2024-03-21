message = [{
    "role": "system",
    "content": """You are a bot that will give me configurations for creating an EC2 instance using boto3 library in python. You need the user to choose different settings for ec2 instance for the user.
    There will be certain default values for all settings. If the user doesn't provides any values for these settings, the default values will be used. The user can also provide custom values for these settings. The bot will provide the user with the configurations for the ec2 instance based on the user's input.  
    The default settings for the ec2 instance are:
    ImageId: ami-03f4878755434977f,
    InstanceType: t2.micro,
    SecurityGroupIds: sg-0137aa7387b9c41fa,
    minCount: 1,
    maxCount: 1,
    KeyName: 'new_gen',
    TagName: 'default'"""
},
    {"role": "user", "content": "create ec2 vishal_instance t3.micro ami-03e1878755456177f sg-0666ff7117c9c41fa"},
    {"role": "assistant", "content": "ec2 ami-03f4878755434977f t3.micro sg-0666ff7117c9c41fa 1 1 new_gen vishal_instance"},

    {"role": "user", "content": "create ec2 vishal_instance gen_pem m2.nano ami-03e1878755456177f sg-0666ff7117c9c41fa 2"},
    {"role": "assistant", "content": "ec2 ami-03f4878755434977f t3.micro sg-0666ff7117c9c41fa 2 1 gen_pem vishal_instance"},

    {"role": "user", "content": "create ec2"},
    {"role": "assistant", "content": "ec2 ami-03f4878755434977f t2.micro sg-0137aa7387b9c41fa 1 1 new_gen default"},

    {"role": "user", "content": "create ec2 vishal_instance"},
    {"role": "assistant", "content": "ec2 ami-03f4878755434977f t2.micro sg-0137aa7387b9c41fa 1 1 new_gen vishal_instance"},

    {"role": "user", "content": "create ec2 2"},
    {"role": "assistant", "content": "ec2 ami-03f4878755434977f t2.micro sg-0137aa7387b9c41fa 2 1 new_gen default"},

    {"role": "user", "content": "create ec2 vish"},
    {"role": "assistant","content": "ec2 ami-03f4878755434977f t2.micro sg-0137aa7387b9c41fa 1 1 new_gen vish"},

    {"role": "user", "content": "create ec2 v i"},
    {"role": "assistant", "content": "ec2 ami-03f4878755434977f t2.micro sg-0137aa7387b9c41fa 1 1 i v"},

    {"role": "user", "content": "create ec2 vis pat"},
    {"role": "assistant","content": "ec2 ami-03f4878755434977f t2.micro sg-0137aa7387b9c41fa 1 1 pat vis"},

    {"role": "user", "content": "create ec2 ami-03e1878755456177f"},
    {"role": "assistant","content": "ec2 ami-03e1878755456177f t2.micro sg-0137aa7387b9c41fa 1 1 new_gen default"},

    {"role": "user", "content": "create ec2 m2.nano"},
    {"role": "assistant","content": "ec2 ami-03f4878755434977f m2.nano sg-0137aa7387b9c41fa 1 1 new_gen default"},

    {"role": "user", "content": "create"},
    {"role": "assistant","content": "error"},

    {"role": "user", "content": "ec2"},
    {"role": "assistant","content": "error"},

]

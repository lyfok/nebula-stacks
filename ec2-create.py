import boto3

myec2 = boto3.resource('ec2')
myinstance = myec2.create_instances(
    BlockDeviceMappings=[
        {
            'Ebs': {
                'DeleteOnTermination': True,
                'Iops': 3000,
                'VolumeSize': 8,
                'VolumeType': 'gp3',
                'Encrypted': True,
                'Throughput': 125
            },
            'DeviceName': '/dev/xvda'
        },
    ],
    ImageId='ami-0af9569868786b23a',
    InstanceType= 't2.micro',
    KeyName='my-jen',
    MaxCount=1,
    MinCount=1,
)
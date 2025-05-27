import boto3

ec2_client = boto3.resource('ec2')
my_insta = ec2_client.create_instances(
    ImageId='ami-0af9569868786b23a',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
)
my_insta[0].create_tags(
    Tags=[
        {
            'Key': 'name',
            'Value': 'Fruit'
        },
    ]    

)


import boto3

my_ec2_client = boto3.resource('ec2')
my_insta=my_ec2_client.create_instances(
    ImageId='ami-0af9569868786b23a',
    InstanceType='t2.micro',
    MaxCount=2,
    MinCount=2
)
i=1
for x in my_insta:
    n='id-'+str(i)
    x.create_tags(
        Tags=[
        {
            'Key': 'roll',
            'Value': n
        },
    ]
   
    )
    i=i+1
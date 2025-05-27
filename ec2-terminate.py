import boto3

my_client = boto3.client('ec2')
my_inst_ter= my_client.terminate_instances(
    InstanceIds=[
        'i-0e0c491e71ce71f8e',
        'i-02433e8fb36a653fe'
    ],
)
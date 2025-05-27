import boto3

myec2 = boto3.client('ec2')
response = myec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ],
)
i=response['Reservations']
for x in i:
    for y in x['Instances']:
        print('instanse id is'+' ',y['InstanceId'])


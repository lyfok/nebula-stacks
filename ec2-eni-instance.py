import boto3

myec2 = boto3.client('ec2')
myinstance = myec2.describe_instances(
    InstanceIds=['i-01b0699cb13f44638']
)
i=myinstance['Reservations']
for x in i:
    for y in x['Instances']:
        in_id=y['InstanceId']
        for z in y['NetworkInterfaces']:
            print(in_id,' ',z['NetworkInterfaceId'])

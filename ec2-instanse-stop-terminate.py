import boto3

myec2 = boto3.client('ec2')
response = myec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped',
            ]
        },
    ],
)
i=response['Reservations']
l=[]
for x in i:
    for y in x['Instances']:
        #for s in y:
            l.append(y['InstanceId'])
if len(l) > 0:
      print('Instances will be deleted now')
      for x in l:
            myec2.terminate_instances(
                  InstanceIds=[x],
            )           
            
            



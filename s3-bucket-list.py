import boto3

my_client = boto3.client('s3')
response = my_client.list_buckets(
    MaxBuckets=12
)

i=response['Buckets']
l=[]
for x in i:
    l.append(x['Name'])
print('####Please find bucket name##')
print(l)
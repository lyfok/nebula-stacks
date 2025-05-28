import boto3
my_s3 = boto3.client('s3')
response = my_s3.list_objects(
    Bucket='all-bottle-in'
)
i=response['Contents']
for x in i:
    print(x['Key'])
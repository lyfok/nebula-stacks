import boto3
my_s3 = boto3.client('s3')
response = my_s3.list_buckets(
    MaxBuckets=12,
)
i=response['Buckets']
print('Please find bucket details')
print()
for x in i:
    buck=x['Name']
    print(buck)
    print('Now below buckets will be deleted:',buck)   
    my_s3.delete_bucket(
    Bucket=buck
)
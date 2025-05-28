import boto3

my_client = boto3.client('s3')
response = my_client.create_bucket(
    Bucket='all-bottle-out',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }    
)
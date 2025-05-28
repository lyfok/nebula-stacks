import boto3
my_s3 = boto3.client('s3')
response = my_s3.list_objects(
    Bucket='all-bottle-in'
)
i=response['Contents']
for x in i:
    k=x['Key']
    print('Now object deletion will start',k)    
    my_s3.delete_object(
        #Bucket='all-bottle-in'
        Key=k,
        Bucket='all-bottle-in'
        
    )


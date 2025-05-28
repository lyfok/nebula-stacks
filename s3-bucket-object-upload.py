import boto3
my_s3 = boto3.client('s3')
my_s3.upload_file(r"C:\Users\bhaba\OneDrive\Desktop\1748171305497.pdf", "all-bottle-in", "1748171305497.pdf")
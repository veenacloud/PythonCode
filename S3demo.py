import boto3
import pandas 
# Creating the low level functional client
client = boto3.client('s3')
    
# Creating the high level object oriented interface
resource = boto3.resource('s3')

# Fetch the list of existing buckets
clientResponse = client.list_buckets()
    
# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')

# Print the file names one by one
print('Printing files names from bucket..')
for key in client.list_objects(Bucket='veenasbucket')['Contents']:
    print(key['Key'])



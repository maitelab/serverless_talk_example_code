import boto3

# Let's use Amazon S3 storage system
s3 = boto3.resource('s3')

# Upload a new file
data = open('sample_data.csv', 'rb')
s3.Bucket('incoming-data-ht').put_object(Key='sample_data8.csv', Body=data)

print("uploading to S3 completed")
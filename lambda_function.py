import json
import urllib.parse
import boto3
import csv

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        
        print ("_FIEST!about to get file and upload to dynamo: " + key)
        s3b = boto3.resource('s3')
        s3b.Bucket('incoming-data-ht').download_file(key, '/tmp/'+key)
        
        dynamodb = boto3.resource('dynamodb',region_name='us-east-2')
        table = dynamodb.Table('input_data')

        # read received file
        with open('/tmp/'+key) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                print(f'>>>{row[0]} works in the {row[1]} department')
                table.put_item(
                   Item={
                        'id': int(row[1]),
                        'friend': row[0]
                    }
                )
        return response['ContentType']
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e 

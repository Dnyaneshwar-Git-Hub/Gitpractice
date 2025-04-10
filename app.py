import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    names = [b['Name'] for b in buckets['Buckets']]
    return {
        'statusCode': 200,
        'body': json.dumps(names)
    }

from __future__ import print_function
import boto3
import os
import json
from urllib.parse import parse_qs

sns = boto3.client('sns')

snsArn = os.environ["snsArn"]

def lambda_handler(event, context):
    
    data = parse_qs(event["body"])
    
    message = {
        "From": data["From"],
        "Message": data["Body"]
    }
    
    sns.publish(
        TargetArn=snsArn,
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )

    twilioResponse = {
        "statusCode": 200,
        "headers": {
          'Content-Type': 'text/xml',
        },
        "body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response></Response>",
    }
    
    return twilioResponse
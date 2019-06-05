from __future__ import print_function
import boto3
import os
import json

sns = boto3.client('sns')

snsArn = os.environ["snsArn"]

def lambda_handler(event, context):
    
    body = event["body"]
    
    message = {
        "From": body["From"],
        "Message": body["Body"]
    }
    
    response = sns.publish(
        TargetArn=snsArn,
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )
    
    print(response)
    
    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
        '<Response></Response>'
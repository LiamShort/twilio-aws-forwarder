import boto3
import os
import json

sns = boto3.client('sns')

snsArn = os.environ["snsArn"]

def lambda_handler(event, context):
    
    data = event["body"]
    
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
import boto3
import os
import json

sns = boto3.client('sns')

snsArn = os.environ["snsArn"]

def lambda_handler(event, context):

    try: 
        data = event["body"]

        message = {
            "From": data["From"],
            "Message": data["Body"]
        }

        sns_response = sns_publish_func(message)
        return(sns_response)


    except:
        return{
            "message": "Incorrect Data Received"
        }

def sns_publish_func(message):

    sns_response = sns.publish(
        TargetArn=snsArn,
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )

    return(sns_response)

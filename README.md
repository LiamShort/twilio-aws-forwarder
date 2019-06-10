# TwilioForwarder

TwilioForwarder is a dynamic way of configuring SMS MFA, allowing users to create accounts or subscribe to services using a programmatic phone number, which forwards messages to a specified email address and phone number. <br/>

## Setup 

### AWS

TwilioForwarder uses the following AWS Services: 
* **API Gateway** - Endpoint which receives data from Twilio and invokes Lambda Function
* **Lambda** - Process the incoming message and invoke SNS Topic (Python 3.6)
* **SNS** - Forwards message to subscribers, via email and SMS<br/>

The application is deployed to AWS using the Serverless Framework. Download the Source Code from GitHub, insert the following details into the dev.yml file: 
* **region** - Region in which the application is deployed
* **phone_number** - Phone Number messages are forwarded to
* **email** - Email messages are forwarded to<br/>

Within the repo of the downloaded source code, run:
* **serverless deploy --aws-profile <INSERT_AWS_PROFILE>**<br/>

Once Serverless has finished deploying the application, take a note of the API Gateway Endpoint URL.<br/>

### Twilio

A Twilio account is required, this can be created at "**https://www.twilio.com/**".<br/>

A number should then be purchased, for a monthly charge of £1 per month, this can be done at https:/"**/www.twilio.com/console/phone-numbers/incoming**".<br/>

After the phone number is purchased, click into the number and under "**Messaging**" > "**A Message Comes In**". Select Webhook from the dropdown menu and insert the API Gateway Endpoint URL into the corresponding field. This will forward all incoming SMS messages to the endpoint.<br/>
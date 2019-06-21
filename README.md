# TwilioForwarder

TwilioForwarder is a dynamic way of configuring SMS MFA, allowing users to create accounts or subscribe to services using a programmatic phone number, which forwards messages to a specified email address and phone number.<br/>

## Setup

### AWS

TwilioForwarder uses the following AWS Services:
* **API Gateway** - Endpoint which receives data from Twilio and invokes Lambda Function
* **SNS** - Forwards message to subscribers, via email and SMS<br/>

The application is deployed to AWS using a Cloud Formation Template. It requires the following parameters:
* **Email Address** - Email messages are forwarded to
* **Phone Number** - Phone Number messages are forwarded to<br/>

### Twilio

A Twilio account is required, this can be created at "**https://www.twilio.com/**".<br/>

A number should then be purchased, for a monthly charge of £1 per month, this can be done at https:/"**/www.twilio.com/console/phone-numbers/incoming**".<br/>

After the phone number is purchased, click into the number and under "**Messaging**" > "**A Message Comes In**". Select Webhook from the dropdown menu and insert the API Gateway Endpoint URL into the corresponding field. This will forward all incoming SMS messages to the endpoint.<br/>

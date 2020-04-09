# nexmo-verify-lambda-python
A Flask based Python Lambda function for Nexmo Verify

## Prerequisites
* Python
* Pip

## Setup Instructions
Clone this repo from GitHub, then proceed.

### Requirements
Install the Nexmo SDK and Flask

```bash
pip install nexmo flask
```

### Environment
Rename `.env.default` to `.env` and add values to `NEXMO_API_KEY` and `NEXMO_API_SECRET` provided by your Vonage APIs account.

```bash
export FLASK_APP=app.py
export APPLICATION_SETTINGS=.env
flash run
```

### Usage

```bash

virtualenv venv --python=python3
source venv/bin/activate

npm init
npm install --save-dev serverless-wsgi serverless-python-requirements

pip install -r requirements.txt
sls wsgi serve

sls deploy

deactivate
```

Go to the URL provided by the deploy:

`https://7ulkcc7lw4.execute-api.us-east-1.amazonaws.com/dev`

returns the default message for the / endpoint

`https://7ulkcc7lw4.execute-api.us-east-1.amazonaws.com/dev/request/<to_number>/Vonage`

will return the `request_id`, and the to_number phone should receive a text with a `code`.

`https://7ulkcc7lw4.execute-api.us-east-1.amazonaws.com/dev/check/<request_id>/<code>`

will return a verification successful message with an `event_id`.

The `request` step gives you 5 minutes to follow up with a `check` step. If not able to do so, you can issue a `cancel` with the following URL.

https://7ulkcc7lw4.execute-api.us-east-1.amazonaws.com/dev/cancel/<request_id>



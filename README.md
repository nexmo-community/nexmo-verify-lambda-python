# nexmo-verify-lambda-python
A Flask based Python Lambda function for Nexmo Verify

## Prerequisites
* Python 3.7+
* Pip
* [Node.js](https://nodejs.org/en/) and npm
* [Serverless Framework](https://serverless.com/framework/docs/getting-started/)

## Setup Instructions
Clone this repo from GitHub, and navigate into the newly created directory to proceed.

### Environment
Rename `.env.default` to `.env` and add values to `NEXMO_API_KEY` and `NEXMO_API_SECRET` provided by your Vonage APIs account.

### Usage
To start, create a virtualenv from within the project root to contain the project as you proceed. Then activate it as follows:

```bash
virtualenv venv --python=python3
source venv/bin/activate
```

Next, initialize npm and follow the prompts selecting the defaults. Unless you desire to change any of them. Also, use npm to install needed dependencies for dev to enable Serverless and Lambda to work with the Flask app.

```bash
npm init
npm install --save-dev serverless-wsgi serverless-python-requirements
```

Now you can use pip to install the required Python dependencies. The dependencies are already listed in the requirements.txt, so instruct pip to use it.

```bash
pip install -r requirements.txt
```

#### Running Local
You can run the app locally and test things out, prior to deploying to AWS Lambda, you can serve it with the following command:

```bash
sls wsgi serve
```

By default this will serve the app at http://localhost:5000. Hitting `Ctrl+c` will close it down.

#### Deploy to Lambda
With all the above finished successfully, you can now use Serverless to deploy the app to AWS Lambda.

```bash
sls deploy
```

#### Available Endpoints
There are 4 URL endpoints available with this client:

* `/`
    - Doesn't perform any actions, but provides a quick way to test

* `/request/<to_number>/<brand>`
    - By passing 2 arguments the client requests a 2FA code to be sent to the `<to_number>` including the national identifier (such as 1 for US), along with a `<brand>` for a more visual identity in the SMS message.

* `/check/<request_id>/<code>`
    - You can then check a 2FA code by passing the `<request_id>` and the `<code` to the `/check` endpoint.

* `/cancel/<request_id>`
    - Sometimes, if a 2FA code gets lost, it is necessary to cancel a request. By passing the `<request_id>` to the `/cancel` endpoint you bypass the 5 minute wait to request a new code.

##### Examples:
Go to the URL provided by the deploy process. Below are some examples of what sample requests may look like:

`https://7ulasfasdasdfw4.execute-api.us-east-1.amazonaws.com/dev/`

The `/` endpoint returns the generic message.

`https://7ulasfasdasdfw4.execute-api.us-east-1.amazonaws.com/dev/request/15554443333/Vonage`

The `request` endpoint will return the `request_id`, and the to_number phone should receive a text with a `code`.

`https://7ulasfasdasdfw4.execute-api.us-east-1.amazonaws.com/dev/check/9807adsf0sae89fu0se87r0sf/654321`

The `check` endpoing will return a verification successful message with an `event_id`.

The `request` step grants you 5 minutes to follow up with a `check` step. If not able to do so, you can issue a `cancel` with the following URL.

`https://7ulasfasdasdfw4.execute-api.us-east-1.amazonaws.com/dev/cancel/9807adsf0sae89fu0se87r0sf`

#### Deactivating Virtualenv
To exit the virtualenv you can deactivate it, when desired.

```bash
deactivate
```

## Contributing

We love questions, comments, issues - and especially pull requests. Either open an issue to talk to us, or reach us on twitter: <https://twitter.com/VonageDev>.

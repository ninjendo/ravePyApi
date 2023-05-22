# Rave Python Serverless API

## Pre-req if using windows
- Install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
- You will need to have Docker installed for local development.

## Install Serverless Framework
If you don’t already have Node.js on your machine, [install it](https://nodejs.org/) first.

```bash
npm init -f
npm install --save-dev serverless-wsgi serverless-python-requirements serverless-api-gateway-throttling
npm install -g serverless
```

#### To uninstall serverless
> npm uninstall -g serverless

#### Test locally
> sls wsgi serve
or 
> python app.py
You can view swagger locally at http://127.0.0.1:5000/api
#### Deploy in AWS
> sls deploy

#### Delete stack
> sls remove

#### View logs
>sls logs -f app

#### Troubleshoot
- API won't redeploy to AWS due to some unknown CF error
Delete the CF stack manually from console. If delete failed, delete the stack while retaining the S3 bucket for it. After successful delete, delete S3 bucket manually.

#### References
- [Deploy Flask API as serverless](https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb)
- [Slim package configuration](https://github.com/UnitedIncome/serverless-python-requirements/issues/441)
- [Enabling CORS in API Gateway using serverless](https://www.serverless.com/framework/docs/providers/aws/events/apigateway/#enabling-cors)
- [More info on CORS in API Gateway](https://www.serverless.com/blog/cors-api-gateway-survival-guide)
- [Using API Key to secure Endpoints](https://lorenstewart.me/2017/10/24/serverless-framework-securing-aws-lambda-endpoints/)
- [API Key in Cloudfront](https://www.youtube.com/watch?v=Ygq4u0B0rF0)
  
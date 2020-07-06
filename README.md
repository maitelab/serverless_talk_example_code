# Source code from the tech talk: Building serverless software
Here you will find the example source code used for the tech talk.

## Requisites to run this software
- Create an Amazon AWS account
- Create a S3 bucket named "incoming-data-ht"
- Create a lambda function, use any name you want, associated to the S3 bucket as "trigger when S3 receives a file", copy the text from "lambda_function.py" into the lambda function
- Create a dynamo table named "input_data"
- Run upload_data_to_s3.py

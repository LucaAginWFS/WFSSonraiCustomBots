import logging
from arnparse import arnparse
import botocore
import boto3
import json

client = boto3.client('lambda')
resourceId = 'arn:aws:ec2:us-east-1:034135693578:instance/i-0ea92f62101214836'
parsesRes = arnparse(resourceId)

testObj = 'nothing'

stopReturn = client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:174388760268:function:TempFunction',
        InvocationType='Event',
        Payload=json.dumps({"test":"test"})
    )
print(stopReturn)

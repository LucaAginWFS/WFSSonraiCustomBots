import logging
import json
import sonrai.platform.aws.arn

def run(ctx):

    lambda_client = ctx.get_client().get('lambda', 'us-east-1')

    lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:174388760268:function:TempFunction',
        InvocationType='Event',
        Payload=json.dumps(ctx)
    )
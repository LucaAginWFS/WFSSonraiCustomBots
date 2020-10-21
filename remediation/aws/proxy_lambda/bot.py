import logging
import json
import sonrai.platform.aws.arn

def run(ctx):

    lambda_client = ctx.get_client().get('lambda', 'us-east-1')

    payload = {}
    payload['resource_id'] = ctx.resource_id
    payload['data'] = ctx.config.get('data')
    payload['policy_evidence'] = ctx.get_policy_evidence()

    lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:174388760268:function:sonrai-remediation-bot-proxy',
        InvocationType='Event',
        Payload=json.dumps(payload)
    )
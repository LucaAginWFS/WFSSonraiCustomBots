import logging
import json
import sonrai.platform.aws.arn

def run(ctx):

    lambda_client = ctx.get_client().get('lambda', 'us-east-1')

    payload = {}
    payload['srn'] = ctx.srn
    payload['severityNumberic'] = ctx.severityNumberic
    payload['resourceId'] = ctx.resourceId
    payload['resourceLabel'] = ctx.resourceLabel
    payload['resourceSRN'] = ctx.resourceSRN
    payload['ticketType'] = ctx.ticketType
    payload['resourceType'] = ctx.resourceType
    payload['ticketKey'] = ctx.ticketKey
    payload['criticalResourceID'] = ctx.criticalResourceID
    payload['severityCategory'] = ctx.severityCategory
    payload['status'] = ctx.status
    payload['createdDate'] = ctx.createdDate
    payload['createdBy'] = ctx.createdBy
    payload['orgName'] = ctx.orgName

    lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:174388760268:function:TempFunction',
        InvocationType='Event',
        Payload=json.dumps(payload)
    )
import logging
from arnparse import arnparse
import botocore
import boto3
import json
client = boto3.client('lambda')

raw_json = '{"data": {"ticket": {"evidence": {"policyEvidence": {"srn": "srn:aws:iam::111111111111/User/User/botcallback_aws_1600099439","resourceId": "arn:aws:iam::111111111111:user/botcallback_aws_1600099439"}},"srn": "srn:myorg::Ticket/1f096ec3-7601-4bcd-aeb7-eacccbc10d8d","severityNumberic": "25","resourceId": "srn:aws:iam::111111111111/User/User/botcallback_aws_1600099439","resourceLabel": "User","resourceSRN": "srn:aws:iam::111111111111/User/User/botcallback_aws_1600099439","ticketType": "Policy","resourceType": "User","ticketKey": "srn:myorg::ControlPolicy/c67edf73-b497-43fe-85eb-a89e6e730d31","criticalResourceID": "arn:aws:iam::111111111111:user/botcallback_aws_1600099439","severityCategory": "LOW","status": "NEW","createdDate": "1600106623000","createdBy": "srn:myorg::SonraiComponent/PolicyEngine","orgName": "myorg"}},"bot": {"id": "srn:supersonrai::bot/750cf807-3bc7-4269-8910-9ae0f5cf0100"}}'
json_obj = json.loads(raw_json)

dictionary = {}

dictionary['test'] = 'test'

print(json.dumps(dictionary))

resourceId = 'arn:aws:ec2:us-east-1:034135693578:instance/i-0ea92f62101214836'
parsesRes = arnparse(resourceId)

testObj = 'nothing'

# stopReturn = client.invoke(
#         FunctionName='arn:aws:lambda:us-east-1:174388760268:function:TempFunction',
#         InvocationType='Event',
#         Payload=json.dumps({"test":"test"})
#     )
# print(stopReturn)

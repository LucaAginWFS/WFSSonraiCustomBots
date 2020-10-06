import logging
from arnparse import arnparse
from datetime import datetime
import botocore
import boto3
import json

with open('test.json') as f:
  json_data = json.load(f)

raw_created_date = int(json_data['data']['ticket']['createdDate'])
print(raw_created_date)

client = boto3.client('iam')
resourceId = 'arn:aws:iam::174388760268:role/Lucas-test-role'
parsesRes = arnparse(resourceId)

created_date = datetime.fromtimestamp(raw_created_date/1000.0)



def within_past_day(date):
    difference = datetime.now() - date
    if difference.days < 1:
        return True
    else:
        return False

print(within_past_day(created_date))

def run(ctx):

    iam_client = ctx.get_client().get('iam')
    logging.info('deleting role: {}'.format(ctx.resource_id))
    
    # Get role name
    resource_arn = sonrai.platform.aws.arn.parse(ctx.resource_id)
    role_name = resource_arn \
        .assert_service("iam") \
        .assert_type("instance") \
        .name

    # https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#roles-managingrole-deleting-api
    instance_profiles = iam_client.list_instance_profiles_for_role(RoleName=role_name)
    for instance_profile in instance_profiles['InstanceProfiles']:
        iam_client.remove_role_from_instance_profile(InstanceProfileName=instance_profile['InstanceProfileName'], RoleName=role_name)

    role_policies = iam_client.list_role_policies(RoleName=role_name)
    for policy_name in role_policies['PolicyNames']:
        iam_client.delete_role_policy(RoleName=role_name, PolicyName=policy_name)

    role_attached_policies = iam_client.list_attached_role_policies(RoleName=role_name)
    for attached_policy in role_attached_policies['AttachedPolicies']:
        iam_client.detach_role_policy(RoleName=role_name, PolicyArn=attached_policy['PolicyArn'])

    logging.info('deleting role: {}'.format(ctx.resource_id))
    iam_client.delete_role(RoleName=role_name)
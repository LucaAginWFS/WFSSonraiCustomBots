import logging
import sonrai.platform.aws.arn

def run(ctx):

    ec2_client = ctx.get_client().get('ec2', 'us-east-1')

    # Get role name
    resource_arn = sonrai.platform.aws.arn.parse(ctx.resource_id)
    ec2_instance_id = resource_arn \
        .assert_service("ec2") \
        .assert_type("instance") \
        .resource

    logging.info('Stoping instance: {}'.format(ctx.resource_id))
    ec2_client.stop_instances(
        InstanceIds = [
            ec2_instance_id
        ]
    )
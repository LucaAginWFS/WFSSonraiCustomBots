import logging
import json
from datetime import datetime
from datetime import timedelta
import sonrai.platform.aws.arn

def run(ctx):

    lambda_client = ctx.get_client().get('lambda', 'us-east-1')

    payload = {}
    payload['resource_id'] = ctx.resource_id
    payload['data'] = ctx.config.get('data')
    payload['policy_evidence'] = ctx.get_policy_evidence()

    # ticket = ctx.config.get('data').get('ticket')
    # ticket_srn = ticket.get("srn")
    # query = '''
    #     mutation snoozeTicket($srn: String, $snoozedUntil: DateTime) {
    #         ReopenTickets(input: {srns: [$srn]}) {
    #             successCount
    #             failureCount
    #             __typename
    #         }
    #         SnoozeTickets(input: {srns: [$srn]}, snoozedUntil: $snoozedUntil) {
    #             successCount
    #             failureCount
    #             __typename
    #         }
    #     }
        
    # '''
    # ticket_snoozeUntil = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
    # variables = { "srn": ticket_srn, "snoozedUntil": ticket_snoozeUntil }
    # response = ctx.graphql_client().query(query, variables)

    lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:174388760268:function:test-function-sonrai-invocation',
        InvocationType='Event',
        Payload=json.dumps(payload)
    )
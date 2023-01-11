from sqs_core import *
import json


def receive_messages(queue_name):
    queue_url = get_queue_url(queue_name)

    sqs = get_sqs_client()

    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=["SentTimestamp"],
        MaxNumberOfMessages=1,
        MessageAttributeNames=["All"],
        VisibilityTimeout=0,
        WaitTimeSeconds=0,
    )

    if response.get('Messages') == None:
        print('No messages to retrive')
        print()
    else:
        message = response['Messages'][0]
        json_formatted_str = json.dumps(message, indent=2)

        print('Message: %s' % json_formatted_str)
        print()

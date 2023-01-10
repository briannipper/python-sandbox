from sqs_core import *
import json


def create_with_deadletter(queue_to_create):
    print()

    # create deadletter queue name
    deadletter_queue_name = queue_to_create + "-deadletter-queue"

    # queue check
    primary_queue_exists = False
    deadletter_queue_exists = False

    for queue_url in list_queues():
        if queue_to_create in queue_url:
            primary_queue_exists = True
        if deadletter_queue_name in queue_url:
            deadletter_queue_exists = True

    if primary_queue_exists:
        print("Primary Queue Exists Skip Create")
        print()
        primary_queue_url = get_queue_url(queue_to_create)
    else:
        print("Primary Queue DOES NOT exist Create")
        print()
        primary_queue_url = create_queue(queue_to_create)

    if deadletter_queue_exists:
        print("Dead letter Queue Exists Skip Create")
        print()
        deadletter_queue_url = get_queue_url(deadletter_queue_name)
    else:
        print("Dead Letter Queue DOES NOT exist Create")
        print()
        deadletter_queue_url = create_queue(deadletter_queue_name)

    # Deadletter Configuration
    dl_queue_iterator = get_dl_collection_iterator_by_url(deadletter_queue_url)

    for dl_queue in dl_queue_iterator:
        if primary_queue_url in dl_queue.url:
            print("Dead Letter Queue Already Configured")
        else:
            print("Need to configure dead letter queue")
            redrive_policy = {
                "deadLetterTargetArn": get_queue_arn_by_url(deadletter_queue_url),
                "maxReceiveCount": "10",
            }
            set_queue_attribues(primary_queue_url, json.dumps(redrive_policy))


"""

# Configure queue to send messages to dead letter queue
response = sqs.get_queue_url(QueueName='bnipper-test-queue')

queue_url = response['QueueUrl']

response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        },
        'TimeStamp': {
            'DataType': 'String',
            'StringValue': datetime.datetime.now().strftime("%c")
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])
"""

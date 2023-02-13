from sqs_core import *
import datetime


def send_message(queue_name):
    queue_url = get_queue_url(queue_name)

    sqs = get_sqs_client()

    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            "Title": {"DataType": "String", "StringValue": "The Whistler"},
            "Author": {"DataType": "String", "StringValue": "John Grisham"},
            "WeeksOn": {"DataType": "Number", "StringValue": "6"},
            "TimeStamp": {
                "DataType": "String",
                "StringValue": datetime.datetime.now().strftime("%c"),
            },
        },
        MessageBody=(
            "Information about current NY Times fiction bestseller for "
            "week of 12/11/2016."
        ),
    )

    print()
    print("Message ID: " + response["MessageId"])
    print()

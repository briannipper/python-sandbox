# sqs_core.py>

import boto3


def get_sqs_client():
    return boto3.client("sqs")


def get_queue_url(queue_name):
    response = boto3.client("sqs").get_queue_url(QueueName=queue_name)
    return response["QueueUrl"]


def create_queue(queue_name):
    response = boto3.client("sqs").create_queue(
        QueueName=queue_name,
        Attributes={"DelaySeconds": "60", "MessageRetentionPeriod": "86400"},
    )
    return response["QueueUrl"]


def list_queues():
    response = boto3.client("sqs").list_queues()

    return response["QueueUrls"]


def set_queue_attribues(queue_url, redrive_policy):
    boto3.client("sqs").set_queue_attributes(
        QueueUrl=queue_url,
        Attributes={"RedrivePolicy": redrive_policy},
    )


def get_queue_arn_by_url(queue_url):
    queue_obj = boto3.resource("sqs").Queue(queue_url)
    queue_obj.load()
    return queue_obj.attributes["QueueArn"]


def get_dl_collection_iterator_by_url(queue_url):
    queue_obj = boto3.resource("sqs").Queue(queue_url)
    return queue_obj.dead_letter_source_queues.all()


def purge_then_delete_queue_by_url(queue_url):
    boto3.client("sqs").purge_queue(QueueUrl=queue_url)
    boto3.client("sqs").delete_queue(QueueUrl=queue_url)

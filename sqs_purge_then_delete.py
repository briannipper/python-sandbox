from sqs_core import *


def purge_then_delete(queue_to_delete):
    print()

    # queue names
    deadletter_queue_name = queue_to_delete + "-deadletter-queue"

    # queue check
    primary_queue_exists = False
    deadletter_queue_exists = False

    for queue_url in list_queues():
        if queue_to_delete in queue_url:
            primary_queue_exists = True
        if deadletter_queue_name in queue_url:
            deadletter_queue_exists = True

    if primary_queue_exists:
        print("Primary Queue Exists Purge then Delete")
        print()
        primary_queue_url = get_queue_url(queue_to_delete)
        purge_then_delete_queue_by_url(primary_queue_url)
    else:
        print("Primary Queue DOES NOT exist")
        print()

    if deadletter_queue_exists:
        print("Dead letter Queue Exists Purge then Delete")
        print()
        deadletter_queue_url = get_queue_url(deadletter_queue_name)
        purge_then_delete_queue_by_url(deadletter_queue_url)
    else:
        print("Dead Letter Queue DOES NOT exist")
        print()

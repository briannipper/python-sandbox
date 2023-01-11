from sqs_create_with_deadletter import *
from sqs_purge_then_delete import *
from sqs_create_message import *
from pick import pick
import os

print()

title = "Please select an operation: "
options = ["Create Queue", "Delete Queue", "Send Message"]

option, index = pick(options, title)

print("You selected: " + option)
print()

if index == 0:
    print("Please enter a queue name:")
    queue_name = input()

    print()
    print("Create Queue: " + queue_name)

    create_with_deadletter(queue_name)

if index == 1:
    print("Please enter a queue name:")
    queue_name = input()

    print()
    print("Delete Queue: " + queue_name)

    purge_then_delete(queue_name)

if index == 2:
    print("Please enter a queue name:")
    queue_name = input()

    print()
    print("Send Message to Queue: " + queue_name)

    send_message(queue_name)

print("Press any key to exit")
os.system("read")

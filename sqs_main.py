from sqs_create_with_deadletter import *
from sqs_purge_then_delete import *
from sqs_create_message import *
from sqs_receive_messages import *
from pick import pick
import os

print()

title = "Please select an operation: "
options = ["Create Queue", "Delete Queue", "Send Message To Queue", "Receive Messages From Queue"]

option, index = pick(options, title)

print("You selected: " + option)
print()

print("Please enter a queue name:")
queue_name = input()

print()
print(option + ": " + queue_name)

if index == 0:
    create_with_deadletter(queue_name)

if index == 1:
    purge_then_delete(queue_name)

if index == 2:
    send_message(queue_name)

if index == 3:
    receive_messages(queue_name)

print("Press any key to exit")
os.system("read")

from sqs_create_with_deadletter import *
from sqs_purge_then_delete import *
from sqs_create_message import *
from sqs_receive_messages import *
from ses_core import *
from pick import pick
import os

def get_queue_name():
    print("Please enter a queue name:")
    result = input()

    print()
    print(option + ": " + result)
    return result

print()

title = "Please select an operation: "
options = [
    "Send Email",
    "Create Queue",
    "Delete Queue",
    "Send Message To Queue",
    "Receive Messages From Queue",
]

option, index = pick(options, title)

print("You selected: " + option)
print()

if index == 0:
    set_email_values()
    
if index == 1:
    queue_name = get_queue_name()
    create_with_deadletter(queue_name)

if index == 2:
    queue_name = get_queue_name()
    purge_then_delete(queue_name)

if index == 3:
    queue_name = get_queue_name()
    send_message(queue_name)

if index == 4:
    queue_name = get_queue_name()
    print("Enter receive count:")
    receive_count = int(input())
    receive_messages(queue_name, receive_count)

print("Press any key to exit")
os.system("read")

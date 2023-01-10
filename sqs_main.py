import time
from sqs_create_with_deadletter import *
from sqs_purge_then_delete import *

print()

print("Please enter a queue name:")

queue_name = input()

print()
print("Working with queue " + queue_name)
print()

create_with_deadletter(queue_name)
time.sleep(120)
purge_then_delete(queue_name)
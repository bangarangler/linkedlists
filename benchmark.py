import time
from linked_lists import LinkedList
'''
Benchmark removing from the fron of a list versus
removing from the front of a linked list
'''

n = 100000

l= [i for i in range(n)]
ll = LinkedList()

for i in range(n):
    ll.add_to_tail(n)

start_time = time.time()
for i in range(n):
    ll.remove_head()
end_time = time.time()
print(f"linked list remove from head runtime: {end_time - start_time}")

start_time = time.time()
for i in range(n):
    l.pop(0)
end_time = time.time()
print(f"list pop from font runtime: {end_time - start_time}")



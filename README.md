# Data Structures

---

06/10/2019

Like your toolkit. They are tools.  Use the one for the right problem you are trying to solve.

Arrays and Hash Tables are so common because they handle many things well. Every data structure has it's use case.

They come up often in interviews.

### *Linked Lists*

similar to their cousin arrays. both used for storing lists of data.

lots of languages don't even include linked lists. Not in JS or python. Java and Rust do.

doesn't have to be right next to each other like an array. They just follow the next arrow or link to get to the next one.

If you are short on memory linked list might be better. We only need enough enough memory for a certain node at each location so they can be scattered throughout memory.

you might pick a linked list if 

reference: head of list and tail of list. 

H = head, T = tail, x = node, - = link

Hx-x-x-x-x-xT

Nothing has to get shifted in a linked list. really no such thing as a hole in a linked list. We can just shift the arrows or the (-, links) around. Nothing in memory has to be shifted around we can just move around the arrows / links.

Removing from front of the list would be O(1)

Adding to the back of list keeps same runtime of array so O(1). We just change the pointer and reassign the tail reference.

### Arrays

similar to a bookshelf or a row of lockers. Data goes into these slots or lockers in order.

x = node - = link

x-x-x-x-x-x

usually stored right next to each other in memory / ram

need to store things continuously. sometimes we can't actually do that

most of the time you will just use an array.

pop(o) will remove that thing from array and then we have hole. arrays don't like holes. only holes at the end allowed. So that extra hole would have to be filled and shifts everything to the left. The runtime would be O(n) to do this. So removing from the front or the middle of an array is a linear operation in the worst case. Removing from the end would be a constant time operation.
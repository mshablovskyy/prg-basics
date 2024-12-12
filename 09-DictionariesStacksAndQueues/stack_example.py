import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""
# Put 2 on the stack
# Put 3 on the stack
# Put 7 on the stack
# Put 4 on the stack
# Put 1 on the stack
# Put 9 on the stack
# Put 8 on the stack
# Sum the last two numbers of the stack and print result
# Calculate the sum of the remaining stack elements and print the result. Use a 'while' loop.

# creates a stack
cards = queue.LifoQueue()
nums = [2,3,7,4,1,9,8]

# adds elements to the top of the stack
for i in nums:
    cards.put(i)

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())
# removes and prints elements from the top of the stack
print(cards.get() + cards.get())
res = 0
while not cards.empty():
    card = cards.get()
    res += card
print(res)

"""
Note the order of the printed elements.
The last added element is printed first.
"""

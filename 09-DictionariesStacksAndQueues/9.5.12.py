import queue
s = input("Enter your string: ")
q = queue.LifoQueue()
for i in s:
    q.put(i)
s = ""
while not q.empty():
    s+=q.get()
print(s)
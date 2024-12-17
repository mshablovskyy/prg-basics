import queue

number = 19
b = queue.LifoQueue()
while number != 0:
    b.put(number%2)
    number = number // 2
while not b.empty():
    print(b.get(), end = "")
print()
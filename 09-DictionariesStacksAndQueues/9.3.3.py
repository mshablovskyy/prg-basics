import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    b = {")": "(", "]": "[", "}": "{"}
    brackets = queue.LifoQueue()
    for i in expression:
        if i in b.values():
            brackets.put(i)
        elif i in b.keys():
            if brackets.get() != b[i]:
                return False
    if brackets.empty():
        return True#True if brackets in expression are ok of False otherwise
    else:
        return False

exp = [expression1, expression2, expression3]

for i in exp:
    print(brackets_ok(i))
l = [0, 1]
t = ""
for i in range(0, 20):
    l.append(l[-2] + l[-1])
for i in l:
    t += str(i) + " "
print(t)
netw = {"facebook" : True,
        "twitter" : False,
        "instagram" : True}
v = 0

for i in netw:
    if netw[i]:
        v += 1

if v >= 2:
    print("You are a good influencer!")
else:
    print("Try more!")
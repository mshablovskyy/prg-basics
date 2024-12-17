basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

data = [basic_data, advanced_data]

add_data = {}

for d in data:
    for k, v in d.items():
        add_data[k] = v
        
print(add_data)
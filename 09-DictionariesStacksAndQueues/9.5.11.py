import json
import os
path = os.path.dirname(__file__) + "/"
# {
#    person_name: number of votes,
#    person_name: number of votes,
#    ...
#    ...
# }

# Read the contents of the json file
with open(path+"votes.json") as file:
    votes = json.load(file)
    
# Vote for a person
person_name = input('Name of the person you are voting for: ')
if person_name in votes.keys():
    votes[person_name] += 1
else:
    votes[person_name] = 1

# Save voting data to json file
with open(path+"votes.json", "w") as file:
    votes = json.dump(votes, file)
import os

###
# Makes a copy of a text file
#

path = os.path.dirname(__file__) + "/"

# file names
original_file = path + 'healthy_lifestyle.txt'
target_file = path + 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file) as file:
   content = file.read()

# write the content to the target file (copy)
with open(target_file, mode="w") as file:
    file.write(content)
import os
###
# Saves to a file a list of employees working at a specified position.
#
path = os.path.dirname(__file__) + "/"
# file names
employees_file = path + 'it_company.csv'
position_file = path + 'software_engineer.csv'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file) as em_file:
    with open(position_file, mode="w") as pos_file:
        for line in em_file:
            pos_file.write(line)
            break
        for line in em_file:
            if job_title in line:
                pos_file.write(line)
# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food = 0
for row in monthly_expenses:
    food += row[0]
transport = 0
for row in monthly_expenses:
    transport += row[1]
utilities = 0
for row in monthly_expenses:
    utilities += row[2]
weekly_expences = []
for row in monthly_expenses:
    exp = 0
    for item in row:
        exp += item
    weekly_expences.append(exp)

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',weekly_expences[0])
print('Week 2:',weekly_expences[1])
print('Week 3:',weekly_expences[2])
print('Week 4:',weekly_expences[3])
print('---------------')
print('TOTAL:',...)
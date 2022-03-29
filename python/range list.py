#declared number of items
total = 0
expense = []
for i in range (7):
  expense.append(float(input('Enter the amount spent.\n')))
total = sum(expense)
print('$', total, ' was spent on food', sep='')
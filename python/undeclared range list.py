total = 0
expenses = []
num_expenses = int(input('Enter number of expenses:\n'))
for i in range(num_expenses):
  expenses.append(float(input('Enter expense:\n')))
total = sum(expenses)
print('You have spent $', total, sep='')
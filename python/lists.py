#duplicate an item
slangs = ['LOL','IDK', 'SMH']
slangs.append('IDK')
print(slangs)
#Remove an item
slangs = ['LOL','IDK', 'SMH']
slangs.remove('IDK')
print(slangs)
#find in list
slangs = ['LOL','IDK', 'SMH']
if 'LOL' in slangs:
 print('It works')
#new line for each item
slangs = ['LOL','IDK', 'SMH']
for slang in slangs:
 print(slang)
 #expense calculator
expenses = [10.50, 8, 5, 15, 20, 5, 3]
add = 0

for x in expenses:
  add = add + x

#sep='' removes the space between dollar and add
print("You spent $", add, ' on lunch this week', sep='')
#We can skip the add = add here and just use add to make things easier.
expenses = [10.5, 8, 5, 15, 20, 5, 3]
total = sum(expenses)
print("You spent $", total, ' on lunch this week', sep='')
#range

import random
roll = random.randint(1,6)
guess = int(input('What number did it roll?\n'))
if roll == guess:
  print('You are so smart')
else:
  print('Better luck next time, computer rolled '+ str(roll))
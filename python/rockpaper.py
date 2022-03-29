import random
computer_choice = random.choice(['scissors', 'paper', 'rock'])

player_choice = input('Rock, paper or scissors\n')
if player_choice == computer_choice:
  print('Tie computer rolled '+ str(computer_choice))
elif player_choice == 'rock' and computer_choice == 'scissors':
  print('Win computer rolled '+ str(computer_choice))
elif player_choice == 'paper' and computer_choice == 'rock':
  print('Win computer rolled '+ str(computer_choice))
elif player_choice == 'scissors' and computer_choice == 'paper':
  print('Win computer rolled '+ str(computer_choice))
else:
  print('You lose computer rolled '+ str(computer_choice))
import random

user_wins = 0
computer_wins = 0
break_value = False
options = ['rock', 'paper', 'scissors']



computer_pick = options[random_number]
while break_value == False:

    user_input = input('Type rock/paper/scissors or Q to quit :').lower()
    print('You picked', user_input)

    random_number = random.randint(0, len(options)-1)
    print  ('computer picked', computer_pick + '.')

    if user_input == 'rock' and computer_pick == 'scissors':
        print (' You won!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print ('You Won!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print ('You won!')
        user_wins += 1
    else:
        print ('computer won!')
        computer_wins += 1
    

print ('You won game' + str(user_wins))
print ('good bye')
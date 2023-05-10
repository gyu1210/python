name = input ('What is your name?').lower()
print('welcom', name, 'to this adventure!')

answer = input('you are on a dirt road, it has come to an end and\
 Which way would you like to go?(left/right)')

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim accross? Type walk/swim')

    if answer == 'swim':
        print('you swan acrross and were eaten by alligator.')
    elif answer == 'walk':
        print('you walked for many miles, ran out of water and you lost game.')
    else:
        print('Not a valid option. you lose')
elif answer == 'right':
    answer = input('you come to a bridge, it looks wobbly, do you want to cross or back?')
    if answer == 'back':
        print('you go back and lose')
    elif answer == 'cross':
        answer = input('you cross the bridge and meet a stranger. Do you wanna talk? yes/no')
    else:
        print('Not a valid option. you lose')  

        if answer =='yes':
            print('you talk to the stranger and they give you gold. You WIN!')
        elif answer == 'no':
            print('you ignore the stranger and they are offended and you lose')
        else:
             print('Not a valid option. you lose')  
else:
        print('Not a valid option. you lose')  

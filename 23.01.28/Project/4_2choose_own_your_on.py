import random

name = input ('What is your name?').lower()
choice = input ('Hi ' + name + ' do you wanna go for adventure with me? (yes/no)')

def main_story(choice):
    choose_journey(choice)

def choose_journey(choice):
    if choice=="yes":
        direction = input('Great, which way do you wanna go? (left/right)')
        choose_direction(direction)
    elif choice == 'No':
     direction = input ("That's shame, Ok see you next time!") 

def choose_direction(direction):
    answer = input ('choose the numebr (1¬100)')
    disaster = random.randint(0,100)
    disaster_trigger(direction, disaster)

def disaster_trigger(direction, disaster):
    if direction == 'left':
        if disaster>=90:
            disaster = input('alright, you chose'+disaster+' incorrect number!')
        else:
            disaster = input('Do you want to go next stage?(yes/no)')
    elif direction == 'right':
        if disaster>=50:
            disaster = input('alright, you chose'+disaster+' incorrect number!')
        else:
            disaster = input('Do you want to go next stage?(yes/no)')  

main_story(name, choice)






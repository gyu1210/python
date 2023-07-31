import random

name = input ('What is your name?').lower()
choice = input ('Hi ' + name + ' do you wanna go for adventure with me? (yes/no)')


class text_game:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
   
        

    def choose_story(self):
        if self.choice == "yes":
            print("You selected yes")
            self.start_journey()
        else:
            print("You selected no")
    
    def start_journey(self):
        self.direction = input("Where do you want to go? left/right")
        if self.direction == 'left':
            print ('you selected left '+self.name)
        else:
            print('you went to right')
        self.choose_ways()

    def choose_ways(self):
        if self.direction == 'left':
            self.transport = input('do you wanna take taxi or bus?')
        
        else:
            self.transport = input('do you wanna go for walk or swim?')


first_game = text_game(name, choice)

first_game.choose_story()

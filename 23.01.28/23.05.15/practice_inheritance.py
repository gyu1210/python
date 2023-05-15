#inheritance

#parent class
class person:
    def __init__(self,fname,lname):
        self.firstname = fname 
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
x = person('Gyu', 'Kim')
x.printname()

#Child class
class person_1:
    def __init__(self,fname_1,lname_1):
        self.firstname = fname_1
        self.lastname = lname_1
    def printname(self):
        print(self.firstname,self.firstname)
class student(person):
    pass
x = student('Mike','Olsen')
x.printname()

#Add __init__ function
class person_2:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person_2):
    def __init__(self, fname, lname):
        person_2 .__init__(self,fname,lname)
x = student('Ed','Payne')
x.printname()

#super() function
class person:
    def __init__ (self, fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname):
        super(). __init__(fname,lname)
x = student('Bella','Bake')
x.printname()

#Add properties
class person:
    def __init__(self,fname,lname):
        self.firstname =fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduation_year = 2019

x = student('John','white')
print(x.graduation_year)

#Add properties2
class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self,fname,lname,year):
        super(). __init__(fname,lname)
        self.graduation_year_1 = year
x = student ('Dr.stranger','walter',2000)
print(x.graduation_year_1)

#Add properties3
class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self,fname,lname, year):
        super(). __init__(fname,lname)
        self.graduation_year_3 = year
    def welcome(self):
        print('welcome', self.firstname, self.lastname, 'to the class', self.graduation_year_3)
x = student('Gyu', 'Young', 2014)
x.welcome()

class person:
    def __init__(self,fname,lname,age):
        self.firstname= fname
        self.lastname = lname
        self.peopleage = age

    def printname (self):
        print(self.firstname, self.lastname,self.peopleage)

    def printage (self):
        print('i am a' ,f"{self.peopleage}", 'years old')

class student(person):
    def __init__(self, fname, lname, age):
        super(). __init__(fname,lname,age)

x1 = student('Mike','Olsen',17)
x2 = student('Joe', 'Bake', 18)
 
x1.printage() 
x2.printage()
        

# class person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname (self):
#         print(self.firstname, self.lastname)


# class student(person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
# x = student('Mike','Olsen', 2019)
# print(x.graduationyear)
    

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.welcome()


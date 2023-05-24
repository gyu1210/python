#class

class my_class:
    x = 5
p1 = my_class()
print(p1.x)

#the__init__()function
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('Gyu',29)

print(p1.name)
print(p1.age)

#object without the __str__function

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person ('Gyu' ,29)
print(p1)

#object with the __str__function
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name},{(self.age)}'
    
p1 = person('Gyu',29)
print(p1)

#object method
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def my_function(self):
        print('Hello, my name is' + ' '+ self.name)
p1 = person('Gyu',29)
p1.my_function()

#self parameter
class person:
    def __init__(my_object,name,age):
        my_object.name = name
        my_object.age = age

    def my_function(abc):
        print('Hello, my name is '+' '+abc.name)

p1 = person('Gyu',29)
p1.my_function()

#Modify object properties
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_function(self):
        print('Hello, my name is' +' '+self.name)
p1 = person('Gyu',29)
p1.age = 40

print(p1.age)

#class polymorphism

class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class car(vehicle):
    def move(self):
        print('Drive')

class boat(vehicle):
    def move(self):
        print('Sail')

class plane(vehicle):
    def move(self):
        print('Fly')

car1 = car('Ford', 'Mustang')
boat1 = boat('Ibiza','Touring28')
plane1 = plane('Boeing','747')

for x in (car1, boat1, plane1):
    print(x.brand,x.model)
    x.move()


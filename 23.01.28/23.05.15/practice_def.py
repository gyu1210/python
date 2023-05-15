#function

#Number of Arguments
def my_function(fname, lname):
    print(fname +' '+ lname)
my_function('Gyu','Kim')

#Arbitary Arguments(args)
def my_function(*kids):
    print('the youngest child is' + kids[2])
my_function('Gyu','Emil','Linus')

#keyword arguments
def my_function(child1, child2, child3):
    print('the youngest child is' + child3)

my_function(child1='Emil',child2='Gyu',child3='Linus')

#Arbitrary keyword arguments
def my_function(**kid):
    print('his last name is' + kid['lname'])

my_function(fname = 'Tobias',lname = 'Refsnes')

#Default parameter value
def my_function(country='Norway'):
    print('I am from' + country)

my_function('Sweden')
my_function('Denmark')
my_function()
my_function('Finnland')

#Passing a list as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits=['apple','banana','cherry']

my_function(fruits)

#Return values
def my_function(x):
    return 5 *x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#Recursion
def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print('\n\nRecursion Example Result')
tri_recursion(6)


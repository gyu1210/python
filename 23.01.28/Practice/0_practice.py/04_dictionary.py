#Keys
this_is_dic = {
    'brand':'Ford',
    'model': 'mustang',
    'year' : 2000
}

for x in this_is_dic.keys():
    print(x)

#values
this_is_dic_1 = {
    'brand':'Ford',
    'model':'mustang',
    'year': 2000
}

for x in this_is_dic_1.values():
    print(x)

#items
this_is_dic_2 = {
    'brand':'Ford',
    'model':'mustang',
    'year': 2000
}

for x,y in this_is_dic_2.items():
    print(x,y)

#print everything
this_is_dic_3 = {
    'brand':'Ford',
    'model':'mustang',
    'year' : 2000
}
print(this_is_dic_3)

#add item
car ={
    'brand':'Ford',
    'model':'mustang',
    'year': 2000
}
x = car.keys()
print(x)

car['colour'] = 'white'
print(x)

#update item
car_1 = {
    'brand':'Ford',
    'model':'mustang',
    'year': 2000
}
car_1['year'] = 2018
print(car_1)

#copy
car_3 = {
    'brnad':'Ford',
    'model' :'mustang',
    'year': 2000
}
car_3 = car_3.copy()
print(car_3)
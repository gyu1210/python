#list
this_is_the_list = ['apple', 'banana', 'cherry']
print(this_is_the_list)

this_is_the_list_1 = ['apple', 'banana','cherry']
this_is_the_list_1[1:2] = ['kiwi', 'lemon']
print(this_is_the_list_1)

#add item
this_is_the_list_2 = ['apple','banana', 'cherry']
this_is_the_list_2.append('orange')
print(this_is_the_list_2)

this_is_the_list_3 = ['apple','banana','cherry']
this_is_the_tuple = ('peach','blackcurrent')
this_is_the_list_3.extend(this_is_the_tuple)
print(this_is_the_list_3)

#remove item
this_is_the_list_4 = ['apple','banana','cherry']
this_is_the_list_4.remove('banana')
print(this_is_the_list_4)

#Loop through list
this_is_the_list_5 =['apple','banana','cherry']
for x in this_is_the_list_5:
    print(x)

#While loop
this_is_the_list_6 = ['apple','banana','cherry']
i = 0
while i < len(this_is_the_list_6):
    print(this_is_the_list_6[i])
    i+= 1

#new list
fruits = ['apple','banana','cherry','mango']
new_list =[]
for x in fruits:
    if 'a' in x:
        new_list.append(x)
print(new_list)

#exchange item
fruits_1 = ['apple','banana','cherry']
new_list_1 = [x if x != 'banana' else 'orange' for x in fruits_1]
print(new_list_1)

#join two list
list_1 = ['a','b','c']
list_2 = ['d','e','f']
list_1.extend(list_2)
print(list_1)
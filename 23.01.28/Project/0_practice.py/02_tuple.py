#Tuple
this_is_tuple = ('apple','banana','cherry')
print(this_is_tuple)

this_is_tuple_1 = ('apple','banana','cherry')
print(this_is_tuple_1[0:1])

#Loop through the index number
this_is_tuple_2 = ('apple','banana','cherry')
for i in range(len(this_is_tuple_2)):
    print(this_is_tuple_2[i])

#While loop
this_is_tuple_3 = ('apple','banana','cherry')
i = 0
while i < len(this_is_tuple_3):
    print(this_is_tuple_3[i])
    i+= 1

#join tuple
this_is_tuple_4 = ('a','b','c')
this_is_tuple_5 = (1,2,3)

this_is_tuple_6 = this_is_tuple_4 + this_is_tuple_5
print(this_is_tuple_6)

#mutiple tuple
fruits = ('apple','banana','cherry')
mytuple = fruits *2
print(mytuple)

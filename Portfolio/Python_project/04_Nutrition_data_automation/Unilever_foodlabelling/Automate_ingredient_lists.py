# Energy value per 100g in kcal
Per_100g = {
    'Energy_kj': {'value':1257,
                  'unit': 'kj'},

    'Energy_kcal': {'value':298,
                  'unit': 'kcal'},
    'Fat': {'value':6.0,
                  'unit': 'g'},
    'Fat_of_saturates':{'value':1.0,
                  'unit': 'g'},
    'Carbohydrate':{'value':52.5,
                  'unit': 'g'},
    'Carbohydrate_of_sugars':{'value':6.0,
                  'unit': 'g'},
    'Salt': {'value':3.0,
                  'unit': 'g'},
    'Calcium': {'value':0.01,
                  'unit': 'mg'},
    'Vitamin_C': {'value':1.45,
                  'unit': 'mcg'},
}


# Calculate energy per % portion (assuming % refers to 1% of the total weight)
reference_intake ={
    'energy': {
        'value': 8400,
        'unit': 'kj'
    },
    'energy': {
        'value': 2000,
        'unit': 'kcal'},

    'fat': {
        'value': 70,
        'unit': 'g'
    },
    'fat_saturates': {
       'value': 20,
        'unit': 'g'
    },
    'Carbohydrate': {
       'value': 260,
        'unit': 'g'
    },
    'Carbohydrate_of_sugars': {
       'value': 90,
        'unit': 'g'
    },
     'Protein': {
       'value': 50,
        'unit': 'g'
    },
    'Salt': {
       'value': 6,
        'unit': 'g'
    },
    'Calcium': {
       'value': 800,
        'unit': 'mg'
    },
     'Vitamin_C': {
       'value': 80,
        'unit': 'mg'
    },
    
}

for key, value in enumerate(ingredients['nutrition']):
    print(ingredients['nutrition'][value],reference_intake[value]['value'])
    print(key,value)
  


#ingredients = {
 #   'quantity' = 100,
 #  nutrition : {
    #'energy': 500,
    #'fat': 20}
#}
#for key, value in enumerate(ingredients['nutrition']):
#    print(ingredients['nutrition'][value],reference_intake[value]['value'])
#    print(key,value)
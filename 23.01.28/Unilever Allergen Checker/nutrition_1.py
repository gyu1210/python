# nutrients  value per 100g 
Per_100g = {
    'Energy_kJ': 1257,
    'Energy_kcal': 298,
    'Fat_g': 6.0,
    'Fat_of_which_saturates_g': 1.0,
    'Carbohydrate_g': 52.5,
    'Carbohydrate_of_which_sugars_g': 6.0,
    'Protein_g': 7.0,
    'Salt_g': 3.00,
    'Calcium_mg': 0.01,
    'Vitamin_C_mcg': 1.45
}



# Reference_intake
Reference_intake = {
    'Energy_kJ': 8400,
    'Energy_kcal': 2000,
    'Fat_g': 70,
    'Fat_of_which_saturates_g': 20,
    'Carbohydrate_g': 260,
    'Carbohydrate_of_which_sugars_g': 90,
    'Protein_g': 50,
    'Salt_g': 6,
    'Calcium_mg': 800,
    'Vitamin_C_mcg': 80
}

for key, value in enumerate(Per_100g):
# nutrients value per 20g 
    value_20g = Per_100g[value]/5
# Calculate energy per % portion 
    percentage_intage = ((value_20g)/(Reference_intake[value]))*100

    print(value,(value_20g),'reference_intake(%)',str(round(percentage_intage,1))+'%')

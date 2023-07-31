# Sample ingredient data
#ingredients = {
#    'Ingredient': ['Flour', 'Sugar', 'Butter', 'Eggs', 'Milk', 'Almonds'],
#    'Amount': [200, 150, 100, 2, 250, 50],
#    'Unit': ['grams', 'grams', 'grams', 'pieces', 'milliliters', 'grams']
#}

import pandas as pd
# Define allergens -importing allergens data with CSV file
allergens = pd.read_csv('allergens.csv')

# Create a DataFrame from the ingredient data
df = pd.read_csv('data.csv')
# Create a DataFrame from the exemptions data
exemptions_df = pd.read_csv('exemptions.csv')
exemptions_list = exemptions_df['Exempted Ingredient'].tolist()
allergens_list = allergens['Allergens'].tolist()

# Create a column to indicate if an ingredient contains allergens and exemptions
df['Contains Allergens'] = df['Ingredients'].apply(lambda x: any(allergen in x for allergen in allergens_list) and x not in exemptions_list)


# Apply style to highlight(yellow) ingredients with allergens
def highlight_allergens(val):
    color = 'background-color: yellow' if val else ''
    return color

# Display the DataFrame
display(df.style.applymap(highlight_allergens, subset=['Contains Allergens']))


df.to_csv('output_example.csv')



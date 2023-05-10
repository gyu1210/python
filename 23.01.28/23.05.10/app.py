from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

recipes = []

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients'].split('\n')
        instructions = request.form['instructions'].split('\n')
        recipe = Recipe(name, ingredients, instructions)
        recipes.append(recipe)
        return redirect('/add_recipe')
    return render_template('add_recipe.html')

@app.route('/remove_recipe/<name>')
def remove_recipe(name):
    for recipe in recipes:
        if recipe.name.lower() == name.lower():
            recipes.remove(recipe)
            break
    return redirect('/')

if __name__ == '__main__':
    app.run()

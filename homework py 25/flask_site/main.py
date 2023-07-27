from flask import Flask, render_template, request, flash, abort
import os
import sqlite3
from Database import DataBase

app = Flask(__name__)
app.config.from_object(__name__)
SECRET_KEY = 'FKOKRFO5KO5KO4567KO32KOKORFVLPL'
app.config['SECRET_KEY'] = SECRET_KEY
app.config.update({'DATABASE': os.path.join(app.root_path, 'website.db')})


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with open('website.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


@app.route('/')
@app.route('/home')
def home():
    connection = connect_db()
    db = DataBase(connection)
    return render_template('home.html', title='Easy Healthy Meal Ideas', menu=db.get_menu())


@app.route('/recipes')
def recipes():
    connection = connect_db()
    db = DataBase(connection)
    return render_template('recipes.html', title='Recipes', menu=db.get_menu(), recipes=db.get_recipes())


@app.route('/recipe/<recipe_title>')
def show_recipe(recipe_title):
    connection = connect_db()
    db = DataBase(connection)

    author, title, category, cooking_time, ingredients, instruction = db.get_recipe(recipe_title)
    if not author:
        abort(404)
    return render_template('recipe.html', author=author, title=title, category=category, cooking_time=cooking_time, ingredients=ingredients, instruction=instruction, menu=db.get_menu())


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    connection = connect_db()
    db = DataBase(connection)

    if request.method == "POST":
        if len(request.form['author']) > 4:
            author = request.form['author']
            title = request.form['title']
            category = request.form['category']
            cooking_time = int(request.form['cooking_time'])
            ingredients = request.form['ingredients']
            instruction = request.form['instruction']

            res = db.add_recipe(author, title, category, cooking_time, ingredients, instruction)
            if res:
                flash('Recipe successfully added', category='success')
            else:
                flash('Failed while adding your recipe', category='error')
        else:
            flash('Failed while adding your recipe', category='error')
    return render_template('add_recipe.html', title='Add a recipe', menu=db.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    connection = connect_db()
    db = DataBase(connection)
    return render_template('page404.html', title='Page not found', menu=db.get_menu())


if __name__ == '__main__':
    create_db()
    app.run(debug=True)

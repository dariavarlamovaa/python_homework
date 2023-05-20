import json


class Recipe:
    def __init__(self, title, author, type_of_recipe, description, link, ingredients, cuisine):
        self.title = title
        self.author = author
        self.type_of_recipe = type_of_recipe
        self.description = description
        self.link = link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def __str__(self):
        return f'{self.title} - {self.author}'


class DecodeError(Exception):
    pass


class Model:
    def __init__(self, filename):
        self.filename = filename
        self.__recipes = {}
        try:
            self.data = json.load(open(self.filename, 'r'))
            for article, recipe in self.data.items():
                self.__recipes[article] = Recipe(
                    recipe['title'],
                    recipe['author'],
                    recipe['type_of_recipe'],
                    recipe['description'],
                    recipe['link'],
                    recipe['ingredients'],
                    recipe['cuisine']
                )
        except json.JSONDecodeError:
            raise DecodeError

        except FileNotFoundError:
            self.data = {}

    @property
    def recipes(self):
        return self.__recipes

    def add_new_recipe(self, recipe_data):
        article = input('Enter its id: ')
        new_recipe = Recipe(*recipe_data.values())
        self.__recipes[article] = new_recipe
        dict_recipes = {article: recipe.__dict__ for article, recipe in self.__recipes.items()}
        json.dump(dict_recipes, open(self.filename, 'w'))

    def find_recipes_by_target(self, target):
        recipes = []
        for article, recipe in self.__recipes.items():
            for tar in target:
                for key, value in recipe.__dict__.items():
                    if tar.lower() in str(value).lower():
                        recipes.append((article, value))
                        break
        return recipes

    def delete_recipe_by_target(self, target):
        del self.__recipes[target[0]]
        dict_recipes = {article: recipe.__dict__ for article, recipe in self.__recipes.items()}
        json.dump(dict_recipes, open(self.filename, 'w'))

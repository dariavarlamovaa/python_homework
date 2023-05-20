class View:
    @staticmethod
    def wait_user_answer():
        print('-' * 20)
        print('1. Add one recipe\n'
              '2. Show all the recipes\n'
              '3. Find a recipe by the target \n'
              '4. Delete a recipe by the target\n'
              '0. Exit the program')
        print('-' * 20)
        query = input('Enter the number: ')
        print('-' * 20)
        return query

    @staticmethod
    def add_new_recipe():
        dict_recipe = {'title': None,
                       'author': None,
                       'type_of_recipe': None,
                       'description': None,
                       'link': None,
                       'ingredients': None,
                       'cuisine': None}
        for key in dict_recipe.keys():
            if key == 'ingredients':
                ingredients = list(input('Input ingredients, comma separate: ').strip().split(','))
                dict_recipe[key] = ingredients
            else:
                dict_recipe[key] = input(f'Input {key.lower()} for the recipe: ').capitalize()
        return dict_recipe

    @staticmethod
    def print_all_recipes(recipes):
        if recipes:
            for i, (recipe_article, recipe) in enumerate(recipes.items(), 1):
                print(f'{i}. {recipe_article}\n'
                      f'Title: {recipe.title}\n'
                      f'Author: {recipe.author}\n'
                      f'Type: {recipe.type_of_recipe}\n'
                      f'Description: {recipe.description}\n'
                      f'Link: {recipe.link}\n'
                      f'Ingredients: {", ".join(recipe.ingredients)}\n'
                      f'Cuisine: {recipe.cuisine}\n')
        else:
            'There is no recipes'

    @staticmethod
    def find_recipe():
        target = input('Enter keywords, comma separate: ').strip().split(',')
        return target

    @staticmethod
    def print_found_recipes(recipe):
        if recipe:
            [print(f'{i}. id: {recipe[0]} - {recipe[1]}') for i, recipe in enumerate(recipe, 1)]
        else:
            'There is no recipes'

    @staticmethod
    def delete_recipe_by_target():
        number = int(input('Enter the number of recipe to delete: '))
        return number

    @staticmethod
    def print_an_error():
        print('Input error. Try again')

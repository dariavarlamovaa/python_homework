from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model('recipes.json')
        self.view = View()

    def run(self):
        query = None
        while query != '0':
            query = self.view.wait_user_answer()
            self.check_user_answer(query)

    def check_user_answer(self, query):
        if query == '1':
            dict_recipe = self.view.add_new_recipe()
            self.model.add_new_recipe(dict_recipe)
        elif query == '2':
            all_recipes = self.model.recipes
            self.view.print_all_recipes(all_recipes)
        elif query == '3':
            target = self.view.find_recipe()
            recipes = self.model.find_recipes_by_target(target)
            self.view.print_found_recipes(recipes)
        elif query == '4':
            target = self.view.find_recipe()
            recipes = self.model.find_recipes_by_target(target)
            if len(recipes) > 1:
                self.view.print_found_recipes(recipes)
                number = self.view.delete_recipe_by_target()
                recipes = [recipes[number - 1]]
            self.model.delete_recipe_by_target(recipes[0])
        elif query == '0':
            pass
        else:
            self.view.print_an_error()






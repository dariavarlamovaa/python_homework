from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model('shoes.csv')
        self.view = View()

    def run(self):
        query = None
        while query != '0':
            query = self.view.wait_user_answer()
            self.eval_user_answer(query)

    def eval_user_answer(self, query):
        if query == '1':
            footwear_data = self.view.get_footwear_data()
            self.model.add_footwear(footwear_data)
        elif query == '2':
            footwear = self.model.database
            self.view.print_footwear(footwear)
        elif query == '3':
            target = self.view.get_target()
            footwear = self.model.get_footwear_by(target)
            self.view.print_footwear(footwear)
        elif query == '4':
            target = self.view.get_target()
            shoes = self.model.get_footwear_by(target)
            if len(shoes) > 1:
                number = self.view.get_deleted_context(shoes)
                shoes = shoes[number - 1]
            self.model.delete_footwear(shoes)
        elif query == '0':
            pass
        else:
            self.view.print_an_error()
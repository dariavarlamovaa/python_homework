# task 1
from abc import ABC, abstractmethod


class PizzaBase(ABC):
    @abstractmethod
    def get_pizza(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class PizzaBase25cm(PizzaBase):
    def get_pizza(self):
        return '25 cm'

    def get_cost(self):
        return 100


class PizzaBase30cm(PizzaBase):
    def get_pizza(self):
        return '30 cm'

    def get_cost(self):
        return 150


class PizzaTemplates(ABC):
    @abstractmethod
    def get_pizza(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class MargheritaPizza(PizzaTemplates):
    def get_pizza(self):
        return 'Margherita pizza: cheese, basil, tomato sauce'

    def get_cost(self):
        return 550


class PepperoniPizza(PizzaTemplates):
    def get_pizza(self):
        return 'Pepperoni pizza: salami, cheese, basil, tomato sauce'

    def get_cost(self):
        return 600


class NeapolitanPizza(PizzaTemplates):
    def get_pizza(self):
        return 'Neapolitan pizza: tomatoes, cheese, basil, tomato sauce'

    def get_cost(self):
        return 650


class VegetarianPizza(PizzaTemplates):
    def get_pizza(self):
        return 'Vegetarian pizza: tomatoes, cheese, olives, pesto sauce'

    def get_cost(self):
        return 500


class MushroomPizza(PizzaTemplates):
    def get_pizza(self):
        return 'Mushroom pizza: mushrooms, cheese, sausage tomato sauce'

    def get_cost(self):
        return 600


class OwnPizza(PizzaTemplates):
    def get_pizza(self):
        return 'Self-made pizza'

    def get_cost(self):
        return 400


class Toppings:
    data = {
        'Cheese': 20,
        'Tomatoes': 25,
        'Pepperoni': 30,
        'Bacon': 35,
        'Mushrooms': 40,
        'Olives': 25,
        'Chicken': 30,
        'Pineapple': 30,
        'Onions': 20,
        'Bell Peppers': 25,
        'Ham': 35,
        'Anchovies': 40,
        'Spinach': 30,
        'Garlic': 20,
        'Jalapenos': 25,
        'Artichokes': 40,
        'Feta Cheese': 35,
        'Sausage': 30,
        'Eggplant': 25,
        'Basil': 20,
        'Tomato Sauce': 15,
        'Pesto Sauce': 20
    }

    def __init__(self, toppings=None):
        self.toppings = toppings
        self.toppings_cost = 0

    def get_toppings(self):
        if self.toppings is None:
            return 'no toppings'
        else:
            return ', '.join(top for top in self.toppings)

    def get_cost(self):
        if self.toppings is not None:
            for key, value in Toppings.data.items():
                for top in self.toppings:
                    if key.lower() == top.lower():
                        self.toppings_cost += value
        return self.toppings_cost


class Pizza:
    def __init__(self, base, pizza, toppings):
        self.base = base
        self.pizza = pizza
        self.toppings = toppings

    @property
    def get_final_cost(self):
        return self.base.get_cost() + self.pizza.get_cost() + self.toppings.get_cost()


class Payment:
    def do_transaction(self, amount):
        raise NotImplementedError


class Cash(Payment):
    def do_transaction(self, amount):
        return f'The order was paid by cash in the amount of {amount} rubles'


class Card(Payment):
    def do_transaction(self, amount):
        return f'The order was paid by card in the amount of {amount} rubles'


class Shop:
    @staticmethod
    def do_payment(payment, amount):
        result = payment.do_transaction(amount)
        print(result)


class Pizzeria:
    def __init__(self):
        self.sold_pizzas = 0
        self.revenue = 0
        self.profit = 0
        self.cart = []

    def run(self):
        query = None
        self.make_an_order()
        while query != 'Exit':
            print('-' * 20)
            query = input('1. Add pizza to cart\n'
                          '2. Delete pizza from cart\n'
                          '3. Show and save your order\n'
                          '4. Clean the cart\n'
                          '5. Pay for your order\n'
                          'Exit. Shutdown\n'
                          'Enter the command: ')
            if query == '1':
                self.add_pizza()
            elif query == '2':
                self.delete_pizza()
            elif query == '3':
                self.show_cart()
                self.save_cart()
            elif query == '4':
                self.cart = []
            elif query == '5':
                self.pay()
                self.show_info()
            else:
                print('Shutdown...')
                break

    def make_an_order(self):
        self.cart = []

    def add_pizza(self):
        query = input('1. Choose an available pizza\n'
                      '2. Make your own pizza\n'
                      'Choose the command: ')
        if query == '1':
            pizza_templates = {'1': MargheritaPizza(),
                               '2': PepperoniPizza(),
                               '3': NeapolitanPizza(),
                               '4': VegetarianPizza(),
                               '5': MushroomPizza()}
            command_pizza = input('1. Margherita\n'
                                  '2. Pepperoni\n'
                                  '3. Neopolitan\n'
                                  '4. Vegetarian\n'
                                  '5. Mushroom\n'
                                  'Enter the number of the pizza: ')
            base = input('25 or 30 cm? Input: ')
            pizza_template = pizza_templates.get(command_pizza)
            if pizza_template is None:
                print('Invalid input')
                return
            if base == '25':
                pizza_base = PizzaBase25cm()
            elif base == '30':
                pizza_base = PizzaBase30cm()
            else:
                print('Invalid input')
                return
            command_topping = input('Do you want to add toppings? yes/no: ').strip().lower()
            if command_topping == 'yes':
                toppings = input('Enter toppings to add, comma separated: ').strip().split(',')
                pizza_toppings = Toppings(toppings)
            else:
                pizza_toppings = Toppings()
            pizza = Pizza(pizza_base, pizza_template, pizza_toppings)
            self.cart.append(pizza)
            print('Pizza added to cart.')
        elif query == '2':
            base = input('25 or 30 cm? Input: ')
            if base == '25':
                pizza_base = PizzaBase25cm()
            elif base == '30':
                pizza_base = PizzaBase30cm()
            else:
                print('Invalid input')
                return
            toppings = input('Enter toppings to add, comma separated: ').strip().split(',')
            pizza_toppings = Toppings(toppings)
            pizza = Pizza(pizza_base, OwnPizza(), pizza_toppings)
            self.cart.append(pizza)
            print('Pizza added to cart.')
        else:
            pass

    def delete_pizza(self):
        if not self.cart:
            return 'Your cart is empty'
        print(self.show_cart())
        pizza_to_del = int(input('Enter the number of the pizza to delete: '))
        self.cart.remove(self.cart[pizza_to_del - 1])
        print('Pizza was deleted from the cart')
        return

    def show_cart(self):
        if not self.cart:
            return 'Your cart is empty'
        cart_items = ''
        for index, pizza in enumerate(self.cart, 1):
            cart_items += f'{index}. {pizza.base.get_pizza()} {pizza.pizza.get_pizza()} ' \
                          f'with {pizza.toppings.get_toppings()} for {pizza.get_final_cost} rub\n'
        print(cart_items)
        return cart_items

    def save_cart(self):
        with open('file.txt', 'w') as f:
            data = self.show_cart()
            if data == 'Your cart is empty':
                return
            f.write(data)

    def pay(self):
        if not self.cart:
            return 'Your cart is empty'
        payment_method = input('Pay by card/cash? Input: ').strip().lower()
        final_cost = sum(pizza.get_final_cost for pizza in self.cart)
        if payment_method == 'cash':
            Shop.do_payment(Cash(), final_cost)
        elif payment_method == 'card':
            Shop.do_payment(Card(), final_cost)
        else:
            return
        self.sold_pizzas += len(self.cart)
        self.revenue += final_cost
        self.profit += final_cost - final_cost * 0.10
        self.make_an_order()

    def show_info(self):
        print(f'Sold pizzas: {self.sold_pizzas}')
        print(f'Revenue: {self.revenue}')
        print(f'Profit: {int(self.profit)}')


def main():
    app = Pizzeria()
    app.run()


if __name__ == '__main__':
    main()

# from abc import ABC, abstractmethod


# task 1
# class Burger:
#     def __init__(self):
#         self.vegan = False
#         self.meat = False
#         self.beef = False
#         self.falafel = False
#         self.buns = False
#         self.sauce = []
#
#     def __str__(self):
#         string = ''
#         if self.vegan:
#             string += 'VEGAN BURGER: '
#         if self.meat:
#             string += 'MEAT BURGER: '
#         if self.beef:
#             string += 'beef, '
#         if self.falafel:
#             string += 'falafel, '
#         if self.buns:
#             string += '2 buns, '
#         if self.sauce:
#             string += 'sauce '
#         for s in self.sauce:
#             string += '- ' + str(s) + '\n'
#         return string
#
#
# class MustardSauce:
#     def __str__(self):
#         return 'mustard'
#
#
# class MayonnaiseSauce:
#     def __str__(self):
#         return 'mayonnaise'
#
#
# class BurgerBuilder(ABC):
#     @abstractmethod
#     def build_burger(self):
#         pass
#
#
# class BeefBurgerBuilder(BurgerBuilder):
#     def __init__(self):
#         self.product = Burger()
#
#     def get_product(self):
#         return self.product
#
#     def build_burger(self):
#         self.product.meat = True
#         self.product.beef = True
#         self.product.buns = True
#         self.product.sauce.append(MustardSauce())
#
#
# class VeganBurgerBuilder(BurgerBuilder):
#     def __init__(self):
#         self.product = Burger()
#
#     def get_product(self):
#         return self.product
#
#     def build_burger(self):
#         self.product.vegan = True
#         self.product.falafel = True
#         self.product.buns = True
#         self.product.sauce.append(MayonnaiseSauce())
#
#
# burger = BeefBurgerBuilder()
# burger.build_burger()
# print(burger.get_product())
#
# burger = VeganBurgerBuilder()
# burger.build_burger()
# print(burger.get_product())


# task 2

# class Pasta:
#     def __init__(self):
#         self.tagliatelle = False
#         self.tortillioni = False
#         self.spaghetti = False
#         self.pasta_type = []
#         self.sauce = []
#         self.filling = []
#         self.additives = []
#
#     def __str__(self):
#         string = ''
#         if self.tagliatelle:
#             string += 'TAGLIATELLE WITH MUSHROOMS IN CREAM SAUCE\n'
#         if self.tortillioni:
#             string += 'TORTILLONI WITH ITALIAN VEGETABLE MIXTURE\n'
#         if self.spaghetti:
#             string += 'SPAGHETTI WITH TOMATOES\n'
#         if self.pasta_type:
#             string += 'Type of pasta:\n'
#         for s in self.pasta_type:
#             string += "- " + str(s) + "\n"
#         if self.sauce:
#             string += 'Sauce:\n'
#         for s in self.sauce:
#             string += "- " + str(s) + "\n"
#         if self.filling:
#             string += 'Filling:\n'
#         for s in self.filling:
#             string += "- " + str(s) + "\n"
#         if self.additives:
#             string += 'Additives\n'
#         for s in self.additives:
#             string += "- " + str(s) + "\n"
#         return string
#
#
# class TagliatellePasta:
#     def __str__(self):
#         return 'tagliatelle'
#
#
# class TortillioniPasta:
#     def __str__(self):
#         return 'tortillioni'
#
#
# class SpaghettiPasta:
#     def __str__(self):
#         return 'spaghetti'
#
#
# class CreamSauce:
#     def __str__(self):
#         return 'cream sauce'
#
#
# class PestoSauce:
#     def __str__(self):
#         return 'pesto sauce'
#
#
# class CheeseSauce:
#     def __str__(self):
#         return 'cheese sauce'
#
#
# class PorciniMushrooms:
#     def __str__(self):
#         return 'porcini mushrooms'
#
#
# class Wine:
#     def __str__(self):
#         return 'white wine'
#
#
# class Garlic:
#     def __str__(self):
#         return 'garlic'
#
#
# class Butter:
#     def __str__(self):
#         return 'butter'
#
#
# class Parmesan:
#     def __str__(self):
#         return 'parmesan'
#
#
# class ItalianBlend:
#     def __str__(self):
#         return 'italian blend'
#
#
# class Tomatoes:
#     def __str__(self):
#         return 'tomatoes'
#
#
# class CherryTomatoes:
#     def __str__(self):
#         return 'cherry tomatoes'
#
#
# class Salt:
#     def __str__(self):
#         return 'salt'
#
#
# class PastaBuilder(ABC):
#     @abstractmethod
#     def reset(self):
#         pass
#
#     @abstractmethod
#     def build_pasta_type(self):
#         pass
#
#     @abstractmethod
#     def build_sauce(self):
#         pass
#
#     @abstractmethod
#     def build_filling(self):
#         pass
#
#     @abstractmethod
#     def build_additives(self):
#         pass
#
#
# class TagliatelleBuilder(PastaBuilder):
#     def __init__(self):
#         self.product = Pasta()
#
#     def reset(self):
#         self.product = Pasta()
#
#     def get_product(self):
#         return self.product
#
#     def build_pasta_type(self):
#         self.product.tagliatelle = True
#         self.product.pasta_type.append(TagliatellePasta())
#
#     def build_sauce(self):
#         self.product.sauce.append(CreamSauce())
#
#     def build_filling(self):
#         self.product.filling.append(PorciniMushrooms())
#         self.product.filling.append(Wine())
#
#     def build_additives(self):
#         self.product.additives.append(Garlic())
#         self.product.additives.append(Butter())
#         self.product.additives.append(Parmesan())
#
#
# class TortillioniBuilder(PastaBuilder):
#     def __init__(self):
#         self.product = Pasta()
#
#     def reset(self):
#         self.product = Pasta()
#
#     def get_product(self):
#         return self.product
#
#     def build_pasta_type(self):
#         self.product.tortillioni = True
#         self.product.pasta_type.append(TortillioniPasta())
#
#     def build_sauce(self):
#         self.product.sauce.append(PestoSauce())
#
#     def build_filling(self):
#         self.product.filling.append(ItalianBlend())
#
#     def build_additives(self):
#         self.product.additives.append(Garlic())
#         self.product.additives.append(Butter())
#         self.product.additives.append(Parmesan())
#         self.product.additives.append(Salt())
#
#
# class SpaghettiBuilder(PastaBuilder):
#     def __init__(self):
#         self.product = Pasta()
#
#     def reset(self):
#         self.product = Pasta()
#
#     def get_product(self):
#         return self.product
#
#     def build_pasta_type(self):
#         self.product.spaghetti = True
#         self.product.pasta_type.append(SpaghettiPasta())
#
#     def build_sauce(self):
#         self.product.sauce.append(CheeseSauce())
#
#     def build_filling(self):
#         self.product.filling.append(Tomatoes())
#
#     def build_additives(self):
#         self.product.additives.append(Garlic())
#         self.product.additives.append(Butter())
#         self.product.additives.append(CherryTomatoes())
#         self.product.additives.append(Salt())
#
#
# pasta = TagliatelleBuilder()
# pasta.build_pasta_type()
# pasta.build_sauce()
# pasta.build_filling()
# pasta.build_additives()
# print(pasta.get_product())
#
# pasta = TortillioniBuilder()
# pasta.build_pasta_type()
# pasta.build_sauce()
# pasta.build_filling()
# pasta.build_additives()
# print(pasta.get_product())
#
# pasta = SpaghettiBuilder()
# pasta.build_pasta_type()
# pasta.build_sauce()
# pasta.build_filling()
# pasta.build_additives()
# print(pasta.get_product())


# task 3
# from copy import deepcopy
#
#
# class Prototype(ABC):
#     @abstractmethod
#     def clone(self):
#         pass
#
#
# class User(Prototype):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.performed_operation = False
#
#     def __operation(self):
#         self.performed_operation = True
#
#     def clone(self):
#         return deepcopy(self)
#
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
#
#
# u1 = User('Leo', 23)
# u2 = u1.clone()
# print(u1)
# print(u2)

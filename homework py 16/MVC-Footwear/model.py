from csv import reader, writer


class Footwear:
    def __init__(self, article, gender, footwear_type, color, price, brand, size):
        self.article = article
        self.gender = gender
        self.footwear_type = footwear_type
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size

    def __str__(self):
        return ', '.join([f'{key.capitalize()}: {value}' for key, value in self.__dict__.items()])


class Model:
    def __init__(self, filename):
        self.filename = filename
        self.database = []

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = reader(f)
                self.database = []
                for string in data:
                    self.database.append(self.__string_to_footwear__(string))
        except FileNotFoundError:
            print('Error in loading database. Proceed with empty data.')

    @staticmethod
    def __string_to_footwear__(string):
        article = string.pop(0)
        gender = string.pop(0)
        footwear_type = string.pop(0)
        color = string.pop(0)
        price = string.pop(0)
        if not price.startswith('$'):
            price = '$' + price
        brand = string.pop(0)
        size = string.pop(0)
        return Footwear(article, gender, footwear_type, color, price, brand, size)

    @staticmethod
    def __footwear_to_string__(footwear):
        result = [footwear.article, footwear.gender, footwear.footwear_type,
                  footwear.color, footwear.price, footwear.brand, footwear.size]
        return result

    def __save_data__(self):
        with open(self.filename, 'w', encoding='utf-8') as csv_file:
            data_writer = writer(csv_file)
            data_writer.writerows(map(self.__footwear_to_string__, self.database))

    def add_footwear(self, footwear_data):
        self.database.append(self.__string_to_footwear__(footwear_data))
        self.__save_data__()

    def get_footwear_by(self, targets):
        targets = list(map(str.strip, targets.split(',')))
        shoes = []
        for target in targets:
            for shoe in self.database:
                if target in ' '.join(map(str, shoe.__dict__.values())) and shoe not in shoes:
                    shoes.append(shoe)
        return shoes

    def delete_footwear(self, footwear):
        self.database.remove(footwear)
        self.__save_data__()

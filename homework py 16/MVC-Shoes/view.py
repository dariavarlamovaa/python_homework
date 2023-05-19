class View:
    @staticmethod
    def wait_user_answer():
        print('Choose the command:\n'
              '1. Add one pair of shoes\n'
              '2. Show all the shoes\n'
              '3. Find a pair of shoes by ... \n'
              '4. Delete a pair of shoes\n'
              '0. Exit the program')
        query = input('Enter the number: ')
        return query

    @staticmethod
    def get_footwear_data():
        props = ['article', 'gender', 'type of footwear', 'color', 'price', 'brand', 'size']
        data = [input(f'Input {prop}: ').capitalize().strip() for prop in props]
        return data

    @staticmethod
    def get_target():
        targets = input('Enter the keywords to find footwear, comma separated: ').capitalize().strip()
        return targets

    @staticmethod
    def print_footwear(footwear):
        if footwear:
            [print(f'{i}. {footwear}') for i, footwear in enumerate(footwear, 1)]
        else:
            'Footwear was not found'

    def get_deleted_context(self, footwear):
        self.print_footwear(footwear)
        number = int(input('Enter number of the footwear you want to delete: '))
        return number

    @staticmethod
    def print_an_error():
        print('Input error. Try again')

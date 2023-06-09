class TaskManager:
    def __init__(self):
        self.__tasks = ['Wash', 'Clean', 'Dance', 'Check', 'Sing']
        self.__users = {'Rx50': {'Name': 'Petro', 'Email': 'email_petro', 'Role': 'Admin', 'Tasks': ['Check']},
                        'U01': {'Name': 'Vova', 'Email': 'email_vova', 'Role': 'Standard', 'Tasks': ['Wash', 'Clean']},
                        'Rx90': {'Name': 'Pablo', 'Email': 'email_pablo', 'Role': 'Admin', 'Tasks': []},
                        'U02': {'Name': 'Leo', 'Email': 'email_leo', 'Role': 'Standard', 'Tasks': ['Sing']}}

    def users(self):
        return self.__users

    def tasks(self):
        return self.__tasks

    def add_task(self, task):
        self.__tasks.append(task)
        print(f'Task "{task}" added successfully')

    def assign_task(self, task, user_id):
        user = self.get_user_by_id(user_id)
        if user is not None:
            if 'tasks' in user:
                user['Tasks'].append(task)
            else:
                user['Tasks'] = [task]
            print(f'Task "{task}" assigned to user {user_id}')
        else:
            print('User not found.')

    def mark_task(self, task):
        if task in self.__tasks:
            self.__tasks.remove(task)
            print(f'Task "{task}" marked as completed')
        else:
            print(f'Task "{task}" is not in the list')

    def print_task(self):
        if self.__tasks:
            for idx, task in enumerate(self.__tasks, 1):
                print(f'{idx}. {task}')
        else:
            print('Tasks list is empty.')

    def get_user_by_id(self, user_id):
        return self.__users.get(user_id)


class User:
    def __init__(self):
        self.__idx = ''
        self.__name = ''
        self.__email = ''
        self.__role = ''
        self.tm = TaskManager()

    def add_user(self, new_idx, new_name, new_email, new_role):
        if self.tm.get_user_by_id(new_idx) is None:
            new_user = {
                'Name': new_name,
                'Email': new_email,
                'Role': new_role,
                'Tasks': []
            }
            self.tm.users()[new_idx] = new_user
            print(f'New user added successfully')
        else:
            print('This user already exists')

    def update_user(self, idx):
        if self.tm.get_user_by_id(idx) is not None:
            new_name = input(f'Enter new name of the {idx} user: ')
            new_email = input(f'Enter new email of the {idx} user: ')
            new_role = input(f'Enter new role of the {idx} user: ')
            self.tm.users()[idx]['Name'] = new_name
            self.tm.users()[idx]['Email'] = new_email
            self.tm.users()[idx]['Role'] = new_role
            print(f'{idx}`s info was updated ')
        else:
            print('User not found')

    def print_assigned_tasks(self, idx):
        user = self.tm.get_user_by_id(idx)
        if user is not None:
            assigned_tasks = user.get('Tasks', {})
            if assigned_tasks:
                print('Assigned tasks:')
                for task_idx, task in enumerate(assigned_tasks, 1):
                    print(f'{task_idx}. {task}')
            else:
                print('No tasks assigned to this user.')
        else:
            print('User not found.')


class Menu:
    def __init__(self):
        self.tm = TaskManager()
        self.us = User()
        self.user_idx = input('Enter your id: ')

    def choose_role(self):
        try:
            if self.tm.users()[self.user_idx].get('Role') == 'Admin':
                self.show_admin_menu()
            elif self.tm.users()[self.user_idx].get('Role') == 'Standard':
                self.show_standard_menu()
        except KeyError:
            print('Permission denied')

    def show_admin_menu(self):
        while True:
            print('-' * 20)
            command = input('1. Add a new user\n'
                            '2. Add a new task\n'
                            '3. Assign a task to the user\n'
                            '4. Mark task as completed\n'
                            '5. Print all tasks\n'
                            '6. Print all assigned tasks of the user\n'
                            '7. Update user`s info\n'
                            '0. Exit\n'
                            'Enter your command: ')
            if command == '1':
                new_idx = input('Enter user`s id: ').strip()
                new_name = input('Enter user`s name: ').strip().title()
                new_email = input('Enter user`s email: ').strip()
                new_role = input('Enter user`s role (admin/standard): ').strip().capitalize()
                if new_role in {'Admin', 'Standard'}:
                    self.us.add_user(new_idx, new_name, new_email, new_role)
                else:
                    print('The role must be Admin or Standard')
                    pass
            elif command == '2':
                title = input('Enter the task`s title: ').capitalize()
                self.tm.add_task(title)
            elif command == '3':
                if self.tm.tasks():
                    self.tm.print_task()
                    choice = int(input('Enter the number of the task to assign: '))
                    task = self.tm.tasks()[choice - 1]
                    user_id = input('Enter user`s id to assign to: ')
                    self.us.tm.assign_task(task, user_id)
                else:
                    print('The list is empty')
            elif command == '4':
                self.tm.print_task()
                choice = int(input('Enter the number of the task to mark as completed: '))
                task = self.tm.tasks()[choice - 1]
                self.tm.mark_task(task)
            elif command == '5':
                self.tm.print_task()
            elif command == '6':
                index = input('Enter user`s id: ')
                self.us.print_assigned_tasks(index)
            elif command == '7':
                index = input('Enter user`s id: ')
                self.us.update_user(index)
            elif command == '0':
                print('Shutting down...Goodbye')
                break
            else:
                print('Invalid input')
                pass

    def show_standard_menu(self):
        while True:
            print('-' * 20)
            command = input('1. Show assigned tasks\n'
                            '0. Exit\n'
                            'Enter your command: ')

            if command == '1':
                self.us.print_assigned_tasks(self.user_idx)
            elif command == '0':
                print('Shutting down...Goodbye')
                break
            else:
                print('Invalid input')
                pass


if __name__ == '__main__':
    Menu().choose_role()

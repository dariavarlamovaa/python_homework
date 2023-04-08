def file_open():
    employees = {}
    while True:
        staff_file = input('enter the file name: ')
        try:
            with open(staff_file, 'r') as f:
                content = f.readlines()
                for line in content:
                    name, age, email, position, salary = line.strip().split(', ')
                    employees[name] = {'age': age, 'email': email, 'position': position, 'salary': salary}
            break
        except (FileNotFoundError, FileExistsError, IsADirectoryError):
            print('file was not found. try again')
            pass
    return employees


def staff(employees):
    while True:
        print('---------------')
        # for e in employees:
        #     print(f'{e}: {employees[e]}', end='\n')
        # print('---------------')
        command = int(input('1-add a new employee\n'
                            '2-edit employee info\n'
                            '3-delete employee info\n'
                            '4-find an employee in the database by last name\n'
                            '5-display information about all employees of the specified age\n'
                            '6-display information about all employees '
                            'whose last name begins with the specified letter\n'
                            '0-exit and save\n'
                            'enter new command: '))
        if command == 1:
            name = input('full name: ').title().strip()
            age = input('age: ').strip()
            email = input('email: ').strip()
            position = input('position: ').capitalize().strip()
            salary = input('salary: ').strip()
            employees[name] = {'age': age, 'email': email, 'position': position, 'salary': salary}
            print(f'{name} was successfully added')
            save_info_file(employees)

        elif command == 2:
            name = input('enter the employee`s name: ')
            matching_employees = []
            for key in employees.keys():
                if name.lower() in key.lower():
                    matching_employees.append(key)
            if not matching_employees:
                print(f'{name} was not found in the database')
            else:
                if len(matching_employees) == 1:
                    employee_name = matching_employees[0]
                    age = input('age: ').strip()
                    email = input('email: ').strip()
                    position = input('position: ').capitalize().strip()
                    salary = input('salary: ').strip()
                    employees[employee_name] = {'age': age, 'email': email, 'position': position, 'salary': salary}
                    print(f'{employee_name}`s has been successfully changed')
                else:
                    print('matching employees are:')
                    for index, person in enumerate(matching_employees, 1):
                        print(f'{index}. {person}')
                    num = int(input('enter the number of the matching employee to replace: '))
                    age = input('age: ').strip()
                    email = input('email: ').strip()
                    position = input('position: ').capitalize().strip()
                    salary = input('salary: ').strip()
                    employees[matching_employees[num - 1]] = {'age': age, 'email': email,
                                                              'position': position, 'salary': salary}
                    print(f'{matching_employees[num - 1]}`s info has been successfully changed')
                save_info_file(employees)

        elif command == 3:
            name = input('enter the employee`s name: ')
            matching_employees = []
            for key in employees.keys():
                if name.lower() in key.lower():
                    matching_employees.append(key)
            if not matching_employees:
                print(f'{name} was not found in the database')
            else:
                if len(matching_employees) == 1:
                    employee_name = matching_employees[0]
                    del employees[employee_name]
                    print(f'{employee_name}`s has been successfully deleted')
                else:
                    print('matching employees are:')
                    for index, person in enumerate(matching_employees, 1):
                        print(f'{index}. {person}')
                    num = int(input('enter the number of the matching employee to delete: '))
                    del employees[matching_employees[num - 1]]
                    print(f'{matching_employees[num - 1]}`s info has been successfully deleted')
                save_info_file(employees)

        elif command == 4:
            last_name = input('enter the employee`s last name: ')
            matching_employees = []
            for employee in employees:
                name = employee.split()
                lst_nm = name[-1]
                if lst_nm == last_name:
                    matching_employees.append(employee)
            if matching_employees:
                print(f'there are {len(matching_employees)} employee(s) with "{last_name}" last name')
                print()
                for person in matching_employees:
                    print(f'Name: {person}')
                    for key, value in employees[person].items():
                        print(f'{key.capitalize()}: {value}')
                    print()
                save_found_info(matching_employees, employees)
            else:
                print(f'there is no employee with the last name {last_name}')

        elif command == 5:
            age = input('enter the age: ')
            matching_employees = []
            for employee, info in employees.items():
                if info['age'] == age:
                    matching_employees.append(employee)
            if matching_employees:
                print(f'there are {len(matching_employees)} employee(s) who are {age} years old')
                print()
                for person in matching_employees:
                    print(f'Name: {person}')
                    for key, value in employees[person].items():
                        print(f'{key.capitalize()}: {value}')
                    print()
                save_found_info(matching_employees, employees)
            else:
                print(f'there is no employee in the database who is {age} years old.')
        elif command == 6:
            letter = input('enter the first letter of the employee`s last name: ')
            matching_employees = []
            for employee in employees:
                name = employee.split()
                last_name = name[-1]
                if last_name.startswith(letter):
                    matching_employees.append(employee)
            if matching_employees:
                print(f'there are {len(matching_employees)} employee(s) '
                      f'whose last name begins with the letter {letter}')
                print()
                for person in matching_employees:
                    print(f'Name: {person}')
                    for key, value in employees[person].items():
                        print(f'{key.capitalize()}: {value}')
                    print()
                save_found_info(matching_employees, employees)
            else:
                print(f'there is no employee whose last name begins with the letter {letter}')
        elif command == 0:
            print('the list of employees has been saved to a file')
            save_info_auto(employees)
        else:
            print('incorrect input.try again')
            pass


def save_info_file(employees):
    save = int(input('do you want to save this information in the file? (1- yes, 2- no): '))
    if save != 1:
        pass
    else:
        with open('main.txt', 'w') as f2:
            new_lines = []
            for n, value in employees.items():
                new_lines.append((n, *value.values()))
            for idx, info in enumerate(new_lines):
                line = ', '.join(info)
                if idx < len(new_lines) - 1:
                    line += '\n'
                f2.write(line)
            print('the list of employees has been saved to a file')


def save_info_auto(employees):
    with open('main.txt', 'w') as f2:
        new_lines = []
        for n, value in employees.items():
            new_lines.append((n, *value.values()))
        for idx, info in enumerate(new_lines):
            line = ', '.join(info)
            if idx < len(new_lines) - 1:
                line += '\n'
            f2.write(line)


def save_found_info(matching_employees, employees):
    save = int(input('do you want to save this information in the file? (1- yes, 2- no): '))
    if save != 1:
        pass
    else:
        while True:
            file_name = input('enter a file name to save the found information: ')
            try:
                with open(file_name, 'w') as fs:
                    for employee in matching_employees:
                        employee_info = [employee]
                        for key, value in employees[employee].items():
                            employee_info.append(str(value))
                        fs.write(', '.join(employee_info) + '\n')
                print('the found information was saved in the file')
                break
            except (FileNotFoundError, FileExistsError, IsADirectoryError):
                print('file was not found. try again')
                pass


staff(file_open())

while True:
    choose = int(input('Выберете номер фигуры (1-10, 0 - для выхода): '))
    if choose == 0:
        print('Пока!')
        break
    elif choose == 1:
        for i in range(5, 0, -1):
            print((5 - i) * ' ' + i * '*')
    elif choose == 2:
        for i in range(1, 6):
            print('*' * i)
    elif choose == 3:
        for i in range(5, 0, -2):
            print((5 - i) // 2 * ' ' + '*' * i)
    elif choose == 4:
        for i in range(1, 6, 2):
            print((6 - i) // 2 * ' ' + '*' * i)
    elif choose == 5:
        for i in range(5, 0, -2):
            print((5 - i) // 2 * ' ' + '*' * i)
        for i in range(1, 6, 2):
            print((6 - i) // 2 * ' ' + '*' * i)
    elif choose == 6:
        for i in range(6, -6, -2):
            print((6 - abs(i)) // 2 * ' * ' + '   ' * abs(i) + (6 - abs(i)) // 2 * ' * ')
    elif choose == 7:
        for i in range(1, 6):
            print('*' * i)
        for i in range(4, 0, -1):
            print('*' * i)
    elif choose == 8:
        for i in range(5, 0, -1):
            print(i * ' ' + (6 - i) * '*')
        for i in range(0, 6):
            print(i * ' ' + (6 - i) * '*')
    elif choose == 9:
        for i in range(5, 0, -1):
            print('*' * i)
    else:
        if choose == 10:
            for i in range(5, 0, -1):
                print(i * ' ' + (6 - i) * '*')
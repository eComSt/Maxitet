# программа для проверки логина и пароля

# login = 'Max'
# password = '123456!'

# login_input = input('Введите логин:')
# password_input = input('Введите пароль:')

# если логин не совпадает ИЛИ пароль не совпадает
# != - это проверка на неравенство
# if login != login_input and password != password_input:
#     print('Доступ запрещен - неверные логин и пароль!')

# проверка, что логин неверный
# elif login != login_input:
#     print('Неверный логин!')

# проверка, что пароль неверный
# elif password != password_input:
#     print('Неверный пароль!')

# else:
#     print('Добро пожаловать!')


# Дорабатываем калькулятор

# number_1 = input('Введите 1-е число:')
# number_2 = input('Введите 2-е число:')

# # проверяем, что number_1 и number_2 состоят из цифр
# if number_1.isnumeric() and number_2.isnumeric():
#     number_1 = int(number_1)
#     number_2 = int(number_2)
#     oper = input('Введите операцию:')

#     # проверка, что введен +
#     if oper == '+':
#         result = number_1 + number_2
#         print('Сумма:', result)
#     # проверка, что введен -
#     elif oper == '-':
#         result = number_1 - number_2
#         print('Разность:', result)
#     # проверка, что введена *
#     elif oper == '*':
#         result = number_1 * number_2
#         print('Произведение:', result)
#     # проверка, что введен /
#     elif oper == '/':
#         if number_2 != 0:
#             result = number_1 / number_2
#             print('Частное от деления:', result)
#         else:
#             print('Делить на ноль нельзя!')
#     # проверка, что введен //
#     elif oper == '//':
#         if number_2 != 0:
#             result = number_1 // number_2
#             print('Целая часть от деления:', result)
#         else:
#             print('Делить на ноль нельзя!')
#     # проверка, что введен %
#     elif oper == '%':
#         if number_2 != 0:
#             result = number_1 % number_2
#             print('Остаток от деления:', result)
#         else:
#             print('Делить на ноль нельзя!')
#     # проверка, что введена некорректная операция
#     else:
#         print('Введена некорретная операция!')
# # проверка, что введены не числа
# else:
#     print('Введены не числа!')

# Функции max() и min()

# num_1 = 1
# num_2 = 543
# print(max(num_1, num_2, 102130, 9, -5, -234324))
# print(min(num_1, num_2, 102130, 9, -5, -234324))
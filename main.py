#1.Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

print("Введите два числа:")
arg_1, arg_2 = int(input()), int(input())
def divide(arg_1, arg_2):
    while True:
        if arg_2 == 0:
            return None
        else:
            return arg_1 / arg_2
print(divide(arg_1, arg_2))


# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

x1,x2,x3,x4,x5,x6 = input("Ведите Ваше имя: "),input("Введите Вашу фамилию: "),input("Введите Ваш год рождения: "),input("Введите Ваш город: "),input("Введите Ваш почтовый ящик: "),input("Введите Ваш номер телефона: ")
def func(x1, x2, x3, x4, x5, x6):
   print(x1,x2,x3, x4, x5, x6)
print(f'Имя: {x1}, Фамилия: {x2}, Год рождения: {x3}, Город проживания: {x4}, Email: {x5}, Телефон: {x6}')


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
   print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')

my_func(
   int(input('Аргумент 1:')),
   int(input('Аргумент 2:')),
   int(input('Аргумент 3:')),
)


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
   if y == 0:
      return 1
   y = abs(y)
   return x * my_func(x, y - 1)
while True:
   try:
      x = float(input('Аргумент 1:'))
      if x < 0:
         print('Неверный формат')
      y = int(input('Аргумент 2:'))
      if y > 0:
         print('Неверный формат')
      print(1 / my_func(x, y))
      break
   except Exception as a:
      print('Неверный формат')


# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

s = 0
try:
    while True:
        for n in map(int, input().split()):
            s += n
        print(s)
except ValueError:
    print(s)

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(*args):
    x = input()
    return(x.capitalize())
print(int_func())

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(*args):
    while True:
        args = input("Введите слова используя пробел: ")
        if args == 'end':
            break
        try:
           return args.title()
        except:
            break
print("Теперь Ваши слова начинаются с заглавной буквы:", int_func())


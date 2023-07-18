
# birds=100
# def print_texas():
#     global birds
#     birds = 5000
#     print('В Техасе обитает', birds, 'птиц.')
#
#
# def print_california():
#     print('В Калифорнии обитает', birds, 'птиц.')
#
#
# print_texas()
# print_california()
#
# print_texas()
# print_california()

# from string import Template
#
# d = dict(who='tim')
# s = Template('$who will not be do it').template
# print(s)
# print(Template('/{who} ${who} $what').safe_substitute(d, what='ttttt'))

# import string
#
# str_ = 'albert sadfsa*sdfsaf'
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.capwords(str_, '*'))

# for align, text in zip('<^>', ['left', 'center', 'right']):
#     print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
# import datetime
#
# # datetime форматирование
# # date = datetime.datetime.now()
# # print(F"It's now: {date=:%Y/%m/%d %H:%M:%S}")
# # print(F"It's now: {date:%Y/%m/%d %H:%M:%S}")
# member_since = datetime.date
# delta = datetime.date.today()- member_since
# print(f' {delta.day=:,d}')
#
# text = (f'nasme{100}',
#         f'age{50}')
# print(text)
# # num = "{:{align}{width}.{precision}f}"
# # n=123
# # # передача кодов формата в качестве аргументов
# # print(num.format(n, align='<', width=8, precision=2))
# # import timeit
# # print(timeit.timeit("""name = "Eric"
# # age = 74
# # '%s is %s.' % (name, age)""", number = 10000))
# # print('test {n1!s:^10.5} vvvvvv {k}'.format(n1='-123123.567', k=2, l=305, b=40))
# # print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
# # print('test %(n1)-10d vvvvvv %(n4)s' % {"n1": 10, "n2": 'asd', "n3": 2, 'n4': 'sss'})
# # print('test %(n1)010d vvvvvv %(n4)s' % {"n1": -10, "n2": 'asd', "n3": 2, 'n4': 'sss'})
# # print('test %*.*s vvvvvv %s' % (10,2,305,40))
#
# # print('Привет,', name := input())
#
# # # объявление функции
# # import math
# #
# #
# # def solve(a, b, c):
# #     discr = b ** 2 - 4 * a * c
# #     # print("Дискриминант D = %.2f" % discr)
# #     if discr > 0:
# #         x2 = (-b - math.sqrt(discr)) / (2 * a)
# #         x1 = (-b + math.sqrt(discr)) / (2 * a)
# #         if x1 >= x2:
# #             return x2, x1
# #         else:
# #             return x1, x2
# #     elif discr == 0:
# #         return -b / (2 * a), -b / (2 * a)
# #
# #
# #
# # # считываем данные
# # a, b, c = int(input()), int(input()), int(input())
# #
# # # вызываем функцию
# # x1, x2 = solve(a, b, c)
# # print(x1, x2)
#
# # def get_all_divisors_brute(n):
# #     numbers= [i for i in range(1, int(n / 2) + 1) if n % i == 0]
# #     numbers.append(n)
# #     return len(numbers)
# #
# # print(get_all_divisors_brute(10))
#
# # import collections
# # import itertools
# #
# #
# # def get_prime_divisors(n):
# #     i = 2
# #     while i * i <= n:
# #         if n % i == 0:
# #             n /= i
# #             yield i
# #         else:
# #             i += 1
# #
# #     if n > 1:
# #         yield n
# #
# #
# # def calc_product(iterable):
# #     acc = 1
# #     for i in iterable:
# #         acc *= i
# #     return acc
# #
# #
# # def get_all_divisors(n):
# #     primes = get_prime_divisors(n)
# #
# #     primes_counted = collections.Counter(primes)
# #
# #     divisors_exponentiated = [
# #         [div ** i for i in range(count + 1)]
# #         for div, count in primes_counted.items()
# #     ]
# #
# #     for prime_exp_combination in itertools.product(*divisors_exponentiated):
# #         yield calc_product(prime_exp_combination)
# #
# # print(list(get_all_divisors(10))) # 8!
# # numbers = [i for i in input() if i.isdigit()]
# # print(''.join(numbers))
# # print(a - b)
# # print(a * b)
# # print(a / b)
# # print(a // b)
# # print(a % b)
# # print((a ** 10 + b ** 10) ** 0.5)
#
# # x1 = int(input())
# # x2 = int(input())
# #
# # if x1 > x2:
# #     print('NO')
# # elif x1 < x2:
# #     print('YES')
# # else:
# #     print('Don\'t know')
# #
# # a, b, c = int(input()), int(input()), int(input())
# # if c >= a + b or b >= a + c or a >= c + b:
# #     print('NO')
# # else:
# #     print('YES')
# # num = int(input())
# # if 999 < num <= 9999 and (num % 7 == 0 or num % 17 == 0):  # num >= 100 and num <= 999
# #     print('YES')
# # else:
# #     print('NO')
#
# # num = int(input())
# # if -30 < num < -1 or 7 < num < 26:     # num >= 100 and num <= 999
# #     print('Принадлежит')
# # else:
# #     print('Не принадлежит')
#
# # a = int(input())
# # if a >= 2 and a <= 17:
# #     b = 3
# #     p = a * a + b * b
# # else:
# #     b = 5
# # p = (a + b) * (a + b)
# # print(p)
#
# # num1 = 34
# # num2 = 81
# # if num1 // 9 == 0 or num2 % 9 == 0:
# #     print('число', num1, 'выиграло')
# # else:
# #     print('число', num2, 'выиграло')
# #
# # a = 2
# # b = 4
# # c = 6
# # print(a == 2 or b > 2)
# # print(6 <= c and a > 3)
# # print(1 != b and c != 3)
# # print(a >= -1 or a <= b)
# # print(not (a > 2))
# # print(not (c <= 10))
#
# # num = int(input())
# # digit3 = num % 10
# # digit2 = (num // 10) % 10
# # digit1 = (num // 100) % 10
# # digit0 = num // 1000
# # print('Цифра в позиции тысяч равна', digit0)
# # print('Цифра в позиции сотен равна', digit1)
# # print('Цифра в позиции десятков равна', digit2)
# # print('Цифра в позиции единиц равна', digit3)
# # print(digit1, digit2, digit3, sep='')
# # print(digit1, digit3, digit2, sep='')
# # print(digit2, digit1, digit3, sep='')
# # print(digit2, digit3, digit1, sep='')
# # print(digit3, digit1, digit2, sep='')
# # print(digit3, digit2, digit1, sep='')
# # a4 = int(input())
# # print(a4, 'мин - это', a4 // 60, 'час', a4 % 60, 'минут')
# #
# # # a = int(input())
# # # print(a, a * 2, a * 3, a * 4, a * 5, sep='---')
# #
# # # a1, a2, a3, a4 = int(input()), int(input()), int(input()), int(input())
# # # print((a1 + a2 + a3 + a4) * 3)
# # #
# # # # a = int(input())
# # # # print('Следующее за числом', a, 'число:', a + 1)
# # # # print('Для числа', a, 'предыдущее число:', a - 1)

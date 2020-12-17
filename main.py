# nums = [num for num in range(20)]
# print(nums)
#
# nums2 = []
# for i in range(20):
#     nums2.append(i)
# print(nums2)
#
# from datetime import datetime
# start = datetime.now()
# nums = [num for num in range(20)]
# print(nums)
# finish = datetime.now()
# print(datetime.now())
# start2 = datetime.now()
# nums2 = []
# for i in range(2000):
#     nums2.append(i)
# print(nums2)
# finish2 = datetime.now()
# print(datetime.now())

# even = [num for num in range(50) if num % 2 == 1 and num % 10 == 1]
# print(even)
#
# my_func = lambda x, y: x + y
# print(my_func(10, 10))

# def add(x,y):
#     return x * y
# print(add(10,10))

# Stroka = 'Hello'
# ne_stroka = list(map('hello'))

# list1 = [1, 4, 6, 7, 9, 3]
# def my_func(x):
#     return x ** x
# new_list = list(map(my_func, list1))
# print(new_list)

# numbers = [1, 2, 5, 6, 9, 3]
# def my_func(x):
#     x += 10
#     return x
# new_num = list(map(my_func, numbers))
# print(new_num)

# text = input('Enter you text: ')
#
# def my_func(x):
#     return x.upper()
# text2 = list(map(my_func, text))
# text3 = ''.join(text2)
# print(text3)

# mixed = ['mac', 'proso', 'mak', 'maker', 'proso', 'mak']
# zolushka = list(filter(lambda x: x == 'mak', mixed))
# print(zolushka)

# from functools import reduce
#
# nums = [x for x in range(50)]
# lambda_func = lambda x, y: x + y
# summ_all = reduce(lambda_func, nums)
# print(summ_all)

# a = [1, 2, 3]
# text = ('hello mama')
# nums = [x for x in range(20)]
# tuple1 = ('ai', 'oi', 'boi', ' hey', ' mey', 'tey')
#
# zip_function = list(zip(a, text, nums, tuple1))
# print(zip_function)
#
# tuple_ = tuple(zip(text, nums))
# print(tuple_)
#
# dict_ = dict(zip(text, nums))
# print(dict_)

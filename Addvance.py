     # FUNCTION


# def wish(name):
#     print("Good morning",name)
# wish("Tophan")


# def square(num):
#     print("The sqare of number :- 4",num*num)
# square(4)


# def even_odd(num):
#     if num%2==0:
#         print(num,"is an even number")
#     else:
#         print(num,"is an odd number")
# even_odd(20)
# even_odd(21)


# def wish(a,b):
#     print(a+b)
#     print(a-b)
# wish(5,3)


# def wish(name,msg):
#     print("Hello",name,msg)
#     print("Hello",msg,name)
# wish("Tophan","Good morning")


# def wish(name="Guest"):
#     print(name)
# wish()


# def local():
#     a=10
#     print(a)
# local()


# a=20
# def globa():
#     print(a)
# globa()

# Factorial

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print('Factorial of 5 is :-', factorial(5))


# Lambda

# a=lambda n:n*n
# print('The square is the number is :-',a(4))


# a=lambda a,b:a+b
# print("The sum number is ",a(10,20))


# a=lambda a,b:a if a>b else b
# print("The biggest nu is",a(10,30))

# Decorater


# def decor(func):
#     def inner(name):
#         if name=="Tophan":
#             print("Hello How are you")
#         else:
#             print("Hello Good morning")
#         func(name)
#     return inner
# @decor
# def wish(name):
#     print("welcome")
# wish("Tophan")
# wish("Suresh")



# Filter

# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# i=[4,8,6,75,5,4,6]
# l=list(filter(even,i))
# print(l)

# Filter with Lambda

# i=[4,8,6,75,5,4,6]
# l=list(filter(lambda n:n%2==0,i))
# print(l)

# Map

# def double(n):
#     return 2*n
# i=[4,5,7,5,6,3]
# l=list(map(double,i))
# print(l)

# Map with Lambda
#
# i=[4,5,7,5,6,3]
# l=list(map(lambda n:n*2,i))
# print(l)


# Reuce
#
# from functools import *
# l=[10,20,30,40]
# result=reduce(lambda a,b:a+b,l)
# print(result)

# Alising

# def wish(name):
#     print("Good Night",name)
# greeting=wish
# wish("Suresh")
# greeting("Tophan")
# print(id(wish))
# print(id(greeting))


# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.cricbuzz.com/")

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.cricbuzz.com/')
time.sleep(5)


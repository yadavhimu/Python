# print("Hello Himanshu")

# a=1000
# b=500
# sum=a-b=
# print(sum)

# how take input from user

# name = input("name :")
# print(name)

# name = input("name :")
# age = int(input("age :"))
# marks = float(input("marks : "))

# print("My name is",name,"ang I am", age,"year old","My marks are",marks)

 
  
# str1 = "This is a string.\nwe are creating it in python"
# str2 = "\nThis is a string.\twe are creating it in python"
# print(str1, str2)

# name = input("Enter your name : ") 
# print("length of name is ", len(name))

# str = "hi my name  hhh  himanshu hhh"
# print(str.count("h"))

# >>> num_list = "0123456789"
# >>> num_list[:]
# '0123456789'
# >>> num_list[3:]
# '3456789'
# >>> num_list[:4] 
# '0123'
# >>> num_list[:-1]
# '012345678'
# >>> num_list[-1:] 
# '9'
# >>> num_list[-2:] 
# '89'
# >>> num_list[:-2] 
# '01234567'
# >>>

# >>> chai_type
# 'masala'
# >>> quantity
# 2
# >>> order
# ' I orderd {} cups of {} chai'
# >>> print(order.format(quantity, chai_type))
#  I orderd 2 cups of masala chai
# >>>

# Conditionals 

# Question = Age Group Categorization
# age = 65

# if age < 13:
#     print("child")
# elif age < 20:
#     print("Teenager")
# elif age < 60:
#     print("adult")
# else:
#     print("senior")

# Question = movie ticket pricing
# age = 25
# day = "Wednesday"

# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     # price = price - 2
#     price -= 2

# print("Ticket price for you is $",price)

# Question = Grade Calculator

# x= int(input("What is your exam Score? "))

# if x >=101:
#     print("Please verify your grade again")
#     exit()
# if x >=90:
#     print('Grade A')
# elif x>=80:
#     print('Grade B') 
# elif x>=70:
#     print('Grade C') 
# elif x>=55:
#     print('Grade D') 
# else:
#     print("fail")   

# fruit = "Banana"
# color = "Yellow"

# if fruit == "Banana":
#     if color == "Green":
#        print("Unripe")
#     elif color == "Yellow":
#         print("Ripe") 
#     elif color == "Brown":
#         print("OverRipe")



# year = 2023

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
#     print(year, "is a leap year")
# else:
#     print(year, "is NOT a leap year")

# Loops Problems

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# positive_number_count = 0
# for num in numbers:
#     if num > 0:
#         positive_number_count += 1
# print("Final count of positive number is:", positive_number_count)

# question calculate even number
# n = 10
# sum_even = 0

# for i in range(1, n+1):
#     if i%2 == 0:
#         sum_even += 1
# print("sum of even number is:",sum_even)

# question print the table of 3 and skip 5th itration
# number = 3

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(number, 'x',i,'=',number * i)

# question reverse string

# input_str = "Python"
# reversed_str = ""

# for char in input_str:
#     reversed_str =  reversed_str + char

# print(reversed_str)

# question first non repeated character

# input_str = "teeteracdacd"

# for char in input_str:
#     print(char)
#     if input_str.count(char) == 1:
#         print("Char is:",char)
#         break

# question Calculate factorial

# number = 6
# factorial = 1

# while number > 0:
#     factorial *= number
#     number -= 1
# print("Factorial of this number is :",factorial)

# question validate Input
# while True :
#     number = int(input("Enter value b/w 1 and 10: "))
#     if 1<= number <= 10:
#         print("thanks")
#         break
#     else:
#         print("Invalid number, Try again")

# Question number is prime or not
# number = 31

# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if(number % i) == 0:
#             is_prime = False
#             break

# print(is_prime)

# question= List  uniqueness checker

# items = ["apple", "banana", "orange","apple","mango"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate:", item)
#         break
#     unique_item.add(item)


# question waiting time 
# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while attempts < max_retries:
#     print("Attempt", attempts + 1 ,"-wait time", wait_time, )
#     time.sleep(wait_time)
#     wait_time *=2
#     attempts += 1


# function problem
# def square (number):
#     return number ** 2
# result = square(4)
# print(result)


# function with multiple parameter
# def add(numOne, numTwo):
#     return numOne + numTwo
# print(add(2,5))


# question Polymorphism in function
# def multiply(p1, p2):
#     return p1 * p2

# print(multiply(8, 5))
# print(multiply('a',5))
# print(multiply(5, 'a'))


# def greet(name = "User"):
#     return "Hello, " + name + " !"


# print(greet("chai"))
# print(greet())



# cube = lambda x: x ** 3

# print(cube(3))


# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#     return sum(args)

# print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_kwargs(name="shaktiman", power="lazer")
# print_kwargs(name="shaktiman")
# print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")

# i = 1
# while i <= 5 :
#     i += 1
#     print(i)
# print(i)

# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         yield i

# for num in even_generator(10):
#     print(num)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# SCOPE

# username = "chaiaurcode"

# def func():
    # username = "chai"
#     print(username)

# print(username)
# func()


# x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 12
    
# func3()
# print(x)



# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# myResult = f1()
# myResult()


# def chaicoder(num):
#     def actual(x):
#         return x ** num
#     return actual



# f = chaicoder(2)
# g = chaicoder(3)

# print(f(3))
# print(g(3))

#oops 
# class Car:
#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand + " !"

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod
#     def general_description():
#         return "Cars are means of transport"
    
#     @property
#     def model(self):
#         return self.__model
    


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type():
#         return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")


# print(my_car.general_description())
# print(my_car.model)


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

# class Battery:
#     def battery_info(self):
#         return "this is battery"

# class Engine:
#     def engine_info(self):
#         return "This is engine"

# class ElectricCarTwo(Battery, Engine, Car):
#     pass

# my_new_tesla = ElectricCarTwo("Tesla", "Model S")
# print(my_new_tesla.engine_info())
# print(my_new_tesla.battery_info())

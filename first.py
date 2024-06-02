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
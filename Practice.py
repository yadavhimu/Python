# x=[0,1,2,3,4,5,6,7,8]
# sliced = x[2:6:2]
# print(sliced)

# x= set()
# s= {4,32,2,2,6}
# s2={3,4,22,1}
# s.remove(2)
# print(s)
# print(4 in s)
# print(s.union(s2))

# x= tuple(i for i in range(100) if i % 5 == 0)
# print(x)

# x= {i for i in range(100) if i % 5 == 0}
# print(x)

# def func(x,y,z=None):
#     print('Run',x,y,z)
#     return x * y,x/y 

# r1,r2= func(5,6,7)
# print(r1,r2)

# def func(x,y):
#     print(x,y)

# pairs = [(1,2),(3,4)]

# for pair in pairs:
#     func(*pair)


# def func(x,y):
#     print(x,y)

# pairs = [(1,2),(3,4)]

# for pair in pairs:
#     func(**{'x':2, 'y':5})

# def func (*args, **kwargs):
#     print(**args)

# func(1,2,3,4,5,one=0,two=1)

# x = [1,2,4,5,3,3,21,2,21,2,313,1,23,142,4]

# mp = map(lambda i: i + 1, x)
# print(list(mp))

# x = [1,2,4,5,3,3,21,2,21,2,313,1,23,142,4]

# mp = map(lambda i: i * 2, x)
# print(list(mp))


# x = [1,2,4,5,3,3,21,2,21,2,313,1,23,142,4]

# mp = filter(lambda i: i % 2 == 0, x)
# print(list(mp))

# name = input("what is your name :")
# Date= input("what is your joining date :")

# print(f"Dear {name}, You are selected {Date}")


# letter = '''Dear <|Name|>,
# You are selected!
# <|Date|>'''

# print(letter.replace("<|Name|>","Himanshu").replace("<|Date|>","30/07/2024"))

# words = {
#     "madad":"help",
#     "kursi":"chair",
#     "billi":"Cat"
# }

# word = input("Enter the word you want meaning of: ")

# print(words[word])

# s = set()
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))

# print(s)


# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') #length of s after these operation
# print(s)
# print(len(s))

# a = int(input("Enter your age: "))
# if(a>=18):
#     print("Yes")

# else:
#     print("not valid")

# a1 = int(input("Enter number 1 : "))
# a2 = int(input("Enter number 2 : "))
# a3 = int(input("Enter number 3 : "))
# a4 = int(input("Enter number 4 : "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Gratest number is a1:", a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Gratest number is a2:", a2)

# elif(a3>a1 and a3>a2 and a3>a4):
#     print("Gratest number is a3:", a3)

# elif(a4>a1 and a4>a2 and a4>a3):
#     print("Gratest number is a4:", a4)

# marks1 = int(input("Enter Marks 1: "))
# marks2 = int(input("Enter Marks 2: "))
# marks3 = int(input("Enter Marks 3: "))

# total_percentage = (100*(marks1 + marks2 + marks3))/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are passed:",total_percentage)

# else:
#     print("You are fail:",total_percentage)


# l = [1, "Hmm", False , "This", "Person", "Rohan", "Shubham"]

# i=0
# while(i<len(l)):
#     print((l[i]))
#     i +=1

# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l :
#     if(name.startswith("H")):
#         print(f"Hello {name}")


# n = int(input("Enter a number:"))
# for i in range(2,n):
#     if(n%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

# n = int(input("Enter the number: "))
# product = 1
# for i in range(1, n+1):
#     product = product * i

# print(f"The factorial of {n} is {product}")

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")

    
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

words = {
    "madad":"help",
    "kursi":"chair",
    "billi":"Cat"
}

word = input("Enter the word you want meaning of: ")

print(words[word])


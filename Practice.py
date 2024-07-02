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

x= {i for i in range(100) if i % 5 == 0}
print(x)

def func(x,y,z=None):
    print('Run',x,y,z)
    return x * y,x/y 

r1,r2= func(5,6,7)
print(r1,r2)
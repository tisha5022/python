# def hello():
#     print("hello")
    
# hello()

# def square(a):
#     print(a*a)
    
# square(11)

# def add(a,b):
#     print(a+b)
    
# add(10,20)

# def add(a,b):
#     return a+b

# k = add(10,20)

# print(k)

# def add(a,b):
#     return a+b
    
# def square(a):
#     return a*a

# k = add(10,20)
# j = square(k)
# print(j)

# def person(id=0,name="tisha",email="abc@gmail.com"):
#     print(id,name,email)
    
# person(10,email="tisha@gmail.com")

# def add(*a):
#     print(a)
    
# add(10,20,30,40,50) 

# def person(**a):
#     print(a)
    
# person(name="devanshi",email="dv@gmail.com")

# a = lambda a,b : a+b
# print(a(10,20))

# b = lambda a : a*a
# print(b(50))


# ===================================== scop ======================================

# a=10

# def test():
#     print("test : ",a)
    
# print(a)
# test()
# print(a)

# a=10

# def test():
#     a=50
#     print("test : ",a)
    
# print(a)
# test()
# print(a)

# a=10

# def test():
#     global a
#     a=50
#     print("test : ",a)
    
# print(a)
# test()
# print(a)


# =========================== recursion ===========================================

# def square(a):
#     print(a*a)
#     a+=1
#     if a<20:
#         square(a)
        
# square(2)    
    
    
# =============================== map =====================================================

l = [10,20,30,40,50,60]  

# def square(a):
#     return a*a  

# s = []
# for i in l:
#     k = square(i)
#     s.append(k)
# print(s)

# def square(a):
#     return a*a

# s = map(square,l)
# print(list(s))

# s = map(lambda a : a*a,l)
# print(list(s))

# =============================== filter ================================================

l = [1,2,3,4,5,6,7,8,9]

# def oddnumber(a):
#     if a%2!=0:
#         return True
#     else:
#         return False
    
# s = []
# for i in l:
#     k = oddnumber(i)
#     if k:
#         s.append(i)
# print(s)    

# s = filter(oddnumber,l)
# print(list(s))

# s = filter(lambda a : a%2==0,l)
# print(list(s))

# ======================= reduce ============================================

from functools import reduce

l = [-1,1,2,3,4,5,6,7,8,9]

# def sum (a,b):
#     if a+b :
#         return a+b
    
# k = reduce(sum,l)
# print(k)

# k = reduce(lambda a,b : a+b,l)
# print(k)

# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
    
# k = reduce(max,l)
# print(k)

# k = reduce(lambda a,b :a if a>b else b,l)
# print(k)

# def min(a,b):
#     if a<b:
#         return a
#     else:
#         return b
    
# k = reduce(min,l)
# print(k)

# k = reduce(lambda a,b :a if a<b else b,l)
# print(k)

# def avg(a,b):
#     print(a,b)
    
# sum = reduce(lambda a,b : a+b ,l)
# avg = sum/len(l)
# print(f"avg : {avg}")


# import math
# l = [1,2,3,4,5,6,7,8,9,25,49]
# def check_p_square(a):
#     if math.sqrt(a).is_integer():
#         return a
    
# k = filter(check_p_square,l)
# print(list(k))

# k = filter(lambda a : math.sqrt(a).is_integer(),l)
# print(list(k))

# =========================================genrater and itrater===============================

# l = [10,20,30,40,50,60]

# def square(a):
#     for i in range(1,a+1):
#         yield i*i
        
# a = iter(square(5))

# print(next(a))

l = ["Tisha","Devanshi","Zeel","dhruvin","sunil"]

k = map(lambda a : "Hello ,"+a ,l)
print(list(k))

        
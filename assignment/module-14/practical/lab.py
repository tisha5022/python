#=============================lab 1===================================================

# Q-1 Write a Python program to create a list with elements of multiple data types (integers, strings, floats,
#     etc.).

# list = [10,20,30,40,50,"Tisha","Sanket","Vansh",3.14,2.14,19.54,1.2,"5j+20","19t+54","20k+21"]

# print(list)

# for i in list:
#     print(i)

# for i in range(len(list)):
#     print(list[i])

# Q-2  Write a Python program to access elements at different index positions.

# name = ["Tisha","Sanket","Vansh","Devanshi","Rinkesh"]

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])
# print(name[-5])
# print(name[2:6])
# print(name[3:])
# print(name[:4])
# print(name[:])
# print(name[:-1])

# ====================Practical Examples==============================================

# Q-1. Write a Python program to create a list of multiple data type elements.

# list1 = ["python","java","c","c++","sql",10,20,30,40,50,3.14,10.20,19.54,10.20,20.30]

# print(list1)

# for i in list1:
#     print(i)

# for i in range(len(list1)):
#     print(list1[i])

# Q-2. Write a Python program to find the length of a list using the len() function. 

# name = ["Tisha","Vansh","Shriya","Nishi","Het"]

# print(len(name))

# ===============================lab 2====================================================

# Q-1 Write a Python program to add elements to a list using insert() and append(). 

# name = ["Tisha","Vansh","Shriya","Nishi","Het"]

# name[1] = "sanket"
# print(name)

# name.insert(1,"Sanket")
# print(name)

# name.append("Kajal")
# print(name)

# Q-2 Write a Python program to remove elements from a list using pop() and remove(). 

# name = ["Tisha","Vansh","Shriya","Nishi","Het"]

# name.pop(3)
# print(name)

# name.pop()
# print(name)

# name.pop(1)
# print(name)

# name.remove("Tisha")
# print(name)

# name.remove("Het")
# print(name)

# =======================Practical Examples=========================================

# Q-3. Write a Python program to update a list using insert() and append(). 

# color = ["Black","White","Yellow","Red","Blue"]

# color[4] = "Brown"
# print(color)

# color.insert(2,"Brown")
# print(color)

# color.append("Green")
# print(color)

# Q- 4 Write a Python program to remove elements from a list using pop() and remove(). 

# color = ["Black","White","Yellow","Red","Blue"]

# color.pop(2)
# print(color)

# color.pop()
# print(color)

# color.pop(0)
# print(color)

# color.remove("White")
# print(color)

# color.remove("Red")
# print(color)

# =======================lab 3====================================================

# Q-1 Write a Python program to iterate over a list using a for loop. 

# name = ["Tisha","Vansh","Shriya","Nishi","Het","Sanket","Kajal"]

# for i in name:
#     print(i)

# Q-2 Write a Python program to sort a list using both sort() and sorted().

# fruit = ["Apples", "Bananas", "Oranges", "Grapes", "Strawberries", "Watermelon"]

# fruit.sort()
# print(fruit)

# fruit.sort(reverse=True)
# print(fruit)

# sorted(fruit)
# print(fruit)


# =======================Practical Examples ========================================

# Q-1 Write a Python program to iterate through a list and print each element.

# Birds=["Peacock","Parrot","Owl","Eagle","Pigeon","Sparrow","Duck","Swan"]

# for Birds in Birds:
#     print(Birds)

#Q-2. Write a Python program to insert elements into an empty list using a for loop and append().

# my_list = []

# n = int(input("How many elements do you want to insert? "))

# for i in range(n):
#     element = input(f"Enter element {i+1}: ")
#     my_list.append(element)


# print("Final list:", my_list)

# ==================================== lab 4 =====================================================

# Q-1 Write a Python program to create a tuple with multiple data types.

# t = (10,20,30,40,50,"Tisha","Vansh","Shriya","Nishi",3.14,19.54,2.50,10.20,"5j+4","10x+20","50y+2")

# print(t)
# print(type(t))

# Q-2 Write a Python program to concatenate two tuples.

# t1 = (10,20,30,40,50,60)
# t2 = (100,3.14,200,10.20,19.54,500)

# t3 = t1 + t2

# print(t3)

# =================================== Practical Examples =====================================

# Q-1. Write a Python program to convert a list into a tuple.

# list=["Python","java","C","C++"] 

# print(type(list))
# t=(tuple(list))
# print(t)
# print(type(t))

# Q-2. Write a Python program to create a tuple with multiple data types. 

# t=(10,20,30,100,"Tisha","Sanket",55.12,11.11,8.00,9.5,"5X","10Y","11Z",True,False,"Red","Black")

# print(t)

# Q-3. Write a Python program to concatenate two tuples into one.

# a=("Red","Black","Yellow")
# b=("Greay","Pink","White")

# c=a+b
# print(c)

# Q-4.Write a Python program to access the value of the first index in a tuple. 


# t1=("Python","Java","C","C++")
# print(t1[0])
# print(t1[1])


#==================================================>Lab-5<=========================================

# Q-1 Write a Python program to access values between index 1 and 5 in a tuple. 

# A=("Computer","Mouse","CPU","Key-Board","Hard-disk","Pen-drive","T.V")
# print(A[1:6])


# Q-2 Write a Python program to access alternate values between index 1 and 5 in a tuple.

# x=(10,20,30,40,50,60,70,80,90)
# print(x[1:6:2])


# ========================================Practical Examples=========================================

# Q-1. Write a Python program to access values between index 1 and 5 in a tuple.

# c=(100,200,300,400,500,600,700,800,900,1000)
# print(c[1:6])


# Q-2. Write a Python program to access the value from the last index in a tuple. 

# A=(10,20,30,40,50,60,70,80,90,100)
# print(A[-1])


#===================================Lab-6=========================================

# Q-1 Write a Python program to create a dictionary with 6 key-value pairs. 

# T={"Name":"Tisha",
#     "email":"tisha@gmail.com",
#     "Phone":"8563239710",
#     "Age":"20",
#     "Subject":"Python",
#     "Duration":"1 Year"
#     }
# print(T)

# Q-2 Write a Python program to access values using dictionary keys. 

# T2={"Name":"Sanket",
#     "email":"sanket@gmail.com",
#     "Phone":"8113239710",
#     "Age":"30",
#     "Subject":"C,C++",
#     "Duration":"3 Month"
#     }
# print(T2["Name"])
# print(T2["email"])
# print(T2["Phone"])
# print(T2["Age"])
# print(T2["Subject"])
# print(T2["Duration"])

# =====================================Practical Examples===============================================

# Q-1. Write a Python program to create a dictionary of 6 key-value pairs. 

# n={"python":"Fees=90000",
# "java":"Fees=85000",
# "C":"Fees=25000",
# "C++":"Fees=30000",
# "Tally Prime":"Fees=5000",
# "CCC":"Fees=4000"}

# print(n)

# Q-2. Write a Python program to access values using keys from a dictionary.

# n={"python":"Fees=90000",
# "java":"Fees=85000",
# "C":"Fees=25000",
# "C++":"Fees=30000",
# "Tally Prime":"Fees=5000",
# "CCC":"Fees=4000"}

# print(n["C"])
# print(n["C++"])
# print(n["CCC"])
# print(n["Tally Prime"])
# print(n["java"])
# print(n["python"])


#=============================================Lab-7================================================

# Q-1 Write a Python program to update a value in a dictionary. 

# a={"Name":"Raj","Email":"Raj@gmail.com","Phone":"1235456987"}
# print(a)
# a.update({"Name":"Tisha","Email":"Tisha@gmail.com","Phobne":"1265497784"})
# print(a)


# Q-2 Write a Python program to merge two lists into one dictionary using a loop. 

# a=["Name","Email","Age"]
# b=["Nishi","Nishii@gmail.com",10]
# c={}

# for i in range(len(a)):
#     c[a[i]]=b
# print(c)

# =======================================Practical Examples=====================================

# Q-1. Write a Python program to update a value at a particular key in a dictionary. 

# a={"Name":"Vansh","Email":"Vansh@gmail.com","Phone":"2345615621"}
# print(a)
# a.update({"Name":"Jenish"})
# print(a)


# Q-2.Write a Python program to separate keys and values from a dictionary using keys() and values() methods.


# a={"Name":"Hardik","Email":"Hardik@gmail.com","Phone":"8866449955","Gradution":"BCA"}
# print(a.keys())
# print(a.values())
# print(a.items())


# Q-3.Write a Python program to convert two lists into one dictionary using a for loop. 

# List1=["A","B","C","D"]
# List2=[100,200,300,400,500]

# result={}
# for i in range(len(List1)):
#     result[List1[i]]=List2[i]
# print(result)


# Q-4. Write a Python program to count how many times each character appears in a string. 

# a="My Name Is Tisha"
# count=0
# for i in a:
#     if str(i).isalpha():
#         count+=1
# print("total character appears in a string : " ,count)

#============================================Lab-8==================================================

# Q-1.Write a Python program to create a function that takes a string as input and prints it.

# def person(Name):
#     print(Name)

# person("MY NAME IS TISHA")    


# Q-2.Write a Python program to create a calculator using functions.

# def add(num1,num2):
#     return num1+num2

# def subtraction(num1,num2):
#     return num1-num2

# def Multipection(num1,num2):
#     return num1*num2

# def divide(num1,num2):
#     return num1/num2

# def Moduls(num1,num2):
#     return num1%num2

# def Exponentiation(num1,num2):
#     return num1**num2

# def Floor_division(num1,num2):
#     return num1//num2

# print("Select Operation:")
# print("1. add")
# print("2. subtraction")
# print("3. Multipection")
# print("4. divide")
# print("5. Moduls")
# print("6. Exponentiation")
# print("7. Floor_division")

# choice=input("Enter Your Choice:")
# num1=float(input("Enetr the value of num1:"))
# num2=float(input("Enetr the value of num2:"))
# if choice=="1":
#     print("Result:",add(num1,num2))
# elif choice=="2":
#     print("Result:",subtraction(num1,num2))
# elif choice=="3":
#     print("Result:",Multipection(num1,num2))
# elif choice=="4":
#     print("Result:",divide(num1,num2))
# elif choice=="5":
#     print("Result:",Moduls(num1,num2))
# elif choice=="6":
#     print("Result:",Exponentiation(num1,num2))
# elif choice=="7":
#     print("Result:",Floor_division(num1,num2))
# else:
#     print("Sorry! Invalid Choice")


# ===================================Practical Examples=============================================

# Q-1.Write a Python program to print a string using a function. 

# def Person_details(Name,Email,Age,Course):
#     print(Name,Email,Age,Course)

# Person_details("Tisha","tisha@gmail.com",20,"Python")


# Q-2. Write a Python program to create a parameterized function that takes two arguments and prints their sum.

# def Addition(Num1,Num2):
#     print(f"Sum Of {Num1} & {Num2} : {Num1+Num2}")

# Addition(100,200)


# Q-3. Write a Python program to create a lambda function with one expression.

# A=lambda a: a*a
# print(A(20))


# Q-4. Write a Python program to create a lambda function with two expressions.

# B=lambda a,b:a**b
# print(B(8,4))

#==========================================Lab-9=============================================


# Q-1. Write a Python program to import the math module and use functions like sqrt(), ceil(), floor(). 

# import math

# print(math.sqrt(121))
# print(math.ceil(15.10))
# print(math.floor(5.5))
# print(math.pow(5,2))
# print(round(10.2))


# Q-2. Write a Python program to generate random numbers using the random module.

# import random
# A=random.randint(10,50)
# print(A)


# ====================================Practical Examples=====================================

# Q-1. Write a Python program to demonstrate the use of functions from the math module.


# import math

# print(math.sqrt(144))
# print(math.ceil(50.69))
# print(math.floor(8.5))
# print(math.pow(10,3))
# print(round(25.69))


# Q-2. Write a Python program to generate random numbers between 1 and 100 using the random module.
 
# import random

# B=random.randint(100,500)
# print(B)
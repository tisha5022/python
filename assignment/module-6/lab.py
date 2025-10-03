# ==================lab Q-1=======================================

# print("Hello, World!")

# print("My name is Tisha.")

# ================lab Q-2==========================================

#Q1.Write a Python program that demonstrates the correct use of indentation, comments, and variables following
# PEP 8 guidelines.


# a=int(input("Enter The Number:-"))
# b=int(input("Enter The Number:-"))
# print(f"a={a}")
# print(f"b={b}")

# a = 20
# b = 30

# Addition=(a+b)
# print(f"Sum of a+b={Addition}")

# Subtraction=(a-b)
# print(f"Subtraction of a-b={Subtraction}")

# Multiplication=(a*b)
# print(f"Multiplication of a*b={Multiplication}")

# Division=(a/b)
# print(f"Division of a/b={Division}")

# Modul=(a%b)
# print(f"Moduls of a%b={Modul}")

# Exponentiation=(a**b)
# print(f"Exponentiation of a**b={Exponentiation}")

# Floor_division=(a//b)
# print(f"floor_division of a//b={Floor_division}")

# ================lab Q-3======================================

#Q1.Write a Python program to demonstrate the creation of variables and different data types.

# a=50 int 
# print(a)

# b= "Tisha" string
# print(b)

# c=3.14 float
# print(c)

# Subject=["Python","c","c++"] list
# print(Subject)

# for i in range(6): range
#     print(b)

#Q2.Practical Example 1: How does the Python code structure work? 

# a = 20
# print(a)

#Q3.Practical Example 2: How to create variables in Python? 

# name = "vansh"
# age = 18
# email = "vansh@gmail.com"

# print(name)
# print(age)
# print(email)

#Q4.Practical Example 3: How to take user input using the input() function.

# name = input("enter the name : ")
# print(name)

#Q5.Practical Example 4: How to check the type of a variable dynamically using type().

# a = 20
# b = 19.54
# Name= "Tisha"
# c=["shriya","vansh","het"]

# print(type(a))
# print(type(b))
# print(type(Name))
# print(type(c))

# ====================lab Q-4===================================================

#Q1.Practical Example 5: Write a Python program to find greater and less than a number using if_else. 

# Number1=int(input("Enter the Number1 "))
# Number2=int(input("Enter the Number2 "))

# if Number1>Number2:
#     print(f"{Number1} is Greater than {Number2}") 
# else:
#     print(f"{Number2} is less than {Number1}") 

#Q2.Practical Example 6: Write a Python program to check if a number is prime using if_else.

# Number=int(input("Enter The Number:"))

# flag=1

# if flag==0:
#         print("number is prime")
# else:
#         print("number is not prime")

#Q3.Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.

# marks = int(input("enter the marks:"))

# if marks>=91 and marks<=100:
#         print("grade A")
# elif marks>=71 and marks<=90:
#         print("grade B")
# elif marks>=51 and marks<=70:
#         print("grade C")
# elif marks>=35 and marks<=50:
#         print("grade D")
# elif marks>=0 and marks<=34:
#         print("grade F")
# else :
#         print("invalid choice")  

#Q4.Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested
#   if. 

# age= int(input("Enter your age : "))

# if age>=18:
#     print("You can go to donate")
#     if age>=18:
#         print("You are eligible to donate blood")
# else:
#     print("You are not eligible to donate blood")

# ===================lab Q-5=====================================================

#Q1.Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. 
#   List1 = ['apple', 'banana', 'mango'].

# List1 = ['apple', 'banana', 'mango']

# for i in range(1):
#     print(List1)

#Q2.Practical Example 2: Write a Python program to find the length of each string in List1.

# List1 = ['apple', 'banana', 'mango']

# print(len(List1))

# for word in List1:
#     print(f"length of {word} is {len(word)}")

#Q3.Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop 
#   and if condition.

# fruit= ['apple', 'banana', 'mango']
# search=input("Enter Your String:")

# for i in fruit:
#     if i==search:
#         print("string in the list")
#         break
#     else:
#         print("string is not in the list")

#Q4.Practical Example 4: Print this pattern using nested for loop: 

# for i in range (5):
#         for j in range(i+1):
#             print("*",end=" ")
#         print()


# for i in range(5):
#     print("* "*(i+1))

# ================lab Q-8=================================================

#Q1.Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement. 
#   List1 = ['apple', 'banana', 'mango'] 

# List1 = ['apple', 'banana', 'mango']

# for i in List1:
#     if i=="banana":
#         continue
#     print(i)

#Q2.Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break 
#   statement.

# List1 = ['apple', 'banana', 'mango']

# for i in List1:
#     if i=="banana":
#         break
#     print(i)

# ====================lab Q-9====================================

#Q1.Write a Python program to demonstrate string slicing. 

# str="Hello Python!"

# print(str[1:])
# print(str[:5])
# print(str[5:9])
# print(str[-5:-2])
# print(str[::-1])
 
#Q2.Write a Python program that manipulates and prints strings using various string methods.

# st= "my name is tisha"
# print(len(st))

# st= "MY NAME IS TISHA"
# print(str.lower(st))

# st= "my name is tisha"
# print(str.upper(st))

# st= "my name is tisha"
# print(str.capitalize(st))

# st= "my name is tisha"
# print(str.title(st))

# st= "  my name is tisha   "
# print(st)
# print(st.strip())

# st= "my name is tisha"
# print(st.replace('i','r',1))

# st= "my name is tisha"
# print(st.find("tisha"))

# st= "my name is tisha"
# print(st.startswith("M"))

# st= "my name is tisha"
# print(st.endswith("a"))

# st= "my name is tisha"
# print(st.split(" ",2))

# print("XYZ".join("abc"))

# print("Tisha".isalpha())

# print("2004".isdigit())

# print("Tisha02".isalnum())

# print("vansh".zfill(50))

# print("vansh".center(50,"*"))     

# ============================== lab 6 ==========================================

# Q-1 Write a generator function that generates the first 10 even numbers. 

# def generate_even_numbers():
#     num = 0
#     count = 0
#     while count < 10:
#         yield num
#         num += 2
#         count += 1

# for even in generate_even_numbers():
#     print(even)
    
# Q-2. Write a Python program that uses a custom iterator to iterate over a list of integers.

# l = [100,200,300,400,500,600,700,800,900,1000]

# k=iter(l)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))

# ============================== lab 7 ==========================================

#Q-1. Practical Example: 1) Write a Python program to print "Hello" using a string. 

# print("Hello")


#Q-2.Practical Example: 2) Write a Python program to allocate a string to a variable and print it

# program="Hello Pyhton!"
# print(program)

#Q-3. Practical Example: 3) Write a Python program to print a string using triple quotes. 

# print(""" My Name is Tisha
#     I am 20 Year Old
#     Currently Learning Python""")

#Q-4.Practical Example: 4) Write a Python program to access the first character of a string using index value.

# st=("Hello World!")
# print(st[0]) 


#Q-5.Practical Example: 5) Write a Python program to access the string from the second position onwards using
# slicing.

# t=("Hello World! Hello Python!") 
# print(t[1:])

#Q-6.Practical Example: 6) Write a Python program to access a string up to the fifth character. 

# T=("Hello World!")
# print(T[:5])


#Q-7.Practical Example: 7) Write a Python program to print the substring between index values 1 and 4.

# T1=("Hello World! Hello Pyhton!")
# print(T1[1:5]) 


#Q-8.Practical Example: 8) Write a Python program to print a string from the last character. 

# A=("Hello World")
# print(A[-1])


#Q-9.Practical Example: 9) Write a Python program to print every alternate character from the string starting from index 1.

# b=("Hello World! Hello Pyhton!") 
# print(b[1::2])

# ======================================= lab 10 ==========================================


#Q-1.Write a Python program to apply the map() function to square a list of numbers. 

# l=[1,2,3,4,5,6,7,8,9]

# s=map(lambda a:a*a,l)
# print(list(s))


#Q-2.Write a Python program that uses reduce() to find the product of a list of numbers.
 
# t=[1,2,3,4,5,6,7,8,9,10]

# from functools import reduce

# product=reduce(lambda a,b: a*b,t)
# print(product)


# Q-3 Write a Python program that filters out even numbers using the filter() function. 

# l = [1,2,3,4,5,6,7,8,9,10]

# s= filter(lambda a : a%2 == 0,l)
# print(list(s))


#==================================================><==================================================
# --------------------------------------------->Assessment:<-------------------------------------------
#==================================================><==================================================

# Create a mini-project where students combine conditional statements, loops, and functions 
# to create a basic Python application, such as a simple calculator or a grade management system.


#---------------> a simple calculator:-

# def add(num1,num2):
#     return num1+num2

# def subtraction(num1,num2):
#     return num1-num2

# def Multipection(num1,num2):
#     return num1*num2

# def divide(num1,num2):
#     return num1/num2

# def Moduls(num1,num2):
#  return num1%num2

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
#  print("Result:",Multipection(num1,num2))
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


#---------------> a grade management system.:-

# choice="y"
# while choice != "n" :
#     marks=int(input("Enter the Marks:"))

#     if marks>=91 and marks<=100:
#         print("your grade is A")
#     elif marks>=71 and marks<=90:
#         print("your grade is B")
#     elif marks>=51 and marks<=70:
#         print("your grade is C")
#     elif marks>=35 and marks<=50:
#         print("your grade is D")
#     else:
#         print("invalid input if out of range(0-100)")

#     choice=input("do you want to continue? yes or no : ")
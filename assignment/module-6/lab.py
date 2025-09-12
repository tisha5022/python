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
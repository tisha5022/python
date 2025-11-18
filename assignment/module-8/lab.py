# ============================== lab 1 ====================================

# Q-1 Write a Python program to print a formatted string using print() and f-string. 

# print("Hello")

# name = "Tisha"
# age = 20
# city = "Surat"

# print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# =========================== Practical Example =====================================

# Q-1 Write a Python program to print “Hello, World!” on the screen. 

# print("Hello, World!")

# ================================ lab 2 ===========================================

# Q-1 Write a Python program to read a name and age from the user and print a formatted output. 

# name = input("Enter your name : ")
# age = input("Enter your age : ")

# print(f"Hello, {name}! you are {age} years old.")

# =============================== Practical Example ========================================

# Q-1  Write a Python program to read a string, an integer, and a float from the keyboard and 
#  display them.

# Student_name = input("Enter the student's name : ")
# Student_age = int(input("Enter the student's age : "))
# Student_GPA = float(input("Enter the student's GPA : "))

# print("=====Student Informations=====")
# print("Name : ",Student_name)
# print("Age  : ",Student_age)
# print("GPA  : ",Student_GPA)

# ============================ lab 3 ================================================

# Q-1 Write a Python program to open a file in write mode, write some text, and then close it.

# file = open("message.txt","w")
# file.write("Welcome to Python programming!")
# file.close()

# ============================= Practical Example ==========================================

# Q-1 Write a Python program to create a file and write a string into it. 

# file = open("myfile.txt", "w")
# file.write("Hello, world! \n")
# file.write("This is a new line. \n")
# file.write("Python is fun! \n")
# file.close()

# ============================== lab 4 ======================================

# Q-1 Write a Python program to read the contents of a file and print them on the console.

# file = open("message.txt", "r")
# print(file.read())
# file.close()

# Q-2 Write a Python program to write multiple strings into a file. 

# with open("Python_lines.txt","w") as file:
#     file.write("Python is easy to learn.\n")
#     file.write("Functions help organize code.\n")
#     file.write("Loops are used for repetition.\n")
#     file.write("Lists can store multiple values.\n")

# ================================= Practical Examples ===================================

# Q-1  Write a Python program to create a file and print the string into the file. 

# file = open("string.txt", "w")
# file.write("Hello, this is a string!")
# file.close()

# Q-2 Write a Python program to read a file and print the data on the console.

# filename = open("string.txt","r")
# data = filename.read()
# print(data)

# Q-3 Write a Python program to check the current position of the file cursor using tell(). 

# with open("string.txt","r")as d:
    
#     data = d.read()
#     print(d.tell())
#     print(data)

# ================================= lab 5 =================================

# Q-1 Write a Python program to handle exceptions in a simple calculator (division by zero,
#  invalid input).

# def simple_calculater():
    
#     print("Simple calculater")
#     print("operations : +,-,*,/")
    
# try:
    
#     num1 = float(input("Enter first number : "))
#     num2 = float(input("enter second number : "))
#     operator = input("Enter operator (+,-,*,/) : ")
    
#     if operator == '+':
#         print("Result : ",num1 + num2)
#     elif operator == '-':
#         print("Result : ",num1 - num2)
#     elif operator == '*':
#         print("Result : ",num1 * num2)
#     elif operator == '/':
#         if num2 == 0:
#             print("cannot divide by zero")
#         else:
#             print("Result : ",num1 / num2)
#     else:
#         print("Invalid operator")
        
# except ValueError:
    
#     print("Please enter valid number.")

# Q-2 Write a Python program to demonstrate handling multiple exceptions.

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a / b)

# except ZeroDivisionError:
#     print("You can't divide by zero!")

# except ValueError:
#     print("Please enter numbers only!")

# except Exception:
#     print("Something went wrong!")

# ====================================== Practical Examples ======================================

# Q-1  Write a Python program to handle exceptions in a calculator. 

# def simple_calculater():
    
#     print("Simple calculater")
#     print("operations : +,-,*,/")
    
# try:
    
#     num1 = float(input("Enter first number : "))
#     num2 = float(input("enter second number : "))
#     operator = input("Enter operator (+,-,*,/) : ")
    
#     if operator == '+':
#         print("Result : ",num1 + num2)
#     elif operator == '-':
#         print("Result : ",num1 - num2)
#     elif operator == '*':
#         print("Result : ",num1 * num2)
#     elif operator == '/':
#         if num2 == 0:
#             print("cannot divide by zero")
#         else:
#             print("Result : ",num1 / num2)
#     else:
#         print("Invalid operator")
        
# except ValueError:
    
#     print("Please enter valid number.")

# Q-2 Write a Python program to handle multiple exceptions (e.g., file not found, division by zero). 

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a / b)

# except ZeroDivisionError:
#     print("You can't divide by zero!")

# except ValueError:
#     print("Please enter numbers only!")

# except Exception:
#     print("Something went wrong!")

# Q-3 Write a Python program to handle file exceptions and use the finally block for closing the file.

# a=""
# try:
#     a=open("message.txt",'r')
#     data = a.read()
#     print(data)
# except Exception as e:
#     print(e)
# finally:
#     if (a is not None):
#         a.close()

# Q-4 Write a Python program to print custom exceptions. 

# class AgeInvalidException(Exception):
#     pass

# def ageCheck(age):
#     if age <18:
#         raise AgeInvalidException("invalid age")
#     else:
#         print("valid age")

# try:
#     ageCheck(18)
# except Exception as e :
#     print(e)

# ====================================== lab 6 =============================================

# Q-1 Write a Python program to create a class and access its properties using an object. 

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p = Person("Tisha", 20)

# print("Name:", p.name)
# print("Age:", p.age)

# ==================================== Practical Examples ======================================

# Q-1 Write a Python program to create a class and access the properties of the class using an object.

# class student:
#     name = "Vansh"
#     age = 18
#     email = "vansh@gmail.com"
    
#     def person(display):
#         print(display.name,display.age,display.email)
        
# s = student()
# s.person()

# Q-2 Write a Python program to demonstrate the use of local and global variables in a class. 

# x = 10

# class demo:
    
#     def show(self):
#         y = 5
#         print("global variable : ",x)
#         print("local variable : ",y)
        
# d=demo()
# d.show()

# ============================== lab 7 ====================================

# Q-1 Write Python programs to demonstrate different types of inheritance (single, multiple, 
# multilevel, etc.). 

#  Single Inheritance
# class Person:
#     def info(self):
#         print("I am a person.")

# class Student(Person): 
#     def study(self):
#         print("I am studying.")
        
# s = Student()
# s.info()
# s.study()

#  Multiple Inheritance
# class Father:
#     def father_info(self):
#         print("Father: Hardworking.")

# class Mother:
#     def mother_info(self):
#         print("Mother: Caring.")

# class Child(Father, Mother):  
#     def child_info(self):
#         print("Child: Learns from parents.")
        
# c = Child()
# c.father_info()
# c.mother_info()
# c.child_info()

#  Multilevel Inheritance
# class Animal:
#     def eat(self):
#         print("Animal eats food.")

# class Mammal(Animal):
#     def walk(self):
#         print("Mammal walks on land.")

# class Dog(Mammal):  
#     def bark(self):
#         print("Dog barks.")
        
# d = Dog()
# d.eat()
# d.walk()
# d.bark()

#  Hierarchical Inheritance
# class Vehicle:
#     def start(self):
#         print("Vehicle starts.")

# class Car(Vehicle):  
#     def drive(self):
#         print("Car drives on road.")

# class Bike(Vehicle):
#     def ride(self):
#         print("Bike rides smoothly.")
        
# c = Car()
# b = Bike()
# c.start()
# c.drive()
# b.start()
# b.ride()

#  Hybrid Inheritance
# class Employee:
#     def work(self):
#         print("Employee works.")

# class TeamLead(Employee):
#     def lead(self):
#         print("TeamLead manages team work.")

# class Developer(Employee):
#     def code(self):
#         print("Developer writes code.")

# class Manager(TeamLead, Developer):  # Hybrid Inheritance
#     def manage(self):
#         print("Manager oversees everything.")
        
# m = Manager()
# m.work()
# m.lead()
# m.code()
# m.manage()

# ================================== Practical Examples ==============================================

# Q-1  Write a Python program to show single inheritance.

# class fruit:
#     def color(self):
#         print("fruits have different colors.")
        
# class apple(fruit):
#     def teste(self):
#         print("apples teste sweet!")
        
# a = apple()
# a.color()
# a.teste()

# Q-2  Write a Python program to show multilevel inheritance.

# class company:
#     def company_name(self):
#         print("company : Tech Solutions Inc.")
        
# class department(company):
#     def department_name(self):
#         print("department : Software Development")
        
# class employee(department):
#     def employee_name(self):
#         print("employee : Devanshi")
        
# e = employee()

# e.company_name()
# e.department_name()
# e.employee_name()

# Q-3 Write a Python program to show multiple inheritance.

# class writer:
#     def write(self):
#         print("i can write stories.")
        
# class singer:
#     def sing(self):
#         print("i can sing songs.")
        
# class artist(writer,singer):
#     def show_telents(self):
#         print("I am an artist with multiple telents!")
        
# a = artist()

# a.write()
# a.sing()
# a.show_telents()

# Q-4 Write a Python program to show hierarchical inheritance.

# class Sport:
#     def start(self):
#         print("Starting the sport")

# class Football(Sport):
#     def play(self):
#         print("Playing football with a team")

# class Tennis(Sport):
#     def play(self):
#         print("Playing tennis singles or doubles")

# f = Football()
# t = Tennis()

# f.start()   
# f.play()   

# t.start()     
# t.play()      

# Q-5  Write a Python program to show hybrid inheritance. 

# class Vehicle:
#     def vehicle_info(self):
#         print("This is a vehicle.")

# class Car(Vehicle):
#     def car_info(self):
#         print("This is a car.")

# class Bike(Vehicle):
#     def bike_info(self):
#         print("This is a bike.")

# class ElectricCar(Car, Bike):
#     def electric_info(self):
#         print("This is an electric car.")

# e = ElectricCar()

# e.vehicle_info()
# e.car_info()
# e.bike_info()
# e.electric_info()

# Q-6  Write a Python program to demonstrate the use of super() in inheritance. 

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello, my name is", self.name)

# class Student(Person):
#     def __init__(self, name, school):
#         super().__init__(name)  
#         self.school = school

#     def greet(self):
#         super().greet() 
#         print("I study at", self.school)

# s = Student("Nishi", "Bhulka Bhavan")
# s.greet()

# ===================================== lab 8 =================================================

# Q-1 Write Python programs to demonstrate method overloading and method overriding.

# class calc:
#     def add(self,a=0,b=0,c=0):
#         print("sum : " ,a+b+c)
        
# c = calc()

# c.add(5,10)
# c.add(2,3,4)
# c.add(1)

# class Parent:
#     def show(self):
#         print("This is the parent class")

# class Child(Parent):
#     def show(self):
#         print("This is the child class")

# p = Parent()
# c = Child()

# p.show()  
# c.show()   

# ================================ Practical Examples ========================================

# Q-1 Write a Python program to show method overloading.

# class Example:
#     def show(self, a=None, b=None):
#         if a is not None and b is not None:
#             print("Two arguments:", a, b)
#         elif a is not None:
#             print("One argument:", a)
#         else:
#             print("No arguments")

# e = Example()

# e.show()
# e.show(10)
# e.show(10, 20)

# Q-2  Write a Python program to show method overriding. 

# class A:
#     def disp(self):
#         print("A disp calling")

# class B(A):
#     def disp(self):
#         print("B disp calling")


# b =B()
# b.disp()

# ================================ lab 9 ========================================

# Q-1 Write a Python program to connect to an SQLite3 database, create a table, insert data, 
# and fetch data. 

# import mysql.connector as sql

# con = sql.connect(
#     host='127.0.0.1',
#     user='root',
#     password='root',
#     port='3306',
#     database='pythonsql'
# )

# cursour = con.cursor()

# cursour.execute("create database pythonsql")

# cursour.execute("create table emp(id int primary key,name varchar(50),email varchar(100))")

# cursour.execute("insert into emp values(1,'Tisha','tisha@gmail.com')")
# con.commit()

# cursour.execute("update emp set email='abc@gmail.com' where id = 3")
# con.commit()

# cursour.execute("delete from emp where id=3")
# con.commit()

# cursour.execute("select * from emp")

# data = cursour.fetchall()  

# print(data)

# ================================== Practical Examples =======================================

# Q-1  Write a Python program to create a database and a table using SQLite3.

# import sqlite3

# db = sqlite3.connect("data.db")

# db.execute("create table emp(id int primary key , name varchar(50),email varchar(50))")
# db.commit()


# Q-2 Write a Python program to insert data into an SQLite3 database and fetch it. 

# import sqlite3

# db = sqlite3.connect("data.db")

# db.execute("create table emp(id int primary key , name varchar(50),email varchar(50))")
# db.execute("insert into emp values(3,'devansi','d@gmail.com')")
# db.commit()

# data = db.execute("select * from emp").fetchall()
# for dt in data:
#     print(dt)

# =================================== lab 10 ========================================

# Q-1 Write a Python program to search for a word in a string using re.search(). 

# import re

# text = "Python is fun"
# word = "Python in"

# match = re.search(word, text)

# if match:
#     print("Word found")
# else:
#     print("Word not found")

# Q-2 Write a Python program to match a word in a string using re.match(). 

# import re

# num = input("Enter your number : ")
# k = re.match('[0-9]{5}$',num)
# if k:
#     print("valid number")
# else:
#     print("invalid number")

# ============================ Practical Examples ==================================

# Q-1 Write a Python program to search for a word in a string using re.search().

# k = re.search('H.l',"Hello python")
# print(k)

# Q-2 Write a Python program to match a word in a string using re.match(). 

# import re

# email = input("Enter your email : ")
# k = re.match('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email)
# if k:
#     print("valid number")
# else:
#     print("invalid number")
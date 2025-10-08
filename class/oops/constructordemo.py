# class student:
    
#     def __init__(self,id,name,email):
#         self.name = name
#         self.email = email
#         self.id = id
        
#     def display(self):
#         print("Runing display.....")
#         print(self.name,self.email,self.id)
            
# s = student(1,"Tisha","tisha@gmail.com")
# s.display()

# class Student:

#     clg = 'DRSTC'
#     def _init_(self,id,name,email):
#         self.name  = name
#         self.email = email
#         self.id = id

#     def display(self):
#         print("Runing display...")
#         print(self.id,self.name,self.email,self.clg)

#     @classmethod
#     def sample(self):
#         print(self.clg)
#         print("Sample calling")

#     @staticmethod
#     def run():
#         print("Run calling")

# Student.clg='ABC'
# Student.sample()

# Student.run("abc")

# s  = Student(10,"sunil",'sunil@gmail.com')
# s.display()

# s1 = Student(11,"Jenil","jenil@gmail.com")
# s1.display()

# def only_number(func):
#     def wrapper(*a):
#         if not str(a[0]).isdigit():
#             print("Only numbers allowed")
#         else:
#          func(*a)
#     return wrapper
    
# @only_number
# def myfunc(a):
#     print(a)
       
# myfunc(10)


# def only_alpha(func):
#     def wrapper(*a):
#         if not str(a[0]).isalpha():
#             print("Only alpha allowed")
#         else:
#          func(*a)
#     return wrapper
    
# @only_alpha
# def myfunc(a):
#     print(a)
       
# myfunc("r")

# def only_numberandalpha(func):
#     def wrapper(*a):
#         if not str(a[0]).isalnum():
#             print("Only number and alpha allowed")
#         else:
#          func(*a)
#     return wrapper
    
# @only_numberandalpha
# def myfunc(a):
#     print(a)
       
# myfunc("r123")

# class demo:
#     id =10
#     def disp(self):
#         print("display calling")
        
#     @classmethod
    # def sample(self):
#         print("sample calling....",self.id)
        
#     @staticmethod
#     def util(self):
#         print("static calling")
        
# # d = demo()
# # d.disp
# # d.sample           

# demo.disp()
# demo.sample()
# demo.util()

class product:
    def __init__(self,pid,pname,price):
        self.pid  = pid
        self.pname = pname
        self.price = price
        
    def display(self):
        print(self.pid,self.pname,self.price)
        
p = product(1,'book',1000)
p.display()

p1 = product(2,'notebook',600)
p1.display()

p2 = product(3,'pen',100)
p2.display()
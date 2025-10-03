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

class Student:

    clg = 'DRSTC'
    def _init_(self,id,name,email):
        self.name  = name
        self.email = email
        self.id = id

    def display(self):
        print("Runing display...")
        print(self.id,self.name,self.email,self.clg)

    @classmethod
    def sample(self):
        print(self.clg)
        print("Sample calling")

    @staticmethod
    def run():
        print("Run calling")

Student.clg='ABC'
Student.sample()

Student.run("abc")

# s  = Student(10,"sunil",'sunil@gmail.com')
# s.display()

# s1 = Student(11,"Jenil","jenil@gmail.com")
# s1.display()
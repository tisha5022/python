# class Demo:
    
#     id = 10
#     name = "abc"
    
#     def __str__(self):
#         return f"my name is {self.name} and id is {self.id}"
    
    
# d = Demo()
# print(d)


# class calc:
    
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
        
#     def __add__(self,obj):
#         return self.a+obj.a,self.b+obj.b
    
# c = calc(10,20)
# c1 = calc(30,40)

# k = c+c1
# print(k)

# class calc:
    
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
        
#     def __mul__(self,obj):
#         return self.a*obj.a,self.b*obj.b
    
# c = calc(10,20)
# c1 = calc(30,40)

# k = c*c1
# print(k)

class demo:
    
    def __init__(self,item):
        self.item = item
        
    def __setitem__(self,index,value):
        self.item[index] = value
        
    def __getitem__(self,index):
        return self.item[index]
    
d = demo([10,20,30,40])
d[2]=100
print(d.item)
print(d[1])
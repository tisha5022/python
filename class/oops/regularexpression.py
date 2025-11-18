import re

# k = re.match('H.l',"Hello python")
# print(k)

# k = re.match('H.l',"aHello pytholn")
# print(k)

# k = re.search('H.l',"Hello python")
# print(k)

# k = re.findall('H.l',"Hello pytHoln")
# print(k)

# k = re.search('H.l',"Hello python")
# print(k)



# num = input("Enter your number : ")
# k = re.match('[0-9]{10}$',num)
# if k:
#     print("valid number")
# else:
#     print("invalid number")

# email = input("Enter your email : ")
# k = re.match('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email)
# if k:
#     print("valid number")
# else:
#     print("invalid number")

password = input("Enter your password : ")
k = re.search('[a-zA-Z0-9]+@[0-9A-za-z]+$',password)
if 5 < len (password) <= 16:
    print("valid password")
else:
    print("invalid password")
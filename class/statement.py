# conditional
#if-else

#looping
#for, while

#control
#break ,continue, pass

# age = 15
# if age >= 18 :
#     print("elegeble for voting")
# else:
#     print("not elegeble...")    

a = 1000000
b = 20000
c = 520

# if a>b:
#     print("A is greater")
# else:
#     print("B is greater")

# if a>b:
#     if a>c:
#         print("A is greater")
#     else:
#         print("C is greater")
# else:
#     if b>c:
#         print("B is greater")
#     else:
#         print("C is greater")

# if a>b and a>c:
#     print("A is greater")
# elif b>a and b>c:
#     print("b is greater")
# elif c>a and c>b:
#     print("C is greater")

marks = input("enter the marks:")
print(marks)

if marks>91 and marks<100:
    print("grade A")
elif marks>71 and marks<90:
    print("grade B")
elif marks>51 and marks<70:
    print("grade C")
elif marks>35 and marks<50:
    print("grade D")
elif marks>0 and marks<35:
    print("grade F")
else:
    print("invalid input if out of range(0-100)")
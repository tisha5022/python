# print("program started")

# try:
#     a=10
#     b=a/0
#     print(b)
    
# except Exception as e:
#     print(e)
    
# else:
#     print("everything is ok")
    
# print("program ended")

# print("program started")

# try:
#     a=10
#     b=a/2
#     print(b)
    
# except Exception as e:
#     print(e)
    
# else:
#     print("everything is ok")
    
# print("program ended")

# print("program started")

# try:
#     a=10
#     b=a/2
#     print(b)
    
# except Exception as e:
#     print(e)
    
# else:
#     print("everything is ok")

# finally:
#     print("always executable")
    
# print("program ended")

# print("program started")

# try:
#     a=10
#     b=a/0
#     print(b)
    
# except Exception as e:
#     print(e)
    
# else:
#     print("everything is ok")

# finally:
#     print("always executable")
    
# print("program ended")

# f = ""

# try:
#     f = open("class.txt",'r')
#     data = f.read()
#     print(data)
    
# except Exception as e:
#     print(e)
    
# finally:
#     if(f is not None):
#         f.close()

def test():
    try:
        a=int(input("enter number : "))
        return 1 
    except Exception as e:
        return 0
    finally:
        print("program exected....")
        
a= test()
print(a)
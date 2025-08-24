# *****
# *****
# *****
# *****
# *****

# for j in range(5):
#     for i in range(5):
#         print("*",end="")
#     print()
    
# for i in range(5):
#     print("*"*5)


# *
# **
# ***
# ****
# *****

# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range(5):
#     print("*"*(i+1))


# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):
#     print("*"*i)

# *****    
#  ****
#   ***
#    **
#     *

# for i in range(5,0,-1):
#     print(' '*(5-i)+"*"*i)


#     *
#    **
#   ***
#  ****
# *****

# for i in range(1,6):
#     print(' '*(5-i)+"*"*i)

#    *
#   * *
#  * * *
# * * * *
#* * * * * 

# for i in range(5):
#     print(' '*(5-i)+"* "*(i+1))

# * * * * * 
#  * * * *
#   * * * 
#    * *
#     *

# for i in range(5,0,-1):
#     print(" "*(5-i)+"* "*(i))
    
#    *
#   *  * 
#  *    *
#   *  *
#     *

# for i in range(5):
#     print(" ")

# 1
# 12
# 123
# 1234
# 12345

for i in range(0,5):
    for j in range(i+1):
        print((j+1) ,end=" ")
    print()
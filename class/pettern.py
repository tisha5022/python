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

#     *
#    ***
#   *****
#  *******
# *********

# 0 1  1
# 2 1  3
# 4 1  5
# 6 1  7
# 4 5  9

# for i in range(5):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range((i*2)+1):
#         print("*",end="")
#     print()    
    
#     *
#    * * 
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# lines = 5
# for i in range(lines):
#     print(" "*(lines-i),"* "*(i+1),end="")
#     print()
# for i in range(lines-1,0,-1):
#     print(" "*((lines-1)-i+2),"* "*(i),end="")
#     print()

#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

# lines = 5
# for i in range(lines):
#     for k in range(lines-i):
#         print(" ",end="")
#     for j in range(i+1):
#         if j==0 or j==(i):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# for i in range(lines-1,0,-1):
#     for k in range((lines-1)-i+2):
#         print(" ",end="")
#     for j in range(i):
#         if j==0 or j==(i-1):
#             print("* ",end="")
#         else:  
#             print("  ",end="")
#     print()

# 1
# 12
# 123
# 1234
# 12345

# for i in range(0,5):
#     for j in range(i+1):
#         print((j+1) ,end=" ")
#     print()

# 1
# 23
# 456
# 78910
# 1112131415

# a=1
# for i in range(1,5):
#     for j in range(i+1):
#         print(a,end="")
#         a+=1
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print((i*(i-1))//2+1+j,end="")
#     print()

# 5
# 45
# 345
# 2345
# 12345

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j,end="")
#     print()

# 0
# 10
# 010
# 1010
# 01010

# for i in range(1,6):
#     for j in range(1,i+1):
#         print((j+i)%2,end="")
#     print()
    
# 1
# 01
# 101
# 0101
# 10101

# for i in range(1,6):
#     for j in range(0,i):
#         print((j-i)%2,end="")
#     print()

# *****
#   *
#   *
#   *
#   *

# print("* "*5)
# for i in range(1,5):
#         print ('  '*(5//2)+'*')

# for i in range(5):
#         for j in range(5):
#                 if i==0 or j==5//2:
#                         print ("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

# *   *
# *   *
# *****
# *   *
# *   *

# for i in range(5):
#         for j in range(5):
#                 if j==0 or j==4 or i==2:
#                       print("*",end="")
#                 else:
#                         print(" ",end="")
#         print()

# A
# BC
# DEF
# GHIJ
# KLMNO

# a='A'
# for i in range(5):
#         for j in range(i+1):
#                 print(a,end="")
#                 a = a + 1
#         print()
        
# *     *
# * * * *
# *  *  *
# * * * *
# *     *

for i in range(1,5+1):
        for j in range(1,i+1):
                if i==j or i+j == 5+1:
                        print("*",end=" ")
                else:
                        print(" ",end="")
        print()

#     *
# * * * *
#        *
# * * * *
#     *

#    *
#   * *
#  *   *
#  *****
#  *****
#  *****

# for i in range(4):
#         for k in range(4-i):
#              print(" ",end="")
#         for j in range(i+1):
#                 if j==0 or j==i:
#                         print("* ",end="")
#                 else:
#                         print("  ",end="")
#         print()
# for i in range(3):
#         print(" *"*4)
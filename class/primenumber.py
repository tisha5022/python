# number = 9
# flag=0

# for i in range(2,number):
#     if number%2 == 0:
#         flag=1
#         break

# if flag==0:
#         print("number is prime")
# else:
#         print("number is not prime")
        
for j in range(3,100):    
    number=j
    flag=0

    for i in range(2,number):
        if number%i==0:
            flag=1
            break
        
    if flag==0:
        print(f"{number} : prime")
    else:
        #print(f"{number} : not prime")
        pass
    
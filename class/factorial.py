number = 10
temp = number
fact = 1

# for i in range(number,0,-1):
#     fact = fact * i
#     print(f"factorial of {num} is {fact} ")

while number != 0:
    fact = fact * number
    number -= 1
    print(f"factorial of {temp} is {fact} ")    
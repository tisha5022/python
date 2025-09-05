#0 1 1 2 3 5 8 13


a = 0
b = 1

print(a,b,end=" ")

for i in range(10):
    c = a + b
    a = b
    b = c
    
    print(c,end=" ")
# def beforetest(test):
#     def wrapper():
#         print("call before test")
#         test()
#     return wrapper

# @beforetest
# def test():
#     print("test calling...")
    

# @beforetest
# def demo():
#     print("demo calling...")
    
# test()
# demo()



def add(calc):
    def wrapper(*a):
        print(a[0]+a[1])
        calc(*a)
    return wrapper


def mul(calc):
    def wrapper(*a):
        print(a[0]*a[1])
        calc(*a)
    return wrapper

@add
@mul
def calc(a,b):
    print("calc operation.....")
    
calc(10,20)
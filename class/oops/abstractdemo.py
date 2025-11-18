# from abc import ABC,abstractmethod


# class Demo(ABC):

#     @abstractmethod
#     def test(self):
#         pass

# class DemoImp(Demo):

#     def test(self):
#         print("test calling...")
   

# # d  =Demo()
# # d.test()

# d = DemoImp()
# d.test()

from abc import ABC,abstractmethod

class Account(ABC):

    balance=0
    @abstractmethod
    def deposite(self,amt):
        pass

    @abstractmethod
    def withdrow(self,amt):
        pass

    def getBalance(self):
        print("Current balaance is : ",self.balance)

class Saving(Account):

    def deposite(self, amt):
        self.balance+=amt

    def withdrow(self, amt):
        if amt>self.balance:
            print("Insufficeinet amount")
        else:
            self.balance-=amt

class Loan(Account):
    def deposite(self, amt):
        self.balance-=amt
    
    def withdrow(self, amt):
        self.balance+=amt


s = Saving()
s.getBalance()
s.deposite(5000)
s.deposite(3000)
s.getBalance()
s.withdrow(5000)
s.getBalance()

print("*")
l = Loan()
l.getBalance()
l.withdrow(500000)
l.getBalance()
l.deposite(200000)
l.getBalance()
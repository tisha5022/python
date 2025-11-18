class InsufficentAmountException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Bank:

    balance=0

    def check_blance(self):
        print("Current balance is :",self.balance)

    def deposite(self,amt):
        self.balance+=amt

    def withdrow(self,amt):
        if amt > self.balance:
            raise InsufficentAmountException(f"you need more {amt-self.balance} in yuor accorunt to withdrow")
        else:
            self.balance-=amt


b  = Bank()
b.check_blance()
b.deposite(5000)
b.deposite(2000)
b.check_blance()
try :
    b.withdrow(20000)
except Exception as e:
    print(e)
b.check_blance()
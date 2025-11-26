import sample

def test(self):
    print("test calling")
    
sample.A.show=test
obj = sample.A()
obj.show()
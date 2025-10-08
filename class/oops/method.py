class Demo:
    id = 10
    def disp(self):
        print("display calling")

    @classmethod
    def sample(self):
        print("Sample calling...",self.id)
    
    @staticmethod
    def util(self):
        print("static calling")

d  = Demo()
# d.disp()
d.sample()

# Demo.disp()
Demo.sample()
Demo.util(10)
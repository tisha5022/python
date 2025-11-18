class sample:
    
    id = 10
    name ="abc"
    
    def display(self):
        return f"my name is {self.name} and id is {self.id}"
    
class demo:
        s = sample()
        
        def show(self):
            return "sho calling"
        
d = demo()
d.s.display()
print(d.s.display())
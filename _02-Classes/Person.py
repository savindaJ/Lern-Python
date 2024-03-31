class Persion:
    x = 5
    pass # pass is a placeholder for future code

p1 = Persion()
p1.name = "John"
print(p1.name) # John
p2 = Persion()
print(p1.x) # 5
print(p2)


class Dog:
    name: str # property
    age: int # property
    color: str  # property
    scretch: bool # property
    
    def bark(self): # definitly wrote one parameter
        print("Bark!")
    
    def walk(self):
        print("Walking")
        
dog= Dog() # always pass dog instance to the class
dog.name = "Rex"
dog.age = 3
dog.color = "Brown"
dog.scretch = False
dog.bark() # Bark!
dog.walk() # Walking

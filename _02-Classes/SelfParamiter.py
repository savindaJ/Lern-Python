class Dog:
    name: str
    age: int 
    color: str  
    scretch: bool 
    
    def __init__(self): # constructor
        pass
    
    def __init__(self,name='',age=0,color='',scretch=False): # constructor
        self.name = name
        self.age = age
        self.color = color
        self.scretch = scretch
        
    def printInfo(self):
        print(f"Name: {self.name}, Age: {self.age}, Color: {self.color}, Scretch: {self.scretch}")
    
    def setName(self, name): # setter
        self.name = name

    def setAge(self, age):
        self.age = age
        
    def setColor(self, color):
        self.color = color
        
    def setScretch(self, scretch):
        self.scretch = scretch
        
    def getName(self): # getter
        return self.name
    
    def getAge(self):
        return self.age
    
    def getColor(self):
        return self.color
    
    def getScretch(self):
        return self.scretch
    
    def bark(self):
        print("Bark!")
    
    def walk(self):
        print("Walking")
        
        
                
dog = Dog()
dog.setName("Rex")
dog.setAge(3)
dog.setColor("Brown")
dog.setScretch(False)

print(dog.getName()) # Rex
print(dog.getAge()) # 3
print(dog.getColor()) # Brown
print(dog.getScretch()) # False

dog2 = Dog("Rex", 3, "Brown", False)
dog2.printInfo() # Name: Rex, Age: 3, Color: Brown, Scretch: False
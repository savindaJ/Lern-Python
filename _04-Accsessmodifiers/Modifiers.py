

# encapsulation , data hiding , access modifiers

class Person:
    def __init__(self, name):
        self.name = name # public attribute
        self.__age = 22 # private attribute , double underscore
        self._address = "Colombo" # protected attribute , single underscore
        
    def setAge(self, age):
        self.__age = age
        
    def getAge(self):
        return self.__age

    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")
        
savinda = Person("Savinda")
savinda.display()
savinda.__age = 22 # creating new attribute , bad practice
print(savinda.name)
savinda.setAge(30)
print(savinda.getAge())
print(savinda.__age) # 22


class Clild(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")
        
sukumala = Clild("Sukumala", 25)
# print(sukumala.__age) # cannot access private attribute
print(sukumala.getAge())
print(sukumala._address) # protected attribute , can access from child class


'''
    __name__ : private attribute
    _name : protected attribute
    name : public attribute
    
'''
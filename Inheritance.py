import datetime


class superClass():
    def __init__(self):
        self.value="SUPER CLASS"
    def display(self):
        print(self.value)


class inheritedClass(superClass): #single inheritance
    def __init__(self,Name):
        self.value=Name
    def __add__(self, other):
        return inheritedClass(self.value + other)
    def __str__(self):
        return "In Side Inherited Class: " + self.value
    def mul(self,n):
        self.value *= n
class anotherClass():
    def timeStamp(self):
        return datetime.date(self)

class anotherInheritedClass(superClass, anotherClass): #multiple inheritance
    def display(self):
       print(self.timeStamp())

def Trial():
    ic=inheritedClass(" Oreilly ")
    book = ic + "Python"
    ic.display() # superClass.display()
    print(ic) # inheritedClass.__str__()
    book.display() # superClass.display()+ "Python"
    ic.mul(3) # inheritedClass.mul()
    print(ic)
    ac= anotherInheritedClass()
    ac.display()
Trial()

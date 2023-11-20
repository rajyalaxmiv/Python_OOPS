class ClassA:
    def __init__(self, value=40):
        print(value)
    def Method1(self):
        print("Method 1")
    def Method2(self):
        print("Method 2")


x = ClassA()
x.Method1()
x.Method2()

a = ClassA(20)
a.Method1()
a.Method2()

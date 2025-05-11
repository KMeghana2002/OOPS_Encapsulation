class sample():
    def __init__(self):
        self.a=200
        self._b=100
        self.__c=10
    def m1(self):
        print(self.a)
        print(self._b)
        print(self.__c)
obj=sample()
obj.m1()
print(obj.a)
print(obj._b)
print(obj.__c)#error beacuse we cannot acces outside the class

#protected acces specifier
class sample():
    def __init__(self):
        self.a=200
        self._b=100
    def m1(self):
        print(self._b)
obj=sample()
obj.m1()
print(obj._b)
print(obj.a)

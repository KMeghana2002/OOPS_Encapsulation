class sample():
    def __init__(self):
        self.a=100
        self._b=200
        self.__c=300
    def getter(self):
        return self.__c
    def setter(self):
        self.__c=420
obj=sample()
print(obj.getter())
obj.setter()
print(obj.getter())

               

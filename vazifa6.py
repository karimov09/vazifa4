class Cat:
    def __init__(self, age):
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        raise AttributeError()
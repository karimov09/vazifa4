class Home:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def __setattr__(self, key, value):
        if key == 'address':
            self.__dict__[key] = value.upper()  
        else:
            self.__dict__[key] = value
    
    def __getattr__(self, item):
        if item == 'name':
            return self.name
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")
    
    def __getattribute__(self, item):
        return super().__getattribute__(item)

home = Home("My Home", "123 Main Street")
print(home.name)  
print(home.address)  
print(home.nonexistent_attr)  
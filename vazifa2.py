class Phone:
    def __init__(self, model, price, color):
        self._model = model  
        self.__price = price  
        self.color = color  
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, new_model):
        self._model = new_model
    
    @model.deleter
    def model(self):
        del self._model
from abc import ABC, abstractmethod

class Tv(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
class SmartTv(Tv):
    def turn_on(self):
        print("telvizor  yoqildi on")
    def turn_off(self):
        print("telvizor  ochdi off.")
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def move():
        pass
class car(vehicle): 
    def move():
        print("it is move")
obj=car
obj.move()        
    
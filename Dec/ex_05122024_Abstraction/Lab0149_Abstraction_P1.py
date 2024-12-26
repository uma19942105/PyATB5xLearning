#abstraction
#wHide  the details and show what is required
#car -with  key__ private ,tyres->public
#car->multiple -Engine, gear box
#car-> driver ->Engine, gearbox?
#from abc import abstractmethod


#from abc import ABC,abstract method

class Animal(ABC):

    def __int__(self,name):
        self.name=name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("bark bark.....")


obj_dog=Dog("Shera")
obj_dog.make_sound()
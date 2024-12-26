from abc import abstractmethod


class GearBox(ABC):

    @abstractmethod

    def set_gear(self):
        pass

class Engine():
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

 class Car(Engine):

     def drive(self):
         self.start()

car_obj=Car()
car_obj.drive()




    #class Car(Engine):
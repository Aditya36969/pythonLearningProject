#abstract class

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        return "bark"
class cat(Animal):
    def sound(self):
        return "Mew mew"

rancho=dog("rancho")
print(rancho.sound())

c =cat("CAT")
print(c.sound())


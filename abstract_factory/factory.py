from abc import ABC, abstractmethod

class ContinentFactory(ABC):
    @abstractmethod
    def CreateHerbivore(self):pass

    @abstractmethod
    def CreateCarnivore(self):pass

class AfricaFactory(ContinentFactory):
    def CreateCarnivore(self):
        return Lion()

    def CreateHerbivore(self):
        return Wildebeest() 

class AmericaFactory(ContinentFactory):
    def CreateCarnivore(self):
        return Wolf()

    def CreateHerbivore(self):
        return Bison()


class Herbivore(ABC):
    pass


class Carnivore(ABC):

    @abstractmethod
    def eat(self,h : Herbivore):pass
   

class Wildebeest(Herbivore):
    pass


class Lion(Carnivore):
    def eat(self,h: Herbivore):
        print(f"lion eat {h.__class__}")


class Bison(Herbivore):
    pass

class Wolf(Carnivore):
    def eat(self,h: Herbivore):
        print(f"wolf eat {h.__class__}")


#client
class AnimalWorld:
    herbivor = None
    carnivor = None

    def __init__(self , factory:ContinentFactory) -> None:
        self.carnivor = factory.CreateCarnivore()
        self.herbivor = factory.CreateHerbivore()


    def food_time(self):
        self.carnivor.eat(self.herbivor)


#for african animals
africa = AfricaFactory()
animal_world = AnimalWorld(africa)
animal_world.food_time()


#for american animals
america = AmericaFactory()
animal_world = AnimalWorld(america)
animal_world.food_time()
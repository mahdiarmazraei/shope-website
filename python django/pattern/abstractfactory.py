class Dog:

    def speak(self):
        return "woof"
    def __str__(self):
        return "Dog"
    

class DogFactory:

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"
    

class PetStore:

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory


    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()




        print("our pet is {}".format(pet))
        print("our pet says hello by {}".format(pet.speak()))
        print("its food is {}".format(pet_food))

factory = DogFactory()


shop = PetStore(factory)

shop.show_pet()
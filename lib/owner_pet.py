
PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
class Pet:
    pass
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None):
        pass
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self,pet_type):
        if(pet_type in PET_TYPES ):
            self._pet_type = pet_type
        else:
            raise Exception("pet must be ")




class Owner:
    pass
    all = []
    def __init__(self,name):
        pass
        self.name = name
        Owner.all.append(self)

    def pets(self):
        pass
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        pass
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise TypeError("pet must be an instance of pet class")
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
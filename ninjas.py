import pets as Pet

class Ninja:

    def __init__(self, first_name, last_name, Pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.Pet = Pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self, minutes):
        print(self.first_name, 'has walked', self.Pet.name+'!')
        self.Pet.play(minutes)
        return self
    
    def feed(self, times):
        print(self.first_name, 'has fed', self.Pet.name+'!')
        self.Pet.eat(times)
        return self

    def bathe(self):
        print(self.first_name, 'has bathed', self.Pet.name+'!')
        self.Pet.noise()



Haseo = Ninja('Haseo', 'PKK', Pet.Atoli, 'cookie', 'Fancy Kibble')
Artina = Ninja('Artina', 'Avarice', Pet.Bongo, 'hornworm', 'mealworm')

Haseo.walk(10).feed(2).bathe()
Artina.walk(8).feed(1).bathe()



class Pet:


    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound
        self.max_health = 100

    def sleep(self, hours):
        if hours == 1:
            print(self.name,"is sleeping for", hours, 'hour!')
        else:
            print(self.name, "is sleeping for", hours, 'hours!')
        self.energy += 25 * hours
        print(self.name+"'s energy is now at", self.energy,"units!")
        return self



    def eat(self, meals):
        if meals == 1:
            print(self.name, 'has eaten', meals, 'meal today!')
        else:
            print(self.name, 'has eaten', meals, 'meals today!')
        self.health += 10 * meals
        self.energy += 5 * meals
        if self.health > 100:
            self.health = self.max_health
        print(self.name,'now has', self.health, 'health and', self.energy, 'energy!')
        return self

    def play(self, minutes):
        if minutes == 1:
            print(self.name, 'has played for', minutes, 'minute!')
        else:
            print(self.name, 'has played for', minutes, 'minutes!')
        self.health += 5 * minutes
        if self.health > 100:
            self.health = self.max_health
        print(self.name+"'s health is now at", self.health, "units!")
        return self
    def noise(self):
        print(self.name, "says", self.sound+"!")
        return self




Bongo = Pet('Bongo', 'Leopard Gecko', 'smile', 0, 0, "aaaaaaaAAAAAAAAAAあああああああ")
Atoli = Pet('Atoli', 'Cat', 'd e s t r o y', 0, 0, "MRRRRAAAAAAWH")

# Bongo.sleep(1).eat(1).play(2).noise()
# Atoli.sleep(12).eat(3).play(20).noise()




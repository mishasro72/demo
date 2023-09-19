class dogs:
    def __init__(self, type, owner_n, age):
        self.type = type
        self.owner_n = owner_n
        self.age = age

    def hello(self):
        print (f"{self.owner_n} has {self.type} {self.age} yeas old")

class owner(dogs):
    def __init__(self, type, owner_n, age, city):
        super().__init__(type, owner_n, age)
        self.city = city

    def city_c(self):
        print(f'{self.owner_n} and his dog {self.type} live in {self.city}')


dog_1 = dogs('Терьер', 'Alex', 7)

person = owner('Такса', 'Андрей', 12, 'Москва')

dog_1.hello()
person.city_c()

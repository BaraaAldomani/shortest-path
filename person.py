

class Person:
    def __init__(self) -> None:
        self.money = 0
        self.power = 0
        self.is_passenger = False

    def __eq__(self, person: object) -> bool:
        if isinstance(person, Person):
            a = self.money == person.money
            b = self.power == person.power
            c = self.is_passenger == person.is_passenger
            return a and b and c

    def set_money(self, money):
        self.money = money

    def set_power(self, power):
        self.power = power

    def set_is_passenger(self, is_passenger: bool):
        self.is_passenger = is_passenger

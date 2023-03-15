# Task Nr.3:

# Define the Animal, Mammal, and Primate classes.
# Animal should have a name attribute and a make_noise() method.
# Mammal should have a warm_blooded attribute and a give_birth() method.
# Primate should have an opposable_thumbs attribute and a swing() method.
# Test the classes by creating a Chimpanzee and making it do various things :) 🐒


class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def make_noise(self) -> str:
        return f"*making random noises*"


class Mammal(Animal):
    def __init__(self, name: str, warm_blooded: bool) -> None:
        super().__init__(name=name)
        self.warm_blooded: bool = warm_blooded

    def give_birth(self) -> str:
        return f"It's baby appeared out of nowhere!"


class Primate(Mammal):
    def __init__(self, name: str, warm_blooded: bool, opposable_thumbs: bool) -> None:
        super().__init__(name=name, warm_blooded=warm_blooded)
        self.opposable_thumbs: bool = opposable_thumbs

    def swing(self) -> str:
        return f"{self.name} is using human swings, that looks interesting"


class Chimpanzee(Primate):
    def __init__(self, name: str, warm_blooded: bool, opposable_thumbs: bool) -> None:
        super().__init__(
            name=name, warm_blooded=warm_blooded, opposable_thumbs=opposable_thumbs
        )
        pass

    def make_it_do_something(self) -> str:
        return f"{self.swing()} while {self.make_noise()}, {self.give_birth()}"


chimpanzee = Chimpanzee("Antanas", True, False)
print(chimpanzee.make_it_do_something())

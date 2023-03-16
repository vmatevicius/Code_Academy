# Task Nr.2:

# Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
# Implement at least five methods in a superclass what would describe those vehicles.


# The default fare charge of any vehicle is seating capacity * 100 . If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance charge.


class Vehicle:
    def __init__(
        self,
        name: str,
        make_year: int,
        color: str,
        max_speed: float,
        max_seats: int,
    ) -> None:
        self.name: str = name
        self.make_year: int = make_year
        if type(color) != str:
            raise TypeError(" Color must be in string format")
        self.color: str = color
        self.max_speed: float = max_speed
        if max_seats == 0:
            raise ValueError(" Max seats cannot be 0")
        self.max_seats: float = max_seats
        self.default_fare_charge = max_seats * 100

    def get_name(self) -> str:
        return f"name is {self.name}"

    def get_color(self) -> str:
        return f"color is {self.color}"

    def get_max_speed(self) -> str:
        return f"max speed is {self.max_speed}"

    def get_max_seats(self) -> str:
        return f"Maximum seats number is {self.max_seats}"

    def get_make_year(self) -> str:
        return f"{self.name} is made in {self.make_year}"

    def get_fare_charge(self) -> str:
        return f"Default fare charge is {self.default_fare_charge}"


class Bus(Vehicle):
    def __init__(
        self,
        name: str,
        make_year: int,
        color: str,
        max_speed: float,
        max_seats: int,
    ) -> None:
        super().__init__(
            name=name,
            make_year=make_year,
            color=color,
            max_speed=max_speed,
            max_seats=max_seats,
        )
        self.default_fare_charge = self.get_bus_fare_charge()

    def get_bus_fare_charge(self):
        default_charge = self.max_seats * 100
        return (default_charge * 10 / 100) + default_charge


class Taxi(Vehicle):
    def __init__(
        self,
        name: str,
        make_year: int,
        color: str,
        max_speed: float,
        max_seats: int,
    ) -> None:
        super().__init__(
            nname=name,
            make_year=make_year,
            color=color,
            max_speed=max_speed,
            max_seats=max_seats,
        )


class Train(Vehicle):
    def __init__(
        self,
        name: str,
        make_year: int,
        color: str,
        max_speed: float,
        max_seats: int,
    ) -> None:
        super().__init__(
            name=name,
            make_year=make_year,
            color=color,
            max_speed=max_speed,
            max_seats=max_seats,
        )


bus = Bus("Superbus", 1999, "blue", 150, 99)
print(bus.get_bus_fare_charge())
print(bus.get_make_year())

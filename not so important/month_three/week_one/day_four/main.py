# Task Nr.1:

# Create a class which takes temperature measurements in Kelvins and add static methods to transform those to Celsius
# and Fahrenheit units. Use OOP abstraction.

# from abc import ABC, abstractmethod


# class Converter(ABC):
#     @abstractmethod
#     def convert_to_celsius(self) -> float:
#         pass

#     @abstractmethod
#     def convert_to_fahrenheit(self) -> float:
#         pass


# class KelvinsConverter(Converter):
#     CONVERSION_NUMBER = 273.15

#     @staticmethod
#     def convert_to_celsius(kelvins: float) -> float:
#         return round(kelvins - 273.15, 2)

#     @staticmethod
#     def convert_to_fahrenheit(kelvins: float) -> float:
#         return round((kelvins - 273.15) * 9 / 5 + 32, 2)


# converter = KelvinsConverter()

# print(converter.convert_to_fahrenheit(500))

# print(f"celsius: {KelvinsConverter.convert_to_celsius(500)}")
# print(f"fahrenheit: {KelvinsConverter.convert_to_fahrenheit(500)}")

# Task Nr.3:

# Create a class called TimeUtils that has a static method called time_to_seconds that takes a time string in the format hh:mm:ss
# and returns the total number of seconds represented by that time. Use functional programing paradigm.


# class TimeUtils:
#     """time string format 'hh:mm:ss'"""

#     @staticmethod
#     def time_to_seconds(time: str) -> int:
#         hours, minutes, seconds = map(int, time.split(":"))
#         return (hours * 60) * 60 + (minutes * 60) + seconds


# print(f"seconds {TimeUtils.time_to_seconds('24:00:00')}")

# Create a class called Employee with a static method called calculate_payroll that takes a list of Employee instances
# and returns the total amount to be paid to all employees. Each Employee instance has two attributes: name and salary.

from typing import List


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name: str = name
        self.salary: float = salary

    @staticmethod
    def calculate_payroll(employees_list: List["Employee"]) -> float:
        return sum(employee.salary for employee in employees_list)


employee_list = [
    Employee(name="Antanas", salary=1000),
    Employee(name="NeAntanas", salary=2000),
    Employee(name="NeAntanas", salary=1234),
]

print(Employee.calculate_payroll(employees_list=employee_list))

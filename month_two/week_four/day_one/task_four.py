# Create a Calculator program :
#     it should contain abstract class with methods (abstract and not),
#     base class, geometry, arithmetic calculator classes.
#     Every subclass should have at least 5 methods to make some meaningful calculus operations.

from abc import ABC, abstractmethod
from typing import Union, Optional


class Calculator(ABC):
    @abstractmethod
    def add_numbers(
        self, number_one: Union[float, int], number_two: Union[float, int]
    ) -> Union[float, int]:
        pass

    @abstractmethod
    def subtract_numbers(
        self, number_one: Union[float, int], number_two: Union[float, int]
    ) -> Union[float, int]:
        pass

    @abstractmethod
    def divide_numbers(
        self, number_one: Union[float, int], number_two: Union[float, int]
    ) -> Optional[float]:
        pass

    @abstractmethod
    def multiply_numbers(
        self, number_one: Union[float, int], number_two: Union[float, int]
    ) -> Union[float, int]:
        pass


class BaseCalculator(Calculator):
    def add_numbers(
        self, number_one: Union[float, int], number_two: Union[float, int]
    ) -> Union[float, int]:
        return number_one + number_two

    def subtract_numbers(
        self, number_one: Union[float, int], number_two: Union[float, int]
    ) -> Union[float, int]:
        return number_one - number_two

    def divide_numbers(
        self, number_one: Union[float, int], number_two: Union[float, int]
    ) -> Optional[float]:
        try:
            return number_one / number_two
        except ZeroDivisionError:
            print("Division by zero is not available")

    def multiply_numbers(
        self, number_one: Union[float, int], number_two: Union[float, int]
    ) -> Union[float, int]:
        return number_one * number_two


class GeometryCalculator(BaseCalculator):
    def get_square_area(self, side_lenght: Union[float, int]) -> Union[float, int]:
        return side_lenght * side_lenght

    def get_square_perimeter(self, side_lenght: Union[float, int]) -> Union[float, int]:
        return side_lenght * 4

    def get_circle_diameter(
        self, circle_radius: Union[float, int]
    ) -> Union[float, int]:
        return circle_radius * 2

    def get_circle_area(self, circle_radius: Union[float, int]) -> Union[float, int]:
        return 3.14 * (circle_radius * circle_radius)

    def get_triangle_perimeter(
        self,
        side_one: Union[float, int],
        side_two: Union[float, int],
        side_three: Union[float, int],
    ) -> Union[float, int]:
        return side_one + side_two + side_three

    def get_triangle_area(
        self, bottom: Union[float, int], height: Union[float, int]
    ) -> Union[float, int]:
        return 0.5 * bottom * height


class AritmethicCalculator(BaseCalculator):
    def do_exponentiation(
        self, number: Union[float, int], power_value: Union[float, int]
    ) -> Union[float, int]:
        return number**power_value

    def get_modulus(
        self, number: Union[float, int], modulus: Union[float, int]
    ) -> Union[float, int]:
        return number % modulus


geometric_calc = GeometryCalculator()
print(geometric_calc.get_square_area(side_lenght=5))
print(geometric_calc.get_circle_area(circle_radius=3))
aritmethic_calc = AritmethicCalculator()
print(aritmethic_calc.do_exponentiation(number=10, power_value=10))
base_calc = BaseCalculator()
print(base_calc.divide_numbers(number_one=10, number_two=2))

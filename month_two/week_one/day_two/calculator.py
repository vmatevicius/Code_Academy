from typing import Union, Optional
import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Calculator:

    def __init__(self, number_one:Union[int, float], number_two:Union[int, float]):
        logging.info(f"Recieved values when creating a calculator object. number_one: {number_one}, number_two: {number_two}")
        if type(number_one) and type(number_two) not in [int, float]:
            logging.error(f"TypeError recieved when creating calculator obj.")
            raise TypeError("Wrong input type")
        self.number_one = number_one
        self.number_two = number_two
            
    @classmethod
    def get_numbers(cls):
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter first number: "))
        return cls(number_one, number_two)
    
    def add(self) -> Optional[Union[int, float]]:
        return self.number_one + self.number_two
        
    def divide(self) -> Optional[float]:
        return self.number_one / self.number_two
        
    def multiply(self) -> Optional[Union[int, float]]:
        return self.number_one * self.number_two
        
    def subtract(self) -> Optional[Union[int, float]]:
        return self.number_one - self.number_two

calculator = Calculator.get_numbers()
print(calculator.add())
# calculator = Calculator(5, 20)
# print(f"Addition: {calculator.add()}, Subtraction: {calculator.subtract()}, Division: {calculator.divide()}, Multiplication: {calculator.multiply()} ")

from typing import Union, Optional
import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Calculator:

    def __init__(self, number_one:Union[int, float], number_two:Union[int, float]):
        logging.info(f"Recieved values when creating a calculator object. number_one: {number_one}, number_two: {number_two}")
        if type(number_one) and type(number_two) not in [int, float]:
            raise TypeError("Wrong input type")
        self.number_one = number_one
        self.number_two = number_two
            
    @classmethod
    def get_numbers(cls):
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter first number: "))
        return cls(number_one, number_two)
    
    def add(self) -> Optional[Union[int, float]]:
        try:
            return self.number_one + self.number_two
        except Exception as e:
            logging.error(f"Error recieved when calling add. {e}")
    def divide(self) -> Optional[float]:
        try:
            return self.number_one / self.number_two
        except Exception as e:
            logging.error(f"Error recieved when calling divide. {e}")
        
    def multiply(self) -> Optional[Union[int, float]]:
        try: 
            return self.number_one * self.number_two
        except Exception as e:
            logging.error(f"Error recieved when calling multiply. {e}")
    def subtract(self) -> Optional[Union[int, float]]:
        try:
            return self.number_one - self.number_two
        except Exception as e:
            logging.error(f"Error recieved when calling subtract. {e}")
    
calculator = Calculator(5, 20)
print(f"Addition: {calculator.add()}, Subtraction: {calculator.subtract()}, Division: {calculator.divide()}, Multiplication: {calculator.multiply()} ")

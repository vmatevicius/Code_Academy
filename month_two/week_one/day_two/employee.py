import logging 

# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Employee():
    
    def __init__(self, first_name: str, last_name: str):
        logging.info(f"Recieved values when creating an employee. first name: {first_name}, last name: {last_name}")
        try:
            self.fullname = f"{first_name} {last_name}"
            self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"
        except Exception as e:
            logging.error(f"Error recieved when setting employee obj. values. {e}")
            
    @classmethod
    def get(cls):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        return cls(first_name, last_name)
    
worker = Employee("Vytautas", "Matevicius")
print(worker.email)

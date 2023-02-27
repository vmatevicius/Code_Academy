import logging
from typing import Union

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# A country can be said as being big if it is:

# Big in terms of population.
# Big in terms of area.

# Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

# Population is greater than 250 million.
# Area is larger than 3 million square km.
# Also, create a method which compares a country's population density to another country object. Return a string in the following format:

# {country} has a {smaller / larger} population density than {other_country}

class Country():
    
    def __init__(self,name: str, population: int, area: Union[int,float]):
        logging.info(f"Recieved values when creating a country object. population: {population}, area: {area}")
        self.name = name
        self.population = population
        self.area = area
            
    def __str__(self) -> str:
        
        return f"{self.name} has {self.population} citizens and occupies {self.area} square km of land"
            
    @classmethod
    def get(cls):
        name = input("Enter countries name: ")
        population = int(input("Enter population: "))
        area = int(input("Enter area size in square km.: "))
        return cls(name, population, area)
            
    def is_big(self) -> bool:
        try:
            if self.population > 250000000 or self.area > 3000000:
                return True
            return False
        except Exception as e:
            logging.error(f"Error recieved when calling is_big. {e}")
            
    def compare_population_density(self, country) -> str:
        # compare population density
        try:
            if (self.population / self.area) > (country.population / country.area):
                return f"{self.name} has a higher population density than {country.name}"
            else:
                return f"{country.name} has a higher population density than {self.name}"
        except Exception as e:
            logging.error(f"Error recieved when calling compare_pd. {e}")
    
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
athens = Country("Athens", 70000, 400)
wonderland = Country.get()

print(wonderland)
print(australia.is_big())
print(andorra.is_big())
print(andorra.compare_population_density(athens))
    
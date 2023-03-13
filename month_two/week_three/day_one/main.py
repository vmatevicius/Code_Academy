# Create a Person class which will have three properties:
#     Name
#     List of foods they like
#     List of foods they hate
# In this class, create the method taste():
#     It will take in a food name as a string.
#     Return {person_name} eats the {food_name}.
#     If the food is in the person's like list, add 'and loves it!' to the end.
#     If it is in the person's hate list, add 'and hates it!' to the end.
#     If it is in neither list, simply add an exclamation mark to the end.
#     p1 = Person("Sam", ["ice cream"], ["carrots"])
#     p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
#     p1.taste("cheese") ➞ "Sam eats the cheese!"
#     p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"


from typing import List, Dict, Union

# class Person:
    
#     def __init__(self, persons_name: str, liked_foods: List[str],hated_foods: List[str]):
#         self.name: str = persons_name
#         self.liked_foods: List[str] = liked_foods
#         self.hated_foods: List[str] = hated_foods
        
#     def taste(self, food: str) -> str:
        
#         if food in self.liked_foods:
#             return f"{self.name} eats the {food} and loves it!"
#         if food in self.hated_foods:
#             return f"{self.name} eats the {food} and hates it!"
#         return f"{self.name} eats the {food}!"

# person_one = Person("Sam", liked_foods= ["ice cream", "sausage"], hated_foods = ["carrots", "beetroots"])
# print(person_one.taste("ice cream"))
# print(person_one.taste("cheese"))
# print(person_one.taste("carrots"))




# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.
#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence.
#     If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
#     Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented.


# class Smoothie:
    
#     def __init__(self, ingredients: Dict[str,Union[int,float]]):
#         self.ingredients = ingredients
        
#     def get_cost(self) -> Union[int,float]:

#         values = list(self.ingredients.values())
#         return sum(values)

#     def get_price(self) -> float:
        
#         price = self.get_cost()
#         return price + (price * 1.5)
    
#     def get_name(self) -> str:
        
#         ingredients_names = list(self.ingredients.keys())
#         ingredients_names.sort()
#         if len(ingredients_names) > 2:    
#             return f'Ingredients for this smoothie are : {", ".join(ingredients_names)}, add everything according to your taste and use "smoothie" function'
#         return f'Ingredients for this smoothie are : {", ".join(ingredients_names)}, add everything according to your taste and use "fusion" function'

# class StomachCleaner(Smoothie):
    
#     INGREDIENTS = {
#     "beer" : 2,
#     "banana" : 1,
#     "butter": 0.5,
#     "sugar": 0.3,
#     "milk": 1,
# }

#     def __init__(self):
#         super().__init__(self.INGREDIENTS)

# class ProteinSmoothie(Smoothie):
    
#     INGREDIENTS = {
#     "vanilla protein powder": 2,
#     "milk": 1,
# }
    
#     def __init__(self):
#         super().__init__(self.INGREDIENTS)
    

# first_smoothie = StomachCleaner()
# print(first_smoothie.get_cost())
# print(first_smoothie.get_price())
# print(first_smoothie.get_name())

# second_smoothie = ProteinSmoothie()
# print(second_smoothie.get_cost())
# print(second_smoothie.get_price())
# print(second_smoothie.get_name())


# Create a class Sudoku that takes a string as an argument. The string will contain the numbers of a regular 9x9 sudoku board left to right and top to bottom, with zeros filling up the empty cells.
# Attributes
# An instance of the class Sudoku will have one attribute:
#     board: a list representing the board, with sublits for each row, with the numbers as integers. Empty cell represented with 0.
# Methods
# An instance of the class Sudoku wil have three methods:
#     get_row(n): will return the row in position n.
#     get_col(n): will return the column in position n.
#     get_sqr([n, m]): will return the square in position n if only one argument is given, and the square to which the cell in position (n, m) belongs to if two arguments are given.
#     game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
# game.board ➞ [
#   [4, 1, 7, 9, 5, 0, 0, 3, 0],
#   [0, 0, 0, 0, 0, 0, 7, 0, 0],
#   [0, 6, 0, 0, 0, 7, 0, 0, 0],
#   [0, 5, 0, 0, 0, 9, 1, 0, 6],
#   [8, 0, 0, 6, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 3, 4, 0, 0],
#   [9, 0, 0, 0, 0, 5, 0, 0, 0],
#   [0, 0, 0, 4, 3, 0, 0, 0, 0],
#   [2, 0, 0, 7, 0, 1, 5, 8, 0]
# ]
# game.get_row(0) ➞ [4, 1, 7, 9, 5, 0, 0, 3, 0]
# game.get_col(8) ➞ [0, 0, 0, 6, 0, 0, 0, 0, 0]
# game.get_sqr(1) ➞ [9, 5, 0, 0, 0, 0, 0, 0, 7]
# game.get_sqr(1, 8) ➞ [0, 3, 0, 7, 0, 0, 0, 0, 0]
# game.get_sqr(8, 3) ➞ [0, 0, 5, 4, 3, 0, 7, 0, 1]

class Sudoku:

    def __init__(self, numbers: str):
        self.board = self.make_board(numbers)
        
    def make_board(self, numbers: str) -> List[int]:
        
        max_columns = 9
        board = []
        column_counter = 0
        row = []
        
        for number in numbers:
            row.append(int(number))
            column_counter += 1
            if column_counter == max_columns:
                board.append(row)
                row = []
                column_counter = 0
            else:
                continue
        return board
    
    def show_board(self) -> None:
        
        index = 0
        for index in range(9):      
            print(self.board[index])
            index += 1   

    def get_row(self, position: int) -> List[int]:
        
        return self.board[position]
    
    def get_col(self, position: int) -> List[int]:
        
        column = []
        
        for row in self.board:
            column.append(row[position])
        return column
    
    def get_sqr(row:int , column:int):
        
        ...
        

            
game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")

print(game.get_row(0))
print(game.get_col(8))
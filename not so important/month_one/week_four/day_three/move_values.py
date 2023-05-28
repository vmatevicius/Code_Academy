from typing import Optional
import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# Write a function that moves all elements of one type to the end of the list:

# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# # Move all the 1s to the end of the array.
# Log out inputs and results in a file.

def move_list_values(list_of_numbers: list) -> Optional[list]:
    logging.info(f"Recieved list of numbers: {list_of_numbers}")
    new_list = []
    list_of_ones = []
    try:
        for number in list_of_numbers:
            if number == 1:
                list_of_ones.append(number)
            else:
                new_list.append(number)
        return new_list + list_of_ones
    except Exception as e:
        logging.error(f"Error recieved: {e}")
        
print(move_list_values([1, 3, 2, 4, 4, 1]))
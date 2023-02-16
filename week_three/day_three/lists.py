# Write a function that takes two lists and adds the first element in the first list with the first element in the second list,
# the second element in the first list with the second element in the second list, etc, etc. Return True if all element combinations add up to the same number. Otherwise, return
# False. Example:

# puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# # 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# # Both lists sum to [5, 5, 5, 5]
# puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
# puzzle_pieces([1, 2], [-1, -1]) ➞ False
# puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False

def compare_list_values(list_one, list_two) -> bool:
    new_list = []
    index = 0
    if len(list_one) != len(list_two):
        return False
    while index != len(list_one):
        new_value = list_one[index] + list_two[index]
        new_list.append(new_value)
        index += 1
    if len(set(new_list)) == 1:
        return True
    else:
        return False
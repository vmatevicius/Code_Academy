# You have to determine which group sums larger: the evens or the odds. The larger group wins.
# Create a function that takes a list of integers, sums the even and odd numbers separately, then returns the difference between the sums of the even and odd numbers.

# Example:

# war_of_numbers([2, 8, 7, 5]) ➞ 2
# # 2 + 8 = 10
# # 7 + 5 = 12
# # 12 is larger than 10
# # So we return 12 - 10 = 2
# war_of_numbers([12, 90, 75]) ➞ 27
# war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168

def get_difference(list_of_numbers) -> int:
    odd = []
    even = []
    for number in list_of_numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    if sum(odd) > sum(even):
        return sum(odd) - sum(even)
    else:
        return sum(even) - sum(odd)
    
print(get_difference([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))
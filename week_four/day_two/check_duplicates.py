def check_duplicate_values(list_of_values) -> bool:

    '''If duplicate found returns True, else False'''
    
    i = 1
    for value in list_of_values:
        if i == len(list_of_values):
            return False
        index = i
        for _ in range(len(list_of_values)):
            if value == list_of_values[index]:
                return True
            elif index == len(list_of_values) -1:
                break
            else:
                index += 1
        i += 1
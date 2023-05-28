# Create a function that adds a string ending to each member in a list.

strings = ["clever", "hard", "common","basic"]

def add_string_ending(list, ending):

    new_list = []
    
    for word in list:
        new_list.append(f"{word}{ending}")
    return new_list

print(add_string_ending(strings, "ly"))
# Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself)

def main():

    numbers = [55, 5, 6, 10]

    print(multiply_list_values(numbers))

def multiply_list_values(your_list):
    
    number = 1
    
    for i in your_list:
        number = number * i
    return number

if __name__ == "__main__":
    main()

import sys

def main():

    # Puting sentences in separate lists and sorting them out in reverse order)

    list_one = sorted(create_list(), reverse=True)
    list_two = sorted(create_list(), reverse=True)
    list_three = sorted(create_list(), reverse=True)
    list_four = sorted(create_list(), reverse=True)
    list_five = sorted(create_list(), reverse=True)
    
    # Creating 5 five new lists that contain first, second  indexed elements from primary lists. (first list containing
    # all first elements of those five, second list second elements and so on).
    
    new_list_one = [list_one[0], list_two[0], list_three[0], list_four[0], list_five[0]]
    new_list_two = [list_one[1], list_two[1], list_three[1], list_four[1], list_five[1]]
    new_list_three = [list_one[2], list_two[2], list_three[2], list_four[2], list_five[2]]
    new_list_four = [list_one[3], list_two[3], list_three[3], list_four[3], list_five[3]]
    new_list_five = [list_one[4], list_two[4], list_three[4], list_four[4], list_five[4]]
    
    # print the length of all list items and print the longest lenght list and shortest.
    
    lenght_one, lenght_two, lenght_three = calculate_lenght( new_list_one),calculate_lenght(new_list_two),calculate_lenght(new_list_three)
    lenght_four, lenght_five = calculate_lenght(new_list_four),calculate_lenght(new_list_five)
    
    lenght_list = [lenght_one, lenght_two, lenght_three,lenght_four, lenght_five]
    
    print("The longest lenght of a list is:", max(lenght_list))
    print("The shortest lenght of a list is:", min(lenght_list))

    # return the lenght of items in the list summed up
def calculate_lenght(list):
    
    lenght = 0
    for j in list:
        lenght += len(j)
    return lenght

    # takes a five word sentence and creates a list out of it   
def create_list():
    
    sentence = input("Enter a 5 word long sentence: ").split(" ")
    if len(sentence) != 5:
        sys.exit("Sentence needs to be 5 words long!")
    else:
        return [x for x in sentence]
    
if __name__ == "__main__":
    main()
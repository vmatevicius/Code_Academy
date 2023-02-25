# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and 15 letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.
import random

def main():
    
    dictionary_of_letters = {}
    words = []
    for _ in range(5):
        words += generate_list()

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
    i = 0
    amounts = []
    for i in range(15):
        x = calculate_letters(words, str(i))
        amounts.append(i)
        i += 1
        
    j = 0
    k = 0
    
    for _ in range(15):
        if amounts[k] > 0:
            dictionary_of_letters[letters[j]] = amounts[k]
            k += 1
            j += 1
        else:
            k += 1
            j += 1
            
    print(dictionary_of_letters)
    print(sorted(words))
    
def calculate_letters(word, letter):

    amount = 0
    for letters in word:
        if letter in letters:
            amount += 1
        else:
            continue
    return amount
        
def generate_list():
    
    new_list = []
    for _ in range(5):
        new_list.append(generate_word())
    return new_list
    

def generate_word():
    
    word = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
    word_lenght = random.randint(5,15)
    for _ in range(word_lenght):
        index = random.randint(0,14)
        letter = letters[index]
        word.append(letter)
    return "".join(word)

if __name__ == "__main__":
    main()
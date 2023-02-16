# Create program that allows user to enter text
# Convert that text to Leet speak 1337

def main():
    
    text = get_input()
    print("".join(replace_letter(text)))

def get_input():
    
    return input("Enter text: ")

def replace_letter(text):
    
    leet = {    
    "O": "0",
    "I": "1",
    "Z": "2",
    "E": "3",
    "A": "4",
    "S": "5",
    "G": "6",
    "T": "7",
    "B": "8",
    "P": "9"
    }
    leet_text = []
    for key in text:
        upper_key = key.upper()
        if upper_key in leet:
            leet_text.append(leet[upper_key])
        else:
            leet_text.append(key)
    return leet_text
                
    
if __name__ == "__main__":
    main()
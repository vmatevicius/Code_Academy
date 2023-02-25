# Create a program that allows user to enter a full sentence
# print the sentence backwards
# print every second letter in the sentence

sentence = input("Enter random sentence: ")

print(sentence[::-1])
print(sentence[::2].replace(" ",""))
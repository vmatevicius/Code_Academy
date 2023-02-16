# Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

users = ["Vytautas","Mindaugas","Rokas"]

name = input("Enter your name: ")
if name in users:
    print("Welcome", name)
else:
    print("Welcome")
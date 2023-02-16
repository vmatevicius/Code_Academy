# Create a variables containing strings for username and password.
# Start Endless loop allowing to enter username and password. If credentials are correct stop endless loop and print greeting message.

user = ["Antanas", "123"]

while True:
    user_login, user_password = input("Enter your login name and password, separated by space: ").split()
    if user_login == user[0] and user_password == user[1]: 
        print(f"Hello {user[0]}!")
        break
    else:
        continue
    
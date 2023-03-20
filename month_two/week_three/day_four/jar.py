class CookieJar:
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("Capacity cannot be a negative number")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        if self.size > 0:
            return self.size * "🍪"
        return "There are no cookies left :("

    def deposit(self, number_of_cookies):
        if number_of_cookies > self.capacity:
            raise ValueError("Jar does not have enough space for that many cookies")
        self.size = self.size + number_of_cookies

    def withdraw(self, number_of_cookies):
        if number_of_cookies > self.size:
            raise ValueError(
                "You cannot withdraw more cookies than there is in the jar"
            )
        self.size = self.size - number_of_cookies
        print(f"*nom nom nom* {number_of_cookies} cookies were eaten")


jar = CookieJar(12)
jar.deposit(8)
print(jar)
print(jar.size)
jar.withdraw(3)
print(jar.size)
jar.withdraw(5)
print(jar.size)
print(jar)

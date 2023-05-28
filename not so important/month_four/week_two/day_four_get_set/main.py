# Write a Temperature class that has a celsius property and a fahrenheit property.
# The celsius property stores the temperature in Celsius, and the fahrenheit property stores the temperature in Fahrenheit.
# The fahrenheit property should be a computed property that converts the Celsius temperature to Fahrenheit.


# class Temperature:
#     def __init__(self) -> None:
#         pass

#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self, temperature_in_celsius: float):
#         self._celsius = temperature_in_celsius

#     @property
#     def fahrenheit(self):
#         return (self.celsius * 1.8) + 32


# termometer = Temperature()
# termometer.celsius = 30
# print(termometer.celsius)
# print(termometer.fahrenheit)


# Task Nr.2 : Write a User class that has a password property.
# The password property should be a computed property that checks whether the password is strong enough.
# A password is considered strong if it has at least 8 characters, contains at least one uppercase letter,
# one lowercase letter, and one number.

import re


class User:
    @property
    def password(self) -> None:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        if not self.is_password_strong(value):
            raise ValueError("why password so weak")
        self._password = value

    @staticmethod
    def is_password_strong(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        return True


user = User()
user.password = "Antanas1"
print(user.password)

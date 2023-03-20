# Create an abstract class Money which takes currency and value as input and initializes it. A class must have these methods:

# get_value method which returns the value of the money.
# get_currency method which returns the currency of the money.
# convert_to_currency abstract method, which takes target currency and conversion rate as input and converts the value of the money to the target currency.
# Now create two subclasses of Money: Cash and Card. The Cash class should take the denomination of the cash as input in the constructor,
# and should implement the convert_to_currency method. The Card class should take the credit limit of the card as input in the constructor,
# and should implement the convert_to_currency method using the conversion rate to convert the value of the card to the target currency.


class Money:
    def __init__(self, currency: str, value: float) -> None:
        self.currency = currency
        self.value = value

    def get_value(self) -> float:
        return self.value

    def get_currency(self) -> str:
        return self.currency

    def convert_to_currency(self, target_currency: str, conversion_rate: float) -> str:
        raise NotImplementedError


class Cash(Money):
    def __init__(self, currency: str, value: float, denomination: int) -> None:
        super().__init__(currency=currency, value=value)
        self.denominatiom = denomination

    def convert_to_currency(self, target_currency: str, conversion_rate: float) -> str:
        return f"{round(self.denominatiom * conversion_rate, 2)}{target_currency}"


class Card(Money):
    def __init__(self, currency: str, value: float, credit_limit: float) -> None:
        super().__init__(currency=currency, value=value)
        self.credit_limit = credit_limit

    def convert_to_currency(self, target_currency: str, conversion_rate: float) -> str:
        return f"{round(self.value * conversion_rate, 2)}{target_currency}"


dollars = Cash("Euro", 100, 100)
print(dollars.get_currency())
print(dollars.get_value())
print(dollars.convert_to_currency("$", 1.07))

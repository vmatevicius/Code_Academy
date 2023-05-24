# def is_leap(year):
#     if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#         return True
#     else:
#         return False


class Sentence:
    def __init__(self, text: str = "Antanas") -> None:
        self.text = text

    def backwards(self) -> str:
        return self.text[::-1]

    def transform_to_uppercase(self) -> str:
        return self.text.upper()

    def transform_to_lowercase(self) -> str:
        return self.text.lower()

    def find(self, what_to_find) -> int:
        return self.text.count(what_to_find)

    def replace(self, old, new) -> str:
        return self.text.replace(old, new)

    def retarded_function(self, number) -> list[str]:
        suskirstytas = self.text.split()
        return suskirstytas[number]

    def info(self) -> dict[str, int]:
        word_count = len(self.text.split())
        numbers = sum(i.isnumeric() for i in self.text)
        upper_letters = sum(i.isupper() for i in self.text)
        lower_letters = sum(i.islower() for i in self.text)
        print(
            f"Word count: {word_count}, numbers: {numbers}, uppercase: {upper_letters}, lowercase: {lower_letters}"
        )
        return {
            "Word count": word_count,
            "Numbers": numbers,
            "Upper Letters": upper_letters,
            "Lower letters": lower_letters,
        }

    def __str__(self) -> str:
        return "Text: " + self.text


if __name__ == "__main__":
    mano_sakinys = Sentence()
    print(mano_sakinys.backwards())
    print(mano_sakinys.transform_to_lowercase())
    print(mano_sakinys.transform_to_uppercase())
    print(mano_sakinys.find("a"))
    print(mano_sakinys.replace("Mano", "Savo"))
    print(mano_sakinys.retarded_function(0))
    mano_sakinys.info()
    print(mano_sakinys)
    # print(is_leap(2000))

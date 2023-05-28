# 1: Create a generator function that takes a positive integer n as input and generates all the even numbers up to and including n.
from collections.abc import Iterator
from typing import Union, List
import time
import sys

# def get_even_numbers(positive_number: int) -> Iterator[int]:
#     for number in range(positive_number + 1):
#         if number % 2 == 0:
#             yield number


# generated_numbers = get_even_numbers(10)

# for number in generated_numbers:
#     print(number)


# Create a generator function that would pick word from a generator and/list of generated random words (should be > 10000) and would stop itterating
# until the word longer than 7 lettters is found.
# Compare sizes of list and generator. Calculate performance per both executions (time to complete in ms)

from py_random_words import RandomWords

rnd_word = RandomWords()

random_words = [rnd_word.get_word() for _ in range(10000)]

words = [word for word in random_words]

generated_words = (word for word in words)


def find_word(words: Union[Iterator[str], List[str]]) -> Union[Iterator[str], str]:
    for word in words:
        if len(word) > 7:
            return word


start = time.time()
print(find_word(words))
end = time.time()
print(f"Time spent using list: {round(end)}")

start = time.time()
print(find_word(generated_words))
end = time.time()
print(f"Time spent using generator: {round(end)}")

print(sys.getsizeof(words))
print(sys.getsizeof(generated_words))

# You are given an input array of bigrams, and an array of words.
# Write a function that returns True if every single bigram from this array can be found at least once in an array of words.

# Example:

# can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) ➞ True
# can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) ➞ False
# # "cu" does not exist in any of the words.
# can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ True
# can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]) ➞ False

import re

def check_bigrams(bigram_list, word_list) -> bool:
    
    for bi in bigram_list:
        if re.search(f"^.*{bi}.*$", " ".join(word_list)):
            continue
        else:

            return False
    return True

print(check_bigrams(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
# We want to check if strings 's' and 't' are each others anagrams. This means that the order
# in which characters of 's' and 't' appear in themselves do not matter as long as it's the
# same characters that appear the same amount of time. This check can be done via a hashmap.

from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    counter = defaultdict(int)

    for char in s:
        counter[char] += 1
    for char in t:
        if char not in counter:
            return False
        else:
            counter[char] -= 1
    is_anagram = all([x == 0 for x in counter.values()])
    return is_anagram

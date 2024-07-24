# Two strings are anagrams if one 
# of the two statements hold true:

# 1. Their sorted versions are same.
# OR
# 2. The mapping of each character to
# it's occurance is identical for both
# strings.

# Method 1. takes O(klogk) time assuming
# both strings have roughly length k
# Method 2. takes O(k) time assuming
# both strings have roughly length k  

def group_anagrams(strs: list[str]) -> list[list[str]]:
    if len(strs) == 1:
        return [strs]
    
    groups = []
    while strs:
        current = strs.pop()
        group = [current]
        for other in strs[::]:
            if is_anagram(current, other):
                strs.remove(other)
                group.append(other)
        groups.append(group)
    
    return groups

# returns true if str1 and str2 are anagrams
def is_anagram(str1: str, str2: str) -> bool:
    # Could use the Counter function
    # from collections library
    
    map1 = {}
    map2 = {}

    def mapify(strx, mapx):
        for char in strx:
            if char not in mapx:
                mapx[char] = 1
            else:
                mapx[char] += 1
    
    mapify(str1, map1)
    mapify(str2, map2)

    return map1 == map2

# Time complexity:
# None of the strings are anagrams so we do
# the is_anagram operation each time we pop
# from the 'strs' array.

# Assuming all strings have length k and 'strs'
# array has length n:
# Time = k(n-1) + k(n-2) + ... + k(1) = O(k * n^2)

# NOTE: I've used list slices to workaround the problem
# of modifying the array while iterating it.

# Okay so this solution exceeds time limit on leetcode.
# Let's try another way.

def group_anagrams(strs: list[str]) -> list[list[str]]:
    hashmap = {}
    
    while strs:
        current = strs.pop()
        key = ''.join(sorted(current)) # to preserve OG string
        if key not in hashmap:
            hashmap[key] = [current]
        else:
            hashmap[key].append(current)
    
    return list(hashmap.values())

# Time complexity:
# Assuming we have n strings of length k,
# the key creation step takes O(klogk) time.
# Everything else in the loop is O(1)
# So we have O(n * klogk)

# Simpler code:
def group_anagrams(strs: list[str]) -> list[list[str]]:
    hashmap = {}

    for word in strs:
        key = ''.join(sorted(word)) # to preserve OG string
        if key not in hashmap:
            hashmap[key] = [word]
        else:
            hashmap[key].append(word)
    
    return list(hashmap.values())

# Can we make this faster?
# We just have to find a way to speed up the
# key generation step. Keys can only be of
# immutable type. We will use tuples.

# We can't use hashmaps like earlier since they
# have no sense of ordering. If we want to maintain
# ordering we would have to sort hashmaps.values()
# which defeats the purpose.

# Credit: https://leetcode.com/problems/group-anagrams/solutions/19176/share-my-short-java-solution

def group_anagrams(strs: list[str]) -> list[list[str]]:
    hashmap = {} # Use defaultdict(list) for
    # concise code.

    for word in strs:
        # key generation step
        char_map = [0] * 26
        for char in word:
            char_map[ord(char) - ord('a')] += 1

        key = tuple(char_map)

        if key not in hashmap:
            hashmap[key] = [word]
        else:
            hashmap[key].append(word)
    
    return list(hashmap.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

# Since the key generation step will take O(k) time,
# Overall time is O(n * k)
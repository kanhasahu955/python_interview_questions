# Two strings are anagrams if:
	# •	both strings contain same characters
	# •	character frequency is same
	# •	order does NOT matter



from collections import Counter,defaultdict

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def group_anagrams(words):
    d=defaultdict(list)
    for word in words:
        key="".join(sorted(word))
        d[key].append(word)
    return list(d.values())


print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
print(group_anagrams(["listen", "silent", "hello", "world"]))  # [['listen', 'silent'], ['hello', 'world']]
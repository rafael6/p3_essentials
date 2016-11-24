from collections import Counter

lst = [1, 1, 1, 2, 3,3,3,3,3]

# {3: 5, 1: 3, 2: 1}) where key is item and value is the number of times item appears
print(Counter(lst))


string = 'hello'
# {'l': 2, 'o': 1, 'e': 1, 'h': 1}
print(Counter(string))


phrase = 'Counts how many times each word appears appears appears yes yes'
words = phrase.split()
# {'appears': 2, 'many': 1, 'how': 1, 'each': 1, 'times': 1, 'word': 1, 'Counts': 1}
print(Counter(words))

c = Counter(words)
# [('appears', 3), ('yes', 2), ('each', 1)]
print(c.most_common(3))
# 11  The sum of all words in the phrase
print(sum(c.values()))

'''
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()                 # most common elements
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''
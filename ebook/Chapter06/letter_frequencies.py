from collections import Counter
from collections import defaultdict
import string


def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


print (letter_frequency('xin chao xin cho toi!'))


num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])


d = defaultdict(tuple_counter)


d['a'][1].append("hello")
d['b'][1].append('world')
d['c'][1].append('da')
print(d)


responses = [
"vanilla",
"chocolate",
"vanilla",
"vanilla",
"caramel",
"strawberry",
"vanilla"
]

def counter_letter_frequency(sentence):
    return Counter(sentence)

print(Counter(responses).most_common(2))
top = Counter(responses).most_common(2)
print(top[0][0], top[0][1])
print(top[1][0], top[1][1])
print("The children voted for {} ice cream".format(Counter(responses).most_common(2)[0][0]))


CHARACTERS = list(string.ascii_letters) + [" "]


print(CHARACTERS)


def list_letter_frequency(sentence):
    frequencies = [(c, 0) for c in CHARACTERS]
    print(frequencies)
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    return frequencies

print(list_letter_frequency('Xin chao dong laos'))
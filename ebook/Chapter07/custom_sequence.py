normal_list = [1, 2, 3, 4, 5]


class CustomSequence:
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return f"x{index}"


class FunkyBackwards:
    def __reversed__(self):
        return "BACKWARDS!"


for seq in normal_list, CustomSequence(), FunkyBackwards():
    print(f"\n{seq.__class__.__name__}: ", end="")
    for item in reversed(seq):
        print(item, end=", ")


class StringJoiner(list):
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
           self.result = "".join(self)

import random, string

with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))

print('join : ', joiner.result),

with StringJoiner() as jo:
    for i in range(15):
        jo.append(random.choice(string.ascii_letters))
        if i == 10:
            raise Exception('spam', 'eggs')

print('join with exception: ', jo.result)



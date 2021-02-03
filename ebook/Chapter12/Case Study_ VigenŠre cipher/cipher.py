import re


class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, data):
        return self.__code(data, combine_character)

    def extend_keyword(self, length):
        repeats = length // len(self.keyword.strip()) + 1
        return (self.keyword.strip() * repeats).upper()

    def decode(self, encrypt):
        return self.__code(encrypt, separate_character)

    def __code(self, data, func):
        self.validate(data, self.keyword)
        data = re.sub(' +', '', data)
        cipher = []
        key = self.extend_keyword(len(data))
        for p, k in zip(data, key):
            cipher.append(func(p, k))
        return "".join(cipher)

    def validate(self, data, key):
        if data is None or data == '':
            raise ValueError('Data invalid!')
        if key is None or key == '':
            raise ValueError('Key invalid!')


def combine_character(plain, keyword):
    return chr(ord("A") + (ord(plain.upper()) + ord(keyword.upper())) % 26)


def separate_character(plain, keyword):
    return chr(ord("A") + (ord(plain.upper()) - ord(keyword.upper())) % 26)

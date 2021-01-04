from model import Cursor, Character


class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self, character):
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, mode="w") as file:
            file.write("".join(self.characters))

    @property
    def to_string(self):
        return "".join(str(c) for c in self.characters)

class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    """is used in string-manipulation functions such as print and the str constructor to convert any class to a string"""

    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "-" if self.underline else ""
        return bold + italic + underline + self.character

import sys

from model import NoteBook


class Menu:
    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_note,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def run(self):
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print('{0} not input valid option'.format(choice))

    def display_menu(self):
        print("""
        Notebook Menu

        1. Show all notes
        2. Search note
        3. Add new note
        4. Modify note
        5. Quit
        """)

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print('{0}: {1}\n{2}'.format(note.get_id(), note.memo, note.tags))

    def search_note(self):
        filter = input('Search note :')
        if not filter:
            print('Input invalid!')
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input('Input memo:')
        self.notebook.new_note(memo)
        print('New node added!')

    def modify_note(self):
        id = int(input("Input note id:"))
        memo = input("Input memo:")
        tags = input("Input tags:")

        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print('Thank you for using montypython')
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()

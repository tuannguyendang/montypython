from .note import Note


class NoteBook:
    def __init__(self):
        self.notes = []

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        note = self.find_note_by_id(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        note: Note = self.find_note_by_id(note_id)
        if note:
            note.tags = str(tags)
            return True
        return False

    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.get_id() == note_id:
                return note
        return None

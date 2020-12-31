from model import Note, NoteBook

n1 = Note('hhii', '111')
print(n1.memo)
print(n1.tags)
n2 = Note('tuan')
print(n2.memo)
print(n2.tags)

nt1 = NoteBook()
nt1.notes.append(n1)
nt1.notes.append(n2)

print(nt1.search('tuan').pop(0).memo)

nt1.new_note('hoang', 2)
nt1.modify_memo(1, 'nguyen dang hoang')
nt1.modify_tags(2, '3.9')

for note in nt1.notes:
    print('{0} : {1} - {2} '.format(note.get_id(), note.memo, note.tags))

assert (nt1.notes[1])
assert (nt1.notes[1].get_id() == 2)

from collections import namedtuple

Book = namedtuple("Book", "author title genre")
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),
]

# set comprehension
fantasy_authors = {b.author for b in books if b.genre == "fantasy"}
print(fantasy_authors)
# dict comprehension
fantasy_titles = {b.title: b for b in books if b.genre == "fantasy"}
print(fantasy_titles)

Student = namedtuple("student", ['id', 'name', 'address', 'major'])
students = [
    Student(1, 'tuan', 'singapore', 'it'),
    Student(2, 'hoang', 'singapore', 'market'),
    Student(3, 'dang', 'singapore', 'accounting'),
    Student(4, 'thuy', 'singapore', 'hr'),
    Student(5, 'linh', 'singapore', 'code'),
    Student(6, 'tuan', 'singapore', 'code'),
]

code_student = {s.name for s in students if s.major == "code"}
print(code_student)

major_student = {s.major : s for s in students if s.major in ['it', 'code'] }
print(major_student)


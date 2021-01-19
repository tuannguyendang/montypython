from queue import Queue

song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
]

artists = set()
for song, artist in song_library:
    artists.add(artist)

print(artists)

alphabetical = list(artists)
alphabetical.sort()
print(alphabetical)

first_artists = {
    "Sarah Brightman",
    "Guns N' Roses",
    "Opeth",
    "Vixy and Tony",
}

second_artists = {"Nickelback", "Guns N' Roses", "Savage Garden"}

print("All: {}".format(first_artists.union(second_artists)))
print("Both: {}".format(second_artists.intersection(first_artists)))
print(
    "Either but not both: {}".format(
        first_artists.symmetric_difference(second_artists)
    )
)
print("Either but not both 2: {}".format(second_artists.symmetric_difference(first_artists)))

bands = {"Guns N' Roses", "Opeth"}

print("first_artists is to bands:")
print("issuperset: {}".format(first_artists.issuperset(bands)))
print("issubset: {}".format(first_artists.issubset(bands)))
print("difference: {}".format(first_artists.difference(bands)))
print("*" * 20)
print("bands is to first_artists:")
print("issuperset: {}".format(bands.issuperset(first_artists)))
print("issubset: {}".format(bands.issubset(first_artists)))
print("difference: {}".format(bands.difference(first_artists)))

def calculationRandom(n):
    queue = Queue()
    queuek = Queue()
    mydata = set()
    mydatak = set()
    for i in range(0,n):
        queue.put(i)
    while not queue.empty():
        num = queue.get()
        mydata.add(num)

    for i in range(5, n):
        queuek.put(i)
    while not queuek.empty():
        num = queuek.get()
        mydatak.add(num)

    print(mydata)
    print(mydatak)
    print(mydatak.issubset(mydata))
    print(mydatak.issuperset(mydata))
    print(mydata.difference(mydatak))
    print(mydatak.symmetric_difference(mydata))

calculationRandom(10)
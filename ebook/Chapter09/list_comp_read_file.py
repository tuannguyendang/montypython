import sys

filename = 'contract.txt'

with open(filename) as file:
    header = file.readline().strip().split("\t")
    contacts = [
        dict(zip(header, line.strip().split("\t")))
        for line in file
    ]

for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))


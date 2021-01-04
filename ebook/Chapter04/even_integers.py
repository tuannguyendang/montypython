class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


even = EvenOnly([2])
print (even.append(10))
print(even)
# print (even.append(3))
print (even.append('hi tuan'))
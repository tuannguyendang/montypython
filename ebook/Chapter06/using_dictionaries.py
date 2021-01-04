stocks = {
    "GOOG": (1235.20, 1242.54, 1231.06),
    "MSFT": (110.41, 110.45, 109.84),
}

print(stocks.get("GOOG"))
print(stocks.get("RIM", "NOT FOUND"))

print(stocks.setdefault("GOOG", "INVALID"))
print(stocks.setdefault("BBRY", (10.87, 10.76, 10.90)))
print(stocks["BBRY"])


for stock in stocks.keys():
    print('key: ', stock),


for values in stocks.values():
    print('value: ', values)

for key, values in stocks.items():
    print(f'{key} = {values}')


random_keys = {}
random_keys["astring"] = "somestring"
random_keys[5] = "aninteger"
random_keys[25.2] = "floats work too"
random_keys[("abc", 123)] = "so do tuples"


class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue


my_object = AnObject(14)
random_keys[my_object] = "We can even store objects"
my_object.avalue = 12
try:
    random_keys[[1, 2, 3]] = "we can't store lists though"
except:
    print("unable to store list\n")

for key, value in random_keys.items():
    print("{} has value {}".format(key, value))

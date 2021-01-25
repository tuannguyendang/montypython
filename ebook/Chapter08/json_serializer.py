import json


class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return {
                "is_contact": True,
                "first": obj.first,
                "last": obj.last,
                "full": obj.full_name,
            }
        return super().default(obj)


def decode_contact(dic):
    if dic.get("is_contact"):
        return Contact(dic["first"], dic["last"])
    else:
        return dic


class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)


c = Contact("John", "Smith")
result = json.dumps(c, cls=ContactEncoder)
print(result) #{"is_contact": true, "first": "John", "last": "Smith", "full": "John Smith"}


c = json.loads(result, object_hook=decode_contact)
print(c.first)
print(c.last)
print(c.full_name)
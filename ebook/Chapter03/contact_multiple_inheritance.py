from operator import __matmul__


class Contact:
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

if __name__ == '__main__':
    kwargs = {
        'name': 'tuan nguyen',
        'email': 'tuan123@gmail.com',
        'street' : 'nguyen duy trinh',
        'city': 'singapore',
        'state': 'singapore',
        'code': '122121'
    }
    friend = Friend('9121212', **kwargs)
    print(friend.phone)
    print(friend.name)
    print(friend.email)
    print(friend.street)
    print(friend.city)
    print(friend.code)
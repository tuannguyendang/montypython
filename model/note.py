import datetime

last_id = 0


class Note:
    def __init__(self, memo, tags=''):
        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tags = tags
        global last_id
        last_id += 1
        self.__id = last_id

    def match(self, filter):
        return filter in self.tags or filter in self.memo

    def get_id(self):
        return self.__id

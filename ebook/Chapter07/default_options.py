def get_pages(*links):
    for link in links:
        # download the link with urllib
        print(link)

get_pages()
get_pages('http://www.archlinux.org')
get_pages('http://www.archlinux.org',
           'http://ccphillips.net/')

class Options:
    default_options = {
        "port": 21,
        "host": "localhost",
        "username": None,
        "password": None,
        "debug": False,
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]

options = Options(username='tuan', debug=True,host='127.0.0.1')
print(options['username'])
print(options['debug'])
print(options['host'])
print(options['password'])
def default_arguments(x, y, z, a="Some String", b=False):
    pass


default_arguments("a string", 'variable', 8, "", True)

default_arguments("a longer string", 'some_variable', 14)

default_arguments("a string", 'variable', 14, b=True)

default_arguments(x='1', y='2', z='3', a='hi')


def kw_only(x, y='defaultkw', *, a, b='only'):
    print(x, y, a, b)


# kw_only('x') -> missing keyword-only argument a
# kw_only('x', 'y', 'a') -> takes from 1 to 2 positional arguments but 3 were given
kw_only('x', a='a', b='b')
kw_only('x', 'mykw', a='a', b='b')


number = 5
# the default value alway 5 can not make dynamic
def funky_function(number=number):
    print(number)

number=6

funky_function(8) # -> 8
funky_function()  # -> 5 it use default number value
print(number)     # -> 6

def hello(b=[]):
    b.append('a')
    print(b)

hello([])
hello(['b'])

def default_check(a, b=None):
    a = a if a !=None else 0
    print (b + a)

default_check(None, 10)
default_check(1,10)
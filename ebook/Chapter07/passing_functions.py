def my_function():
    print("The Function Was Called")


my_function.description = "A silly function"


def second_function():
    print("The second was called")


second_function.description = "A sillier function."


def another_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("The name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now I'll call the function passed in")
    function()


another_function(my_function)
another_function(second_function)


class A:
    def print(self):
        print("my class is A")


def fake_print(self):
    print("my class is not A")


a = A()
a.print()
# a.print = fake_print
# a.print()


print('--------')
A.print = fake_print
a.print()
a1 = A()
a1.print()


class testMOD(object):
    def testFunc(self, variable):
        var = variable
        self.something = var + 12
        print('Original:', self.something)


def alternativeFunc2(self, variable):
    var = variable
    self.something = var + 1.2
    print('Alternative2:', self.something)


mytest2 = testMOD()
mytest2.testFunc(10)  # Original: 22

testMOD.testFunc = alternativeFunc2
mytest2.testFunc(10)  # Alternative2: 11.2
mytestX = testMOD()
mytestX.testFunc(10)  # Alternative2: 11.2

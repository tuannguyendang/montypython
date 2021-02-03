def setup_module(module):
    print("setting up MODULE {0}".format(module.__name__))


def teardown_module(module):
    print("tearing down MODULE {0}".format(module.__name__))


def test_a_function():
    print("RUNNING TEST FUNCTION")


class BaseTest:
    def setup_class(cls):
        print("setting up CLASS {0}".format(cls.__name__))

    def teardown_class(cls):
        print("tearing down CLASS {0}\n".format(cls.__name__))

    def setup_method(self, method):
        print("setting up METHOD {0}".format(method.__name__))

    def teardown_method(self, method):
        print("tearing down  METHOD {0}".format(method.__name__))


class TestClass1(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 1-1")

    def test_method_2(self):
        print("RUNNING METHOD 1-2")


class TestClass2(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 2-1")

    def test_method_2(self):
        print("RUNNING METHOD 2-2")

# pytest test_pytest_setups.py -s

# test_pytest_setups.py setting up MODULE test_pytest_setups
# RUNNING TEST FUNCTION
# .setting up CLASS TestClass1
# setting up METHOD test_method_1
# RUNNING METHOD 1-1
# .tearing down  METHOD test_method_1
# setting up METHOD test_method_2
# RUNNING METHOD 1-2
# .tearing down  METHOD test_method_2
# tearing down CLASS TestClass1
#
# setting up CLASS TestClass2
# setting up METHOD test_method_1
# RUNNING METHOD 2-1
# .tearing down  METHOD test_method_1
# setting up METHOD test_method_2
# RUNNING METHOD 2-2
# .tearing down  METHOD test_method_2
# tearing down CLASS TestClass2
#
# tearing down MODULE test_pytest_setups

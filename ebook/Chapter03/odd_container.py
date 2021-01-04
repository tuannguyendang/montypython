from collections.abc import Container


class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True


odd_container = OddContainer()

print(isinstance(odd_container, Container))

print(issubclass(OddContainer, Container))

print(1 in odd_container)

print(2 in odd_container)

print(3 in odd_container)

print("a string" in odd_container)

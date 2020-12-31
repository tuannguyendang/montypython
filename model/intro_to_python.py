from services.abstract import Assignment


class IntroToPython:
    def lesson(self):
        return f"""Hello {self.student}. define two variables,
            an integer named a with value 1
            and a string named b with value 'hello'"""

    def check(self, code):
        return code == "a = 1\nb = 'hello'"

print("IntroToPython is Assignment subclass:", issubclass(IntroToPython, Assignment))
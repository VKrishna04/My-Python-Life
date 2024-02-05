import copy


class Main:
    def __init__(self, name):
        """
        Initialize the Main class with a name.

        Args:
            name (str): The name to assign to the Main instance.
        """
        self.name = name

    def __help(self):
        """
        Help function.
        """
        print("Help!")


M1 = Main("Hello")
M2 = copy.deepcopy(M1)
print(f"M1: {M1.name}")
print(f"M2: {M2.name}")
M2.name = "World"
print(f"M1: {M1.name}")
print(f"M2: {M2.name}")
# print(f"M1.__help: {M1._Main__help}")
print(f"{Main.dir()}")

# Create a class that collects two strings as input. Class should also contain a method that compares the lengths of two strings and displays which string is longest one. You can use string library functions. `__len()__` method can be used to find the length of a string.


class StringComparator:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def compare(self):
        len1 = len(self.string1)
        len2 = len(self.string2)

        if len1 > len2:
            print(f"'{self.string1}' is longer than '{self.string2}'")
        elif len1 < len2:
            print(f"'{self.string2}' is longer than '{self.string1}'")
        else:
            print("Both strings are of equal length")


# User inputs the strings
str1 = input("Please enter string 1 : ")
str2 = input("Please enter string 2 : ")
# Create an instance of StringComparator
comparator = StringComparator(str1, str2)
comparator.compare()

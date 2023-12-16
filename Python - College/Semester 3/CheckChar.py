# Check the type of character entered by the user.

char = input("Enter the character")

if char.isalpha():
    print(f"{char} is a lexicon character")
elif char.isalnum():
    print(f"{char} is a number")
elif char.isspace():
    print(f"{char} is a space.")

else:
    print(f"{char} is a special character.")

# Take all the possible tokens and make a list
# Check if each of the tokens contain any of these `Invalid characters are A, E, I, O, U, L, S, 0, 1 and 5`
# Print all the tokens which do not contain these invalid characters
print(
    "Please enter all the tokens in successive lines and please give a blank token to end the input sequence"
)
invalid_characters = ["A", "E", "I", "O", "U", "L", "S", "0", "1", "5"]
tokens = []
validTokens = []
while True:
    token = input()
    if token == "":
        break
    tokens.append(token)

for token in tokens:
    if all(char not in token for char in invalid_characters):
        validTokens.append(token)

print("Printing Valid Tokens: ")
if len(validTokens) == 0:
    print("There are no valid tokens")
else:
    for token in validTokens:
        print(token)

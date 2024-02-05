class Main:
    name = "Hello"


print(Main.name)
c = int(input("Enter the temperature in Celsius "))
f = (c * 9 / 5) + 32
assert f >= 99, "Fever is there"
print("Temperature in Fahrenheit = ", f)

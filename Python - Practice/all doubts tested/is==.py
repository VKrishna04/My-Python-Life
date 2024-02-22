a=3
b=3
print(a is b)  # True
print(a == b)  # True

a+=1
print(a is b)  # False
print(a == b)  # False

a = b = [1, 2, 3]
b.append(4)

print(a is b)  # True
print(a == b)  # False

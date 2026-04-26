# == checks whether two objects have the same value. is checks whether two variables point to the same object in memory.

# a = [1, 2, 3]
# b = a  # b points to the same list object as a
# print(id(a))
# print(id(b))
# print(a == b)  # Output: True (values are the same)
# print(a is b)  # Output: True (both variables point to the same object)

# c = [1, 2, 3]  # c is a new list object with the same values as a
# print(id(c))
# print(a == c)  # Output: True (values are the same)
# print(a is c)  # Output: False (a and c are different objects in memory)    


string1 = "Hello"
string2 = "Hello"
print(id(string1))
print(id(string2))
print(string1 == string2)  # Output: True (values are the same)
print(string1 is string2)  # Output: True (string literals are interned by Python, so they point to the same object in memory)
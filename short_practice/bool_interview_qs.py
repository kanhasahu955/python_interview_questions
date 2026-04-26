print(bool(print("Hello")))  # Output: Hello, returns None, which is False
print(bool(0))  # Output: False
print(bool(1))  # Output: True
print(bool(""))  # Output: False
print(bool("Hello"))  # Output: True
print(bool([]))  # Output: False
print(bool([1, 2, 3]))  # Output: True
print(bool(None))  # Output: False
print(bool(False))  # Output: False
print(bool(True))  # Output: True   
print(bool(()))  # Output: False
print(bool((1, 2, 3)))  # Output: True
print(bool({}))  # Output: False
print(bool({'key': 'value'}))  # Output: True

print(bool(0.0))  # Output: False
print(bool(0j))  # Output: False
print(bool(0.1))  # Output: True
print(bool(1e-10))  # Output: True

print(bool(set()))  # Output: False
print(bool({1, 2, 3}))  # Output: True

print(bool(range(0)))  # Output: False
print(bool(range(1)))  # Output: True   

print(bool(object()))  # Output: True (every object is considered True)
print(bool(type))  # Output: True (the type class is also considered True)

print(bool(float('nan')))  # Output: True (NaN is considered True in Python)
print(bool(float('inf')))  # Output: True (infinity is considered True in Python)
print(bool(float('-inf')))  # Output: True (negative infinity is considered True in Python)
print(bool(float('nan') == float('nan')))  # Output: False (NaN is not equal to itself)

print(type(bool(0)))  # Output: <class 'bool'>, the type of the result is bool
print(type(print("Hello")))  # Output: <class 'NoneType'>, the type of the result is NoneType   
print(type(None))  # Output: <class 'NoneType'>, the type of None is NoneType
print(bool(None))  # Output: False, None is considered False in a boolean context



# dict ={
#     '__init__': lambda self, name, age: setattr(self, 'name', name) or setattr(self, 'age', age),
#     'greeting': lambda self: f'Hi, I am {self.name}. I am {self.age} year old.'
# }

# Person = type('Person', (object,), dict)
# person1 = Person('Alice', 30)
# print(person1.greeting())  # Output: Hi, I am Alice. I am 30 year old.



dict = {
    'name':'ashok sahu',
    'age': 30,
}

print([ key for key in dict ])
print([ value for value in dict.values() ])
print([ key for key in dict.keys() ])
print([ (key, value) for key, value in dict.items() ])

print('name' in dict)  # Output: True
print('age' in dict)   # Output: True
print('gender' in dict)  # Output: False

print('name' not in dict)  # Output: False
print('age' not in dict)   # Output: False
print('gender' not in dict)  # Output: True

print('name' in dict.keys())  # Output: True
print('age' in dict.keys())   # Output: True
print('gender' in dict.keys())  # Output: False

print('name' in dict.values())  # Output: False
print('ashok sahu' in dict.values())  # Output: True
print(30 in dict.values())  # Output: True
print('gender' in dict.values())  # Output: False

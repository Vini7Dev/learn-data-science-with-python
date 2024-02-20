# Chapter 4 - Introduction to Python

### Numbers and Operators

```python
# Arithmetic Operators

4 + 4.2

4 - 3

3 * 3.5

4 / 2

4 // 2

3 ** 2

10 % 2

# Type

type(5) # Returns: <class 'int'>

## Type conversion

float(9) # Returns: 9.0

int(2.5) # Returns: 2

str(10) # Returns: '10'

bool(1) # Returns: True

# Bexadecimal and Binary

hex(394) # Returns: '0x18a'

bin(390) # Returns: '0b110000110'

# Other functions

abs(-8) # Returns: 8

round(3.14151922, 2) # Returns: 3.14

pow(4, 2) # Returns: 16

```

### Variables

```python
# Variables

variable = 1

print(variable)

type(variable) # Returns: <class 'int'>

variable = 1.5 # Dynamic type

type(variable) # Returns: <class 'float'>

# Multiple Declaration

person1, person2, person3 = 'John', 'Jane', 'Joe'

fruit1, fruit2, fruit3 = 'Watermelon'

```

### Strings and Indexing

```python
# Strings

'Hello World!'
"Hello 'World'!"

# Print String

print('Hello World!')

# Indexing Strings

name = 'John Doe'

print('name', name)

print('name[1]', name[1])

print('name[2:]', name[2:])

print('name[:4]', name[:4])

print('name[-1]', name[-1])

print('name[:-1]', name[:-1])

print('name[1::]', name[1::])

print('name[::2]', name[:2:])

# String Properties

name = 'John'

name[0] = 'Z' # ERROR, it's not possible

name = name + ' Doe'

name * 3

# Built-in Functions

name = 'John Doe'

name.upper()

name.lower()

name.split()

name.split(' ')

# String Functions

name = 'John doe'

name.capitalize()

name.count('o')

name.isalnum()

name.islower()

name.isspace()

name.endswith('a')

# Comparing Strings

'John' == 'Jane'

```

### Data Structure: Lists

```python
# Working with Lists

persons = ['John', 'Jane', 'Joe']

type(persons) # Returns: <class 'list'>

different_types = [10, 'Home', 1.5]

item0 = different_types[0]

print(item0)

# Updating List Item

different_types[1] = 'Door'

# Deleting List Item

del different_types[2]

# List of Lists

lists = [[0, 1, 2], [3, 4, 5]]

list_0 = lists[0]

list_0_1 = list_0[1]

list_1_0 = list[1][0]

# Concatenate List

list_0 = [0, 1, 2]

list_1 = [3, 4, 5]

list_0 + list_1

# Operator IN

operation_values = [100, 8, -5, 4.5]

print(10 in operation_values)

print(100 in operation_values)

# Built-in Functions

numbers = [10, 20, -30, 20]

len(numbers)

max(numbers)

min(numbers)

numbers.append(50)

numbers.count(20)

new_numbers = []

for number in numbers:
  new_numbers.append(number)

cities = ['Franca', 'São Paulo']

cities.extend('Rio de Janeiro', 'Recife')

cities.index('São Paulo')

cities.index('Rifaina')

cities.insert(1, 'Paulo São')

cities.remove(2)

cities.reverse()

numbers = [5, 4, 3, 2, 1, 0]

numbers.sort()

```

### Data Structure: Dictionaries

```python
# Working with Dictionaries

studants_dic = { 'John': 19, 'Jane': 20, 'Joe': 23}

studants_dic['John']

studants_dic['Any'] = 21

studants_dic.clear()

del studants_dic

len(studants_dic)

studants_dic.keys()

studants_dic.values()

studants_dic.items()

studants_dic2 = { 'Mike': 25 }

studants_dic.update(studants_dic2)

# Dictionary of Lists

dictionary = { 'key1': 1230, 'key2': [0, 1, 2, 3] }

dictionary['key2'][1] += 2

# Aligned Dictionaries

aligned_dictionaries = { 'key1': { 'key1_1': 0, 'key1_2': 1 } }

aligned_dictionaries['key1']['key2']

```

### Data Structure: Tuples (Immutable)

```python
# Working with Tuples

tuple1 = ('John', 42, False, 1.5)

len(tuple1)

tuple1[0]

tuple1[1:]

tuple1.index(False)

list1 = list(tuple1)

list1['John'] = 'Jane'

tuple1 = tuple(list1)

```

### Exercises

```python
# Exercise 1 - Print the numbers 1 to 10 on the screen. Use a list to store the numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)

# Exercise 2 - Create a list of 5 objects and print it on the screen

objects = [{ 'name': 'John' }, { 'name': 'Jane' }, { 'name': 'Joe' }, { 'name': 'Mia' }, { 'name': 'Alice' }]

print(objects)

# Exercise 3 - Create two strings and concatenate the two into a third string

str1 = 'Hello '
str2 = 'World!'
str3 = str1 + str2
str3

# Exercise 4 - Create a tuple with the following elements: 1, 2, 2, 3, 4, 4, 4, 5 and then use the count function
# tuple object to check how many times the number 4 appears in the tuple

numbers_tuple = (1, 2, 2, 3, 4, 4, 4, 5)

numbers_tuple.count(4)

# Exercise 5 - Create an empty dictionary and print it on the screen

dictionary = {}

print(dictionary)

# Exercise 6 - Create a dictionary with 3 keys and 3 values and print it on the screen

dictionary = { 'name': 'John', 'age': 20, 'gender': 'M' }

print(dictionary)

# Exercise 7 - Add one more element to the dictionary created in the previous exercise and print it on the screen

dictionary['document'] = '123.456.789-00'

print(dictionary)

# Exercise 8 - Create a dictionary with 3 keys and 3 values.
# One of the values must be a list of 2 numeric elements.
# Print the dictionary on the screen.

order = { 'id': 1001, 'costumer': 'johndoe@mail.com', 'totals': [10, -5] }

print(order)

# Exercise 9 - Create a list of 4 elements. The first element must be a string,
# the second a tuple of 2 elements, the third a dictionary with 2 keys and 2 values and
# the fourth element is a float value.
# Print the list.

elements = ['John', (0, 1), { 'id': 102, 'name': 'Phone' }, 2.5]

print(elements)

# Exercise 10 - Consider the string below. Print only characters from position 1 to 18 on the screen.

phrase = 'Cientista de Dados é o profissional mais sexy do século XXI'

print(phrase[1:18])

```

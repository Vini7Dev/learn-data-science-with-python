# Chapter 5 - Loops, Conditionals, Methods and Functions

### Conditionals

```python
# Conditionals

value = 5

if value > 5:
  print('Result A')
elif value == 5:
  print('Result B')
else:
  print('Result C')

if 2 < 10:
  if 2 > 5:
    print('Result A')
  else:
    print('Result B')
else:
  print('Result C')

if 2 < 10 and 2 > 5:
  print('Result A')
elif (2 > 10) & (2 < 5):
  print('Result B')
elif ((2 > 10) or (2 < 5)) and 2 != 3:
  print('Result C')
elif (2 > 10 | 2 < 5) & 2 == 3:
  print('Result D')
else:
  print('Result E')

if not(2 < 10):
  print('Result A')
else:
  print('Result B')

```

### Loops

```python
# For Loop

tupleExample = (2, 3, 4)

for i in tupleExample:
  print(i)

for count in range(0, 5):
  print(count)

strings = ['John', 'Doe']

for item in strings:
  print(item)

for num in range(0, 10):
  if num % 2 == 0:
    print(num)

for num in range(0, 10, 2):
  print(num)

chars = 'Hello World!'

for char in chars:
  print(char)

numbers = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
]

for i in numbers:
  print(i)
  for j in i:
    print(j)

dictionary = { 'name': 'John Doe', 'city': 'Franca' }

for key in dictionary:
  print(dictionary[key])

for key,value in dictionary.items():
  print(key, value)

# While Loop

count = 0

while(count < 10):
  if count == 5:
    break
  elif count > 5:
    continue
  else:
    pass
  print(count)
  count += 1
else:
  print('Finished!')

for num in range(2, 100):
  result = True
  for div in range(2, num):
    if num % div == 0:
      result = False
      break
  if result:
    print(num)

```

### Methods

```python
# Methods

myList = [11, 7, -1, 12, 65, 0]

type(myList)

myList

myList.append(7)

myList.count(7)

help(myList.count)

dir(myList)

phrase = "Hello, World!"

type(phrase)

phrase

print(phrase.split())
```

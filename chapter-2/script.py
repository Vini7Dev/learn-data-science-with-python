numbers = list(range(1, 101))

print(type(numbers))

for number in numbers:
  if number % 2 == 0 and number % 4 == 0:
    print(number)

print('=======================================')

result = [number for number in numbers if number % 2 == 0 and number % 4 == 0]

print(result)

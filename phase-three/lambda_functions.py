square = lambda x: x ** 2 # A lambda function that squares a number
print(square(5))  # 25

add = lambda x, y: x + y # A lambda function that adds two numbers
print(add(3, 5))  # 8

# Often used with the map(), filter(), sorted() and reduce() functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

sorted_numbers = sorted(numbers, key=lambda x: x % 2)
print(sorted_numbers)  # [1, 3, 5, 2, 4]

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
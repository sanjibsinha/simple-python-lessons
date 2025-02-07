'''
**Functions**
   - Defining functions with `def`.
   - Arguments and return values.
   - Understanding scope (local vs global).
   - Lambda functions (brief intro).

'''

# defining a function
def greet(name): # name is a parameter (input to the function)
    print(f"Hello, {name}!") # body of the function
    
# calling or invoking the function
greet("Alice") # "Alice" is an argument (value passed to the function)
greet("Bob") # "Bob" is an argument

def add(a, b):
    result = a + b
    return result # return value

sum_of_two_numbers = add(2, 3)
print(f"Sum of 2 and 3 is {sum_of_two_numbers}")
    
# get the user's name
name = input("Please enter your name: ")

# get the user's age
try:
    age = int(input("Please enter your age: "))
    print(f"Hello {name}, you are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a number for your age.")

# greet the user
print(f"Hello {name}, you are {age} years old.")
print("Hello, " + name + "!")
print(f"Hello, {name}!")
print("Hello, {}!".format(name))
print("You are " + str(age) + " years old.")

# check if the user is a teenager
if 13 <= age <= 19:
    print("You are a teenager.")    
else:
    print("You are not a teenager.")

is_teenager = 13 <= age <= 19
if is_teenager:
    print("You are a teenager.")
else:
    print("You are not a teenager.")

# calculate the age of the user in 10 years
age_in_10_years = age + 10
print(f"You will be {age_in_10_years} years old in 10 years.")
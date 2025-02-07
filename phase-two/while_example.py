count = 0

while count < 5:
    print(count)
    count = count + 1

# Example with user input
name = input("Enter your name: ")

while name != "quit":
    # print("Hello, " + name + "!")
    print(f"Hello, {name}!")
    name = input("Enter your name: ")
    if name == "quit":
        break



# Teach Yourself Error Handling in Python with AI Agents

## Original Prompt to AI Agents

Act as a senior developer and please teach me Python considering I am a layman who wants to start learning Python from scratch. 
However, I want to learn all the key concepts that will help me to build my personal projects with your guidabce.
These projects should not be very complex but could range from small to medium size as long as complexity is concerned. 
Moreover, I would like you to move your lessons from less complex to medium to advanced concepts by creating a Python app so that I can learn to implement my knowledge instantly. 
The whole lesson could be big, that is not an issue but I would like you to cover everything that is available in Python documentation. 
So today teach me the following concepts with examples and explanations.

**Error Handling**
   - Using `try`, `except` blocks for exception handling.
   - Catching specific exceptions.
   - Raising exceptions manually.
   
After that build a small application based on today's lesson.

========== End of Prompt ==============


========= Gemii 2.0 Output ==========

I'm excited to guide you on your Python learning journey. It's fantastic that you're starting from scratch and aiming to build your own projects. Python is an excellent choice for that!

We'll take a practical approach, moving from fundamental to more advanced concepts, and building a Python application step-by-step. Today, we'll focus on **Error Handling**. This is a crucial aspect of programming that makes your applications robust and user-friendly.

Let's dive into the concepts first, and then we'll build a small application to solidify your understanding.

### **Error Handling in Python**

In programming, errors are inevitable. They can occur for various reasons: invalid user input, network issues, file not found, division by zero, and many more.  Without proper handling, these errors can crash your program or lead to unexpected behavior. Error handling is the process of anticipating and gracefully managing these errors.

In Python, errors are called **exceptions**. Python provides a robust mechanism to handle these exceptions using `try`, `except`, `else`, and `finally` blocks. Today, we'll focus on `try` and `except` blocks, and raising exceptions.

#### **1. Using `try` and `except` Blocks for Exception Handling**

The fundamental structure for error handling in Python is the `try...except` block.

*   **`try` block**:  This block encloses the code that might potentially raise an exception. Think of it as saying, "Try to execute this code, and if something goes wrong..."
*   **`except` block**: This block specifies how to handle the exception if one occurs within the `try` block. It's like saying, "...if an error occurs, handle it in this way."

Here's the basic syntax:

```python
try:
    # Code that might raise an exception
    # ...
except:
    # Code to handle the exception
    # ...
```

**Example:** Let's consider a simple scenario where we try to divide a number by another number provided by the user. Division by zero is a common error.

```python
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except:
    print("Error: Division by zero is not allowed!")
```

**Explanation:**

1.  We use `try:` to start a block where we anticipate a potential error.
2.  Inside the `try` block, we take two integer inputs from the user and perform division.
3.  If the user enters `0` as the denominator, a `ZeroDivisionError` will occur.
4.  The `except:` block immediately follows the `try` block. If *any* exception occurs in the `try` block, the code inside the `except` block is executed. In this case, we print an error message.
5.  If no exception occurs in the `try` block, the `except` block is skipped, and the program continues normally.

**Try running this code and test it with different inputs, including dividing by zero.**

#### **2. Catching Specific Exceptions**

In the previous example, the `except:` block was very general. It would catch any type of exception. However, it's often better to catch specific exceptions so you can handle different errors in different ways.

Python has various built-in exception types. Some common ones include:

*   `ValueError`: Raised when a function receives an argument of the correct type but an inappropriate value (e.g., trying to convert a non-numeric string to an integer).
*   `TypeError`: Raised when an operation or function is applied to an object of inappropriate type (e.g., adding a string to an integer).
*   `FileNotFoundError`: Raised when a file or directory is requested but cannot be found.
*   `ZeroDivisionError`: Raised when the second operand of division or modulo operation is zero.
*   `IndexError`: Raised when trying to access an index that is out of range for a sequence (like a list or string).
*   `KeyError`: Raised when trying to access a key that is not found in a dictionary.

You can catch specific exceptions by specifying the exception type after the `except` keyword:

```python
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
```

**Explanation:**

1.  Now we have two `except` blocks.
2.  `except ZeroDivisionError:` will only catch `ZeroDivisionError` exceptions. If a `ZeroDivisionError` occurs, the first error message is printed.
3.  `except ValueError:` will only catch `ValueError` exceptions. If a `ValueError` occurs (e.g., if the user enters text instead of a number when prompted for input), the second error message is printed.
4.  If any other type of exception occurs, it will not be caught by these specific `except` blocks and might cause the program to crash (if not handled elsewhere).

**Try running this code and test it with:**

*   Dividing by zero.
*   Entering text when asked for a number.
*   Entering valid numbers.

You can have multiple `except` blocks to handle different types of exceptions. This makes your error handling more precise and allows you to provide more informative error messages or take different actions based on the type of error.

#### **3. Raising Exceptions Manually**

Sometimes, you might want to raise exceptions explicitly in your code. This is useful when you detect a condition that your program cannot handle or should not proceed with. You can use the `raise` keyword to raise an exception.

```python
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return number ** 0.5

try:
    num = float(input("Enter a number to calculate its square root: "))
    sqrt_result = calculate_square_root(num)
    print("Square root:", sqrt_result)
except ValueError as e:
    print("Error:", e)
```

**Explanation:**

1.  We define a function `calculate_square_root` that should calculate the square root of a number.
2.  Inside the function, we check if the input `number` is negative.
3.  If `number` is negative, we use `raise ValueError("Cannot calculate square root of a negative number.")` to manually raise a `ValueError` exception. The string in parentheses is the error message associated with the exception.
4.  In the main part of the code, we call `calculate_square_root` within a `try` block.
5.  We use `except ValueError as e:` to catch specifically `ValueError` exceptions. The `as e` part is optional but useful; it assigns the exception object to the variable `e`, allowing you to access the error message (e.g., `e` in our `print` statement).
6.  If a `ValueError` is raised (because the input was negative), the `except` block will execute, and the error message will be printed.

**Try running this code with:**

*   A positive number.
*   A negative number.
*   Text input (to see how it interacts with the outer `try-except` for `ValueError` from `float()` if you enter non-numeric text).

Raising exceptions manually is a good practice to signal errors or invalid states in your program, making it more robust and easier to debug.

### **Small Application: Simple Command-Line Calculator with Error Handling**

Now, let's build a very basic command-line calculator that demonstrates error handling. This calculator will perform addition, subtraction, multiplication, and division. We'll incorporate error handling to manage invalid inputs and division by zero.

Here's the plan for our calculator app:

1.  **Get user input:** Ask the user to enter two numbers and an operation (+, -, \*, /).
2.  **Perform calculation:** Based on the operation, perform the calculation.
3.  **Handle errors:**
    *   Use `try-except` to catch `ValueError` if the user enters non-numeric input for numbers.
    *   Use `try-except` to catch `ZeroDivisionError` if the user tries to divide by zero.
    *   Handle invalid operation input.
4.  **Display result or error message.**

Here's the Python code for our simple calculator:

```python
def simple_calculator():
    while True: # Keep the calculator running until the user quits
        print("\nSimple Calculator")
        print("Operations: +, -, *, /, quit")

        operation = input("Enter operation: ")
        if operation == 'quit':
            print("Exiting calculator.")
            break # Exit the loop, thus ending the calculator

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please choose from +, -, *, / or quit.")
            continue # Go to the next iteration of the loop

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2 # Potential ZeroDivisionError here

            print("Result:", result)

        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e: # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}") # Print the error message for debugging
            print("Please try again.")

if __name__ == "__main__":
    simple_calculator()
```

**Explanation of the Calculator App:**

1.  **`simple_calculator()` function:** Encapsulates the calculator logic.
2.  **`while True:` loop:**  Creates a loop so the calculator keeps running until the user explicitly enters 'quit'.
3.  **Operation Input:** Prompts the user to enter an operation.
4.  **Quit Condition:** If the user enters 'quit', the loop breaks, and the program exits.
5.  **Operation Validation:** Checks if the entered operation is valid (+, -, \*, /). If not, it prints an error message and continues to the next iteration of the loop.
6.  **`try` block:** Encloses the number input and calculation part, where potential `ValueError` (from `float()`) and `ZeroDivisionError` might occur.
7.  **Number Input:** Takes two numbers as input from the user, converting them to floats to handle decimal numbers.
8.  **Calculation:** Performs the selected operation based on the user's input.
9.  **`except ValueError:`:** Catches `ValueError` if the user enters non-numeric input when asked for numbers.
10. **`except ZeroDivisionError:`:** Catches `ZeroDivisionError` if division by zero is attempted.
11. **`except Exception as e:`:** This is a general exception handler. It catches any other type of exception that might occur (that we haven't specifically handled). It's good practice to include a general exception handler to catch unexpected errors and prevent the program from crashing abruptly. We also print the exception message `e` for debugging purposes.
12. **`if __name__ == "__main__":`:** This standard Python construct ensures that the `simple_calculator()` function is called only when the script is run directly (not when it's imported as a module).

**How to run this code:**

1.  Save the code in a file named `calculator.py`.
2.  Open a command prompt or terminal.
3.  Navigate to the directory where you saved `calculator.py`.
4.  Run the script using the command: `python calculator.py`
5.  Follow the prompts to use the calculator.

**Experiment and Test:**

*   Run the calculator and try different operations and numbers.
*   Test error conditions:
    *   Try to divide by zero.
    *   Enter text instead of numbers.
    *   Enter an invalid operation.

**Key Takeaways from Today's Lesson:**

*   Error handling is essential for writing robust Python programs.
*   `try...except` blocks are used to handle exceptions.
*   You can catch specific exception types for more precise error management.
*   You can manually raise exceptions using the `raise` keyword to signal errors in your code.
*   Error handling makes your applications more user-friendly and easier to debug.

This is just the beginning of your Python journey! Error handling is a fundamental concept, and mastering it will significantly improve the quality of your code. In our next lessons, we'll build upon these basics and explore more exciting Python concepts and projects.

Feel free to experiment with the calculator app, modify it, and try to add more features or error handling scenarios. If you have any questions or want to explore specific aspects in more detail, please ask! Let me know when you are ready to move to the next lesson.

=========== End of Gemini==============

=========== ChatGPT Output =====================

Absolutely! I’m excited to help you get started with Python and guide you on your journey to building practical projects. Let’s dive into the first lesson of error handling in Python.

### **Error Handling in Python**

Error handling is a crucial skill in programming. It helps you deal with unexpected situations in your code, ensuring your program doesn't crash when something goes wrong. In Python, this is primarily done using `try`, `except`, `else`, and `finally` blocks.

### **1. Using `try`, `except` blocks for exception handling**

The basic structure for error handling in Python is as follows:

```python
try:
    # Code that may raise an exception
    risky_code = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handling the exception
    print("You can't divide by zero!")
```

#### How it works:
- The code inside the `try` block is executed.
- If an exception occurs (like dividing by zero), Python jumps to the `except` block.
- The `except` block handles the error, and the program continues executing afterward.

#### Example: Dividing numbers with error handling

```python
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
    except TypeError:
        print("Error: Both inputs must be numbers!")
        
divide_numbers(10, 2)  # No error
divide_numbers(10, 0)  # Will print error
divide_numbers(10, "a")  # Will print error
```

### **2. Catching specific exceptions**

You can catch specific types of exceptions using `except` followed by the exception type. This is useful when you want to handle different errors differently.

Here’s an example of catching specific exceptions:

```python
try:
    num = int(input("Enter a number: "))
    print(f"Number is {num}")
except ValueError:
    print("Error: That's not a valid number!")
except KeyboardInterrupt:
    print("\nError: You interrupted the program!")
```

- **ValueError**: Raised if the user doesn’t enter a number.
- **KeyboardInterrupt**: Raised if the user presses Ctrl+C to interrupt the program.

### **3. Raising exceptions manually (`raise`)**

You can raise exceptions manually using the `raise` keyword. This allows you to enforce rules in your code, such as validating input or signaling an error when certain conditions are met.

```python
def validate_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old!")
    print(f"Age {age} is valid.")

try:
    validate_age(15)
except ValueError as e:
    print(f"Error: {e}")
```

- In the code above, `raise ValueError` forces an exception if the age is below 18.

### **4. `else` and `finally` blocks**

- **`else` block**: If no exceptions occur in the `try` block, the code in the `else` block runs.
- **`finally` block**: This block is always executed, regardless of whether an exception occurred or not. It's useful for cleanup tasks, such as closing files or releasing resources.

Example:

```python
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print(f"The result is: {result}")
    finally:
        print("This block always runs!")

divide_numbers(10, 2)
divide_numbers(10, 0)
```

### **Putting it all together: Building a Small Application**

Let’s build a simple Python app where users can input two numbers and perform division, handling errors along the way. We’ll include:
- User input validation.
- Handling division by zero.
- Ensuring valid numeric input.

Here's the app:

```python
def get_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            # Try to convert input into a number
            return float(user_input)
        except ValueError:
            print("That's not a valid number! Please enter a number.")

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: You can't divide by zero!"
    else:
        return f"The result of {a} divided by {b} is {result}"
    finally:
        print("Thank you for using the division tool.")

def main():
    print("Welcome to the Division App!")
    
    num1 = get_input("Enter the first number: ")
    num2 = get_input("Enter the second number: ")

    result = divide_numbers(num1, num2)
    print(result)

# Run the application
if __name__ == "__main__":
    main()
```

#### How the app works:
- **Input Validation**: The `get_input()` function ensures the user enters a valid number.
- **Error Handling**: The `divide_numbers()` function handles division errors (like dividing by zero).
- **Final Cleanup**: The `finally` block is used to thank the user, regardless of success or failure.

### **Breakdown of the Application:**
- **User Input**: We repeatedly ask the user for input until they enter a valid number (`get_input()`).
- **Division**: We perform the division in `divide_numbers()`, where we handle errors such as dividing by zero.
- **Flow Control**: We use `else` to ensure the result is printed if no error occurs, and `finally` to execute any cleanup code.

### **Conclusion**
Error handling is a crucial skill in any programming language. By using `try`, `except`, `else`, `finally`, and `raise`, you can ensure your programs are more robust and user-friendly, even when things go wrong.

In this lesson, you've learned:
- How to use `try`, `except`, and catch specific exceptions.
- How to raise exceptions manually with `raise`.
- How to clean up with `finally`.
- How to build a small application that uses error handling for user input and division.

---

Let me know if you'd like any clarifications on the concepts or if you'd like to move to the next lesson!

=========== End of ChatGPT  ===============


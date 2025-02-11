### 1. **Reading and Writing Text Files**
In Python, you can read from and write to text files using built-in functions. Here's a simple introduction to working with text files.

#### **Reading from a Text File**
You can open a file and read its content using the `open()` function. The function returns a file object, which you can use to perform operations on the file.

**Example:**

```python
# Opening a file in read mode ('r')
file = open("example.txt", "r")

# Reading the contents of the file
content = file.read()
print(content)

# Closing the file after use
file.close()
```

This code will open a file named `example.txt` and print its content to the screen.

**Important Notes:**
- You should always close the file after you're done using it to free up system resources.
- If the file doesn't exist, you will get a `FileNotFoundError`.

#### **Writing to a Text File**
You can write to a text file using the `open()` function in write mode (`'w'`).

**Example:**

```python
# Opening a file in write mode ('w')
file = open("example.txt", "w")

# Writing text to the file
file.write("Hello, world!\nWelcome to Python.")

# Closing the file after writing
file.close()
```

- **Write Mode ('w')**: If the file doesn't exist, it will create a new one. If it exists, it will overwrite the existing content.
- **Append Mode ('a')**: If you want to add content to an existing file without overwriting it, you can use `'a'` mode.

**Example of Appending:**

```python
# Opening a file in append mode ('a')
file = open("example.txt", "a")

# Appending text to the file
file.write("\nThis is a new line of text.")

# Closing the file
file.close()
```

---

### 2. **Using Context Managers (`with` statement)**
In Python, it's common to use the `with` statement to manage file operations. It ensures that the file is properly closed after the block of code inside the `with` statement is executed, even if an error occurs during the process.

**Example:**

```python
# Using the 'with' statement
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

Here, the file is automatically closed after the code block inside the `with` statement finishes execution, even if there’s an exception.

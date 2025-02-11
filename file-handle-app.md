Let's learn **file handling** in Python from the ground up. By the end of this lesson, you'll be able to read from and write to text files, work with CSV and JSON files, and understand how to use context managers with the `with` statement. After that, we'll use this knowledge to build a small application together.

Let's break it down step by step:

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

---

### 3. **Working with CSV Files**
CSV (Comma-Separated Values) files are often used to store tabular data. Python provides the `csv` module to work with these files.

#### **Reading CSV Files**

```python
import csv

# Opening the CSV file in read mode
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of values
```

#### **Writing to CSV Files**

```python
import csv

# Data to be written to the CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
]

# Opening the CSV file in write mode
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Writing multiple rows at once
```

- **`newline=""`** ensures that blank lines are not inserted between rows on some systems (e.g., Windows).

---

### 4. **Working with JSON Files**
JSON (JavaScript Object Notation) is a lightweight format for data exchange. Python provides the `json` module to work with JSON data.

#### **Reading JSON Files**

```python
import json

# Opening the JSON file in read mode
with open("data.json", "r") as file:
    data = json.load(file)  # Parse the JSON data into a Python dictionary
    print(data)
```

#### **Writing to JSON Files**

```python
import json

# Data to be written to the JSON file
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Opening the JSON file in write mode
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)  # Writing the data with pretty indentation
```

---

### **Building a Simple Application**
Now that we've covered how to read from and write to text, CSV, and JSON files, let's build a small Python application that handles user data. The app will:
1. Store user information in a CSV file.
2. Read the user information and display it.
3. Allow the user to save new information to the CSV file.

#### **Step-by-step Code Implementation**

```python
import csv
import json

# Function to add a new user
def add_user_to_csv(name, age, city):
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, city])

# Function to display all users from CSV
def display_users_from_csv():
    try:
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}")
    except FileNotFoundError:
        print("No users found.")

# Function to save user data to JSON file
def save_users_to_json():
    users = []
    try:
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                users.append({"name": row[0], "age": row[1], "city": row[2]})
    except FileNotFoundError:
        print("No users found.")
        return

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Function to load user data from JSON
def load_users_from_json():
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
            for user in users:
                print(f"Name: {user['name']}, Age: {user['age']}, City: {user['city']}")
    except FileNotFoundError:
        print("No users found.")

# Main Menu to interact with the program
def main():
    while True:
        print("\n--- User Data Management ---")
        print("1. Add user")
        print("2. Display users (CSV)")
        print("3. Save users to JSON")
        print("4. Load users from JSON")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            city = input("Enter city: ")
            add_user_to_csv(name, age, city)
            print("User added successfully.")
        
        elif choice == "2":
            display_users_from_csv()
        
        elif choice == "3":
            save_users_to_json()
            print("Users saved to JSON file.")
        
        elif choice == "4":
            load_users_from_json()
        
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### **How the Application Works:**
1. **Add User**: This option allows the user to add their name, age, and city to a CSV file (`users.csv`).
2. **Display Users (CSV)**: This displays all the users currently stored in the CSV file.
3. **Save Users to JSON**: This converts all the users in the CSV file into a JSON file (`users.json`).
4. **Load Users from JSON**: This loads and displays all users from the JSON file.
5. **Exit**: This exits the program.

### **Running the Application**:
- Run the Python script in your terminal.
- You can keep adding users, displaying them, and converting between CSV and JSON formats.

---

### **Summary of Concepts Covered:**
- **Reading/Writing Text Files**: Basic file I/O operations using `open()`.
- **Context Managers (`with` statement)**: Automatic resource management.
- **CSV Files**: Handling tabular data with the `csv` module.
- **JSON Files**: Handling structured data with the `json` module.
- **Building an App**: Combining these concepts into a small application to manage user data.

Let me know if you need further clarification or any additional help with this!

==================


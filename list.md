Let's start from the basics with **Collections in Python**, focusing on **Lists**, **Tuples**, and **Dictionaries**. These are essential data structures in Python, and understanding them will give you the foundation you need to work with data effectively in your projects.

### 1. **Lists**
A **list** is an ordered, mutable (changeable) collection of items. Lists are one of the most commonly used data structures in Python.

#### **List Basics:**
- **Creation**: You can create a list by placing elements inside square brackets `[]`.
- **Indexing**: Elements are accessed via their index, starting from `0`.
- **Slicing**: Allows you to extract a portion of the list.
- **Adding/Removing Elements**: Lists support operations like appending, removing, inserting, etc.

#### **Example**:
```python
# List creation
my_list = [1, 2, 3, 4, 5]

# Accessing elements by index
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5 (last element)

# Slicing
print(my_list[1:4])  # Output: [2, 3, 4]

# Adding elements
my_list.append(6)  # Adds 6 to the end
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Inserting elements at a specific position
my_list.insert(2, 10)  # Inserts 10 at index 2
print(my_list)  # Output: [1, 2, 10, 3, 4, 5, 6]

# Removing elements
my_list.remove(10)  # Removes the first occurrence of 10
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Popping an element (removes and returns it)
popped_element = my_list.pop(3)  # Removes element at index 3 (value 4)
print(popped_element)  # Output: 4
print(my_list)  # Output: [1, 2, 3, 5, 6]
```

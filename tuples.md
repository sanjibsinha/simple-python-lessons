### 2. **Tuples**
A **tuple** is similar to a list, but it is **immutable** (cannot be changed after creation). Tuples are used when you want to make sure the data cannot be altered.

#### **Tuple Basics:**
- **Creation**: Defined with parentheses `()`.
- **Immutability**: Once created, tuples cannot be modified (you cannot add, remove, or change elements).
- **Use Cases**: Use a tuple when you want to ensure that data stays constant (e.g., for fixed configurations, or as dictionary keys).

#### **Example**:
```python
# Tuple creation
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements by index
print(my_tuple[1])  # Output: 2
print(my_tuple[-1])  # Output: 5

# Slicing
print(my_tuple[2:4])  # Output: (3, 4)

# Tuples are immutable: the following will raise an error
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

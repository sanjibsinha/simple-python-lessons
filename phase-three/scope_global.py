def my_function():
    local_variable = 10
    print(local_variable)

my_function() # 10
# print(local_variable) # NameError: name 'local_variable' is not defined

global_variable = 20
print(global_variable)

def another_function():
    print(global_variable)

another_function() # 20

count = 0

def increment_count():
    global count # Declare count as a global variable
    count = count + 1
    print(count)

increment_count() # 1
increment_count() # 2
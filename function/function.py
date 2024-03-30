def sum (a, b):
    return a + b
print(sum(1, 2))

def subtract(a, b=2): # default value of b is 2
    return a - b

print(subtract(5))
print(subtract(5, 3))

# named arguments
def multiply(a, b):
    return a * b

# positional arguments and named arguments can be mixed in a function call
# named arguments must be after positional arguments d=2, a=3 is illigal

print(multiply(a=2, b=3)) # ligel to multiply(2, 3)
# print(multiply(b=3, 2)) # illigal


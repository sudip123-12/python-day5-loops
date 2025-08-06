# Day 6: Nested Loops & Functions Practice

# Star Pattern - Right-angled triangle
def right_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

# Star Pattern - Inverted triangle
def inverted_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

# Function to print square of a number
def square(num):
    return num * num

# Function to check even or odd
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Calling functions
right_triangle(4)
print()
inverted_triangle(4)
print("\nSquare of 5 is:", square(5))
print("7 is", even_or_odd(7))

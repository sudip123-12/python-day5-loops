# Day 5 - Python While Loop Practice by Sudip Sharma

# 1. Print numbers from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

print("\n")

# 2. Find the sum of first 100 natural numbers
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("Sum of first 100 natural numbers:", total)

print("\n")

# 3. Print the multiplication table of a given number
num = 5  # Change this as needed
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

print("\n")

# 4. Check if a number is prime or not
num = 29  # Change this as needed
i = 2
is_prime = True

while i <= num // 2:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if num <= 1:
    print(num, "is NOT a Prime number")
elif is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is NOT a Prime number")

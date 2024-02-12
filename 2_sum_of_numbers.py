"""This program outputs numbers 20 to 25 inclusive and their sum"""

# print numbers 20 - 25
number = 20
while number < 26:
    print(number)
    number += 1

# Calculate and print the sum
numbers = list(range(20, 26))
total_sum = sum(numbers)
print(f"Sum:", total_sum)

# given a positive integer, determine whether it is a narcissistic number.
# a number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
# for example, 153 has 3 digits, and 1"3 + 5"3 + 3"3 = 153, so it is narcissitic.

num = int(input("Enter a number: "))

# Convert number to string to count digits
num_digits = len(str(num))

# Calculate sum of digits raised to power
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** num_digits
    temp //= 10

# Check if narcissistic
if total == num:
    print(num, "is a narcissistic number")
else:
    print(num, "is not a narcissistic number")
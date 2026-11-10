# given a positive integer, determine whether it is a narcissistic number.
# a number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
# for example, 153 has 3 digits, and 1^3 + 5^3 + 3^3 = 153, so it is narcissistic.

def is_narcissistic(num):
    """Return True if num equals the sum of its digits, each raised to the number of digits."""
    # Convert number to string to count digits
    num_digits = len(str(num))

    # Calculate sum of digits raised to power
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10

    return total == num


def parse_number(text):
    """Convert text to a whole number that is 0 or greater.

    Raises ValueError with a user-facing message if the text is not valid.
    """
    text = text.strip()
    if not text:
        raise ValueError("Please enter a number.")
    try:
        num = int(text)
    except ValueError:
        raise ValueError("Please enter a whole number, e.g. 153.") from None
    if num < 0:
        raise ValueError("Please enter a whole number that is 0 or greater.")
    return num


def main():
    try:
        num = parse_number(input("Enter a number: "))
    except ValueError as error:
        print(error)
        return

    if is_narcissistic(num):
        print(num, "is a narcissistic number")
    else:
        print(num, "is not a narcissistic number")


if __name__ == "__main__":
    main()
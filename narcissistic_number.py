# given a positive integer, determine whether it is a narcissistic number.
# a number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
# for example, 153 has 3 digits, and 1^3 + 5^3 + 3^3 = 153, so it is narcissistic.

SUPERSCRIPTS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def digit_power_breakdown(num):
    """Show the sum of digit powers as text, e.g. 153 -> '1³ + 5³ + 3³ = 153'.

    num must be 0 or greater.
    """
    digits = str(num)
    power = len(digits)
    exponent = str(power).translate(SUPERSCRIPTS)
    terms = " + ".join(f"{digit}{exponent}" for digit in digits)
    total = sum(int(digit) ** power for digit in digits)
    return f"{terms} = {total}"


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


MAX_RANGE_LIMIT = 100_000


def find_narcissistic_numbers(limit):
    """Return every narcissistic number from 0 up to and including limit.

    Raises ValueError if limit is above MAX_RANGE_LIMIT.
    """
    if limit > MAX_RANGE_LIMIT:
        raise ValueError(
            f"Please enter {MAX_RANGE_LIMIT:,} or less to keep the search quick."
        )
    return [n for n in range(limit + 1) if is_narcissistic(n)]


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
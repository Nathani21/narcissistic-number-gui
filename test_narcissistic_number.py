import pytest

from narcissistic_number import digit_power_breakdown, is_narcissistic, parse_number


def test_single_digit_numbers_are_narcissistic():
    for n in range(10):
        assert is_narcissistic(n)


def test_three_digit_narcissistic_numbers():
    for n in (153, 370, 371, 407):
        assert is_narcissistic(n)


def test_four_digit_narcissistic_numbers():
    for n in (1634, 8208, 9474):
        assert is_narcissistic(n)


def test_larger_narcissistic_numbers():
    for n in (54748, 92727, 93084, 548834):
        assert is_narcissistic(n)


def test_non_narcissistic_numbers():
    for n in (10, 100, 152, 154, 9475):
        assert not is_narcissistic(n)


def test_no_two_digit_narcissistic_numbers():
    for n in range(10, 100):
        assert not is_narcissistic(n)


def test_all_narcissistic_numbers_below_10000():
    found = [n for n in range(10000) if is_narcissistic(n)]
    assert found == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]


def test_negative_numbers_are_not_narcissistic():
    for n in (-1, -153):
        assert not is_narcissistic(n)


def test_returns_a_bool():
    assert is_narcissistic(153) is True
    assert is_narcissistic(154) is False

def test_parse_number_accepts_digits():
    assert parse_number("153") == 153


def test_parse_number_strips_whitespace():
    assert parse_number("  153  ") == 153


def test_parse_number_accepts_zero():
    assert parse_number("0") == 0


def test_parse_number_rejects_empty_input():
    for text in ("", "   "):
        with pytest.raises(ValueError, match="enter a number"):
            parse_number(text)


def test_parse_number_rejects_non_numbers():
    for text in ("abc", "12a", "1.5"):
        with pytest.raises(ValueError, match="whole number"):
            parse_number(text)


def test_parse_number_rejects_negative_numbers():
    with pytest.raises(ValueError, match="0 or greater"):
        parse_number("-5")

def test_breakdown_for_narcissistic_numbers():
    assert digit_power_breakdown(153) == "1³ + 5³ + 3³ = 153"
    assert digit_power_breakdown(407) == "4³ + 0³ + 7³ = 407"
    assert digit_power_breakdown(9474) == "9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474"


def test_breakdown_for_non_narcissistic_numbers():
    assert digit_power_breakdown(154) == "1³ + 5³ + 4³ = 190"
    assert digit_power_breakdown(10) == "1² + 0² = 1"


def test_breakdown_for_single_digits():
    assert digit_power_breakdown(7) == "7¹ = 7"
    assert digit_power_breakdown(0) == "0¹ = 0"


def test_breakdown_total_agrees_with_is_narcissistic():
    for n in range(1000):
        total = int(digit_power_breakdown(n).split("= ")[1])
        assert (total == n) == is_narcissistic(n)
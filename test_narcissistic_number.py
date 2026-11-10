from narcissistic_number import is_narcissistic


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
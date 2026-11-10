# Narcissistic Number Checker

![Tests](https://github.com/Nathani21/narcissistic-number-gui/actions/workflows/tests.yml/badge.svg)

A small desktop app (Python and CustomTkinter) that checks whether a number is narcissistic, shows the working, and lists every narcissistic number up to a limit.

A number is narcissistic if the sum of its digits, each raised to the power of the number of digits, equals the number itself. For example, 153 has 3 digits and 1³ + 5³ + 3³ = 153.

## Features

- Check any whole number that is 0 or greater
- See the working, for example `1³ + 5³ + 3³ = 153`
- Find every narcissistic number up to a limit (up to 100,000)
- Friendly messages for invalid input instead of crashes
- Follows your system's light or dark theme

## Run it

Needs Python 3 (tested on 3.13).

```
git clone https://github.com/Nathani21/narcissistic-number-gui.git
cd narcissistic-number-gui
pip install -r requirements.txt
python narcissistic_gui.py
```

A console version is also included: `python narcissistic_number.py`

## How it works

- `narcissistic_number.py` holds the logic as plain functions: `is_narcissistic`, `digit_power_breakdown`, `find_narcissistic_numbers` and `parse_number` (input validation)
- `narcissistic_gui.py` is the window. It reads the input, calls those functions and shows the result or the error message
- Keeping the logic separate from the window is what makes it testable

## Tests

```
pip install pytest
python -m pytest
```

The tests cover the logic. The window itself is not covered. They also run automatically on every pull request through GitHub Actions.

## License

MIT, see [LICENSE](LICENSE).
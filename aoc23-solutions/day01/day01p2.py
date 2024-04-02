import sys
from typing import Iterable

word_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def find_digit(line: Iterable[str]) -> str:
    for c in line:
        if c.isdigit():
            return int(c)
    raise ValueError(f"No digits found in {line}.")

def get_value(line: str) -> int:
    return 10 * find_digit(line) + find_digit(reversed(line))

def main():
    print(sum(get_value(line) for line in sys.stdin))

if __name__ == "__main__":
    main()

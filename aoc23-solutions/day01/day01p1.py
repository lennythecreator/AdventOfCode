import sys
from typing import Iterable

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

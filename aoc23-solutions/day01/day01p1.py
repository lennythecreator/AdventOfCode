from typing import IO

def find_digit(start: int, stop: int, line: str, skip: int=1) -> str:
    for char in range(start, stop, skip):
        if line[char].isdigit():
            return line[char]
    return "0"

def main(line: str) -> int:
    size: int = len(line)
    str_number = find_digit(0, size, line) + find_digit(size - 1, -1, line, skip=-1)
    return int(str_number)

if __name__ == "__main__":
    inputs: IO[str] = open(file="input.txt", mode="r", encoding="utf-8").readlines()
    result: int = 0

    for line in inputs:
        result += main(line)

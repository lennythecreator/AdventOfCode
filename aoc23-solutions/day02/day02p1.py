from typing import IO

def is_possible(
    cubes: str,
    colors: dict
) -> bool:
    
    cubes_split = cubes.split(';')

    for _, cube in enumerate(cubes_split):
        cube_subset = cube.split(',')

        for subset in cube_subset:
            count, color = subset.strip().split(' ')
            if colors[color] < int(count):
                return False
    return True


def main(line: str) -> int:
    game, cubes = line.split(':')
    _, game_number = game.split(' ')

    if is_possible(
        cubes,
        { 'red' : 12, 'green' : 13, 'blue' : 14 }
    ):
        return int(game_number)
    return 0


if __name__ == "__main__":
    inputs: IO[str] = open(file="input.txt", mode="r", encoding="utf-8").readlines()
    result: int = 0

    for idx, line in enumerate(inputs):
        result += main(line)
    print(result)

# testing git hooks
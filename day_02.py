from lib import read, tee
from math import prod


def part_1(games: list[str]) -> int:
    reqs = (12, 13, 14)

    return sum(
        game_id(game)
        * all(is_allowed(reqs, handful) for handful in deserialize_handfuls(game))
        for game in games
    )


def part_2(games: list[str]) -> int:
    return sum(prod(min_cubes(deserialize_handfuls(game))) for game in games)


def game_id(s: str) -> int:
    return int(s.strip().split(":")[0].split(" ")[1])


def deserialize_handfuls(s: str) -> list[tuple[int, int, int]]:
    return [count_cubes(handful) for handful in s.strip().split(":")[1].split(";")]


def count_cubes(handful: str) -> tuple[int, int, int]:
    r, g, b = 0, 0, 0

    cubes = handful.strip().split(",")
    for cube_color in cubes:
        count = int(cube_color.strip().split(" ")[0])
        if "red" in cube_color:
            r = count
        elif "green" in cube_color:
            g = count
        elif "blue" in cube_color:
            b = count

    return (r, g, b)


def is_allowed(reqs: tuple[int, int, int], handful: tuple[int, int, int]) -> bool:
    for i, color in enumerate(handful):
        if reqs[i] < color:
            return False
    return True


def min_cubes(handfuls: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    return tuple(max(x) for x in zip(*handfuls))


if __name__ == "__main__":
    games = read("day_02.txt").strip().split("\n")

    print("Part 1")
    print(part_1(games))
    print()

    print("Part 2")
    print(part_2(games))
    print()

from lib import read, tee
from collections import namedtuple
from math import sqrt, prod


Race = namedtuple("Race", "time distance")

def part_1(races: list[Race]) -> int:
    return prod(win_states(quadratic(race.time, race.distance)) for race in races)

def part_2(race: Race) -> int:
    return win_states(quadratic(race.time, race.distance))


def quadratic(time: int, distance: int) -> tuple[float,float]:
    # Solves for the hold time to based on a given time limit and distance traveled.
    # Returns the two solutions as (+,-)

    a = -(time/2)
    b = sqrt(time**2 - 4*distance)/2

    return (-(a+b),-(a-b))

def win_states(bounds: tuple[float,float]) -> int:
    lower, upper = bounds

    states = int(upper)-int(lower)
    if upper == float(int(upper)):
        states -= 1

    return states

def parse_for_part_1(raw: str) -> list[Race]:
    rows = raw.strip().split("\n")
    times = [
        int(time.strip())
        for time in rows[0].strip().split(":")[1].strip().split(" ")
        if time != ""
    ]
    distances = [
        int(distance.strip())
        for distance in rows[1].strip().split(":")[1].strip().split(" ")
        if distance != ""
    ]

    races = []
    for race in zip(times, distances):
        races.append(Race(race[0], race[1]))

    return races

def parse_for_part_2(raw: str) -> Race:
    rows = raw.strip().split("\n")
    time = int("".join([
        time.strip()
        for time in rows[0].strip().split(":")[1].strip().split(" ")
        if time != ""
    ]))
    distance = int("".join([
        distance.strip()
        for distance in rows[1].strip().split(":")[1].strip().split(" ")
        if distance != ""
    ]))

    return Race(time, distance)


if __name__ == "__main__":
    puzzle_file = "day_06.txt"

    print("Day 1")
    print(part_1(parse_for_part_1(read(puzzle_file))))
    print()

    print("Day 2")
    print(part_2(parse_for_part_2(read(puzzle_file))))
    print()

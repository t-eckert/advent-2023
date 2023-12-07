from lib import read, tee
from collections import namedtuple


Translation = namedtuple("Translation", "destination_start source_start length")


class Map:
    def __init__(self, source: str, destination: str, translations: list[Translation]):
        self.source = source
        self.destination = destination
        self.translations = translations

    def __repr__(self) -> str:
        return f"{self.source}-to-{self.destination}: {len(self.translations)}"

    def append(self, translation: Translation):
        self.translations.append(translation)


Almanac = tuple[list[int], list[Map]]


def part_1(almanac: Almanac) -> int:
    field_1 = almanac[0]

    for mapping in almanac[1]:
        field_1 = translate_forwards(field_1, mapping.translations)

    print(field_1)

    field = almanac[0]

    locations = []
    for seed in field:
        for mapping in almanac[1]:
            x = seed
            for translation in mapping.translations:
                x = forward(x, translation)
            locations.append(x)
    print(field)
    print(min(field))

    return min(field_1)


def part_2(almanac: Almanac) -> int:
    seeds = [
        x + seed[0]
        for seed in chunk(almanac[0], 2)
        for x in range(seed[1])
    ]

    return 0


def parse_almanac(raw: list[str]) -> Almanac:
    seeds = [int(seed) for seed in raw[0].split(":")[1].strip().split(" ")]

    maps = []
    map_buffer = None
    for i, line in enumerate(raw[0:]):
        if "map" in line and map_buffer is None:
            source, destination = (
                x for x in line.split(" ")[0].strip().split("-") if x != "to"
            )
            map_buffer = Map(source, destination, [])
        elif (line == "" or i == len(raw[0:]) - 1) and map_buffer is not None:
            maps.append(map_buffer)
            map_buffer = None
        elif map_buffer is not None:
            source_start, destination_start, length = (
                int(x) for x in line.strip().split(" ")
            )
            map_buffer.append(Translation(source_start, destination_start, length))

    return (seeds, maps)

def forward(x: int, translation: Translation) -> int:
    if (
        translation.source_start
        <= x
        < translation.source_start + translation.length
    ):
        return translation.destination_start + x - translation.source_start
    return x

def translate_forwards(field: list[int], translations: list[Translation]) -> list[int]:
    for i, spot in enumerate(field):
        for translation in translations:
            if (
                translation.source_start
                <= spot
                < translation.source_start + translation.length
            ):
                field[i] = (
                    translation.destination_start + spot - translation.source_start
                )

    return field

def translate_backwards(location: int, translations: list[Translation]) -> int:

    return 0



def chunk(l: list[int], size: int):
    for i in range(0, len(l), size):
        yield l[i : i + size]


if __name__ == "__main__":
    puzzle_file = "day_05_test.txt"

    print("Part 1")
    print(part_1(parse_almanac(read(puzzle_file).strip().split("\n"))))
    print()

    print("Part 2")
    print(part_2(parse_almanac(read(puzzle_file).strip().split("\n"))))
    print()

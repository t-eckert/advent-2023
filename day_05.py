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
    field = almanac[0]

    for mapping in almanac[1]:
        print(mapping)
        field = translate(field, mapping.translations)

    return min(field)


def part_2(almanac: Almanac) -> int:
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


def translate(field: list[int], translations: list[Translation]) -> list[int]:
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


if __name__ == "__main__":
    almanac = parse_almanac(read("day_05.txt").strip().split("\n"))

    print("Part 1")
    print(part_1(almanac))
    print()

    print("Part 2")
    print(part_2(almanac))
    print()

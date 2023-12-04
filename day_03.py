from lib import read, tee
from itertools import groupby

digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def part_1(engine_rows: list[str], symbols: set[str]) -> int:
    engine_dimensions = (len(engine_rows), len(engine_rows[0]))

    reading_number = False
    subject_buffer = set()
    number_buffer = ""

    total = 0

    for row, vals in enumerate(engine_rows):
        for col, char in enumerate(vals):
            if char in digits:
                subject_buffer.add((row, col))
                number_buffer += char
                reading_number = True
            else:
                if reading_number:
                    if has_symbol(
                        engine_rows, border(subject_buffer, engine_dimensions), symbols
                    ):
                        total += int(number_buffer)
                    subject_buffer.clear()
                    number_buffer = ""
                reading_number = False

    return total


def part_2(engine_rows: list[str]) -> int:
    engine_dimensions = (len(engine_rows), len(engine_rows[0]))

    reading_number = False
    subject_buffer = set()
    number_buffer = ""

    numbers = []

    for row, vals in enumerate(engine_rows):
        for col, char in enumerate(vals):
            if char in digits:
                subject_buffer.add((row, col))
                number_buffer += char
                reading_number = True
            else:
                if reading_number:
                    numbers.append(
                        PartNumber(int(number_buffer), subject_buffer.copy())
                    )
                    subject_buffer.clear()
                    number_buffer = ""
                reading_number = False

    gears = {}
    for number in numbers:
        for neighbor in border(number.cells, engine_dimensions):
            if engine_rows[neighbor[0]][neighbor[1]] == "*":
                if neighbor in gears.keys():
                    gears[neighbor].append(number)
                else:
                    gears[neighbor] = [number]

    total = 0
    for _, numbers in gears.items():
        if len(numbers) == 2:
            total += numbers[0].value * numbers[1].value

    return total


class PartNumber:
    def __init__(self, value: int, cells: set[tuple[int, int]]):
        self.value = value
        self.cells = cells

    def __repr__(self) -> str:
        return f"{self.value}\t{self.cells=}"


def has_symbol(
    engine_rows: list[str], locations: set[tuple[int, int]], symbols: set[str]
) -> bool:
    for loc in locations:
        if engine_rows[loc[0]][loc[1]] in symbols:
            return True
    return False


def border(
    subject: set[tuple[int, int]], engine_dimensions: tuple[int, int]
) -> set[tuple[int, int]]:
    height, width = engine_dimensions

    borders = set()

    for cell in subject:
        row, col = cell[0], cell[1]

        # Iterate clockwise around the location
        if row > 0 and col > 0:
            borders.add((row - 1, col - 1))  # above left
        if row > 0:
            borders.add((row - 1, col))  # above center
        if row > 0 and col < width - 1:
            borders.add((row - 1, col + 1))  # above right
        if col < width - 1:
            borders.add((row, col + 1))  # center right
        if row < height - 1 and col < width - 1:
            borders.add((row + 1, col + 1))  # below right
        if row < height - 1:
            borders.add((row + 1, col))  # below center
        if row < height - 1 and col > 0:
            borders.add((row + 1, col - 1))  # below left
        if col > 0:
            borders.add((row, col - 1))  # center left

    return borders - subject


if __name__ == "__main__":
    engine_rows = read("day_03.txt").strip().split("\n")

    symbols = set()
    for row in engine_rows:
        for c in row:
            if c not in "0123456789.":
                symbols.add(c)

    print("Part 1")
    print(part_1(engine_rows, symbols))
    print()

    print("Part 2")
    print(part_2(engine_rows))
    print()


def border_test():
    tests = [
        ({(0, 0)}, (4, 4), {(1, 0), (1, 1), (0, 1)}),
        (
            {(1, 1), (1, 2), (1, 3)},
            (4, 4),
            {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)},
        ),
    ]

    for test in tests:
        assert test[2] == border(test[0], test[1])

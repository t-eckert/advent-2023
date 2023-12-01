""" Advent of Code 2023, Day 1

"""

from lib import read


################################################################################
# Part 1 #######################################################################
################################################################################
def part_1(lines: list[str]) -> int:
    return sum([int(first_number(line) + first_number(line[::-1])) for line in lines])


def is_number(c: str) -> bool:
    return c in "0123456789"


def first_number(line: str) -> str:
    for c in line:
        if is_number(c):
            return c
    return ""


################################################################################
# Part 2 #######################################################################
################################################################################
def part_2(lines: list[str]) -> int:
    return sum(
        [int(first_number_or_word(line) + last_number_or_word(line)) for line in lines]
    )


def first_number_or_word(line: str) -> str:
    for i, c in enumerate(line):
        if is_number(c):
            return c
        if matches := number_words.get(c):
            for number_word in matches:
                word = line[i : i + len(number_word)]
                if word == number_word:
                    return number_words[c][number_word]
    return ""


def last_number_or_word(line: str) -> str:
    for i, c in enumerate(line[::-1]):
        if is_number(c):
            return c
        if matches := number_words.get(c):
            for number_word in matches:
                offset = len(line) - i - 1
                word = line[offset : offset + len(number_word)]
                if word == number_word:
                    return number_words[c][number_word]
    return ""


number_words: dict[str, dict[str, str]] = {
    "z": {"zero": "0"},
    "o": {"one": "1"},
    "t": {
        "two": "2",
        "three": "3",
    },
    "f": {
        "four": "4",
        "five": "5",
    },
    "s": {
        "six": "6",
        "seven": "7",
    },
    "e": {"eight": "8"},
    "n": {"nine": "9"},
}


if __name__ == "__main__":
    lines = read("day_01.txt").strip().split("\n")

    print("Part 1")
    print(part_1(lines))
    print()

    print("Part 2")
    print(part_2(lines))
    print()

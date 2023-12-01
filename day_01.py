from lib import read


def part_1(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        first = None
        last = None
        for c in line:
            if is_number(c):
                first = c
                break
        for c in line[::-1]:
            if is_number(c):
                last = c
                break
        assert first
        assert last
        sum += int(first + last)
    return sum


def part_2(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        sum += get_numbers_with_words(line)
    return sum


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


def is_number(c: str) -> bool:
    return c in "0123456789"


def get_numbers_with_words(line: str) -> int:
    print("=========")
    print(line)
    first = None
    last = None

    # Find the first number or number word moving in from the left.
    for i, c in enumerate(line):
        if is_number(c):
            first = c
            break
        if matches := number_words.get(c):
            for number_word in matches:
                if line[i : len(number_word)] == number_word:
                    first = number_words[c].get(number_word)
                break
            if first:
                break

    # Find the last number or number word moving in from the right.
    for i, c in enumerate(line[::-1]):
        print(i, c)
        if is_number(c):
            last = c
            break
        if matches := number_words.get(c):
            print(matches)
            for number_word in matches:
                offset = len(line) - i - 1
                word = line[offset : offset + len(number_word)]
                print(word)
                if word == number_word:
                    print("matched!")
                    last = number_words[c].get(number_word)
                    print(last)
                break
            if last:
                break

    assert first
    assert last
    print(line, "|", first, last)

    return int(first + last)


if __name__ == "__main__":
    lines = read("day_01.txt").strip().split("\n")

    print("Part 1")
    print(part_1(lines))
    print()

    print("Part 2")
    print(part_2(lines))
    print()

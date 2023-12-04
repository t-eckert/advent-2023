from lib import read, tee


def part_1(cards: list[str]) -> int:
    return sum(int(2 ** (count_winning(deserialize_card(card)) - 1)) for card in cards)


def part_2(cards: list[str]) -> int:
    return 0


def count_winning(number_sets: tuple[set[int], set[int]]) -> int:
    return len(number_sets[0].intersection(number_sets[1]))


def deserialize_card(card: str) -> tuple[set[int], set[int]]:
    mine, winning = card.split(":")[1].strip().split("|")
    return (to_set(mine), to_set(winning))


def to_set(numbers: str) -> set[int]:
    return {int(num) for num in numbers.strip().split(" ") if num != ""}


if __name__ == "__main__":
    cards = read("day_04.txt").strip().split("\n")

    print("Part 1")
    print(part_1(cards))
    print()

    print("Part 2")
    print(part_2(cards))
    print()

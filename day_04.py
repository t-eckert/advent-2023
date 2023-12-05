from lib import read, tee
from collections import namedtuple

Card = namedtuple("Card", "mine winning")

def part_1(cards: list[str]) -> int:
    return sum(int(2 ** (count_winning(deserialize_card(card)) - 1)) for card in cards)


def part_2(cards: list[str]) -> int:
    """
    Each card wins you more cards

    """



    return 0


def count_winning(number_sets: Card) -> int:
    return len(number_sets.mine.intersection(number_sets.winning))


def deserialize_card(card: str) -> Card:
    mine, winning = card.split(":")[1].strip().split("|")
    return Card(to_set(mine), to_set(winning))


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

from lib import read, tee
from collections import namedtuple

Card = namedtuple("Card", "id mine winning")


def part_1(cards: list[str]) -> int:
    return sum(int(2 ** (count_winning(deserialize_card(card)) - 1)) for card in cards)


def part_2(raw_input: list[str]) -> int:
    tally = []

    cards = [deserialize_card(raw) for raw in raw_input[::-1]]
    for card in cards:
        wins = count_winning(card)
        won_cards = 0
        if 0 < wins:
            won_cards = sum(tally[-wins:])
        tally.append(1 + won_cards)

    return sum(tally)


def count_winning(card: Card) -> int:
    return len(card.mine.intersection(card.winning))


def deserialize_card(raw: str) -> Card:
    id = raw.split(":")[0]
    mine, winning = raw.split(":")[1].strip().split("|")
    return Card(id, to_set(mine), to_set(winning))


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

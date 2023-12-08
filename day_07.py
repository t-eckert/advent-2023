from lib import read, tee

file = "day_07.txt"

labels = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
labels_jokers_wild = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
categories = [
    "High card",
    "One pair",
    "Two pair",
    "Three of a kind",
    "Full house",
    "Four of a kind",
    "Five of a kind",
]


class Card:
    def __init__(self, label: str, labels: list[str] = labels):
        self.label = label
        self.labels = labels

    def __repr__(self):
        return self.label

    def __hash__(self):
        return self.labels.index(self.label)

    def __lt__(self, other):
        return self.labels.index(self.label) < self.labels.index(other.label)

    def __gt__(self, other):
        return self.labels.index(self.label) > self.labels.index(other.label)

    def __eq__(self, other):
        return self.labels.index(self.label) == self.labels.index(other.label)


class Hand:
    def __init__(self, cards: list[Card], bid: int, jokers_wild: bool = False):
        self.cards = cards
        self.bid = bid
        self.jokers_wild = jokers_wild

    def __repr__(self):
        return f"{self.cards}: {self.bid}"

    def category(self) -> str:
        if self.jokers_wild and Card("J", labels=labels_jokers_wild) in self.cards:
            return self.__category_jokers_wild()

        sorted_cards = sorted(self.cards)

        if len(set(self.cards)) == 1:
            return "Five of a kind"
        elif len(set(self.cards)) == 2:
            if (
                sorted_cards[0] == sorted_cards[1] == sorted_cards[2] == sorted_cards[3]
                or sorted_cards[1]
                == sorted_cards[2]
                == sorted_cards[3]
                == sorted_cards[4]
            ):
                return "Four of a kind"
            else:
                return "Full house"
        elif len(set(self.cards)) == 3:
            if (
                sorted_cards[0] == sorted_cards[1] == sorted_cards[2]
                or sorted_cards[1] == sorted_cards[2] == sorted_cards[3]
                or sorted_cards[2] == sorted_cards[3] == sorted_cards[4]
            ):
                return "Three of a kind"
            else:
                return "Two pair"
        elif len(set(self.cards)) == 4:
            return "One pair"
        else:
            return "High card"

    def __category_jokers_wild(self) -> str:
        """Jokers are wild and can be used to complete any hand."""

        return "High card"

    def __hash__(self):
        return hash(self.cards)

    def __lt__(self, other):
        if categories.index(self.category()) < categories.index(other.category()):
            return True
        elif categories.index(self.category()) > categories.index(other.category()):
            return False
        else:
            for i in range(len(self.cards)):
                if self.cards[i] < other.cards[i]:
                    return True
                elif self.cards[i] > other.cards[i]:
                    return False

        return False

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)

    def __eq__(self, other):
        return (
            categories.index(self.category()) == categories.index(other.category())
            and self.cards == other.cards
        )


def part_1(puzzle: list[str]) -> int:
    return sum(
        [hand.bid * (rank + 1) for rank, hand in enumerate(sorted(parse(puzzle)))]
    )


def part_2(puzzle: list[str]) -> int:
    return sum(
        [hand.bid * (rank + 1) for rank, hand in enumerate(sorted(parse_jokers_wild(puzzle)))]
    )


def parse(puzzle: list[str]) -> list[Hand]:
    hands = []
    for line in puzzle:
        cards, bid = line.split(" ")
        hands.append(Hand([Card(card) for card in cards], int(bid.strip())))
    return hands

def parse_jokers_wild(puzzle: list[str]) -> list[Hand]:
    hands = []
    for line in puzzle:
        cards, bid = line.split(" ")
        hands.append(Hand([Card(card, labels_jokers_wild) for card in cards], int(bid.strip())))
    return hands

def test_hands():
    tests = [
        ("7227Q 52", "Two pair"),
        ("67Q64 732", "One pair"),
        ("33Q33 573", "Four of a kind"),
        ("58ATQ 939", "High card"),
        ("32T3K 765", "One pair"),
        ("T55J5 684", "Three of a kind"),
        ("KK677 28", "Two pair"),
        ("KTJJT 220", "Two pair"),
        ("QQQJA 483", "Three of a kind"),
        ("93K53 840", "One pair"),
        ("55AJ8 496", "One pair"),
        ("6ATAT 863", "Two pair"),
        ("26J77 1", "One pair"),
        ("TTQAT 381", "Three of a kind"),
        ("2J2J2 322", "Full house"),
        ("342Q2 409", "One pair"),
        ("3444Q 864", "Three of a kind"),
        ("77J67 31", "Three of a kind"),
        ("772QJ 796", "One pair"),
        ("5388J 956", "One pair"),
        ("7JJ7J 88", "Full house"),
        ("5Q555 626", "Four of a kind"),
        ("77AK8 588", "One pair"),
        ("AAAAA 1", "Five of a kind"),
    ]

    for test in tests:
        hand = Hand(
            [Card(card) for card in test[0].split(" ")[0]], int(test[0].split(" ")[1])
        )
        print(hand, hand.category())
        assert hand.category() == test[1]


def test_sorting():
    tests = [
        # ["K8624 20", "A8624 20"],
        ["9TJ67 20", "A8624 20"],
    ]

    for test in tests:
        cards = parse(test)
        assert cards == tee(sorted(cards))


if __name__ == "__main__":
    puzzle = read(file).strip().splitlines()

    print("Part 1")
    print(part_1(puzzle))
    print()

    print("Part 2")
    print(part_2(puzzle))
    print()

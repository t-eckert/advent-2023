from day_01 import get_numbers_with_words


def test_get_numbers_with_words():
    table = [
        ("9cbncbxclbvkmfzdnldc", 99),
        ("jjn1drdffhs", 11),
        ("3six7", 37),
        ("38rgtnqqxtc", 38),
        ("nineninezsstmkone4sjnlbldcrj4eight", 98),
        ("7pqrstsixteen", 76),
        ("zoneight234", 14),
        ("xtwone3four", 24),
        ("6nseven16lbztpbbzthree8five", 65),
        ("6fivejttmkvvpntvqlfpbjbcfkcztltwosix", 66),
        ("rvbfnddhg25lpthcsfxfdkmseven", 27),
        ("hksp3gdmcldnvbts1", 31),
        ("xvcpr86btlptpnphhsix5fivenine", 89)
    ]

    for test in table:
        assert test[1] == get_numbers_with_words(test[0])

test_get_numbers_with_words()

"""
CS 3A  - Assignment 7, Slot Machine
Brandon Cunnane
Note: Using instructor solution for TripleString class
"""

import random


class TripleString:
    MAX_LEN = 100
    MIN_LEN = 1
    DEFAULT_STRING = "(undefined)"
    num_triple_strings = 0

    def __init__(self, string1, string2, string3):
        TripleString.num_triple_strings += 1
        if not self.set_string1(string1):
            self.string1 = self.DEFAULT_STRING
        if not self.set_string2(string2):
            self.string2 = self.DEFAULT_STRING
        if not self.set_string3(string3):
            self.string3 = self.DEFAULT_STRING

    def set_string1(self, the_str):
        if not self.validate_string(the_str):
            return False
        self.string1 = the_str
        return True

    def set_string2(self, the_str):
        if not self.validate_string(the_str):
            return False
        self.string2 = the_str
        return True

    def set_string3(self, the_str):
        if not self.validate_string(the_str):
            return False
        self.string3 = the_str
        return True

    def get_string1(self):
        return self.string1

    def get_string2(self):
        return self.string2

    def get_string3(self):
        return self.string3

    def __str__(self):
        return self.string1 + ", " + self.string2 + ", " + self.string3

    @classmethod
    def validate_string(cls, the_str):
        return cls.MIN_LEN <= len(the_str) <= cls.MAX_LEN

    @classmethod
    def get_number_of_instances(cls):
        return TripleString.num_triple_strings


SLOT_BAR = 'BAR'
SLOT_SEVEN = '7'
SLOT_CHERRY = 'cherries'
SLOT_SPACE = '(space)'

PROB_BAR = 38
PROB_SEVEN = 15
PROB_CHERRY = 40
PROB_SPACE = 7

BET_MAX = 50
BET_MIN = 1
UI_EXIT = 0

CHERRY_XCHERRY_ANY_PAY_FACTOR = 5
CHERRY_CHERRY_XCHERRY_PAY_FACTOR = 15
CHERRY_CHERRY_CHERRY_PAY_FACTOR = 30
BAR_BAR_BAR_PAY_FACTOR = 50
SEVEN_SEVEN_SEVEN_PAY_FACTOR = 100


def get_bet():
    """
    Gets bet from user
    :return: user's bet as integer
    """
    the_bet = int(input(f"How much would you like to bet "
                        f"({BET_MIN} - {BET_MAX}) or {UI_EXIT} to quit? "))
    return the_bet


def rand_string():
    """
    Creates single random slot machine result based on probabilities
    :return: slot result as string
    """
    num = random.randrange(100)
    if 0 <= num < PROB_CHERRY:
        return SLOT_CHERRY
    elif PROB_CHERRY <= num < PROB_CHERRY + PROB_BAR:
        return SLOT_BAR
    elif PROB_CHERRY + PROB_BAR <= num < PROB_CHERRY + PROB_BAR + PROB_SEVEN:
        return SLOT_SEVEN
    else:
        return SLOT_SPACE


def pull():
    """
    Simulated slot machine pull
    :return: slot machine pull as TripleString
    """
    this_pull = TripleString(rand_string(), rand_string(), rand_string())
    return this_pull


def get_pay_multiplier(the_pull):
    """
    Determines pay multiplier for specific slot machine results
    :return: resulting multiplier as integer
    """
    if str(the_pull) == f"{SLOT_SEVEN}, {SLOT_SEVEN}, {SLOT_SEVEN}":
        return SEVEN_SEVEN_SEVEN_PAY_FACTOR
    elif str(the_pull) == f"{SLOT_BAR}, {SLOT_BAR}, {SLOT_BAR}":
        return BAR_BAR_BAR_PAY_FACTOR
    elif str(the_pull) == f"{SLOT_CHERRY}, {SLOT_CHERRY}, {SLOT_CHERRY}":
        return CHERRY_CHERRY_CHERRY_PAY_FACTOR
    elif (the_pull.get_string1() == SLOT_CHERRY
          and the_pull.get_string2() != SLOT_CHERRY):
        return CHERRY_XCHERRY_ANY_PAY_FACTOR
    elif (the_pull.get_string1() == SLOT_CHERRY
          and the_pull.get_string2() == SLOT_CHERRY
          and the_pull.get_string3() != SLOT_CHERRY):
        return CHERRY_CHERRY_XCHERRY_PAY_FACTOR
    else:
        return 0


def display(the_pull, winnings):
    """
    Displays slot machine simulation
    :return: None
    """
    print(f"Whirrrrrr .... and your pull "
          f"(#{TripleString.get_number_of_instances()}) is ... ")
    print(str(the_pull))
    if winnings == 0:
        print("Sorry, you lose\n")
    else:
        print(f"Congratulations, you win: {winnings}.\n")


def test_get_pay_multiplier():
    """
    Tests get_pay_multiplier() function for specific test cases
    :return: None
    """
    fctrs = []
    fctrs.append(get_pay_multiplier(TripleString("7", "7", "7")))
    fctrs.append(get_pay_multiplier(TripleString("BAR", "BAR", "BAR")))
    fctrs.append(get_pay_multiplier(TripleString("cherries", "cherries",
                                                 "cherries")))
    fctrs.append(get_pay_multiplier(TripleString("cherries", "cherries", "7")))
    fctrs.append(get_pay_multiplier(TripleString("cherries", "7", "7")))
    fctrs.append(get_pay_multiplier(TripleString("BAR", "7", "cherries")))
    return fctrs


def test_rand_string():
    """
    Tests that rand_string() function results match probabilities
    :return: counts as tuple
    """
    count_cherry = 0
    count_bar = 0
    count_seven = 0
    count_space = 0
    for k in range(10000):
        result = rand_string()
        if result == SLOT_CHERRY:
            count_cherry += 1
        elif result == SLOT_BAR:
            count_bar += 1
        elif result == SLOT_SEVEN:
            count_seven += 1
        else:
            count_space += 1
    return count_cherry, count_bar, count_seven, count_space


def main():
    # print(test_rand_string())
    # print(test_get_pay_multiplier())
    while True:
        the_bet = get_bet()
        if the_bet == UI_EXIT:
            break
        elif not (BET_MIN <= the_bet <= BET_MAX or the_bet == UI_EXIT):
            print("Invalid input.")
            continue
        the_pull = pull()
        multiplier = get_pay_multiplier(the_pull)
        winnings = the_bet * multiplier
        display(the_pull, winnings)
    print("Bye!")


if __name__ == '__main__':
    main()

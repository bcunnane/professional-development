"""
CS3A, Assignment 05, Functions and Lists
Brandon Cunnane
Extracts statistical info from integer list
*** Extra Credit work #1 and #2 is included ***
"""


def get_integers():
    """
    This function asks user to type a list of integers separated by space, and
    returns the list
    :return: a list of integers
    """
    while True:
        try:
            integers = input("Please type a list of integers, separated by space: ")
            integers = integers.split()
            integers = [int(i) for i in integers]
            return integers
        except ValueError as e:
            print("Bad input:", e)


def get_key():
    """
    This function asks user to type in a single key integer, and returns the
    number
    :return: an integer
    """
    while True:
        try:
            key = int(input("Please enter the key number: "))
            return key
        except ValueError as e:
            print("Bad input:", e)


def add_all(values):
    """
    Calculates the sum of all integers in the list.
    :param values: list of integers
    :return: an integer
    """
    total = 0
    for i in range(len(values)):
        total = total + values[i]
    return total


def average(values):
    """
    Calculates the average of all integers in the list
    :param values: list of integers
    :return: an integer
    """
    if len(values) == 0:
        return None
    else:
        ave = add_all(values) / len(values)
        return ave


def minmax(values):
    """
    Determines the minimum and maximum value in the list
    :param values: list of integers
    :return: tuple of integers
    """
    if len(values) == 0:
        return None, None

    min = values[0]
    max = values[0]
    for i in range(len(values)):
        if values[i] < min:
            min = values[i]
        elif values[i] > max:
            max = values[i]
    return min, max


def count_key(values, key):
    """
    Counts the number of occurrences of key in the list
    :param values: list of integers
    :param key: an integer
    :return: an integer
    """
    count = 0
    for i in range(len(values)):
        if values[i] == key:
            count += 1
    return count


def is_in(values, key):
    """
    Determines if the key is present in the list
    :param values: list of integers
    :param key: an integer
    :return: a string
    """
    for i in range(len(values)):
        if values[i] == key:
            return "is"
    return "is not"


def double(values):
    """
    Doubles the value of each integer in the list
    :param values: list of integers
    :return: list of integers
    """
    doubles = []
    for i in range(len(values)):
        doubles.append(2 * values[i])
    return doubles


def mask(integers, key):
    """
    Replaces any occurrence of key in the list with None
    :param integers: list of integers
    :param key: an integer
    :return: None
    """
    for i in range(len(integers)):
        if integers[i] == key:
            integers[i] = None


def extra_credit1():
    """
    My functions can work with lists containing non-int types since logic like
    " == " works for non-int types. For example, the function count_key() will
    work on a list of strings if given a string key.
    :return: None
    """
    str_list = ['To', 'be', 'or', 'not', 'to', 'be']
    key = 'be'
    result = count_key(str_list, key)
    print(f"EC1: {key} occurs {result} times")


def extra_credit2():
    """
    A string is essentially a tuple of characters, so my functions can also
    work on strings. For example, the function count_key() will work on a
    string if given a character key.
    :return: None
    """
    str = "To be or not to be"
    key = "b"
    result = count_key(str, key)
    print(f"EC2: {key} occurs {result} times")


def main():
    integers = get_integers()
    key = get_key()
    print(f"Integers is {integers}; key is {key}")

    result = add_all(integers)
    print(f"Sum is {result}")

    result = average(integers)
    print(f"Average is {result}")

    result = minmax(integers)
    print(f"Smallest is {result[0]}; largest is {result[1]}")

    result = count_key(integers, key)
    print(f"{key} occurs {result} times")

    result = is_in(integers, key)
    print(f"{key} {result} in the list")

    result = double(integers)
    print(f"Result of doubling integers is {result}")

    mask(integers, key)
    print(f"Result of masking {key} in integers is {integers}")

    extra_credit1()
    extra_credit2()


if __name__ == '__main__':
    main()

"""
*** Output WITHOUT extra credit

Please type a list of integers, separated by space: 
Please enter the key number: 1
Integers is []; key is 1
Sum is 0
Average is None
Smallest is None; largest is None
1 occurs 0 times
1 is not in the list
Result of doubling integers is []
Result of masking 1 in integers is []

Please type a list of integers, separated by space: 1
Please enter the key number: 1
Integers is [1]; key is 1
Sum is 1
Average is 1.0
Smallest is 1; largest is 1
1 occurs 1 times
1 is in the list
Result of doubling integers is [2]
Result of masking 1 in integers is [None]

Please type a list of integers, separated by space: 9 535 230 66 -99 87 -99 3 3 3 9 11 3
Please enter the key number: 3
Integers is [9, 535, 230, 66, -99, 87, -99, 3, 3, 3, 9, 11, 3]; key is 3
Sum is 761
Average is 58.53846153846154
Smallest is -99; largest is 535
3 occurs 4 times
3 is in the list
Result of doubling integers is [18, 1070, 460, 132, -198, 174, -198, 6, 6, 6, 18, 22, 6]
Result of masking 3 in integers is [9, 535, 230, 66, -99, 87, -99, None, None, None, 9, 11, None]

Please type a list of integers, separated by space: 1 2 3
Please enter the key number: 0
Integers is [1, 2, 3]; key is 0
Sum is 6
Average is 2.0
Smallest is 1; largest is 3
0 occurs 0 times
0 is not in the list
Result of doubling integers is [2, 4, 6]
Result of masking 0 in integers is [1, 2, 3]

Please type a list of integers, separated by space: 1 2 3
Please enter the key number: 1
Integers is [1, 2, 3]; key is 1
Sum is 6
Average is 2.0
Smallest is 1; largest is 3
1 occurs 1 times
1 is in the list
Result of doubling integers is [2, 4, 6]
Result of masking 1 in integers is [None, 2, 3]

Please type a list of integers, separated by space: 1 1 1 2 3 
Please enter the key number: 1
Integers is [1, 1, 1, 2, 3]; key is 1
Sum is 8
Average is 1.6
Smallest is 1; largest is 3
1 occurs 3 times
1 is in the list
Result of doubling integers is [2, 2, 2, 4, 6]
Result of masking 1 in integers is [None, None, None, 2, 3]

*** Output WITH extra credit ***

Please type a list of integers, separated by space: 1 2 3 
Please enter the key number: 1
Integers is [1, 2, 3]; key is 1
Sum is 6
Average is 2.0
Smallest is 1; largest is 3
1 occurs 1 times
1 is in the list
Result of doubling integers is [2, 4, 6]
Result of masking 1 in integers is [None, 2, 3]
EC1: be occurs 2 times
EC2: b occurs 2 times
"""
"""
CS3A, Lab Assignment 8 - String Reversal
Brandon Cunnane
Reverses string order
"""

import time


class Reverser:
    @staticmethod
    def reverse_str_iter(string):
        """
        Uses iteration to reverse the string
        :return: reversed string
        """
        str_len = len(string)
        reversed_char_list = [" "] * str_len
        for i in range(len(string)):
            reversed_char_list[str_len - 1 - i] = string[i]
        new_string = ''.join(reversed_char_list)
        return new_string

    @staticmethod
    def reverse_str_stack(string):
        """
        Uses a stack to reverse the string
        :return: reversed string
        """
        stack = []
        new_string = ''
        [stack.append(char) for char in string]
        for j in range(len(stack)):
            new_string = new_string + stack.pop()
        return new_string

    @staticmethod
    def reverse_str_rec(string):
        """
        Uses recursion to reverse the string.
        *** Longest string length possible is 995 ***
        :return: reversed string
        """
        if string == '':
            return ''
        return string[-1] + Reverser.reverse_str_rec(string[0:-1])

    @staticmethod
    def reverse_str_builtin(string):
        """
        Uses built-in Python way to reverse string
        :return: Reversed string
        """
        return string[::-1]


def remove_char(string, char):
    """
    Removes the character from the string
    :return: string without the specified character
    """
    if string == '':
        return ''
    elif string[0] == char:
        return '' + remove_char(string[1:], char)
    return string[0] + remove_char(string[1:], char)


def test():
    """Tests the Reverser class
    The fastest Reverser method is Built-in, and the slowest is Recursive.
    I expected Recursive to be the slowest since we learned in class that it is
    not efficient.
    I also expected Built-in to be the fastest since it is a standard function.
    """
    starts = []
    durations = []
    test_strs = ['', 'a', 'abcdefghijk', '1' * 995]

    starts.append(time.perf_counter())
    iter_result = [Reverser.reverse_str_iter(ts) for ts in test_strs]
    durations.append(time.perf_counter() - starts[-1])

    starts.append(time.perf_counter())
    stack_result = [Reverser.reverse_str_stack(ts) for ts in test_strs]
    durations.append(time.perf_counter() - starts[-1])

    starts.append(time.perf_counter())
    rec_result = [Reverser.reverse_str_rec(ts) for ts in test_strs]
    durations.append(time.perf_counter() - starts[-1])

    starts.append(time.perf_counter())
    builtin_result = [Reverser.reverse_str_builtin(ts) for ts in test_strs]
    durations.append(time.perf_counter() - starts[-1])

    print(f"Test Strings:     {test_strs}\n"
          f"Iterative Result: {iter_result}\n"
          f"Stack Result:     {stack_result}\n"
          f"Recursive Result: {rec_result}\n"
          f"Built-in Result:  {builtin_result}\n")
    print(f"Respective Durations: {durations}\n")


def remove_char_test():
    """ Tests the remove_char() function """
    test_strs = ['', 'a', 'b', 'abbccc', 'abbccc', 'aaa']
    test_chars = ['a', 'a', 'a', 'a', 'b', 'A']
    for i in range(len(test_strs)):
        print(f"Removing '{test_chars[i]}' from '{test_strs[i]}' "
              f"gives '{remove_char(test_strs[i],test_chars[i])}'")


if __name__ == '__main__':
    test()
    remove_char_test()

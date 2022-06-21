"""
CS3A, Assignment #6, A triple string class
Brandon Cunnane
"""


class TripleString:
    """ Encapsulates a triple-string object """

    # Class constants
    MIN_LEN = 1  # Inclusive min length for attribute string1, string2, string3
    MAX_LEN = 100  # Inclusive max length for attribute string1,string2,string3
    DEFAULT_STRING = "(undefined)"  # Default value for the string attributes

    # Initializer
    def __init__(self, string1, string2, string3):
        if not self.set_string1(string1):
            self.string1 = TripleString.DEFAULT_STRING
        if not self.set_string2(string2):
            self.string2 = TripleString.DEFAULT_STRING
        if not self.set_string3(string3):
            self.string3 = TripleString.DEFAULT_STRING

        self.set_string1(string1)
        self.set_string2(string2)
        self.set_string3(string3)

    def __str__(self):
        return f"Strings 1, 2, and 3 are {self.string1}, {self.string2}, and "\
               f"{self.string3}, respectively."

    # Setters
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

    # Getters
    def get_string1(self):
        return self.string1

    def get_string2(self):
        return self.string2

    def get_string3(self):
        return self.string3

    # Validate string method
    def validate_string(self, the_str):
        if TripleString.MIN_LEN <= len(the_str) <= TripleString.MAX_LEN:
            return True
        else:
            return False


def test():
    """Tests for TripleString class"""
    # Test 1
    ts1 = TripleString("a", "b", "c")
    ts2 = TripleString("sun", "moon", "star")
    ts3 = TripleString("", "", "")
    ts4 = TripleString("", "1", "2")
    ts5 = TripleString("1", "", "2")
    ts6 = TripleString("1", "2", "")

    # Test 2
    print(str(ts1))
    print(str(ts2))
    print(str(ts3))
    print(str(ts4))
    print(str(ts5))
    print(str(ts6))

    # Test 3
    if ts1.set_string1("x"):
        print(f"ts1.string1 is {ts1.get_string1()}")
        print("set_string1('x') succeeds, expected.")
    else:
        print(f"ts1.string1 is {ts1.get_string1()}")
        print("set_string1('x') fails, unexpected.")
    if not ts1.set_string1(""):
        print(f"ts1.string1 is {ts1.get_string1()}")
        print("set_string1('') fails, expected.")
    else:
        print(f"ts1.string1 is {ts1.get_string1()}")
        print("set_string1('') succeeds, unexpected.")

    if ts1.set_string2("x"):
        print(f"ts1.string2 is {ts1.get_string2()}")
        print("set_string2('x') succeeds, expected.")
    else:
        print(f"ts1.string2 is {ts1.get_string2()}")
        print("set_string2('x') fails, unexpected.")
    if not ts1.set_string2(""):
        print(f"ts1.string2 is {ts1.get_string2()}")
        print("set_string2('') fails, expected.")
    else:
        print(f"ts1.string2 is {ts1.get_string2()}")
        print("set_string2('') succeeds, unexpected.")

    if ts1.set_string3("x"):
        print(f"ts1.string3 is {ts1.get_string3()}")
        print("set_string3('x') succeeds, expected.")
    else:
        print(f"ts1.string3 is {ts1.get_string3()}")
        print("set_string3('x') fails, unexpected.")
    if not ts1.set_string3(""):
        print(f"ts1.string3 is {ts1.get_string3()}")
        print("set_string3('') fails, expected.")
    else:
        print(f"ts1.string3 is {ts1.get_string3()}")
        print("set_string3('') succeeds, unexpected.")

    # Test 4
    print(f"String 1 of ts2 is {ts2.get_string1()}")
    print(f"String 2 of ts2 is {ts2.get_string2()}")
    print(f"String 3 of ts2 is {ts2.get_string3()}")


if __name__ == '__main__':
    test()

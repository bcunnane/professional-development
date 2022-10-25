"""
Brandon Cunnane
Lab 4: Recursion
Pascal's Triangle function
"""

def pascal(n, _line=[1]):
    # validate input
    if type(n) != int:
        return 'Error: Input must be an integer.'
    elif n < 0:
        return 'Error: Input must be nonnegative.'
    
    # generate result
    elif n == 0:
        return _line
    elif n > 0:
        middle = []
        for i in range(len(_line) - 1):
            middle.append(_line[i] + _line[i+1])
        _line = [1] + middle + [1]
        return pascal(n-1, _line)
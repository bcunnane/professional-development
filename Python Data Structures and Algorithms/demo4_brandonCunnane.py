"""
Brandon Cunnane
Lab 4: Recursion
Test driver
"""

from brandonCunnaneLab4 import pascal


def test():
    # test valid cases
    tests = [0,1,2,3,4,5,6,len('brandoncunnane')]
    for n in tests:
        print('row ' + str(n) +': ' + str(pascal(n)))
    
    # test error cases
    print('')
    print(pascal('a'))
    print(pascal(-1))
    

if __name__ == '__main__':
    test()


"""
row 0: [1]
row 1: [1, 1]
row 2: [1, 2, 1]
row 3: [1, 3, 3, 1]
row 4: [1, 4, 6, 4, 1]
row 5: [1, 5, 10, 10, 5, 1]
row 6: [1, 6, 15, 20, 15, 6, 1]
row 14: [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1]

Error: Input must be an integer.
Error: Input must be nonnegative.
"""
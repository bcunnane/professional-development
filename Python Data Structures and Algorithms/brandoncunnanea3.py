"""
Brandon Cunnane
CS C3 assignment 3
Test driver

Time complexity - O(n)
The algorithm loops thorugh every character in the string

Space complexity - O(n)
The algorithm creates 4 additional variables and 1 data structure
"""

from brandoncunnanestack import Stack


def balanced_symbols(string):
    opens = '([{'
    closes = ')]}'
    
    the_stack = Stack()
    balanced = True
    idx = 0
    while idx < len(string):
        
        # check for open symbol
        if string[idx] in opens:
            the_stack.push(string[idx])
        
        # check for close symbol
        elif string[idx] in closes:
            # check if stack is empty
            if the_stack.is_empty():
                balanced = False
                break
            
            # check if close symbol matches open symbol
            else:
                symbol_type = closes.index(string[idx])
                popped = the_stack.pop().get_data()
                if popped != opens[symbol_type]:
                    balanced = False
                    break
        idx += 1
    return balanced


def test():
    case1 = '([|)]'
    case2 = '() (() [()])'
    case3 = '{{([][])}()}'
    non_symbols = '{2x+4}*[x^(3n) + x^(2n) + x^(n) + 17]'
    pop_empty = ']'
    incorrect_pair = '([)]'
    
    test_cases = [case1, case2, case3, non_symbols, pop_empty, incorrect_pair]
    for case in test_cases:
        print(case)
        if balanced_symbols(case):
            print('Balanced\n')
        else:
            print('Error: unbalanced\n')


if __name__ == '__main__':
    test()


"""
([|)]
Error: unbalanced

() (() [()])
Balanced

{{([][])}()}
Balanced

{2x+4}*[x^(3n) + x^(2n) + x^(n) + 17]
Balanced

]
Error: unbalanced

([)]
Error: unbalanced
"""
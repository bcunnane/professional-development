"""
Brandon Cunnane Lab 2 Demo
Tests Latin translation into English

get_translation()
time complexity: O(n^2) because replace() and split() methods are each O(n)


translate()
time complexity: O(n) where n is the number of words in the passed phrase
benchmarking: running 1000 times took 0.0008973999993031612 seconds
"""

from brandonCunnaneLab2 import get_translation, translate
import timeit

def test():
    # create latin translation file
    latin_file = open('latin.txt','r')
    translator = get_translation(latin_file)
    latin_file.close()
    
    # test translation
    menu = """
    Translate latin into english!
    Enter desired latin phrase into prompt
    Unknown words will be returned as "???"
    Enter "exit" to stop
    """
    print(menu)
    while True:
        phrase = input('Enter a latin phrase: ')
        if phrase == 'exit':
            print('vale!')
            break
        else:
            translation = translate(phrase, translator)
            print(f'English translation: {translation}\n')
    


if __name__ == '__main__':
    test()
    # benchmark
    setup_code = """
from brandonCunnaneLab2 import get_translation, translate
latin_file = open('latin.txt','r')
translator = get_translation(latin_file)
latin_file.close()
phrase = 'post hoc ergo propter hoc'
    """
    statement = 'translate(phrase, translator)'
    benchmark = timeit.timeit(stmt=statement, setup=setup_code, number=1000)


"""
    Translate latin into english!
    Enter desired latin phrase into prompt
    Unknown words will be returned as "???"
    Enter "exit" to stop
    
Enter a latin phrase: post hoc ergo propter hoc
English translation: after this therefore because of this

Enter a latin phrase: veni vidi vici
English translation: come see conquer

Enter a latin phrase: aut cum scuto aut in scuto
English translation: either ??? ??? either in ???

Enter a latin phrase: abbas absque abundantia
English translation: father without abundance

Enter a latin phrase: benigne bibo bis
English translation: kindly  drink twice

Enter a latin phrase: exit
vale!
"""
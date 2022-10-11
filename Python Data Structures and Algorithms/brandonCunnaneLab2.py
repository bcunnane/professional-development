"""
Brandon Cunnane Lab 2
Functions to create translation reference object, and translate phrases


"""


def get_translation(file):
    """
    Accepts file of words and their translations
    Returns Python dict file for translation
    Expects file has: translation separted by commas, words by newline
    """
    translator = {}
    for line in file:
        word, translation = line.replace('\n','').split(', ')
        translator[word] = translation
    return translator


def translate(phrase, translator):
    """
    Accepts phrase and translator dictionary
    Returns translated phrase using translator
    Unavailable translations return "???"
    """
    phrase = phrase.split()
    
    trans_phrase = []
    for word in phrase:
        try:
            trans_phrase.append(translator[word])
        except:
            trans_phrase.append('???')
    
    trans_phrase = ' '.join(trans_phrase)
    return trans_phrase

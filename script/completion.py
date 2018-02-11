import marisa_trie
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
import re
import sys

trie = marisa_trie.Trie()
# regular expression for tokenizing sentences into words
tokenizer = RegexpTokenizer('[a-zA-Z0-9\']+')


def load():
    """
    Load the file and generate n-grams list
    Args :
        none
    Returns :
        trie
    """
    sentences = text_to_string("../data/Newspaper2013.txt")
    trigrams = generate_ngrams(sentences, 3)
    mostCommon = have_frequency(counter(trigrams), 100)
    global trie
    trie = marisa_trie.Trie(mostCommon)
    return trie


def candidates(prefix):
    """
    Find and returns word candidates with the given prefix
    Args :
        prefix : str
    Returns :
        list
    """
    global trie
    return trie.keys(prefix.lower())


def normalize(string):
    """
    Substitute special characters ` and ’
    into single quotes
    Args :
        string : str
    Returns :
        string normalized : str
    """
    print("Normalizing")
    # substitue special characters with single quotes
    pattern = re.compile('[`’]')
    return pattern.sub('\'', string)


def text_to_string(file):
    """
    Convert a file into a string
    Args :
        file : str
    Returns :
        string containing all the file : str
    """
    print("Converting file into a string")
    # reading the given file
    with open(file, 'r') as input:
        # generate a list with all the lines
        lines = [line.rstrip() for line in input]
    # transform the list into a string
    return normalize(' '.join(lines))


def generate_ngrams(string, n):
    """
    Generate n-grams list
    Args :
        string : str
        n, the number of words for creating n-grams : int
    Returns :
        allNgrams, list of generated n-grams : list
    """
    print("Tokenizing")
    # tokenize string into sentences
    sentences = sent_tokenize(string.lower())
    print("Generating ngrams")
    # tokenize sentence into words and generate a list of n-grams sequences
    temp = [list(ngrams(tokenizer.tokenize(sent), n)) for sent in sentences]
    # generate n-grams list
    return [' '.join(words) for item in temp for words in item]


def counter(list):
    """
    Count the frequency of items in a list
    Args :
        list, the given list : list
    Returns :
        dict, items in list with their frequency : dict
    """
    print("Counting")
    # generate a dictionary with the given list
    dict = {}
    for item in list:
        if item in dict:
            dict[item] += 1
        else:
            dict.setdefault(item, 1)
    return dict


def have_frequency(dict, n):
    """
    Create a list with the items of the given dictionary
    that have higher frequency than the given number
    Args :
        dictionary with items and their frequency : dict
        n, frequency : int
    Returns :
        frequencyList : list
    """
    print("Creating frequency list")
    # generate list with the given dictionary and frequency
    return [item for item, frequency in dict.items() if frequency >= n]

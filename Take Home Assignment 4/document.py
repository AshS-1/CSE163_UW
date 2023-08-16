'''
This file contains the Document class, represents the a single document
in SearchEngine.
'''
from cse163_utils import normalize_token


class Document:
    '''
    The Document class represents data from a single web page. The class
    contains methods to compute the term frequency, which determines the
    ratio of terms in the document to the total number of words in all.
    It also contains methods that return the path name or the list of
    distinct words in the document.
    '''
    def __init__(self, path: str) -> None:
        '''
        Takes a string path to the document and initializes the data
        for the document. It precomputes the term frequency which
        will be returned in the term_frequency method. Returns none.
        '''
        self._path = path
        self._tf_dict = {}
        self._all_words = 0
        with open(path, 'r') as file:
            self._all_words = file.read().split()
            word_count = {}
            for word in self._all_words:
                new_word = normalize_token(word)
                if new_word not in word_count.keys():
                    word_count[new_word] = 0
                word_count[new_word] = word_count.get(new_word) + 1
            total_length = len(self._all_words)
            for term, count in word_count.items():
                term_frequency = count / total_length
                self._tf_dict[term] = term_frequency

    def term_frequency(self, term: str) -> float:
        '''
        Takes in a string term, and returns a float value of the term
        frequency of the specific term. The term frequency represents
        the ratio between the number of that specific term to the total
        number of words in the document.
        '''
        new_term = normalize_token(term)
        return self._tf_dict.get(new_term, 0)

    def get_path(self) -> str:
        '''
        Returns a string value for the path of the document.
        '''
        return self._path

    def get_words(self) -> list[str]:
        '''
        Returns a list of strings of the distinct words in the document.
        '''
        return list(self._tf_dict.keys())

    def __str__(self) -> str:
        '''
        Returns a string representation of the document, with the path
        name followed by the number of words it has.
        '''
        return "Document(" + self._path + ", words: " + \
            str(len(self._all_words)) + ")"

'''
Represents the SearchEngine class and the command-line interference.
'''
import os
import math
from document import Document
from cse163_utils import normalize_token


class SearchEngine:
    '''
    The SearchEngine class represents a corpus of documents. It has methods
    that can comput the td-idf statistics between a document and a query, as
    well as implement a search function that returns a list of paths sorted
    based on their td-idf statistics.
    '''
    def __init__(self, corpus_path: str) -> None:
        '''
        Takes in a string corpus_path, and returns None. Initializes
        the SearchEngine by using the corpus path and corresponds the
        term int he corpus to the list of documents that have the term.
        '''
        self._corpus_path = corpus_path
        self._result = {}
        self._num_doc = len(os.listdir(corpus_path))
        for filename in os.listdir(self._corpus_path):
            filepath = os.path.join(self._corpus_path, filename)
            document = Document(filepath)
            all_words = document.get_words()
            for word in all_words:
                if word not in self._result.keys():
                    self._result[word] = []
                if document not in self._result[word]:
                    self._result[word].append(document)
        # find out the words in the document
        # see if the word is in the result Dictionary
        # if it is, then add the name of the file to the dictionary

    def _calculate_idf(self, term: str) -> float:
        '''
        Passes in a string term. This method calculates the inverse
        document frequency of that term. If the term is not in the
        corpus, the method returns 0.
        '''
        if term in self._result:
            return math.log(self._num_doc / len(self._result[term]))
        else:
            return 0

    def __str__(self) -> str:
        '''
        Returns a string representation of the SearchEngine by providing
        the corpus path and the size of the directory.
        '''
        return "SearchEngine(" + self._corpus_path + ", size: " + \
            str(self._num_doc) + ")"

    def search(self, query: str) -> list[str]:
        '''
        Takes in a string query with one or more terms. This method returns
        a list of string document paths that are sorted in descending order
        based on the td-idf statistic.
        '''
        # Split the terms in the query
        terms = query.split()
        # Create the dictionary of the document, float pairs
        tfidf = {}
        # For each terms in the query (document)
        for term in set(terms):
            term = normalize_token(term)
            # Calculate the idf value for the document
            idf_value = self._calculate_idf(term)
            for doc in self._result.get(term, []):
                tf = doc.term_frequency(term)
                # Initialize the document with some value 0
                if doc._path not in tfidf:
                    tfidf[doc._path] = 0
                # Assign the document with the tf-idf statistic
                tfidf[doc._path] += tf * idf_value
        # Sort the documents by the tfidf values
        sorted_all = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)
        # Return the first in the list
        return [doc[0] for doc in sorted_all]

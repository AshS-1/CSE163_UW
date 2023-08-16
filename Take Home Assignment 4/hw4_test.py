'''
Tests the functions from the document and search_engine classes.
'''

from cse163_utils import assert_equals
from document import Document
from search_engine import SearchEngine


def test_term_frequency(doc1: Document, doc2:
                        Document, doc3: Document) -> None:
    '''
    Tests the term_frequency
    '''
    assert_equals(0.6, Document.term_frequency(doc1, "row"))
    assert_equals(0.2, Document.term_frequency(doc2, "five"))
    assert_equals(1, Document.term_frequency(doc3, "cse163"))


def test_get_path(doc1: Document, doc2: Document, doc3: Document) -> None:
    '''
    Tests get_path
    '''
    assert_equals("/home/testing1.txt", doc1.get_path())
    assert_equals("/home/testing2.txt", doc2.get_path())
    assert_equals("/home/testing3.txt", doc3.get_path())


def test_get_words(doc1: Document, doc2: Document, doc3: Document) -> None:
    '''
    Tests get_words
    '''
    assert_equals(['row', 'your', 'boat'], Document.get_words(doc1))
    assert_equals(['there', 'are', 'five', 'words', 'here'],
                  Document.get_words(doc2))
    assert_equals(['cse163'], Document.get_words(doc3))


def test_str(doc1: Document, doc2: Document, doc3: Document) -> None:
    '''
    Tests string method.
    '''
    assert_equals("Document(/home/testing1.txt, words: 5)", str(doc1))
    assert_equals("Document(/home/testing2.txt, words: 5)", str(doc2))
    assert_equals("Document(/home/testing3.txt, words: 1)", str(doc3))


def test_search(corpus1: SearchEngine, corpus2: SearchEngine,
                corpus3: SearchEngine) -> None:
    '''
    Tests search method
    '''
    assert_equals("['/home/search1/search11.txt']", str(corpus1.search('lot')))
    assert_equals("['/home/search2/search24.txt']",
                  str(corpus2.search('rainier')))
    assert_equals("['/home/search3/search31.txt']",
                  str(corpus3.search('world')))


def main():
    doc1 = Document("/home/testing1.txt")
    doc2 = Document("/home/testing2.txt")
    doc3 = Document("/home/testing3.txt")
    corpus1 = SearchEngine("/home/search1")
    corpus2 = SearchEngine("/home/search2")
    corpus3 = SearchEngine("/home/search3")
    test_term_frequency(doc1, doc2, doc3)
    test_get_path(doc1, doc2, doc3)
    test_get_words(doc1, doc2, doc3)
    test_str(doc1, doc2, doc3)
    test_search(corpus1, corpus2, corpus3)


if __name__ == '__main__':
    main()

import pytest

def test_library_add_book():
    """Test adding books works"""
    from library import Library
    library = Library()
    library.add_book('My First Book', 'Alice')
    library.add_book('My Second Book', 'Alice')
    library.add_book('A Different Book', 'Bob')
    
    assert len(library.books) == 3


def test_library_len():
    """Test 'len` works"""
    from library import Library
    library = Library()
    library.add_book('My First Book', 'Alice')
    library.add_book('My Second Book', 'Alice')
    library.add_book('A Different Book', 'Bob')
    
    assert len(library) == 3
    
    
def test_library_get_book():
    """Test getting books by author works"""
    from library import Library
    library = Library()
    library.add_book('My First Book', 'Alice')
    library.add_book('My Second Book', 'Alice')
    library.add_book('A Different Book', 'Bob')
    
    book = library[1]
    assert book.title == 'My Second Book'


def test_library_by_author():
    """Test getting books by author works"""
    from library import Library
    library = Library()
    library.add_book('My First Book', 'Alice')
    library.add_book('My Second Book', 'Alice')
    library.add_book('A Different Book', 'Bob')
    
    books = library.by_author('Alice')
    assert len(books) == 2
    assert [b.author for b in books] == ['Alice']*2
    

def test_library_by_author_missing():
    """Test getting books by author works when author is missing"""
    from library import Library
    library = Library()
    library.add_book('My First Book', 'Alice')
    library.add_book('My Second Book', 'Alice')
    library.add_book('A Different Book', 'Bob')
    
    with pytest.raises(KeyError):
        library.by_author('Carol')


def test_library_authors():
    """Test getting all authors in the library"""
    from library import Library
    library = Library()
    library.add_book('My First Book', 'Alice')
    library.add_book('My Second Book', 'Alice')
    library.add_book('A Different Book', 'Bob')
    
    authors = library.authors
    assert set(authors)=={'Alice','Bob'}
    

def test_library_titles():
    """Test getting all titles in the library"""
    from library import Library
    library = Library()
    library.add_book('My First Book', 'Alice')
    library.add_book('My Second Book', 'Alice')
    library.add_book('A Different Book', 'Bob')
    
    titles = library.titles
    assert set(titles)=={'My First Book','My Second Book', 'A Different Book'}

def test_library_merge():
    """Test merging two libraries"""
    from library import Library
    library1 = Library()
    library1.add_book('My First Book', 'Alice')
    library1.add_book('A Different Book', 'Bob')
    
    library2 = Library()
    library2.add_book('My First Book', 'Alice')
    library2.add_book('My Second Book', 'Alice')
    library2.add_book('A Different Book', 'Bob')
    library2.add_book('Yet another Book', 'Carol')
    
    new_library = library1.union(library2)
    assert len(new_library)==4
    
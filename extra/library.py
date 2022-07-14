class Book:
    def __init__(self, title, author) -> None:
        self.title=title
        self.author=author
    
    def __str__(self) -> str:
        return "{} by {}".format(self.title, self.author)

    def __eq__(self, other: object) -> bool:
        return self.title == other.title and self.author==other.author


class Library:
    def __init__(self, books=None) -> None:
        self.books = [] if books is None else books
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
    
    def by_author(self, author):
        books =  [b for b in self.books if b.author==author]
        if not books:
            raise KeyError("Author {} does not exist in the library".format(author))
        return books
    
    def union(self, other):
        books = []
        for b in self.books:
            books.append(b)
        for b in other.books:
            if not b in books:
                books.append(b)
        return Library(books)
    
    @property
    def authors(self):
        return {book.author for book in self.books}
    
    @property
    def titles(self):
        return {book.title for book in self.books}
    
    def __len__(self):
        return len(self.books)

    def __getitem__(self,i):
        return self.books[i]
    

# Code provided by the exercise
def check_output():
    library = Library()

    library.add_book('My First Book', 'Alice')
    library.add_book('My Second Book', 'Alice')
    library.add_book('A Different Book', 'Bob')

    print(len(library))

    book = library[2]
    print(book)

    books = library.by_author('Alice')
    for book in books:
        print(book)

    books = library.by_author('Carol')


if __name__ == '__main__':
    check_output()

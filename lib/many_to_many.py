class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.name = name
        self._contracts = []
        self._books = []

    def contracts(self):
        return self._contracts
    
    def books(self):
        return self._books
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        if book not in self._books:
            self._books.append(book)
        return contract
    
    def total_royalties(self):
        total = 0
        for contract in self._contracts:
            total += contract.royalties
        return total


class Book:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.title = title
        self._contracts = []
        self._authors = []

    def contracts(self):
        return self._contracts
    
    def authors(self):
        return self._authors
    def total_royalties(self):
        return self._total_royalties

class Contract:
    all = []  # Class-level list to track all contracts

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        
        # Add this contract to the book's contracts
        book._contracts.append(self)
        # Add the author to the book's authors if not already present
        if author not in book._authors:
            book._authors.append(author)
        
        # Add this contract to the author's contracts
        author._contracts.append(self)
        # Add the book to the author's books if not already present
        if book not in author._books:
            author._books.append(book)
        
        # Add to class-level list
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        return [contract for contract in cls.all if contract.date == date]
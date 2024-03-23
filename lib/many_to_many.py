class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.author]

    def books(self):
        return [contract.book for contract in Contract.all if self == contract.author]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if self == contract.author])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.book]
    
    def authors(self):
        return [contract.author for contract in Contract.all if self == contract.book]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)



    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception('exception')
        self._author = author


    @property
    def book(self):
        return self._book
        
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception('exception')
            
    @property
    def date(self):
        return self._date
        
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception('exception')

    @property
    def royalties(self):
        return self._royalties
        
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception
        else:
            self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

            
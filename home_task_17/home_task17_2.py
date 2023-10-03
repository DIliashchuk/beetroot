#Library

#Write a class structure that implements a library. Classes:

#1) Library - name, books = [], authors = []
#2) Book - name, year, author (author must be an instance of Author class)
#3) Author - name, country, birthday, books = []

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"Library: {self.name}"

    def __repr__(self):
        return f"Library(name='{self.name}')"


class Book:
    total_books = 0



    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1

    def __str__(self):
        return f"Book: {self.name}, Year: {self.year}, Author: {self.author}"

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={self.author})"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"Author: {self.name}, Country: {self.country}, Birthday: {self.birthday}"

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

# Example usage:
author1 = Author("Author 1", "Country 1", "2000-01-01")
library = Library("My Library")
book1 = library.new_book("Book 1", 2000, author1)
book2 = library.new_book("Book 2", 2005, author1)

print(library.group_by_author(author1))
print(library.group_by_year(2000))
print(Book.total_books)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if any(b.title == book.title for b in self.books):
            print(f"Book '{book.title}' already exists in the library.")
            return
        self.books.append(book)
        print(f"Added book: {book}")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed book: '{title}'")
                return
        print(f"Book '{title}' not found in the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return
        print("Books in the library:")
        for book in self.books:
            print(book)


lib = Library()

book1 = Book("1984", "Harry potter", 1949)
book2 = Book("1999", "ragaca", 1960)
book3 = Book("1984", "Harry potter", 1949)  


lib.add_book(book1)  
lib.add_book(book2)  
lib.add_book(book3)  

lib.list_books()


lib.remove_book("1984")  
lib.list_books()




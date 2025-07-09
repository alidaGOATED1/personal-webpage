class Book:
    def __init__(self, title, author, pages, ):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def __str__(self):
        return f"The book '{self.title}' is written by {self.author} and has {self.pages} pages."
    def open_book(self):
        self.is_open = True
        print("The book is now open.")

    def close_book(self):
        self.is_open = False
        print("The book is now closed.")

    def turn_page(self):
        if self.is_open:
            if self.current_page < self.pages:
                self.current_page += 1
                print(f"You are now on page {self.current_page}.")
            else:
                print("You are already on the last page.")
        else:
            print("You can't turn the page because the book is closed.")

    def go_to_page(self, page_number):
        if self.is_open:
            if 1 <= page_number <= self.pages:
                self.current_page = page_number
                print(f"You are now on page {self.current_page}.")
            else:
                print("Invalid page number.")
        else:
            print("You can't go to a page because the book is closed.")

    def is_long_book(self):
        return self.pages > 300



book1 = Book("The Alchemist", "Paulo Coelho", 208)
book2 = Book("The Bible", "Many Scholars", 1225)

print(book1)
book1.open_book()
book1.turn_page()
book1.turn_page()
book1.go_to_page(100)
book1.close_book()
print(book1.is_long_book())

print(book2)
book2.open_book()
book2.turn_page()
book2.turn_page()
book2.go_to_page(100)
book2.close_book()
print(book2.is_long_book())

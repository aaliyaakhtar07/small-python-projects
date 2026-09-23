class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None
    
    def __str__(self):
        if self.available:
            return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Available"
        else:
            return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Not Available"
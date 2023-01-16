class Book():
    TYPE = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight


    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"


    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPE[0], page_weight + 100)


    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPE[1], page_weight)




book = Book.hardcover('harry Portter', 1500)
light = Book.paperback('Python 101', 600)

print(book)
print(light)


class Book:

    cover = 'Hard'

    # Initialize the object attributes
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Provides a string representation of the class/object attributes
    def __str__(self):
        return 'Tile: {}, Author: {}, Pages: {}, Cover: {}'.format(
            self.title, self.author, self.pages, Book.cover)

    # Method len used to return the number of pages
    def __len__(self):
        return self.pages

    # Deletes the book object and print massage when object is gone
    def __del__(self):
        print('The book is gone!')


b = Book('Green eggs and ham', 'Rafael', 100)
print(b)  # __srt__
print(len(b))  # __len__
del(b)
print(b)

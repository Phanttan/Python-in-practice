class Book:
    """A empty class for e-book"""


if __name__ == "__main__":

    b = Book()
    b.title = 'Python programming'
    b.authors = 'Donald Trump'
    b.year = 2020
    print(b.title, b.authors, b.year) # kết quả là 'Python programming Donald Trumo 2020'
    b2 = Book()
    print(b2.title) # lỗi, không có attribute title trong object b2

def add_book(title, author):
    import requests
    base_url = "http://pulse-rest-testing.herokuapp.com/books/"
    new_book = requests.post(base_url, data={"title": title, "author": author})
    return new_book.json()


if __name__ == "__main__":
    print(add_book("Test_Book_7", "Test_Author_7"))



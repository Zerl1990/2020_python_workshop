from flask import Flask, request
from books.books_model import Books

app = Flask(__name__)
my_books = Books()


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        data = request.json
        return my_books.add(data.get("name"), data.get("author"))
    else:
        return my_books.get_all()


@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def book(book_id):
    book_id = book_id
    if request.method == 'GET':
        return my_books.get(book_id)
    elif request.method == 'PUT':
        data = request.json
        return my_books.edit(book_id, data.get("views"))
    else:
        return my_books.delete(book_id)


if __name__ == '__main__':
    app.run(debug=True)

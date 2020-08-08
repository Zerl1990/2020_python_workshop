import uuid
import collections
import logging
from flask import jsonify, abort


class Book(object):
    """Book model"""

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.views = 0

    def increase_views(self):
        self.views += 1


class Books(object):
    """Class to control book collection"""

    def __init__(self):
        """Initialize our collection"""
        self.books = dict()
        self.books["1"] = Book('Dracula', 'Bram Stoker')
        self.books["2"] = Book('Pedro Paramo', 'Juan Rulfo')
        self.books["3"] = Book('Por quien doblan las campanas', 'Ernest Hemingway')
        self.books["4"] = Book('El fin del mundo y un despiadado pais de las maravillas', 'Haruka Murakami')

    def get_all(self):
        """Get all books"""
        response = []
        for book_id in self.books.keys():
            response.append(self.__book_to_dict(book_id))
        return jsonify(response)

    def get(self, book_id):
        """Get book by id"""
        book = self.__find_book(book_id)
        book.increase_views()
        return self.__book_to_json(book_id)

    def delete(self, book_id):
        """Delete book by id"""
        self.books.pop(book_id, None)
        response = {
            'msg': f'Book {book_id} deleted'
        }
        return jsonify(response)

    def add(self, name, author):
        """Add book by id"""
        logging.debug(f'Adding book {name} - {author}')
        book_id = str(uuid.uuid1())
        self.books[book_id] = Book(name, author)
        return self.__book_to_json(book_id)

    def edit(self, book_id, views):
        """Edit book by id"""
        book = self.__find_book(book_id)
        book.views = views
        return self.__book_to_json(book_id)

    def __book_to_json(self, book_id):
        return jsonify(self.__book_to_dict(book_id))

    def __book_to_dict(self, book_id):
        book = self.__find_book(book_id)
        response = {
            'id': book_id,
            'name': book.name,
            'author': book.author,
            "views": book.views
        }
        return response

    def __find_book(self, book_id):
        if book_id in self.books:
            return self.books[book_id]
        else:
           abort(404)

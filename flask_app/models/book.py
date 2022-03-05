from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import author

class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.language = data["language"]
        self.pages = data["pages"]
        self.author_id = data["author_id"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.author = {}
    
    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, pages, language, description, author_id, created_at, updated_at) VALUES (%(title)s, %(pages)s, %(language)s, %(description)s, %(author_id)s, NOW(), NOW());"
        
        results = connectToMySQL('book_authors').query_db(query, data)
        
        return results
    
    @classmethod
    def get_books_with_authors(cls):
        query = "SELECT * FROM books LEFT JOIN authors ON author_id = authors.id;"
        
        results = connectToMySQL('book_authors').query_db(query)
        
        books = []
        
        for row in results:
            book = cls(row)
            author_data = {
                "id" : row['authors.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "created_at" : row['authors.created_at'],
                "updated_at" : row['authors.updated_at']
            }
            book.author = author.Author(author_data)
            books.append(book)
        return books
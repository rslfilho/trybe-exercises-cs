from pymongo import MongoClient


with MongoClient() as client:
    db = client.library
    books = db.books.find({"status": "PUBLISH"}, projection=['categories'])

    print(books[0])

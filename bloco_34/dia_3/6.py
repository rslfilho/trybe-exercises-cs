from pymongo import MongoClient


def list_by_category(category):
    with MongoClient() as client:
        db = client.library
        books = db.books.find({
            'categories': category
        }, {
            "title": 1,
            "_id": 0
        })

        for book in books:
            print(book['title'])


list_by_category('Mobile')

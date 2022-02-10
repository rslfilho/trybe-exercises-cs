import json
import csv


with open("books.json") as file:
    books = json.load(file)

categories = {
    category for book in books for category in book["categories"] if category
}

result = []

for category in categories:
    count = 0
    for book in books:
        if category in book["categories"]:
            count += 1
    result.append({
        "categoria": category,
        "porcentagem": count / len(books),
    })


with open("pct.csv", mode="w") as file:
    header = ["categoria", "porcentagem"]

    writer = csv.DictWriter(file, fieldnames=header)

    for row in result:
        writer.writerow(row)

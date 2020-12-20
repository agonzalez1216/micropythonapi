import csv
import os
from .models import Book

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'static/booksapi/bestsellers-with-categories.csv')
with open(path) as f:
    reader = csv.reader(f)
    next(reader, None)  # skip the headers
    for row in reader:
        _, created = Book.objects.get_or_create(
            name=row[0],
            author=row[1],
            rating=row[2],
            reviews=row[3],
            price=row[4],
            year=row[5],
            genre=row[6],
        )
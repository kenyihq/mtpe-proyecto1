import csv
from book import Book

book = Book()

def read_books(file):
    with open(file, encoding='utf-8') as f:
        reader = csv.reader(f)
        datos = []
        for i in reader:
            datos.append(i)

        
    return datos

def new_book(file):

    new_info = book.add_book()
    with open(file, 'a', encoding='utf-8') as f:
        for info in new_info:
            f.write(f'{info},')
        f.write(f'\n')

import csv

def read_books(file):
    with open(file, encoding='utf-8') as f:
        reader = csv.reader(f)
        datos = []
        for i in reader:
            datos.append(i)

        
    return datos
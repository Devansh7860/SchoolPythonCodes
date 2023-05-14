# CSV QUESTIONS

import csv

def search():
    with open('details.csv' , 'r') as fobj:
        obj = csv.reader(fobj)
        next(obj) # ignores the first row since string can't be compared with no.
        for i in obj:
            if int(i[2]) > 25:
                print(i)
search()

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Book
import csv


engine= create_engine("postgresql://cddgttjzphkwuv:1685ae007abc0fe6e9c3b16930e6070757af35fec4e7c1ce163ec95b6380fa39@ec2-3-226-59-11.compute-1.amazonaws.com:5432/d7qj61bulrq5i1")
db_session = scoped_session(sessionmaker(bind=engine))
with open('books.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        new_book= Book(isbn=row[0],name=row[1],author=row[2], year=row[3])
        db_session.add(new_book)
db_session.commit()
db_session.close()

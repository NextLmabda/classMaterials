import pickle
import os

dest = os.path.join('movieclassifier', 'pkl_objects')
if not os.path.exists(dest):
    os.makedirs(dest)


import sqlite3
import os

if os.path.exists('reviews.sqlite'):
    os.remove('reviews.sqlite')

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()
c.execute('CREATE TABLE review_db(review TEXT, sentiment INTEGER, date TEXT)')

example1 = 'I LOVE THIS MOVIE'
c.execute("INSERT INTO review_db"\
    " (review, sentiment, date) VALUES"\
    " (?, ?, datetime('now'))", (example1, 1))

example2 = 'I dislike this movie'

c.execute("INSERT INTO review_db"\
    " (review, sentiment, date) VALUES"\
    " (?, ?, datetime('now'))", (example2, 0))

conn.commit()

conn.close()

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()
c.execute("SELECT * FROM review_db")

results = c.fetchall()

conn.close()
print(results)
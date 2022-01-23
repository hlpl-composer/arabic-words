
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(current_directory, 'hlpl_arabic_words.db')


import sqlite3
def get(case):
    conn = sqlite3.connect(db)
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    
    if case=='فاعل':
       lst=cur.execute("SELECT * FROM ism_fa3il").fetchall()
       return lst 

    if case=='مفعول':
       lst=cur.execute("SELECT * FROM ism_maf3ol").fetchall()
       return lst
      
    if case=='مصدر':
       lst=cur.execute("SELECT * FROM masdar").fetchall()
       return lst
       
    if case=='فعل':
       lst=cur.execute("SELECT * FROM ar_verbs_lst").fetchall()
       return lst

    if case=='بداية-فعل':
       lst=cur.execute("SELECT * FROM v_f").fetchall()
       return lst

    if case=='نهاية-فعل':
       lst=cur.execute("SELECT * FROM v_b").fetchall()
       return lst
       
    if case=='بداية-اسم':
       lst=cur.execute("SELECT * FROM n_f").fetchall()
       return lst
       
    if case=='نهاية-اسم':
       lst=cur.execute("SELECT * FROM n_b").fetchall()
       return lst

    if case=='أداة':
       lst=cur.execute("SELECT * FROM ar_articles_lst").fetchall()
       return lst 

    if case=='connection':
       return conn       



import sqlite3
#Creating the db        # test.db is the database
conn = sqlite3.connect('dbSubmission.db')

with conn:              # Creating columns
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_documents( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_documents TEXT \
    )")
    conn.commit()
conn.close()            #Closing the door

conn = sqlite3.connect('dbSubmission.db')

with conn:              # Inserting into columns columns
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_documents(col_documents) VALUES (?)", \
                ('information.docx',))
    cur.execute("INSERT INTO tbl_documents(col_documents) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_documents(col_documents) VALUES (?)", \
                ('myImage.png',))
    cur.execute("INSERT INTO tbl_documents(col_documents) VALUES (?)", \
                ('myMovie.png',))
    cur.execute("INSERT INTO tbl_documents(col_documents) VALUES (?)", \
                ('World.txt',))
    cur.execute("INSERT INTO tbl_documents(col_documents) VALUES (?)", \
                ('data.pdf',))
    cur.execute("INSERT INTO tbl_documents(col_documents) VALUES (?)", \
                ('myPhoto.jpg',))
    conn.commit()
conn.close()            #Closing the door

conn = sqlite3.connect('dbSubmission.db')

with conn:              # Reading columns
    cur = conn.cursor()
    cur.execute("SELECT col_documents FROM tbl_documents WHERE col_documents = '.txt'")
    varDocument = cur.fetchall()
    for item in varDocument:
        msg = "txt doc: {}".format(item[0])
    print(msg)


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.png', 'World.txt', 'data.pdf', 'myPhoto.jpg')

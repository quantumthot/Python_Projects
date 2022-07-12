

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

# Tuple of documents
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.png', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#loop through each object in the tuple to find the names that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one name out of the tuple therfore (x,)
        # will denote a one element tuple for each name ending in .txt
            cur.execute("INSERT INTO tbl_documents (col_documents) VALUES (?)", (x,))
            print(x)

conn.close()



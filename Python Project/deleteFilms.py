from ffdbConnection import *
from readFilms import *
import time

def delRecord():
    #enter id of record to be updated
    filmID = input("Enter ID of record to be deleted: ")
    
    try:
        cursor.execute("DELETE FROM tblFilms WHERE filmID=" + filmID)
        conn.commit()
        print("Record " + filmID + " Deleted")

        cursor.execute('SELECT * FROM tblFilms ') # read all records from members table
        row = cursor.fetchall()# use fetchall method to fetch all records in table members
        for record in row:# iterate over the fetched records stored in the row varible above
            print(record)
    except:
        print("Record " + filmID + " Not Deleted!")
    
# delRecord()
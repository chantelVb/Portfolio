from ffdbConnection import *
import time

def addFilms():
    
    films = []
   
    filmID = cursor.lastrowid
    title = input("Enter film title: ")
    yearReleased = int(input("Enter year film released: "))
    rating = input("Enter film rating - U, PG, 12A, 15 or 18: ")
    duration = int(input("Duration of film in minutes: "))
    genre = input("Enter film genre: ")

    films.append(filmID)
    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    try:
        cursor.execute('INSERT INTO tblFilms VALUES (?,?,?,?,?,?)', films)
        conn.commit()
        print("Film Added")

        time.sleep(3)
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("Film: "+ title + " not added")
        
# addFilms()


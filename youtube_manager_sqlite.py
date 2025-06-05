# Storing data in sqlite3

import json
import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor() 

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_video():
    cursor.execute('SELECT * from videos')
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute('INSERT INTO videos(name, time) VALUES (?, ?)', (name, time))
    conn.commit()

def main():
    
    while True:
        print("\n Youtube Manager App")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        choice = input("Enter choice: ")

        match choice:
            case "1": 
                list_video()
            case "2":
                name = input("Enter the video name: ")
                time = input ("Enter the video time: ")
                add_video(name, time) 
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                print("Invalid choice")

    conn.close()
            
if __name__ == "__main__":
    main()
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
                pass
            case "2":
                pass
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
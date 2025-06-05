# Storing data in sqlite3
import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor() 

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               duration TEXT NOT NULL
    )
''')

def list_video():
    cursor.execute('SELECT * from videos')
    rows = cursor.fetchall()
    if not rows:
        print("Videos not found")
    else: 
        for row in rows:
            print(row)

def add_video(name, duration):
    cursor.execute('INSERT INTO videos(name, duration) VALUES (?, ?)', (name, duration))
    conn.commit()
    list_video()

def update_video(video_id, new_name, new_duration):
    cursor.execute('UPDATE videos SET name=?, duration=? WHERE id=?', (new_name, new_duration, video_id))
    conn.commit()
    print("Video details updated successfully")

def delete_video(video_id):
    cursor.execute('DELETE FROM videos WHERE id=?', (video_id))
    conn.commit()
    print("Video deleted successfully")

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
                duration = input ("Enter the video duration: ")
                add_video(name, duration) 
            case "3":
                list_video()
                video_id = input("Enter the video id: ")
                name = input("Enter the video name: ")
                duration = input ("Enter the video duration: ")
                update_video(video_id, name, duration) 
            case "4":
                list_video()
                video_id = input("Enter the video id: ")
                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid choice")

    conn.close()
            
if __name__ == "__main__":
    main()
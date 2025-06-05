# Storing data in mongodb
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)
db = client['youtube_manager']
videos_collection = db['videos']

def list_video():
    for video in videos_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Duration: {video['duration']}")

def add_video(name, duration):
    videos_collection.insert_one({'name': name, 'duration': duration})
    list_video()

def update_video(video_id, new_name, new_duration):
    videos_collection.update_one({'_id': ObjectId(video_id)}, {'$set': {'name': new_name, 'duration': new_duration}})
    print("Video details updated successfully")
    
def delete_video(video_id):
    videos_collection.delete_one({'_id': ObjectId(video_id)})
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
            
if __name__ == "__main__":
    main()
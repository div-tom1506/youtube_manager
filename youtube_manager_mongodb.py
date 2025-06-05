# Storing data in mongodb


def list_video():
    pass

def add_video(name, time):
    pass

def update_video(video_id, new_name, new_time):
    pass

def delete_video(video_id):
    pass

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
                list_video()
                video_id = input("Enter the video id: ")
                name = input("Enter the video name: ")
                time = input ("Enter the video time: ")
                update_video(video_id, name, time) 
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
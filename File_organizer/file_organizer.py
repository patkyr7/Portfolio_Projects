import os
import time

def path_ask(prompt):
    path = input(f"Please enter the exact path to your folder.\n{prompt}")
    return path

def choice_user(prompt):
    choice = input(prompt)
    return choice

def hidden_or_system_files(full_path):
    try:
        attrs = os.stat(full_path).st_file_attributes
        file_attribute_hidden = 0x2
        file_attribute_system = 0x4

        return bool(attrs and (file_attribute_hidden | file_attribute_system))
    except AttributeError:
        return False

acceptable_types = {"sound": {".mp3", ".aac", ".wav", ".flac", ".ogg", ".m4a"},
                    "image": {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp"},
                    "video": {".mp4", ".webm", ".mov", ".mkv", ".avi"},
                    "documents": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt", ".csv"},
                    "compressed_files": {".zip", ".rar", ".7z", ".tar"}}

scan = True


while scan:
    hidden_or_system = False
    folder_path = path_ask("Otherwise type Exit to terminate the program.\n")
    while not os.path.exists(folder_path) or folder_path.lower() == 'exit':
        if folder_path.lower() == 'exit':
            print("Exiting...")
            exit()
        if not os.path.exists(folder_path):
            print("The path is wrong or your input is not an available option. Please try again.")
            folder_path = path_ask("Otherwise type Exit to terminate the program.\n")
        items = os.listdir(folder_path)
        files = [f for f in items if os.path.isfile(os.path.join(folder_path, f))]
        
        for file in files:
            full_path = os.path.join(folder_path, file)
            name = os.path.basename(file)
            ext = os.path.splitext(file)[1].lower()
            print(f"File: {name}, Extension: {ext}")

            if file.startswith('.'):
                hidden_or_system = True
                continue
                
            if hidden_or_system_files(full_path):
                hidden_or_system = True
                continue
                
        user_choice = choice_user("Do you wish to continue with this file?\n")
        while user_choice.lower() != 'no' or choice_user.lower() != 'yes':
            time.sleep(2)
            print("I don't understand.\n")
            time.sleep(1)
            user_choice = choice_user("Do you wish to continue with this file?\n")
        time.sleep(2)

        if user_choice.lower() == 'no':
            print("Restarting process...")
            time.sleep(2)
            path_check = True
        else:
            continue
            
        if hidden_or_system == False:
            print("There are unknown type of files in the folder. Should I gather them in a folder called Unknown Files, ignore them or stop the process?\n")
            user_choice = choice_user("Type yes to create an Unknown Files subfolder and move the items there, ignore to ignore them or stop to stop the process.\n")
            while user_choice.lower() not in ['yes', 'ignore', 'stop']:
                time.sleep(2)
                print("I don't understand.")
                time.sleep(1)
                user_choice = choice_user("Type yes to create an Unknown Files subfolder and move the items there, ignore to ignore them or stop to stop the process.\n")
            if user_choice.lower() == 'yes':
                os.makedirs("Unknown Files", exist_ok=True)
            elif user_choice.lower() == 'ignore':
                continue
            elif user_choice.lower() == 'stop':
                exit()
    
    name_choice = input("How should I name the folder with the image files?\n")
    os.makedirs(name_choice, exist_ok=True)
    time.sleep(2)
    name_choice = input("How should I name the folder with the video files?\n")
    os.makedirs(name_choice, exist_ok=True)
    time.sleep(2)
    name_choice = input("How should I name the folder for the sound files?\n")
    os.makedirs(name_choice, exist_ok=True)
    time.sleep(2)
    name_choice = input("How should I name the folder for the document files?\n")
    os.makedirs(name_choice, exist_ok=True)
    time.sleep(2)
    name_choice = input("How should I name the folder for the compressed files?\n")
    os.makedirs(name_choice, exist_ok=True)
    time.sleep(2)
    
            

        
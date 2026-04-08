import os
import time
import shutil

def path_ask(prompt):
    path = input(f"Please enter the exact path to your folder.\n{prompt}")
    return path

def choice_user(prompt):
    choice = input(prompt)
    return choice

def hidden_or_system_files(full_path):
    try:
        attrs = os.stat(full_path).st_file_attributes
        return bool(attrs & (0x2 | 0x4)) 
    except AttributeError:
        return False

acceptable_types = {"sound": {".mp3", ".aac", ".wav", ".flac", ".ogg", ".m4a"},
                    "image": {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp", ".cube"},
                    "video": {".mp4", ".webm", ".mov", ".mkv", ".avi"},
                    "documents": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt", ".csv"},
                    "compressed_files": {".zip", ".rar", ".7z", ".tar"}}



scan = True


while scan:
    move_count = 0
    folders = {}
    hidden_or_system = False
    folder_path = path_ask("Otherwise type Exit to terminate the program.\n")

    if folder_path.lower() == 'exit':
        print("Exiting...")
        exit()
    while not os.path.exists(folder_path) and folder_path.lower() != 'exit':
        print("The path is wrong or your input is not an available option. Please try again.")
        folder_path = path_ask("Otherwise type Exit to terminate the program.\n")
        if folder_path.lower() == 'exit':
            print("Exiting...")
            exit()
       

    items = os.listdir(folder_path)
    files = [f for f in items if os.path.isfile(os.path.join(folder_path, f))]

    print ("The file you gave in the input has the following items:")
    for file in files:
        full_path = os.path.join(folder_path, file)
        name = os.path.basename(file)
        ext = os.path.splitext(file)[1].lower()
        print(f"File: {name}, Extension: {ext}")

        if hidden_or_system_files(full_path):
            hidden_or_system = True
            continue
            
    user_choice = choice_user("Do you wish to continue with this file?\n")
    while user_choice.lower() not in ['yes', 'no']:
        time.sleep(1)
        print("I don't understand.\n")
        time.sleep(1)
        user_choice = choice_user("Do you wish to continue with this file?\n")
    time.sleep(1)

    if user_choice.lower() == 'no':
        print("Restarting process...")
        time.sleep(1)
        continue
    else:
        print("Proceeding...")
        time.sleep(1)
        
        
    if hidden_or_system == True:
        print("There are unknown type of files in the folder. The program will ignore them.\n")
        time.sleep(1)


    name_choice = input("How should I name the folder with the image files?\n")
    folders["image"] = os.path.join(folder_path, name_choice)
    os.makedirs(folders["image"], exist_ok=True)
    time.sleep(1)
    name_choice = input("How should I name the folder with the video files?\n")
    folders["video"] = os.path.join(folder_path, name_choice)
    os.makedirs(folders["video"], exist_ok=True)
    time.sleep(1)
    name_choice = input("How should I name the folder for the sound files?\n")
    folders["sound"] = os.path.join(folder_path, name_choice)
    os.makedirs(folders["sound"], exist_ok=True)
    time.sleep(1)
    name_choice = input("How should I name the folder for the document files?\n")
    folders["documents"] = os.path.join(folder_path, name_choice)
    os.makedirs(folders["documents"], exist_ok=True)
    time.sleep(1)
    name_choice = input("How should I name the folder for the compressed files?\n")
    folders["compressed_files"] = os.path.join(folder_path, name_choice)
    os.makedirs(folders["compressed_files"], exist_ok=True)
    time.sleep(1)
    
    user_choice = choice_user("Do you wish to continue with organizing the files? This action will not be reversable.\n")
    while user_choice.lower() not in ['yes', 'no']:
        time.sleep(1)
        print("I don't understand.\n")
        time.sleep(1)
        user_choice = choice_user("Do you wish to continue with organizing the files? This action will not be reversable.\n")
    time.sleep(1)

    if user_choice.lower() == 'no':
        user_choice = choice_user("Do you wish to restart the process or close the program?\n")
        time.sleep(1)
        while user_choice.lower() not in ['close', 'restart']:
            time.sleep(1)
            print("I don't understand.\n")
            time.sleep(1)
            user_choice = choice_user("Please type Restart or Close.\n")
        if user_choice.lower() == 'close':
            print("Program shutting down...")
            exit()
        else:
            print("Restarting process...")
            time.sleep(1)
            break
    else:
        print("Proceeding...")
        time.sleep(1)        
        
    for file in files:
        full_file_path = os.path.join(folder_path, file)
        ext = os.path.splitext(file)[1].lower()

        if hidden_or_system_files(full_file_path):
                print("fuck u chat u were right")
                continue
        for category, extensions in acceptable_types.items():
            print("loop enteredc")
            print(f"checking: {file} ({ext})", flush= True)
            if ext in extensions:
                destination = os.path.join(folders[category], file)
                shutil.move(full_file_path, destination)
                print(f"matched {file} -- {category}")
                move_count += 1
                break
            
    print("Moving completed. Do you wish to organize another file?\n",
          move_count, "files were moved.\n")
    user_choice = choice_user("Type Restart to organize a new file or Exit to close the program.\n")
    while user_choice.lower() not in ['restart', 'exit']:
        time.sleep(1)
        print("I don't understand.\n")
        time.sleep(1)
        user_choice = choice_user("Type Restart to organize a new file or Exit to close the program.\n")
    time.sleep(1)
    if user_choice.lower() == 'restart':
        continue
    else:
        print("Exiting...")
        exit() 
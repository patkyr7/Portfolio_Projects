## File Organizer Bot

to do list:
1. it should scan a folder, not the subfolders for version 1.00
2. be able to sort files by type and arrange them in newly created subfolders
3. rename subfolders at creation point to user's wish
4. create folders
5. detects duplicates based on file name and size
6. unknown file types should be gathered in their own seperate subfolder together
7. it should only move files, never copy them.
8. It shall not be able to touch hidden files or os-related files

how it should work:
1. There should be an input from the user regarding the path of the desired folder to be organized.
2. It should have a loop where the user can choose a new file to organize or exit.
3. The path should be double checked, maybe through asking the user if the file's name is correct?
4. It should list the files in the folder that will be impacted and if something is wrong, it should allow the user to exit. If file/subfolder starts with . then its hidden, should be ignored.
5. It should let the user know which files will be moved together to a new folder and allow the user to name the folder or stop the prompt.
6. It should, of course, be able to move the files according to the user's wish and safely.
7. In case of detected duplicates, ask the user if their wish is to for them to be deleted. If yes, then it should move them to the recycle bin, if not, they should be moved to the subfolder based on their data type.


pseudocode:

1. promt to ask user for file path. ## done
    - user types exit: exit ## done
    - user types mambo jumbo: ask again till exit or existing path ## done
2. check if there are any crucial(os binding data) or hidden files ## done
    - if above data exists: ignore and continue ## done
3. check for unknown types of data
    -if yes: a) ask user if to move them in a seperate subfolder named unknown_files
                b) ask user if to ignore them
                c) ask if to exit
    -if no: continue
- if no valid files found: repeat loop and ask for new path
4. print the names of all the items that are in the file # done
5. confirm once again with user if they want to proceed. #done
    -if user wants to proceed: continue, otherwise: exit #done
6. check if duplicates based on items' names and sizes exist.
    - if yes: print duplicates
    a) ask to move either of them in recycling bin.
    b) ask to move items in data according subfolder
    c) ask to ignore items
    d) ask to exit        
    - if no:  continue   
7. in case an item will be moved to a subfolder and in the subfolder exists a file with the same name:
    - rename moving item to name_moved
7. print the items that will be moved to each subfolder.
a) to name the subfolder,
b) ask user to agree with the creation of subfolder, 
c) confirm to move the items to subfolder and/or
d) exit
8. print final situation of the folder, print all newly created subfolders, print all items that were moved in each subfolder seperately and in different colors
9. ask user input if they want to organize another folder
    -if yes: return to main loop and start over
    -if no: repeat = false and loop ends


groups of files:
images = .jpg, .jpeg, .png, .gif, .svg, .webp, .bmp
videos = .mp4, .webm, .mov, .mkv, .avi
sounds = .mp3, .aac, .wav, .flac, .ogg, .m4a
documents = .pdf, .doc, .docx, .xls, .xlsx, .txt, .csv
compressed files = .zip, .rar, .7z, .tar
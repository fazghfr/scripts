import os
import shutil

PATH = '\\PATH\\TO\\YOUR\\DIRECTORY' # TODO IMPORTANT : MAKE SURE TO CHANGE THIS TO YOUR DESIRED PATH.

FILE_CAT = ['documents', 'photo',  'video', 'scripts-code', 'others', 'installer-exe'] # MAKE SURE YOUR DIRECTORY DOES NOT HAVE A DIRECTORY WITH THESE NAMES

FOLDER_DOC = ['doc', 'docx', 'odt','pdf','xls', 'xlsx', 'ppt','pptx', 'pptm', 'txt', 'csv']
FOLDER_PHOTO = ['jpg', 'JPG', 'jpeg', 'png', 'PNG', 'gif', 'bmp', 'tiff', 'jfif', 'webp', 'psd', 'heic', 'mfj', 'mdj', 'xcf']
FOLDER_VIDEO = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm']
FOLDER_EXE = ["exe", "msi", "dmg", "pkg", "deb", "rpm", "AppImage", "dmg"]
FOLDER_SCRIPTS = ["py", "js", "java", "cpp", "h", "c", "cs", "html", "htm", "css", "rb", "go", 'sql', 'json']
FOLDER_AUDIO = ["mp3", "wav", "flac", "ogg", "aac", "m4a", "wma", "alac", "aiff", "mid"]
# you can add or change the list of the above arrays

def create_folder():
    for folder_name in FILE_CAT :
        if(os.path.isdir(folder_name) == False) :
            os.makedirs(folder_name)
            

# Move All file listed in arr into the folders.
# arr : a list of files inside PATH directory
def move_all():
    arr = os.listdir(os.getcwd())
    for file in arr:
        
        if os.path.isdir(file) :
            # move dir into others
            if (FILE_CAT.count(file) != 0) :
                continue;
            shutil.move(file, FILE_CAT[-2])

        elif file.split('.')[-1] in FOLDER_DOC :
            shutil.move(file, FILE_CAT[0])
        
        elif file.split('.')[-1] in FOLDER_PHOTO :
            shutil.move(file, FILE_CAT[1])

        elif file.split('.')[-1] in FOLDER_VIDEO or file.split('.')[-1] in FOLDER_AUDIO :
            shutil.move(file, FILE_CAT[2])           

        elif file.split('.')[-1] in FOLDER_SCRIPTS :
            shutil.move(file, FILE_CAT[3])
        
        elif file.split('.')[-1] in FOLDER_EXE :
            shutil.move(file, FILE_CAT[5])
        
        else :
            shutil.move(file, FILE_CAT[-2])

def start():
    os.chdir(PATH)

    create_folder()
    move_all()

start()


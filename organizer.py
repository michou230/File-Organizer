import os
import shutil 



file_extensions = {
    'PDFs' : ['.pdf', '.pdf/a'],
    'Images' : ['.jpeg', '.jpg', '.gif', '.png', '.jfif', '.svg', '.webp', '.tiff', '.bmp', '.tif', '.heic', '.psd', '.ai', '.raw', '.cr2', '.nef', '.ico', 'eps', '.indd'],
    'Documents' : ['.doc', '.docx', '.txt', '.rtf', '.pages', '.odt', '.md', '.epub', '.mobi', '.tex', '.ppt', '.pptx', '.wpd', '.log', '.py'],
    'Videos' : ['.mp4', '.mkv', '.avi', '.flv', '.wmv', '.mov', '.webm', '.vob', '.mpeg', '.mpg', '.3gp', '.m4v', '.divx', '.ogv', '.mts', '.m2ts', '.hevc'],
    'Music' : ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.wma', '.ogg', '.alac', '.aiff', '.opus', '.amr', '.mid', '.midi', '.aif', '.aifc', '.ape', '.m4b'],
    'Executables' : ['.exe', '.msi', '.bat', '.cmd', '.ps1', '.scr', '.sh'],
    'Archives' : ['.zip', '.rar', '.tar', '.gz', '.7z', '.rar5', '.iso', '.sitx', '.dmg', '.cab', '.pkg', '.apk', '.bz2'],
    'Data' : ['.csv', '.json', '.xml', '.sql', '.xlsx', '.xls', '.ods', '.tsv', '.db', '.sqlite', '.yaml', '.yml', '.parquet', '.hdf5', '.sas7bdat', '.sav'],
}

def organize_files_by_extension(directory):
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)

        if not os.path.isfile(full_path):
            continue 
            
        extension = os.path.splitext(file)[1].lower()
        moved = False
        
        for folder, extensions in file_extensions.items():
            if extension in extensions:
                destination = os.path.join(directory, folder)
                os.makedirs(destination, exist_ok=True)

                shutil.move(full_path, os.path.join(destination, file))
                moved = True
                break

        if not moved:
            destination = os.path.join(directory, "Others")
            os.makedirs(destination, exist_ok=True)
            shutil.move(full_path, os.path.join(destination, file))


def organize_by_name(directory, name):
    folder_path = os.path.join(directory, name)
    
    found = False

    for file in os.listdir(directory):

        old_path = os.path.join(directory, file)
        file_name = os.path.splitext(file)[0]

        if os.path.isfile(old_path) and file_name.lower() == name.lower():
            if not found:
                os.makedirs(folder_path, exist_ok=True)
                found = True
            new_path = os.path.join(folder_path, file)
            shutil.move(old_path, new_path)

    return found
       
                
def organize_all(directory):
    groups = {}

    for file in os.listdir(directory):
        name = os.path.splitext(file)[0]

        if name not in groups:
            groups[name] = []
        groups[name].append(file)

    for name, files in groups.items():
        destination = os.path.join(directory, name)
        os.makedirs(destination, exist_ok=True)

        for file in files:
            old_path = os.path.join(directory, file)

            if os.path.isdir(old_path):
                continue

            new_path = os.path.join(destination, file)
            shutil.move(old_path, new_path)
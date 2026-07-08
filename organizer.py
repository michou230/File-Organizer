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

def organize_files(directory):
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)

        if os.path.isfile(full_path):
            extension = os.path.splitext(file)[1].lower()
        
        for folder, extensions in file_extensions.items():
            if extension in extensions:
                destination = os.path.join(directory, folder)
                if not os.path.exists(destination):
                    os.makedirs(destination)
                shutil.move(full_path, os.path.join(destination, file))
                print("Moved:", file, "to", folder)
                break

   
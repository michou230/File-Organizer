# File Organizer

This is a python desktop app that automatically organizes files into folders based on their extension or group them by name (manual name submission or automatic name detection).

## Features
- GUI with CustomTkinter
- Automatic file sorting
- Cross-Platform suuport
- Executable app build support

Files include: **Images, Videos, Documents, PDF, Music, Data, Archive and Executables**.<br>
Any other extensions not included will be added in a folder called **Others**.<br>
If you wish an extension to be added just reach out to me ^^

Note: You CANNOT undo the changes so choose the folder you want to sort carefully.<br>
Note2: Supports Windows, Mac and Linux.
## Requirements
- Python 3.10+
- CustomTkinter

Just run this line for these requirements:

```pip install -r requirements.txt``` or ```python -m pip install -r requirements.txt```

or (if the above fails)

```pip install customtkinter==5.2.2``` or ```python -m pip install customtkinter==5.2.2```

then run *Organizer.py* for the actual app.

If you wish to make the app an executable please follow these steps:
- Download pyinstaller via:
 ```pip install pyinstaller``` or ```python -m pip install pyinstaller```
- Make sure you are in the **Organizer.py** file and open the terminal.
- Run the next command based on your OS

### Windows
```pyinstaller --onefile --windowed --icon="Assets/favicon.ico" --add-data "assets;assets" Organizer.py```

### Mac
```pyinstaller --onefile --icon="Assets/favicon.icns" --add-data "assets:assets" Organizer.py```

### Linux
```pyinstaller --onefile --windowed --icon="Assets/favicon.png" --add-data "assets:assets" Organizer.py```

Then you can find the executable app in the "dist" folder.

## LICENSE:
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

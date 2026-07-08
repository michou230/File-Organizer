import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from organizer import organize_files


selected_folder = ""

def choose_folder():
    global selected_folder
    
    selected_folder = filedialog.askdirectory()
    folder_label.configure(
        text=selected_folder,
        font = ("Segoe UI", 14, "bold"),
        text_color = "#8AD2DC",
        fg_color = "#000000",
        corner_radius = 10,
        width = 400,
        height = 40
                )
                           


def organize():
    if selected_folder:
        answer = messagebox.askyesno("Confirm", "Are you sure you want to organize the files in this folder?")
        if answer:
            organize_files(selected_folder)
            folder_label.configure(
                text="Operation done ^^ files organized successfully.",
                font = ("Segoe UI", 14, "bold"),
                text_color = "#4B905D",
                fg_color = "#000000",
                corner_radius = 10,
                width = 400,
                height = 40
                )
            app.after(5000, lambda: reset())
            os.startfile(selected_folder)
        else:
            folder_label.configure(
                text="Operation canceled.",
                font = ("Segoe UI", 14, "bold"),
                text_color = "#AC4242",
                fg_color = "#000000",
                corner_radius = 10,
                width = 400,
                height = 40
                )
            app.after(3000, lambda: reset())
    else:
        folder_label.configure(
            text="No folder selected. Please choose a folder first.",
            font = ("Segoe UI", 14, "bold"),
            text_color = "#AC4242",
            fg_color = "#000000",
            corner_radius = 10,
            width = 400,
            height = 40
            )


def reset():
    global selected_folder
    selected_folder = ""
    folder_label.configure(
        text="No folder selected",
        font = ("Segoe UI", 14, "bold"),
        text_color = "#616766",
        fg_color = "#000000",
        corner_radius = 10,
        width = 400,
        height = 40
        )

#Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Window
app  = ctk.CTk()
app.configure(fg_color="#190e2d")
app.title("File Organizer")
app.geometry("600x400")

# ORGANZE BUTTON
button = ctk.CTkButton(
    app, 
    text="🔁 Organize Files", 
    command=organize,
    width = 200,
    height = 50,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#44838B",                   
    hover_color = "#71B8C1",                 )
button.pack(pady=70)

# FOLDER SELECTION BUTTON
browse_button = ctk.CTkButton(
    app,
    text="📂 Choose Folder",
    command=choose_folder,
    width = 200,
    height = 50,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#35163F",                   
    hover_color = "#4F245D",  
    )
browse_button.pack()

# FOLDER LABEL 
folder_label = ctk.CTkLabel(
    app, 
    text="No folder selected",
    font = ("Segoe UI", 14, "bold"),
    text_color = "#616766",
    fg_color = "#000000",
    corner_radius = 10,
    width = 400,
    height = 40
    )
folder_label.pack(pady=50)


#EXE
app.mainloop()

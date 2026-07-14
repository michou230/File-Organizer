import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from PIL import Image
from organizer import organize_files_by_extension, organize_by_name, organize_all

##IMAGE

back_icon = ctk.CTkImage(
    light_image = Image.open("back.png"),
    size = (35, 35)
)
############################FUNCTIONS
selected_folder = ""
def choose_folder():
    global selected_folder
    
    selected_folder = filedialog.askdirectory()
    for label in [folder_label_name, folder_label_extension]:
        label.configure(
        text=selected_folder,
        font = ("Segoe UI", 14, "bold"),
        text_color = "#8AD2DC",
        fg_color = "#000000",
        corner_radius = 10,
        width = 400,
        height = 40
                )
                           
def back_btn():
    show_main_page()
    reset()

def confirmation():
    answer = messagebox.askyesno("Confirm", "Are you sure you want to organize the files in this folder?")
    if answer:
        return True
    else:
        return False

def operation_done():
    for label in [folder_label_name, folder_label_extension]:
        label.configure(
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

def operation_cancelled():
    for label in [folder_label_name, folder_label_extension]:
        label.configure(
        text="Operation cancelled.",
        font = ("Segoe UI", 14, "bold"),
        text_color = "#AC4242",
        fg_color = "#000000",
        corner_radius = 10,
        width = 400,
        height = 40
        )
    app.after(3000, lambda: reset())
    
def no_folder_selected():
    for label in [folder_label_name, folder_label_extension]:
        label.configure(
        text="No folder selected. Please choose a folder first.",
        font = ("Segoe UI", 14, "bold"),
        text_color = "#AC4242",
        fg_color = "#000000",
        corner_radius = 10,
        width = 400,
        height = 40
        )
    

def extension_organize():
    if not selected_folder:
        no_folder_selected()
    else:
        answer = confirmation()
        if answer == True:
            organize_files_by_extension(selected_folder)
            operation_done()
        else:
            operation_cancelled()

def name_organize():
    if not selected_folder:
        no_folder_selected()
    else:
        answer = confirmation()
        if answer == True:
            mode = radio_var.get()
            if mode == "custom":
                dialog = ctk.CTkInputDialog(text="Enter the file name to organize by:", title="File Name")
                name = dialog.get_input()
                if not name or not name.strip():
                    messagebox.showwarning(
                    "Invalid Name",
                    "Please enter a valid name."
                    )
                    return
                
                name = name.strip()
                success = organize_by_name(selected_folder, name)
                if success:
                    operation_done()
                else:
                    messagebox.showwarning(
                    "No files found",
                    f"No files matching '{name}' were found.")
            else:
                organize_all(selected_folder)
                operation_done()
        else:
            operation_cancelled()
        

def reset():
    global selected_folder
    selected_folder = ""
    for label in [folder_label_name, folder_label_extension]:
        label.configure(
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
app.title("File Organizer")
app.geometry("600x400")


def show_main_page():
    main_frame.pack(fill = "both", expand = True)
    name_frame.pack_forget()
    extension_frame.pack_forget()


def show_name_page():
    main_frame.pack_forget()
    extension_frame.pack_forget()
    name_frame.pack(fill = "both", expand = True)
    

def show_extension_page():
    main_frame.pack_forget()
    name_frame.pack_forget()
    extension_frame.pack(fill = "both", expand = True)

#####################################################################MAIN PAGE

main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True)

title = ctk.CTkLabel(
    main_frame,
    text="File Organizer",
    font = ("Times New Roman", 24, "italic")
    )
title.pack(pady=30)

extension_button = ctk.CTkButton(
    main_frame, 
    text="Organize by extension", 
    command=show_extension_page,
    width = 200,
    height = 50,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#909320",                   
    hover_color = "#CB911D"
     )
extension_button.pack(pady=30)

name_button = ctk.CTkButton(
    main_frame,
    text="Organize by name", 
    width = 200,
    height = 50,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#B63C50",                   
    hover_color = "#89364B",
    command = show_name_page
)
name_button.pack(pady = 10)

#############################################################organize by name frame
radio_var = ctk.StringVar()
name_frame = ctk.CTkFrame(app)

title2 = ctk.CTkLabel(
    name_frame,
    text = "Organize by name",
    font = ("Times New Roman", 24, "italic")
)
title2.pack(pady=15)

description = ctk.CTkLabel(
    name_frame,
    text = "Select an option.",
    font = ("Times New Roman", 20, "bold")
)
description.pack(pady=5)

all_button = ctk.CTkRadioButton(
    name_frame,
    text = "Group all matching names",
    font= ("Segoe UI", 16),
    radiobutton_width = 30,
    radiobutton_height = 30,
    hover=True,
    variable = radio_var,
    value = "all"
)
all_button.pack()

custom_button = ctk.CTkRadioButton(
    name_frame,
    text = "Submit a specific name",
    font= ("Segoe UI", 16),
    radiobutton_width = 30,
    radiobutton_height = 30,
    hover=True,
    variable = radio_var,
    value = "custom"
)
custom_button.pack(pady = 10)

name_org_button = ctk.CTkButton(
    name_frame, 
    text="🔁 Organize Files", 
    command= name_organize,
    width = 200,
    height = 35,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#44838B",                   
    hover_color = "#71B8C1"                 
    )
name_org_button.pack(pady= 20)

browse_button = ctk.CTkButton(
    name_frame,
    text="📂 Choose Folder",
    command=choose_folder,
    width = 200,
    height = 35,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#35163F",                   
    hover_color = "#4F245D",  
    )
browse_button.pack(pady = 5)

# FOLDER LABEL 
folder_label_name = ctk.CTkLabel(
    name_frame, 
    text="No folder selected",
    font = ("Segoe UI", 14, "bold"),
    text_color = "#616766",
    fg_color = "#000000",
    corner_radius = 10,
    width = 400,
    height = 40
    )
folder_label_name.pack(pady=10)

back_button = ctk.CTkButton(
    name_frame,
    text = "",
    image = back_icon,
    width = 40,
    command = back_btn,
    fg_color="transparent"
)
back_button.place(x= 15, y=15)

##############################################################organize by extension frame

extension_frame = ctk.CTkFrame(app)

title2 = ctk.CTkLabel(
    extension_frame,
    text = "Organize by extension",
    font = ("Times New Roman", 24, "italic")
)
title2.pack(pady=25)


# ORGANZE BUTTON
ex_org_button = ctk.CTkButton(
    extension_frame, 
    text="🔁 Organize Files", 
    command= extension_organize,
    width = 200,
    height = 50,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#44838B",                   
    hover_color = "#71B8C1"                 
    )
ex_org_button.pack(pady=10)

# FOLDER SELECTION BUTTON
browse_button = ctk.CTkButton(
    extension_frame,
    text="📂 Choose Folder",
    command=choose_folder,
    width = 200,
    height = 50,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#35163F",                   
    hover_color = "#4F245D",  
    )
browse_button.pack(pady = 30)

# FOLDER LABEL 
folder_label_extension = ctk.CTkLabel(
    extension_frame, 
    text="No folder selected",
    font = ("Segoe UI", 14, "bold"),
    text_color = "#616766",
    fg_color = "#000000",
    corner_radius = 10,
    width = 400,
    height = 40
    )
folder_label_extension.pack(pady=10)

back_button = ctk.CTkButton(
    extension_frame,
    text = "",
    image = back_icon,
    width = 40,
    command = back_btn,
    fg_color="transparent"
)
back_button.place(x=15, y=15)

#EXE
app.mainloop()
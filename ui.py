import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from PIL import Image
from organizer import organize_files_by_extension, organize_by_name, organize_all

##IMAGE

extension_back_icon = ctk.CTkImage(
    light_image = Image.open("blue_back.png"),
    size = (35, 35)
)

name_back_icon = ctk.CTkImage(
    light_image = Image.open("pink_back.png"),
    size = (35, 35)
)

info_back_icon = ctk.CTkImage(
    light_image = Image.open("green_back.png"),
    size = (35, 35)
)

info_about_icon = ctk.CTkImage(
    light_image = Image.open("about.png"),
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
        text_color = "#639BA2",
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
        )
    app.after(5000, lambda: reset())
    os.startfile(selected_folder)

def operation_cancelled():
    for label in [folder_label_name, folder_label_extension]:
        label.configure(
        text="Operation cancelled.",
        font = ("Segoe UI", 14, "bold"),
        text_color = "#C25A5A",
        )
    app.after(3000, lambda: reset())
    
def no_folder_selected():
    for label in [folder_label_name, folder_label_extension]:
        label.configure(
        text="No folder selected. Please choose a folder first.",
        font = ("Segoe UI", 14, "bold"),
        text_color = "#AC4242",
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
            elif mode == "all":
                organize_all(selected_folder)
                operation_done()
            else:
                messagebox.showinfo(
                "No option selected",
                "Please choose a name organization method first."
            )
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
        )
        

#Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Window
app  = ctk.CTk()
app.title("File Organizer")
app.geometry("600x400")
app.resizable(False, False)

def show_main_page():
    main_frame.pack(fill = "both", expand = True)
    name_frame.pack_forget()
    extension_frame.pack_forget()
    info_frame.pack_forget()


def show_name_page():
    main_frame.pack_forget()
    extension_frame.pack_forget()
    info_frame.pack_forget()
    name_frame.pack(fill = "both", expand = True)
    

def show_extension_page():
    main_frame.pack_forget()
    name_frame.pack_forget()
    info_frame.pack_forget()
    extension_frame.pack(fill = "both", expand = True)


def show_info_page():
    main_frame.pack_forget()
    name_frame.pack_forget()
    extension_frame.pack_forget()
    info_frame.pack(fill = "both", expand = True)

#####################################################################MAIN PAGE

main_frame = ctk.CTkFrame(
    app,
    fg_color= "#064B3C",
    )
main_frame.pack(fill="both", expand=True)


title = ctk.CTkLabel(
    main_frame,
    text="File Organizer",
    fg_color="transparent",
    text_color="#71BDAC",
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
    fg_color = "#020444",                   
    hover_color = "#1C1E5F",
    text_color="#51E1EC"
     )
extension_button.pack(pady=30)

name_button = ctk.CTkButton(
    main_frame,
    text="Organize by name", 
    width = 200,
    height = 50,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#2B0852",                   
    hover_color = "#37175C",
    text_color="#AA5984",
    command = show_name_page
)
name_button.pack(pady = 10)

about_button = ctk.CTkButton(
    main_frame,
    text = "",
    image = info_about_icon,
    width = 40,
    command = show_info_page,
    fg_color="transparent"
)
about_button.place(x=550, y=0)

#############################################################organize by name frame
radio_var = ctk.StringVar()
name_frame = ctk.CTkFrame(
    app,
    fg_color="#2B0852"
    )

title2 = ctk.CTkLabel(
    name_frame,
    text = "Organize by name",
    font = ("Times New Roman", 24, "italic", "bold"),
    text_color="#AA5984"
)
title2.pack(pady=15)

description = ctk.CTkLabel(
    name_frame,
    text = "Select an option.",
    font = ("Times New Roman", 12, "bold"),
    text_color="#AA5984"
)
description.pack()

all_button = ctk.CTkRadioButton(
    name_frame,
    text = "Group all matching names",
    font= ("Segoe UI", 17),
    radiobutton_width = 15,
    radiobutton_height = 15,
    hover=True,
    variable = radio_var,
    value = "all",
    text_color="#AE1E6B",
    fg_color="#3D0A25",
    border_color="#E77FB6",
    hover_color="#F04AA2"
)
all_button.pack(pady = 10)

custom_button = ctk.CTkRadioButton(
    name_frame,
    text = "Submit a specific name",
    font= ("Segoe UI", 17),
    radiobutton_width = 15,
    radiobutton_height = 15,
    hover=True,
    variable = radio_var,
    value = "custom",
    text_color="#AE1E6B",
    fg_color="#3D0A25",
    border_color="#E77FB6",
    hover_color="#F04AA2"
)
custom_button.pack(pady = 10)

name_org_button = ctk.CTkButton(
    name_frame, 
    text="🔁 Organize Files", 
    command= name_organize,
    width = 200,
    height = 50,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#5200AF",                   
    hover_color = "#690BD4",
    text_color="#C08AFE"                 
    )
name_org_button.pack(pady= 20)

browse_button = ctk.CTkButton(
    name_frame,
    text="📂 Choose Folder",
    command=choose_folder,
    width = 200,
    height = 50,
    corner_radius = 15,
    font = ("Times New Roman", 16),                   
    fg_color = "#61107C",                   
    hover_color = "#4F245D",  
    text_color="#F89BFF"
    )
browse_button.pack(pady = 10)

# FOLDER LABEL 
folder_label_name = ctk.CTkLabel(
    name_frame, 
    text="No folder selected",
    font = ("Segoe UI", 14, "bold"),
    text_color = "#616766",
    fg_color = "#2C0B41",
    corner_radius = 10,
    width = 400,
    height = 40
    )
folder_label_name.pack(pady=10)

back_button = ctk.CTkButton(
    name_frame,
    text = "",
    image = name_back_icon,
    width = 40,
    command = back_btn,
    fg_color="transparent"
)
back_button.place(x= 15, y=15)

##############################################################organize by extension frame

extension_frame = ctk.CTkFrame(
    app,
    fg_color="#020444"
    )

title2 = ctk.CTkLabel(
    extension_frame,
    text = "Organize by extension",
    font = ("Times New Roman", 24, "italic"),
    text_color="#51E1EC"
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
    fg_color = "#0C0F6B",                   
    hover_color = "#303387",
    text_color= "#51E1EC"           
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
    fg_color = "#3357C2",                   
    hover_color = "#1438A4",  
    text_color="#809CF1"
    )
browse_button.pack(pady = 30)

# FOLDER LABEL 
folder_label_extension = ctk.CTkLabel(
    extension_frame, 
    text="No folder selected",
    font = ("Segoe UI", 14, "bold"),
    text_color = "#363938",
    fg_color = "#398DA4",
    corner_radius = 10,
    width = 400,
    height = 40
    )
folder_label_extension.pack(pady=10)

back_button = ctk.CTkButton(
    extension_frame,
    text = "",
    image = extension_back_icon,
    width = 40,
    command = back_btn,
    fg_color="transparent"
)
back_button.place(x=15, y=15)

#########################################################info frame
info_frame = ctk.CTkFrame(
    app,
    fg_color="#064B3C"
    )

title3 = ctk.CTkLabel(
    info_frame,
    text = "About",
    font = ("Times New Roman", 24, "italic", "bold"),
    text_color="#71bdac"
)
title3.pack(pady=15)

description1 = ctk.CTkLabel(
    info_frame,
    text="""File Organizer is a simple application that helps you sort your files into folders.

    
    Current features include automatic sorting (by name or extension) or custom name sorting.

    
    If you find any bugs or issues please contact me on GitHub (michou230)

    
    You can use this app however you want as long as you follow the License set with it.

    
    Enjoy ^^

    
    Hope it actually helped :p
""",
    font=("Times New Roman", 14),
    wraplength=515,
    justify="center",
    text_color="#94c9b9"
)

description1.pack(pady=20)


back_button = ctk.CTkButton(
    info_frame,
    text = "",
    image = info_back_icon,
    width = 40,
    command = back_btn,
    fg_color="transparent"
)
back_button.place(x=15, y=15)

#EXE
app.mainloop()
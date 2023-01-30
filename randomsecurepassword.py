import customtkinter
import random
from tkinter import *
import pyperclip

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.title("")
root.resizable(False,False)
root.attributes('-alpha',0.9) 
root.geometry("320x135")
root.title("Secure Password Generator")

label = customtkinter.CTkLabel(master=root, width=50,height=10, bg_color="#242424", fg_color="#242424", font=("Roboto", 15))
label.configure(text="")
label.pack(pady=10)
label2 = customtkinter.CTkLabel(master=root, width=50,height=10, bg_color="#242424", fg_color="#242424", font=("Roboto",10))
label2.configure(text="")
label2.pack(pady=10)

# Function to generate 32 random numbers and convert it to its respective ASCII characters
def securePass():
    rawpass = []
    for _ in range(32):
        rawpass.append(chr(random.randint(33, 126)))
    return "".join(rawpass)

def generate_button():
    password = securePass()
    pyperclip.copy(password)
    label.configure(text=password)
    label2.configure(text="Password copied.")

CTkFrame = customtkinter.CTkFrame(root)
CTkFrame.pack(fill="both", expand=True)

generate_button = customtkinter.CTkButton(CTkFrame, text="Generate and copy.", command=generate_button)
generate_button.pack(pady=20)

root.mainloop()
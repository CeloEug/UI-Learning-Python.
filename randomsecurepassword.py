import customtkinter, random, requests, pyperclip, mouse
from tkinter import *

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.title("")
root.attributes('-alpha',0.95) 
root.overrideredirect(True)
#root.geometry("400x140")
root.resizable(False,False)
root.bind("<B1-Motion>", lambda e: event(e, Mode=True))
root.bind("<ButtonRelease-1>", lambda e: standard_bind())

# Function to generate random numbers and convert it to its respective ASCII characters, and then concatenate them with a random word.
def securePass():
    rawpass = []
    wordpass = requests.get("https://www.mit.edu/~ecprice/wordlist.10000").text.splitlines()[random.randint(4, 9999)]
    for char in wordpass:
        if char == "a":
            rawpass.append("@")
        elif char == "e":
            rawpass.append("3")
        elif char == "I":
            rawpass.append("1")
        elif char == "S":
            rawpass.append("$")
        elif char == "O":
            rawpass.append("0")
        else:
            rawpass.append(char)
    
    while len(rawpass) < 12:
        rawpass.append(chr(random.randint(48, 122)))
        if rawpass[-1] == "a":
            rawpass[-1] = "@"
        elif rawpass[-1] == "e":
            rawpass[-1] = "3"
        elif rawpass[-1] == "I":
            rawpass[-1] = "1"
        elif rawpass[-1] == "S":
            rawpass[-1] = "$"
        elif rawpass[-1] == "O":
            rawpass[-1] = "0"
            
    return "".join(rawpass[:12])

def generate_button():
    password = securePass()
    pyperclip.copy(password)
    label.configure(text=password)
    label2.configure(text="Password copied.")

def stop_program():
    root.destroy()

def standard_bind():
   root.bind('<B1-Motion>', lambda e: event(e, Mode=True))

def event(widget, Mode=False):
    global x, y
    if Mode:
        x = widget.x
        y = widget.y
    root.bind('<B1-Motion>', lambda e: event(e))
    root.geometry('+%d+%d' % (mouse.get_position()[0]-x, mouse.get_position()[1]-y))

bardrag = customtkinter.CTkButton(root, corner_radius=0, width=25, height=25,text="☰", fg_color="#242424", hover_color="#242424")
buttonexit = customtkinter.CTkButton(root, corner_radius=0, width=40, height=25,text="✖", fg_color="#242424", hover_color="#a22630", command=stop_program)
label = customtkinter.CTkLabel(root, width=200,height=10, bg_color="#242424", fg_color="#242424", font=("Roboto", 15))
label2 = customtkinter.CTkLabel(root, width=50,height=10, bg_color="#242424", fg_color="#242424", font=("Roboto", 12))  #bg_color="#242424", fg_color="#242424"
generatebutton = customtkinter.CTkButton(root, width=50,height=10, fg_color=("#8e57f7"), hover_color=("#a269ff"), text="Generate", command=generate_button, font=("Roboto-Bold", 15))

bardrag.grid(row=0, pady=5, padx=10, column=0,  sticky='nw')

buttonexit.grid(row=0, column=4,  sticky='ne')

label.configure(text="")
label.grid(row=1, pady=10, padx=10, column=1)

label2.configure(text="")
label2.grid(row=2, column=1)

generatebutton.grid(row=3, pady=15,column=1, columnspan=2)

root.mainloop()

import customtkinter
from tkinter import *
import mouse

root = customtkinter.CTk()
root.title("")
root.resizable(False,False)
root.attributes('-alpha',0.8) 
root.overrideredirect(True)
root.bind("<B1-Motion>", lambda e: event(e, Mode=True))
root.bind("<ButtonRelease-1>", lambda e: standard_bind())
root.geometry("200x400")

global x, y

customtkinter.set_appearance_mode("dark")

e = customtkinter.CTkEntry(master=root, width=200,height=50, corner_radius=10, bg_color="#242424", fg_color="#242424", font=("Roboto-Bold.ttf", 30), justify="right", border_width=0, border_color="white")
s = customtkinter.CTkLabel(master=root, width=50,height=20, corner_radius=10, bg_color="#242424", fg_color="#242424", font=("Roboto", 15), justify="right")
s.configure(text="") 

#Calculator Buttons
def button_clear():
    e.delete(0, END)
    s.configure(text="") 

def when_click(number):
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    global operation
    operation = "+"
    global f_num 
    f_num = float(first_number)
    e.delete(0, END)
    s.configure(text = str(first_number) + (" "+ operation)) 

def button_sub():
    first_number = e.get()
    global operation
    operation = "-"    
    global f_num 
    f_num = float(first_number)
    e.delete(0, END)
    s.configure(text = str(first_number) + (" "+ operation)) 

def button_mul():
    first_number = e.get()
    global operation
    operation = "x"
    global f_num 
    f_num = float(first_number)
    e.delete(0, END)
    s.configure(text = str(first_number) + (" "+ operation)) 

def button_div():
    first_number = e.get()
    global operation
    operation = "/"
    global f_num 
    f_num = float(first_number)
    e.delete(0, END)
    s.configure(text = str(first_number) + (" "+ operation)) 

def button_per():
    first_number = e.get()
    global operation
    operation = "1/"
    global f_num 
    f_num = float(first_number)
    e.delete(0, END)
    s.configure(text = (operation) + str(first_number) ) 

def button_exp():
    first_number = e.get()
    global operation
    operation = "**"
    global f_num 
    f_num = float(first_number)
    e.delete(0, END)
    s.configure(text = str(first_number) + (" "+ operation)) 

def button_rad():
    first_number = e.get()
    global operation
    operation = "**/"
    global f_num 
    f_num = float(first_number)
    e.delete(0, END)
    s.configure(text = str(first_number) + (" "+ operation)) 

def button_equal():
    chest_number = e.get()
    e.delete(0, END)
    if operation == "+":
        e.insert(0, f_num + float(chest_number))
    elif operation == "-":
        e.insert(0, float(chest_number) - f_num)
    elif operation == "x":
        e.insert(0, f_num * float(chest_number))
    elif operation == "/":
        
        e.insert(0, 1/(float(chest_number)) * f_num)
    elif operation == "1/":
        e.insert(0, 1/f_num)
    elif operation == "**":
        e.insert(0, f_num ** float(chest_number))
    elif operation == "**/":
        e.insert(0, float(chest_number) ** (1/f_num))
    else:
        e.insert(0, "error")

##program functionality
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

##numbers
button0 = customtkinter.CTkButton(root, text="0", hover_color="#ffc041", fg_color="#ffa500",width=150, height=50, command=lambda:when_click(0))
button1 = customtkinter.CTkButton(root, text="1", hover_color="#ffc041", fg_color="#ffa500",width=50, height=50, command=lambda:when_click(1))
button2 = customtkinter.CTkButton(root, text="2", hover_color="#ffc041", fg_color="#ffa500",width=50, height=50,command=lambda:when_click(2))
button3 = customtkinter.CTkButton(root, text="3", hover_color="#ffc041", fg_color="#ffa500",width=50, height=50,command=lambda:when_click(3))
button4 = customtkinter.CTkButton(root, text="4", hover_color="#ffc041", fg_color="#ffa500",width=50, height=50,command=lambda:when_click(4))
button5 = customtkinter.CTkButton(root, text="5", hover_color="#ffc041", fg_color="#ffa500",width=50, height=50,command=lambda:when_click(5))
button6 = customtkinter.CTkButton(root, text="6", hover_color="#ffc041", fg_color="#ffa500",width=50, height=50,command=lambda:when_click(6))
button7 = customtkinter.CTkButton(root, text="7", hover_color="#ffc041", fg_color="#ffa500",width=50, height=50,command=lambda:when_click(7))
button8 = customtkinter.CTkButton(root, text="8", hover_color="#ffc041", fg_color="#ffa500",width=50, height=50,command=lambda:when_click(8))
button9 = customtkinter.CTkButton(root, text="9", hover_color="#ffc041", fg_color="#ffa500",width=50, height=50,command=lambda:when_click(9))

##operations
buttonplus = customtkinter.CTkButton(root, width=50, height=50,text="+", fg_color="azure4", hover_color="azure3", command=button_add)
buttonminus = customtkinter.CTkButton(root, width=50, height=50,text="-", fg_color="azure4", hover_color="azure3", command=button_sub)
buttondiv = customtkinter.CTkButton(root, width=50, height=50,text="÷", fg_color="azure4", hover_color="azure3", command=button_div)
buttonmul = customtkinter.CTkButton(root, width=50, height=50,text="x", fg_color="azure4", hover_color="azure3", command=button_mul)
buttonper = customtkinter.CTkButton(root, width=50, height=50,text="⅟", fg_color="azure4", hover_color="azure3", command=button_per)
buttonexp = customtkinter.CTkButton(root, width=50, height=50,text="xˣ", fg_color="azure4", hover_color="azure3", command=button_exp)
buttonrad = customtkinter.CTkButton(root, width=50, height=50,text="√ˣ", fg_color="azure4", hover_color="azure3", command=button_rad)

##functions
buttonres = customtkinter.CTkButton(root, width=50, height=100,text="=", fg_color="#a22630", hover_color="#c63a4b", command=button_equal)
buttonclear = customtkinter.CTkButton(root, width=100, height=50,text="C", fg_color="azure4", hover_color="azure3", command=button_clear)
buttonback = customtkinter.CTkButton(root, width=50, height=50,text=".", fg_color="azure4", hover_color="azure3", command=lambda:when_click("."))
buttonexit = customtkinter.CTkButton(root, corner_radius=0, width=40, height=25,text="✖", fg_color="#242424", hover_color="#a22630", command=stop_program)
bardrag = customtkinter.CTkButton(root, corner_radius=0, width=25, height=25,text="☰", fg_color="#242424", hover_color="#242424")

#grid assembling
buttonclear.grid(row=7, column=0, rowspan=1, columnspan=2, sticky='ew')
buttonback.grid(row=7, column=2, sticky='s')
buttonmul.grid(row=7, column=3) 

button0.grid(row=6, column=0, columnspan=3, sticky='w')
buttondiv.grid(row=6, column=3)

button1.grid(row=5, column=0, sticky='w')
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
buttonplus.grid(row=5, column=3)

button4.grid(row=4, column=0, sticky='w')
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
buttonminus.grid(row=4, column=3)

button7.grid(row=3, column=0, sticky='w')
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

buttonper.grid(row=2, column=0, sticky='nw')
buttonexp.grid(row=2, column=1, sticky='n')
buttonrad.grid(row=2, column=2, sticky='n')
buttonres.grid(row=2, column=3, rowspan=2)

e.grid(row=1, column=0, columnspan=4, sticky='n')
s.grid(row=1, column=0, columnspan=4, sticky='nw')

buttonexit.grid(row=0, column=3, sticky='e')
bardrag.grid(row=0, column=0, rowspan=4, sticky='nw')


root.mainloop()
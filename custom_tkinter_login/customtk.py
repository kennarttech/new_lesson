#importing required modules
import tkinter
import customtkinter
from tkinter import *
from PIL import ImageTk,Image



customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("850x540+240+80")
app.title('Login')
# app.iconbitmap("New_research/custom_tkinter_login/KM.ico")


def register():
    reg = customtkinter.CTk()
    reg.geometry('400x400')
    reg.title('Reset password')
    app.destroy()


def button_function():
    app.destroy()            # destroy current window and creating new one 
    w = customtkinter.CTk()  
    w.geometry("1380x720")
    w.title('Welcome')
    l1=customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
    l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
    w.mainloop()
    


img1=ImageTk.PhotoImage(Image.open("New_research/custom_tkinter_login/pattern.png"))

l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
l2.place(x=50, y=45)


entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username', corner_radius=6)
entry1.place(x=50, y=95, height=32)
entry1.focus()


entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*", corner_radius=6)
entry2.place(x=50, y=150, height=32)


l3 = customtkinter.CTkButton(master=frame, fg_color='#393939', hover_color='teal',
                            border_width=0, text="Forget password?",
                            font=('Century Gothic',12), command=register)
l3.place(x=129,y=198)


#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240, height=32)


img2=customtkinter.CTkImage(Image.open("New_research/custom_tkinter_login/Gsvg.webp").resize((20,20), Image.Resampling.BICUBIC))

img3=customtkinter.CTkImage(Image.open("New_research/custom_tkinter_login/124010.png").resize((20,20), Image.Resampling.BICUBIC))

button2= customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button2.place(x=50, y=290, height=30)

button3= customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button3.place(x=170, y=290, height=30)




# You can easily integrate authentication system 

app.mainloop()

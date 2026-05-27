from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    screen = Tk()
    screen.geometry("375x398")

    #Icon
    image_icon = PhotoImage(file="key.png")
    screen.iconphoto(False,image_icon)
    
    screen.title("Encription Text")
    screen.mainloop()

main_screen()

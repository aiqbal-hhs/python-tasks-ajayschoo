import os
import Intro_Frames
import customtkinter
import time
import threading
from PIL import ImageTk
from tkinter import *

# This function when the user clicks the ckeck out button it will dsiplay a frame and restart the whole code
def restart():
    Intro_Frames.window.destroy()
    os.startfile('Henderson_Pizza_Palace_Tkinter.py')
def chect_out():
    thank_you_window = Toplevel(Intro_Frames.window)
    thank_you_window.overrideredirect(True)
    thank_you_window.configure(background='white')
    thank_you_window.update()
    height_thank_you = 90
    width_thank_you = 500
    width_of_window = Intro_Frames.window.winfo_width()
    height_of_window = Intro_Frames.window.winfo_height()
    # Putting the message box window corners in a way to make the middle of message box in middle of main window
    x_value_main_window = Intro_Frames.window.winfo_x()
    y_value_mai_window = Intro_Frames.window.winfo_y()
    x = ((width_of_window / 2) - (width_thank_you / 2)) + x_value_main_window
    y = ((height_of_window / 2) - (height_thank_you / 2)) + y_value_mai_window
    thank_you_window.geometry(f"{width_thank_you}x{height_thank_you}+{int(x)}+{int(y)}")
    #thank_you_window.wait_window()
    check_image = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\tick image resized.jpg")
    fake_button_as_thank_you = customtkinter.CTkButton(thank_you_window, text_font=("Bahnschrift SemiBold", 22), image= check_image, text_color='#12C000', text='Thank you for Ordering from\nHenderson Pizza Palace', border_color='black', border_width=2, height=90, width=500, fg_color='white', hover_color='white')
    fake_button_as_thank_you.pack()
    thank_you_window.after(2000, restart)







# All the Moduels
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import customtkinter
import mouse

# This run when the cancel button is clicked
def normal_button():
        helper_pop_up.destroy()
        Intro_Frames.help_button.entryconfig("Help", state = "normal")
        # Undisbales the main window
        #Intro_Frames.window.wm_attributes('-disabled', False)
        Intro_Frames.window.focus_set()







# general info
def general_info():
    order_page_helper.destroy()
    next_button.configure(text="Finish",command =  normal_button, padx= 55)
    general_info = Frame(custom_message_frame, bg='white', height='130')
    general_info.grid(row=0, column=0)

    general_help_title = Label(general_info, text="General Info:", font=("Georgia", 12),background='white', border=0)
    general_help_title.grid(row=0, column=0, sticky='nw')

    global info_image
    info_image = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\info icon.png")
    packing_info_image = Label(general_info, image=info_image, background='white', border=0)
    packing_info_image.grid(row=1, column=0, pady=(30, 10), padx=20, sticky='w')

    info_for_general = Label(general_info, text="""1: Maximun of  5  pizzas allowed at onces.
    2: You need one order in Order List to Check Out.""", background='white', font=('Georgia', 10))
    info_for_general.grid(row=1, column=1, sticky='nesw')



# even more information on different pages if next is clicked on the button
def order_page_help():
    global order_page_helper
    detail_page_helper.destroy()
    order_page_helper = Frame(custom_message_frame,bg = 'white', height='130')
    order_page_helper.grid(row=0,column=0)


    order_help_title = Label(order_page_helper, text="Order Page Info:", font=("Georgia", 12), background='white', border=0)
    order_help_title.grid(row=0, column=0, sticky='nw')

    global info_image
    info_image = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\info icon.png")
    packing_info_image = Label(order_page_helper, image=info_image, background='white', border=0)
    packing_info_image.grid(row=1, column=0, pady=(30, 10), padx=20, sticky='w')

    info_for_order_page = Label(order_page_helper, text= """Press or click the "Order list" in the menu bar to go back to the pervious page.""", background='white', font=('Georgia', 10))
    info_for_order_page.grid(row=1, column=1, sticky='nesw')




# even more information on different pages if next is clicked on the button
def detail_page_info():
    global detail_page_helper
    menu_helper.destroy()
    global detail_page_helper
    detail_page_helper = Frame(custom_message_frame,bg = 'white', height='130')
    detail_page_helper.grid(row=0,column=0)

    delailed_help_title = Label(detail_page_helper, text="Detailed Pizza Page Info:", font=("Georgia", 12), background='white', border=0)
    delailed_help_title.grid(row=0, column=0, sticky='nw')

    global info_image
    info_image = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\info icon.png")
    packing_info_image = Label(detail_page_helper, image=info_image, background='white', border=0)
    packing_info_image.grid(row=1, column=0, pady=(30, 10), padx=20, sticky='w')

    info_for_detailed_page = Label(detail_page_helper, text= """Your changes will be saved until you have added them 
    to the Order List""", background='white', font=('Georgia', 10))
    info_for_detailed_page.grid(row=1, column=1, sticky='nesw')


# more information on differnt pages if next is clicked on the button
def menu_page_info():
    global menu_helper
    home_page_help.destroy()
    menu_helper = Frame(custom_message_frame,bg = 'white', height='130')
    menu_helper.grid(row=0,column=0)

    menu_help_title = Label(menu_helper, text="Menu Page Info:", font=("Georgia", 12), background='white', border=0)
    menu_help_title.grid(row = 0, column = 0, sticky='nw')

    global info_image
    info_image = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\info icon.png")
    packing_info_image = Label(menu_helper, image=info_image, background='white', border=0)
    packing_info_image.grid(row=1, column=0, pady=(30, 10), padx=20, sticky='w')


    # info writeup
    info_for_menu_page = Label(menu_helper, text= """Click on "Add" to view any pizza in detail.""", background='white', font=('Georgia', 10))
    info_for_menu_page.grid(row=1, column=1, sticky='nesw')

# mini windowfor meassges
def helper_slide():
    global helper_pop_up
    helper_pop_up = Toplevel(Intro_Frames.window)
    #helper_pop_up.title("Help")
    helper_pop_up.overrideredirect(True)
    # Disabling the main window so the user have to like delete on the toplevel window to get back
    #Intro_Frames.window.wm_attributes('-disabled', True)


    #helper_pop_up.iconbitmap(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\pizza_zEj_icon.ico")
    helper_pop_up.config(background='grey')
    helper_pop_up.wm_attributes("-transparent", 'grey')

    # Cnetering the message box in the app
    width_message_box = 600
    height_message_box = 160
    Intro_Frames.window.update()
    width_of_window = Intro_Frames.window.winfo_width()
    height_of_window = Intro_Frames.window.winfo_height()
    # Putting the message box window corners in a way to make the middle of message box in middle of main window
    x_value_main_window = Intro_Frames.window.winfo_x()
    y_value_mai_window = Intro_Frames.window.winfo_y()
    x = ((width_of_window/2) - (width_message_box/2)) + x_value_main_window
    y = ((height_of_window/2) - (height_message_box/2)) + y_value_mai_window
    helper_pop_up.geometry(f"{width_message_box}x{height_message_box}+{int(x)}+{int(y)}")
    helper_pop_up.resizable(False, False)


    # Creating a frame for all the button and widgets to be placed in
    global custom_message_frame
    custom_message_frame = customtkinter.CTkFrame(helper_pop_up, corner_radius=20, fg_color='white')
    custom_message_frame.pack(expand=1, fill=BOTH)


    # Frame for home page help
    global home_page_help
    home_page_help = Frame(custom_message_frame, bg = 'white', height='130')
    home_page_help.grid(row=0,column=0)


    # Image of info sign that work for all helper frames
    global info_image
    info_image = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\info icon.png")


    # Information about home page
    title_of_help_home = Label(home_page_help, text = "Home Page Info:", font=("Georgia", 12), background='white', border=0)
    title_of_help_home.grid(row=0, column=0, sticky='nw')
    packing_info_image = Label(home_page_help, image= info_image, background='white', border=0)
    packing_info_image.grid(row=1, column = 0, pady=(30,10), padx = 20, sticky='w')
    info_for_home = Label(home_page_help, text="""Tap "Start Ording" to go to Menu page,
    or use the menu buttons to switch between pages according to their title.""" , background='white', font=('Georgia', 10))
    info_for_home.grid(row=1, column=1, sticky='nesw')


    # All the info about buttons' next and cancel
    labelframe_for_buttons = LabelFrame(custom_message_frame, background='white', border=0)
    labelframe_for_buttons.place(x = 280, y = 117)


    # function for nect button
    global counter_moves
    counter_moves = 0
    def next_move():
        global counter_moves
        if counter_moves == 0:
            menu_page_info()
        elif counter_moves == 1:
            detail_page_info()
        elif counter_moves == 2:
            order_page_help()
        elif counter_moves == 3:
            general_info()
        counter_moves += 1


    # Button in the main window to avoid repeation
    global next_button
    next_button = Button(labelframe_for_buttons, text="Next Info", font=('Bahnschrift SemiBold', 10), pady = 5, padx = 45, command = next_move,background='white',activebackground='#1AFF09', cursor='hand2')
    next_button.grid(row=0, column=1, sticky='e', pady=0, padx = (20,0))


    # changing colour when hover on both button
    def hover_on_for_next(e):
        next_button.config(bg = '#1AFF09', fg = 'black')
    def hover_off_for_next(e):
        next_button.config(bg = 'white', fg = 'black')

    next_button.bind("<Enter>", hover_on_for_next)
    next_button.bind("<Leave>", hover_off_for_next)

    cancel_button = Button(labelframe_for_buttons, text="Cancel", font=('Bahnschrift SemiBold', 10), pady = 5, padx = 45, command = normal_button ,background='white',activebackground='red', cursor='hand2')
    cancel_button.grid(row=0, column=0, sticky='e', pady=0)


    # changing colour when hover on both button
    def hover_on_for_cancel(e):
        cancel_button.config(bg = 'red', fg = 'black')
    def hover_off_for_cancel(e):
        cancel_button.config(bg = 'white', fg = 'black')

    cancel_button.bind('<Enter>', hover_on_for_cancel)
    cancel_button.bind('<Leave>', hover_off_for_cancel)


    # Button get disbaled when clicked once and get backed to normal when the cross is pressed
    Intro_Frames.help_button.entryconfig("Help", state = "disabled")




# Again Intro Frames here to avoid import loop
import Intro_Frames



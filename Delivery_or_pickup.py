# All the Moduels
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import time as t
import customtkinter
import Intro_Frames
import Warning_message_box
import expanding_pages
import Total_cost_order

customtkinter.set_appearance_mode('light')


#  Creating a variabel that tell other moduel wheather a user has chosen pick up or delivery. 0 being pick up and 1 being delivery
global delivery_or_pickup_teller
delivery_or_pickup_teller = 0

# Frame for the delivery and pickup page on order list frame
frame_for_delivery_pickup = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white')
frame_for_delivery_pickup.place(x=0, y =0, width=1066, height=600)


# background image for the delivery image.
image_fordelivery_pixkup_page = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\delivery_pixkup image.jpg")
putting_delivery_image = customtkinter.CTkLabel(frame_for_delivery_pickup, image=image_fordelivery_pixkup_page, anchor='nw')
putting_delivery_image.place(x = -8, y = 0)

# Delivery boyt and pickup photo
image_for_delivery = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\delivery boy editedresziednow.png")
image_for_pick_up = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\pickupeditedcroppedresized.png")


# alsoing putting the chocie frame in function so user can go back when want
def back_to_choice():
    hiding_option_frames()
    frame_for_delivery_pickup.place(x=0, y=0, width=1066, height=600)


def pickup_function():
    hiding_option_frames()
    pickup_frame.place(x=0, y=0, width=1066, height=600)


def delivery_finction():
    hiding_option_frames()
    delivery_frame.place(x=0, y=0, width=1066, height=600)


def hiding_option_frames():
    delivery_frame.place_forget()
    frame_for_delivery_pickup.place_forget()
    pickup_frame.place_forget()


# Pickup and delivery buttons wiht images
delivery_button_bigger = customtkinter.CTkButton(frame_for_delivery_pickup, text='  Delivery', text_font=('robot', 30), cursor='hand2', image=image_for_delivery, corner_radius=10, height=80, width=340, text_color='black', hover_color ='#0C9FD6', command=delivery_finction, fg_color= "#57A1E8")
delivery_button_bigger.place(y = 375, x = 363)
pickup_button = customtkinter.CTkButton(frame_for_delivery_pickup, text='  Pick Up', text_font=('robot', 30), cursor='hand2', image=image_for_pick_up, corner_radius=10, height=80, width=340, text_color='black', fg_color='#FF9D22', hover_color='#DE940C', command=pickup_function)
pickup_button.place(y = 480, x = 363)

# frame for both options
pickup_frame = Frame(Intro_Frames.order_list_frame, bg ="#F2F2F2")
delivery_frame = Frame(Intro_Frames.order_list_frame,  bg ="#F2F2F2")


# time detail for delivery page
delivery_label_time = customtkinter.CTkLabel(delivery_frame, text="DELIVERY TIME:", text_color='black', border = 0, text_font=('Bahnschrift SemiBold', 18))
delivery_label_time.grid(row =0, column=0,sticky= 'nw', padx=300, pady=(15, 0) )


# time frame for delivery page
time_frame = customtkinter.CTkFrame(delivery_frame, width=450, height=100, fg_color='white')
time_frame.grid(row=1, column=0,sticky= 'nw', padx=300, pady=(0, 30))


# Label for the deliveryd detail
delivery_label = customtkinter.CTkLabel(delivery_frame, text="DELIVERY DETAIL: ($3 Charge)", text_color='black', border = 0, text_font=('Bahnschrift SemiBold', 18))
delivery_label.grid(row =2, column=0,sticky= 'nw', padx=300, pady=(15, 5) )


# mini frame in delivery frame
mini_delivery_frame = customtkinter.CTkFrame(delivery_frame, height=250, width=450, fg_color = 'white')
mini_delivery_frame.grid(row=3, column=0,sticky=N, padx=300, pady=(0,40), ipady=8)


# This function create a menu file when the user clicks the confirm button
delivery_button_displayer = Menu(Intro_Frames.page_menu_of3, tearoff=False)


# Delivery time display
delivery_time_display_label = Label(Intro_Frames.total_cost_frame, text="", background='white', font=("Bahnschrift SemiLight", 13))

def add_delivery_to_order_list():

    global delivery_or_pickup_teller

    # Name error handling
    name_is_string = name_entry_box.entry_box.get()
    separate_name = name_is_string.split(" ")
    combined_name_as_one = ""
    for letter_in_name in separate_name:
        combined_name_as_one += letter_in_name
    if combined_name_as_one.isalpha() == True:
        name_length = len(name_entry_box.entry_box.get())
        if name_length <= 1:
            name_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            name_entry_box.title_of_requirment_outside.configure(foreground='red')
            name_entry_box.warning.configure(text='Not a purpoer Full Name.')
            return 'break'
        elif name_length > 1:
            pass
    elif combined_name_as_one.isalpha() == False:
        name_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)
        name_entry_box.title_of_requirment_outside.configure(foreground='red')
        name_entry_box.warning.configure(text='Not a purpoer Full Name.')
        return 'break'


    # Phone error handling
    if phone_number_entry_box.entry_box.get().isnumeric() == True:
        phone_number_length = len(phone_number_entry_box.entry_box.get())
        if phone_number_length < 9 or phone_number_length > 9:
            phone_number_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            phone_number_entry_box.title_of_requirment_outside.configure(foreground='red')
            phone_number_entry_box.warning.configure(text='Requires 9 digits and only digits allowed.')
            return 'break'
        elif phone_number_length == 9:
            pass
    elif phone_number_entry_box.entry_box.get().isnumeric() == False:
        phone_number_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
        phone_number_entry_box.title_of_requirment_outside.configure(foreground='red')
        phone_number_entry_box.warning.configure(text='Requires 9 digits and only digits allowed.')
        return 'break'


    # Unit error handling
    if unit_entry_box.entry_box.get().isnumeric() == True:
        unit_length = len(unit_entry_box.entry_box.get())
        if unit_length <= 0:
            unit_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            unit_entry_box.title_of_requirment_outside.configure(foreground='red')
            unit_entry_box.warning.configure(text='Not a purpoer Unit Number.')
            return "break"
        elif unit_length > 0:
            pass
    elif unit_entry_box.entry_box.get().isnumeric() == False:
        unit_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
        unit_entry_box.title_of_requirment_outside.configure(foreground='red')
        unit_entry_box.warning.configure(text='Not a purpoer Unit Number.')
        return 'break'


    # Street number error handling
    if street_entry_box.entry_box.get().isnumeric() == True:
        street_number_length = len(street_entry_box.entry_box.get())
        if street_number_length <= 0:
            street_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            street_entry_box.title_of_requirment_outside.configure(foreground='red')
            street_entry_box.warning.configure(text='Not a purpoer Street Number.')
            return "break"
        elif street_number_length > 0:
            pass
    elif street_entry_box.entry_box.get().isnumeric() == False:
        street_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
        street_entry_box.title_of_requirment_outside.configure(foreground='red')
        street_entry_box.warning.configure(text='Not a purpoer Street Number.')
        return 'break'



    # Street Name error handling
    street_name_is_string = street_name_entry_box.entry_box.get()
    separate_street_name = street_name_is_string.split(" ")
    combined_street_name_as_one = ""
    for letter_in_street_name in separate_street_name:
        combined_street_name_as_one += letter_in_street_name
    if combined_street_name_as_one.isalpha() == True:
        street_name_length = len(street_name_entry_box.entry_box.get())
        if street_name_length <= 1:
            street_name_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            street_name_entry_box.title_of_requirment_outside.configure(foreground='red')
            street_name_entry_box.warning.configure(text='Not a purpoer Street Name.')
            return 'break'
        elif street_name_length > 1:
            pass
    elif combined_street_name_as_one.isalpha() == False:
        street_name_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)
        street_name_entry_box.title_of_requirment_outside.configure(foreground='red')
        street_name_entry_box.warning.configure(text='Not a purpoer Street Name.')
        return 'break'


    # Suburb Name error handling
    suburb_name_is_string = suburb_name_entry_box.entry_box.get()
    separate_suburb_name = suburb_name_is_string.split(" ")
    combined_suburb_name_as_one = ""
    for letter_in_suburb_name in separate_suburb_name:
        combined_suburb_name_as_one += letter_in_suburb_name
    if combined_suburb_name_as_one.isalpha() == True:
        suburb_name_length = len(suburb_name_entry_box.entry_box.get())
        if suburb_name_length <= 1:
            suburb_name_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            suburb_name_entry_box.title_of_requirment_outside.configure(foreground='red')
            suburb_name_entry_box.warning.configure(text='Not a purpoer Suburb Name.')
            return 'break'
        elif suburb_name_length > 1:
            pass
    elif combined_suburb_name_as_one.isalpha() == False:
        suburb_name_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)
        suburb_name_entry_box.title_of_requirment_outside.configure(foreground='red')
        suburb_name_entry_box.warning.configure(text='Not a purpoer Suburb Name.')
        return 'break'


    # Postcode error handling
    if postcode_entry_box.entry_box.get().isnumeric() == True:
        postcode_number_length = len(postcode_entry_box.entry_box.get())
        if postcode_number_length < 4 or postcode_number_length > 4:
            postcode_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            postcode_entry_box.title_of_requirment_outside.configure(foreground='red')
            postcode_entry_box.warning.configure(text='Require 4 didgits for a PostCode.')
            return "break"
        elif postcode_number_length == 4:
            pass
    elif postcode_entry_box.entry_box.get().isnumeric() == False:
        postcode_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
        postcode_entry_box.title_of_requirment_outside.configure(foreground='red')
        postcode_entry_box.warning.configure(text='Require 4 didgits for a PostCode.')
        return 'break'


    # Telling the code that this a delivery so add three dollars
    delivery_or_pickup_teller = 1

    # packing display labels
    # Name display packing
    name_display_label.grid(row=0, column=0, pady=(15,0), padx= (10,4), sticky='w')
    name_display_label.configure(text = f"Delivery To: {name_entry_box.entry_box.get().title()}")
    # Phone display packing
    phone_display_label.grid(row=1, column=0, pady=(15, 0), padx=(10, 4), sticky='w')
    phone_display_label.configure(text=f"Phone Number: {phone_number_entry_box.entry_box.get()}")
    # street name display packing
    address_display_label.grid(row=2, column=0, pady=(15, 0), padx=(10, 4), sticky='w')
    address_display_label.configure(text=f"Address: {unit_entry_box.entry_box.get()}/{street_entry_box.entry_box.get()} {street_name_entry_box.entry_box.get().title()} {suburb_name_entry_box.entry_box.get().title()} {postcode_entry_box.entry_box.get()}")
    # delivery time display
    delivery_time_display_label.grid(row=3, column=0, pady=(15, 0), padx=(10, 4), sticky='w')
    delivery_time_display_label.configure(text=f"""Delivery Time: {todays_day}/{month}  {update_hours}:{updating_min} {t.strftime("%p")}""")
    # Delivery charge display
    delivery_charge_display_label.grid(row=4, column=0, pady=(15, 0), padx=(10, 4), sticky='w')
    delivery_charge_display_label.configure(text = f"Delivery Charge: $3")
    # Configure the total cost to 3 dollars as now deliveryas been added
    total_label.grid(row=5, column=0, pady=(15, 20), padx=(10, 4), sticky='w')
    # A new variabel for total totla cost in Delivery moduel
    if delivery_or_pickup_teller == 1:
        Total_cost_order.checker_delivery_or_pickup()
    # Puts the name in the delivery in the menu
    name_to_delivery = name_entry_box.entry_box.get()
    Intro_Frames.page_menu_of3.add_cascade(label=f" Delivery To: {name_to_delivery.title()}", font=('Robot',10), menu = delivery_button_displayer )
    delivery_button_displayer.add_command(label="Change", font=('Robot',10), command = Intro_Frames.run_again_delivery_and_pickup)
    # Deleting the frames for delivery and choice frame.
    delivery_frame.destroy()
    frame_for_delivery_pickup.destroy()









# confirm button
confirm_button = customtkinter.CTkButton(delivery_frame, text = 'Confirm', text_font=('Bahnschrift SemiBold', 20), cursor='hand2', corner_radius = 6, text_color='white', hover_color ='#858585', fg_color= '#9B9B9B', height=40, width=250, command= add_delivery_to_order_list)
confirm_button.grid(row=4, column=0)

# A mini frame inside the time frame to get a better palcement
now_time_frame = customtkinter.CTkFrame(time_frame, borderwidth=0, bg_color='white', fg_color='white')
now_time_frame.grid(row=0, columnspan=2,column=0, padx=3, pady=5)

# tiny labelframe for order time and order date
date_label_frame = LabelFrame(now_time_frame, background='white', width = 450, height=60, borderwidth=0)
date_label_frame.grid(column=0, row = 1, sticky='w', padx = (2,10), pady = (5,2))


# Time and date updates from real time
def timer_set():
    hours = t.localtime()
    minutes = t.gmtime()
    global updating_min,update_hours
    updating_min = minutes.tm_min
    update_hours = hours.tm_hour
    updating_min = minutes.tm_min + 40
    adding_together = ""
    if updating_min >= 60:
        update_hours = hours.tm_hour + 1
        updating_min -=  60
        spaces_between_mins = " ".join(str(updating_min))
        removing_space = spaces_between_mins.split(" ")
        if len(removing_space) > 1:
            removing_space.pop(1)
            removing_space.append("0")
            for one_int in removing_space:
                adding_together += one_int
            updating_min = adding_together
        else:
            updating_min = 10
    else:
        spaces_between_mins = " ".join(str(updating_min))
        removing_space = spaces_between_mins.split(" ")
        if len(removing_space) > 1:
            removing_space.pop(1)
            removing_space.append("0")
            for one_int in removing_space:
                adding_together += one_int
            updating_min = adding_together
        else:
            updating_min = 10

    # Time in delivery
    today_time.config(text=f"""{update_hours}:{updating_min} {t.strftime("%p")}""")
    today_time.after(100, timer_set)




# Order date detail
todays_day = t.strftime("%a")
month = t.strftime("%m")
year = t.strftime("%y")


order_date_label = Label(date_label_frame, text="Order Date:", font= ('Bahnschrift SemiBold',13), borderwidth=0, background='white', foreground='black')
order_date_label.grid(row=0, column =0, pady=(3,0), padx=(5, 5), sticky='w')

today_date = customtkinter.CTkLabel(date_label_frame, text = f"{todays_day}/{month}/{year}", text_font = ("robot",15), bg_color='white', corner_radius=8, fg_color='#F2F2F2', width=200, height=30)
today_date.grid(row=1, column =0, pady=(0,3), padx=(5, 5))


#Another mini labelframe on the side in the delivery
time_label_frame = LabelFrame(now_time_frame, background='white', width = 450, height=60, borderwidth=0)
time_label_frame.grid(column=1, row = 1, sticky='w', padx= (2,10), pady=(5,2))

order_time_label = Label(time_label_frame, text="Order Time:", font= ('Bahnschrift SemiBold',13), borderwidth=0, background='white', foreground='black')
order_time_label.grid(row=0, column =1, pady=(3,0), padx=(5, 5), sticky='w')

today_time = customtkinter.CTkLabel(time_label_frame, text = f"", text_font = ("robot",15), bg_color='white', corner_radius=8, fg_color='#F2F2F2', width=200, height=30)
today_time.grid(row=1, column =1, pady=(0,3), padx=(5, 5))




# Setting the focus on delivery frame and other frame if the user clicks out of the entry box
delivery_frame.bind("<Button-1>", lambda e: delivery_frame.focus_set())
time_frame.canvas.bind("<Button-1>", lambda e: time_frame.focus_set())
mini_delivery_frame.canvas.bind("<Button-1>", lambda e: mini_delivery_frame.focus_set())
confirm_button.canvas.bind("<Button-1>", lambda e: confirm_button.focus_set())




# adding entry boxes in the mini_delivery frame
class Entry_generator():
    def __init__(self, master_frame, requirment_title, requirment_row, requirment_column, requirement_columnspan, warning_message, outside_title):
        self.mini_labelframe_for_each_requirment = LabelFrame(master_frame, border=0, bg = 'white')
        self.mini_labelframe_for_each_requirment.grid(row = requirment_row, column= requirment_column, pady= (5,0), padx=6, columnspan = requirement_columnspan,sticky='nw')
        self.title_of_requirment_outside = Label(self.mini_labelframe_for_each_requirment, text= outside_title, fg='blue', font=('robot', 8), bg= 'white')
        self.title_of_requirment_outside.grid(row=0, column=0, sticky='SW', padx=2)
        self.entry_box = customtkinter.CTkEntry(self.mini_labelframe_for_each_requirment, placeholder_text = requirment_title, corner_radius = 5, fg_color = 'white', border_color='#A7A7A7', border_width = 2, width =  210)
        self.entry_box.grid(row=1, column=0, sticky='s')
        self.warning = Label(self.mini_labelframe_for_each_requirment, text = warning_message, foreground='red', font=('robot',7), background='white', border=0)



# Name entry box and all the error telling detail here
name_entry_box = Entry_generator(mini_delivery_frame,'e.g: Ajay (Max 26  Characters)', 0, 0, 1, "Exceeded max length of 26", "Full Name")



# Function that take of errors in the name entry box and all the detail about name function
def errors_telling_name(e):
    # This the lneght error that could happen in the entry box. So the min is -1, and max is 26
    length_of_name = len(name_entry_box.entry_box.get() + e.char)
    if length_of_name < 0:
        name_entry_box.title_of_requirment_outside.configure(foreground='blue')
    elif length_of_name >= 0 and length_of_name < 26:
        name_entry_box.title_of_requirment_outside.configure(foreground='blue')
        name_entry_box.warning.grid_forget()
    elif length_of_name > 26:
        name_entry_box.title_of_requirment_outside.configure(foreground='red')
        name_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)


def errors_for_backspace_and_delete_name(e):
    # This the lneght error that could happen in the entry box. So the min is -1, and max is 26
    length_of_name = len(name_entry_box.entry_box.get()  + e.char)
    try:
        selection_length_of_name = len(name_entry_box.entry_box.selection_get())
        final_length_name = length_of_name - selection_length_of_name
        if length_of_name < 0:
            return 'break'
        elif final_length_name < 29:
            name_entry_box.title_of_requirment_outside.configure(foreground='blue')
            name_entry_box.warning.grid_forget()
        elif final_length_name > 27:
            name_entry_box.title_of_requirment_outside.configure(foreground='red')
            name_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)
    except TclError:
        if length_of_name < 0:
            return 'break'
        elif length_of_name >= 0 and length_of_name < 29:
            name_entry_box.title_of_requirment_outside.configure(foreground='blue')
            name_entry_box.warning.grid_forget()
        elif length_of_name > 27:
            name_entry_box.title_of_requirment_outside.configure(foreground='red')
            name_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)


name_entry_box.entry_box.bind("<Key>", errors_telling_name)
name_entry_box.entry_box.bind('<BackSpace>', errors_for_backspace_and_delete_name)
name_entry_box.entry_box.bind('<Delete>', errors_for_backspace_and_delete_name)
name_entry_box.entry_box.bind("<Control-c>", lambda _: "break")
name_entry_box.entry_box.bind("<Control-v>", lambda _: "break")




# Phone number entry box and all the error telling detail
phone_number_entry_box = Entry_generator(mini_delivery_frame,'e.g: 641234242: (Max 9#)', 0, 1, 1, "Requires 9 digits or have gaps.", "Phone Number")


def error_phone(e):
    # Eaching key will be counted and only 9 keyboard entre at once.
    phone_number_entry_box_length = len(phone_number_entry_box.entry_box.get() + e.char)
    _phone_turn_list = phone_number_entry_box.entry_box.get() + e.char
    in_list_phone = _phone_turn_list.split(" ")
    if phone_number_entry_box_length < 0:
        phone_number_entry_box.title_of_requirment_outside.configure(foreground='red')
    elif phone_number_entry_box_length >= 0 and phone_number_entry_box_length < 9:
        phone_number_entry_box.title_of_requirment_outside.configure(foreground='blue')
        phone_number_entry_box.warning.grid_forget()
        if "" in in_list_phone:
            phone_number_entry_box.title_of_requirment_outside.configure(foreground='red')
            phone_number_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            phone_number_entry_box.warning.configure(text ="Spaces can not be added")
            return 'break'
    elif phone_number_entry_box_length > 9:
        phone_number_entry_box.title_of_requirment_outside.configure(foreground='red')
        phone_number_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)
        phone_number_entry_box.warning.configure(text = "Requires 9 digits or have gaps.")

def error_removing_phone(e):
    # This the lneght error that could happen in the entry box. So the min is -1, and max is 26
    phone_number_entry_box_length = len(phone_number_entry_box.entry_box.get()  + e.char)
    try:
        selection_length_of_phone = len(phone_number_entry_box.entry_box.selection_get())
        final_length_phone = phone_number_entry_box_length - selection_length_of_phone
        if phone_number_entry_box_length < 0:
            return "break"
        elif final_length_phone < 11:
            phone_number_entry_box.title_of_requirment_outside.configure(foreground='blue')
            phone_number_entry_box.warning.grid_forget()
        elif final_length_phone > 11:
            phone_number_entry_box.title_of_requirment_outside.configure(foreground='red')
            phone_number_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
    except TclError:
        if phone_number_entry_box_length <= -1:
            return "break"
        elif phone_number_entry_box_length >= 0 and phone_number_entry_box_length < 12:
            phone_number_entry_box.title_of_requirment_outside.configure(foreground='blue')
            phone_number_entry_box.warning.grid_forget()
        elif phone_number_entry_box_length > 11:
            phone_number_entry_box.title_of_requirment_outside.configure(foreground='red')
            phone_number_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)

phone_number_entry_box.entry_box.bind("<Key>", error_phone)
phone_number_entry_box.entry_box.bind("<BackSpace>", error_removing_phone)
phone_number_entry_box.entry_box.bind('<Delete>', error_removing_phone)
phone_number_entry_box.entry_box.bind("<Control-c>", lambda _: "break")
phone_number_entry_box.entry_box.bind("<Control-v>", lambda _: "break")



# All the unit entry box detail here
unit_entry_box = Entry_generator(mini_delivery_frame,'e.g: 4: (Max 9#)', 1, 0, 1, "Exceeded max length of 9 or have gaps.", "Unit Number")


def error_unit(e):
    # Eaching key will be counted and only 9 keyboard entre at once.
    length_of_unit = len(unit_entry_box.entry_box.get() + e.char)
    _unit_turn_list = unit_entry_box.entry_box.get() + e.char
    in_list_unit = _unit_turn_list.split(" ")
    if length_of_unit <= -1:
        unit_entry_box.title_of_requirment_outside.configure(foreground='red')
    elif length_of_unit >= 0 and length_of_unit < 9:
        unit_entry_box.title_of_requirment_outside.configure(foreground='blue')
        unit_entry_box.warning.grid_forget()
        if "" in in_list_unit:
            unit_entry_box.title_of_requirment_outside.configure(foreground='red')
            unit_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            unit_entry_box.warning.configure(text ="Spaces can not be added")
            return 'break'
    elif length_of_unit > 9:
        unit_entry_box.title_of_requirment_outside.configure(foreground='red')
        unit_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)
        unit_entry_box.warning.configure(text="Exceeded max length of 9 or have gaps.")


def error_removing_unit(e):
    # This the lneght error that could happen in the entry box. So the min is -1, and max is 26
    length_of_unit = len(unit_entry_box.entry_box.get()  + e.char)
    # getting the lenght of the selection part
    try:
        selection_length_unit = len(unit_entry_box.entry_box.selection_get())
        final_length_unit = length_of_unit - selection_length_unit
        if length_of_unit < 0:
            return "break"
        elif final_length_unit < 11:
            unit_entry_box.title_of_requirment_outside.configure(foreground='blue')
            unit_entry_box.warning.grid_forget()
        elif final_length_unit > 11:
            unit_entry_box.title_of_requirment_outside.configure(foreground='red')
            unit_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
    except TclError:
        if length_of_unit < 0:
            return "break"
        elif length_of_unit >= 0 and length_of_unit < 12:
            unit_entry_box.title_of_requirment_outside.configure(foreground='blue')
            unit_entry_box.warning.grid_forget()
        elif length_of_unit > 11:
            unit_entry_box.title_of_requirment_outside.configure(foreground='red')
            unit_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)


unit_entry_box.entry_box.bind("<Key>", error_unit)
unit_entry_box.entry_box.bind("<BackSpace>", error_removing_unit)
unit_entry_box.entry_box.bind('<Delete>', error_removing_unit)
unit_entry_box.entry_box.bind("<Control-c>", lambda _: "break")
unit_entry_box.entry_box.bind("<Control-v>", lambda _: "break")



# All the unit entry box detail here
street_entry_box = Entry_generator(mini_delivery_frame,'e.g: 90: (Max 9#)', 1, 1, 1, "Exceeded max length of 9 or have gaps.", "Street Number")


def error_street(e):
    # Eaching key will be counted and only 9 keyboard entre at once.
    length_of_street = len(street_entry_box.entry_box.get() + e.char)
    _street_turn_list = street_entry_box.entry_box.get() + e.char
    in_list_street = _street_turn_list.split(" ")
    if length_of_street <= -1:
        street_entry_box.title_of_requirment_outside.configure(foreground='red')
    elif length_of_street >= 0 and length_of_street < 9:
        street_entry_box.title_of_requirment_outside.configure(foreground='blue')
        street_entry_box.warning.grid_forget()
        if "" in in_list_street:
            street_entry_box.title_of_requirment_outside.configure(foreground='red')
            street_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            street_entry_box.warning.configure(text ="Spaces can not be added")
            return 'break'
    elif length_of_street > 9:
        street_entry_box.title_of_requirment_outside.configure(foreground='red')
        street_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)
        street_entry_box.warning.configure(text="Exceeded max length of 9 or have gaps.")

def error_removing_street(e):
    # This the lneght error that could happen in the entry box. So the min is -1, and max is 26
    length_of_street = len(street_entry_box.entry_box.get()  + e.char)
    # getting the lenght of the selection part
    try:
        selection_length_street = len(street_entry_box.entry_box.selection_get())
        final_length_street = length_of_street - selection_length_street
        if length_of_street < 0:
            return "break"
        elif final_length_street < 11:
            street_entry_box.title_of_requirment_outside.configure(foreground='blue')
            street_entry_box.warning.grid_forget()
        elif final_length_street > 11:
            street_entry_box.title_of_requirment_outside.configure(foreground='red')
            street_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
    except TclError:
        if length_of_street < 0:
            return "break"
        elif length_of_street >= 0 and length_of_street < 12:
            street_entry_box.title_of_requirment_outside.configure(foreground='blue')
            street_entry_box.warning.grid_forget()
        elif length_of_street > 11:
            street_entry_box.title_of_requirment_outside.configure(foreground='red')
            street_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)


street_entry_box.entry_box.bind("<Key>", error_street)
street_entry_box.entry_box.bind("<BackSpace>", error_removing_street)
street_entry_box.entry_box.bind('<Delete>', error_removing_street)
street_entry_box.entry_box.bind("<Control-c>", lambda _: "break")
street_entry_box.entry_box.bind("<Control-v>", lambda _: "break")



# All the unit entry box detail here
street_name_entry_box = Entry_generator(mini_delivery_frame,'e.g: Bruce Mclaren', 2, 0, 2, "","Street")
street_name_entry_box.entry_box.configure(width=60)
def error_street(e):
    # Eaching key will be counted and only 9 keyboard entre at once.
    length_of_street_name = len(street_name_entry_box.entry_box.get() + e.char)
    if length_of_street_name <= -1:
        street_name_entry_box.title_of_requirment_outside.configure(foreground='red')
    elif length_of_street_name >= 0 and length_of_street_name < 1000:
        street_name_entry_box.title_of_requirment_outside.configure(foreground='blue')
        street_name_entry_box.warning.grid_forget()




street_name_entry_box.entry_box.bind("<Key>", error_street)
street_name_entry_box.entry_box.bind("<Control-c>", lambda _: "break")
street_name_entry_box.entry_box.bind("<Control-v>", lambda _: "break")


# All the unit entry box detail here
suburb_name_entry_box = Entry_generator(mini_delivery_frame,'e.g: New Lynn', 3, 0, 1, "","Subrub")

def error_suburb(e):
    # Eaching key will be counted and only 9 keyboard entre at once.
    length_of_suburb_name = len(suburb_name_entry_box.entry_box.get() + e.char)
    if length_of_suburb_name <= -1:
        suburb_name_entry_box.title_of_requirment_outside.configure(foreground='red')
    elif length_of_suburb_name >= 0 and length_of_suburb_name < 1000:
        suburb_name_entry_box.title_of_requirment_outside.configure(foreground='blue')
        suburb_name_entry_box.warning.grid_forget()




suburb_name_entry_box.entry_box.bind("<Key>", error_suburb)
suburb_name_entry_box.entry_box.bind("<Control-c>", lambda _: "break")
suburb_name_entry_box.entry_box.bind("<Control-v>", lambda _: "break")


# All the unit entry box detail here
postcode_entry_box = Entry_generator(mini_delivery_frame,'e.g: 5673: (Max 4#)', 3, 1, 1, "Requires 4 digits or have gaps or have gaps.", "PostCode")


def error_postcode(e):
    # Eaching key will be counted and only 9 keyboard entre at once.
    length_of_postcode = len(postcode_entry_box.entry_box.get() + e.char)
    _postcode_turn_list = postcode_entry_box.entry_box.get() + e.char
    in_list_postcode = _postcode_turn_list.split(" ")
    if length_of_postcode <= -1:
        postcode_entry_box.title_of_requirment_outside.configure(foreground='red')
    elif length_of_postcode >= 0 and length_of_postcode < 5:
        postcode_entry_box.title_of_requirment_outside.configure(foreground='blue')
        postcode_entry_box.warning.grid_forget()
        if "" in in_list_postcode:
            postcode_entry_box.title_of_requirment_outside.configure(foreground='red')
            postcode_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
            postcode_entry_box.warning.configure(text ='Space can not be added')
            return 'break'
    elif length_of_postcode > 4:
        postcode_entry_box.title_of_requirment_outside.configure(foreground='red')
        postcode_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
        postcode_entry_box.warning.configure(text='Requires 4 digits or have gaps.')


def error_removing_postcode(e):
    # This the lneght error that could happen in the entry box. So the min is -1, and max is 26
    length_of_postcode = len(postcode_entry_box.entry_box.get()  + e.char)
    # getting the lenght of the selection part
    try:
        selection_length_postcode = len(postcode_entry_box.entry_box.selection_get())
        final_length_postcode = length_of_postcode - selection_length_postcode
        if length_of_postcode < 0:
            return "break"
        elif final_length_postcode < 6:
            postcode_entry_box.title_of_requirment_outside.configure(foreground='blue')
            postcode_entry_box.warning.grid_forget()
        elif final_length_postcode > 6:
            postcode_entry_box.title_of_requirment_outside.configure(foreground='red')
            postcode_entry_box.warning.grid(row=2, column=0, sticky=W, padx=2)
    except TclError:
        if length_of_postcode < 0:
            return "break"
        elif length_of_postcode >= 0 and length_of_postcode < 7:
            postcode_entry_box.title_of_requirment_outside.configure(foreground='blue')
            postcode_entry_box.warning.grid_forget()
        elif length_of_postcode > 6:
            postcode_entry_box.title_of_requirment_outside.configure(foreground='red')
            postcode_entry_box.warning.grid(row=2,column=0, sticky=W, padx=2)


postcode_entry_box.entry_box.bind("<Key>", error_postcode)
postcode_entry_box.entry_box.bind("<BackSpace>", error_removing_postcode)
postcode_entry_box.entry_box.bind('<Delete>', error_removing_postcode)
postcode_entry_box.entry_box.bind("<Control-c>", lambda _: "break")
postcode_entry_box.entry_box.bind("<Control-v>", lambda _: "break")


# name, address, phone, display
name_display_label = Label(Intro_Frames.total_cost_frame, text = "", background='white', font=("Bahnschrift SemiLight", 13))
phone_display_label = Label(Intro_Frames.total_cost_frame, text="",background='white', font=("Bahnschrift SemiLight", 13) )
address_display_label = Label(Intro_Frames.total_cost_frame, text="",background='white', font=("Bahnschrift SemiLight", 13) )
delivery_charge_display_label = Label(Intro_Frames.total_cost_frame, text="", background='white', font=("Bahnschrift SemiLight", 13))
total_label = Label(Intro_Frames.total_cost_frame, text="Total Cost:", borderwidth=0, background='white', font=("Bahnschrift SemiBold", 18)) # total cost label



















# All the pickup detail and managment here
# time detail for delivery page
pickup_label_time = customtkinter.CTkLabel(pickup_frame, text="PICKUP TIME:", text_color='black', border = 0, text_font=('Bahnschrift SemiBold', 18))
pickup_label_time.grid(row =0, column=0,sticky= 'nw', padx=300, pady=(15, 0) )


# time frame for delivery page
time_frame_pickup = customtkinter.CTkFrame(pickup_frame, width=450, height=100, fg_color='white')
time_frame_pickup.grid(row=1, column=0,sticky= 'nw', padx=300, pady=(0, 30))


# Label for the deliveryd detail
pickup_label = customtkinter.CTkLabel(pickup_frame, text="PICKUP DETAIL:", text_color='black', border = 0, text_font=('Bahnschrift SemiBold', 18))
pickup_label.grid(row =2, column=0,sticky= 'nw', padx=300, pady=(15, 5) )


# mini frame in pickup frame
mini_pickup_frame = customtkinter.CTkFrame(pickup_frame, height=250, width=450, fg_color = 'white')
mini_pickup_frame.grid(row=3, column=0,sticky=N, padx=300, pady=(0,40), ipady=8)


# This function create a menu file when the user clicks the confirm button
pickup_button_displayer = Menu(Intro_Frames.page_menu_of3, tearoff=False)


# Pickup Details functions that add these pickup details to the main order list so it can be displayed
def add_pickup_details():

    global delivery_or_pickup_teller


    # Name error handling
    name_is_string = name_entry_box_pickup.entry_box.get()
    separate_name = name_is_string.split(" ")
    combined_name_as_one = ""
    for letter_in_name in separate_name:
        combined_name_as_one += letter_in_name
    if combined_name_as_one.isalpha() == True:
        name_length = len(name_entry_box_pickup.entry_box.get())
        if name_length <= 1:
            name_entry_box_pickup.warning.grid(row=2, column=0, sticky=W, padx=2)
            name_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
            name_entry_box_pickup.warning.configure(text='Not a purpoer Full Name.')
            return 'break'
        elif name_length > 1:
            pass
    elif combined_name_as_one.isalpha() == False:
        name_entry_box_pickup.warning.grid(row=2, column=0, sticky=W, padx=2)
        name_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
        name_entry_box_pickup.warning.configure(text='Not a purpoer Full Name.')
        return 'break'

    # Phone error handling
    if phone_number_entry_box_pickup.entry_box.get().isnumeric() == True:
        phone_number_length = len(phone_number_entry_box_pickup.entry_box.get())
        if phone_number_length < 9 or phone_number_length > 9:
            phone_number_entry_box_pickup.warning.grid(row=2, column=0, sticky=W, padx=2)
            phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
            phone_number_entry_box_pickup.warning.configure(text='Requires 9 digits and only digits allowed.')
            return 'break'
        elif phone_number_length == 9:
            pass
    elif phone_number_entry_box_pickup.entry_box.get().isnumeric() == False:
        phone_number_entry_box_pickup.warning.grid(row=2, column=0, sticky=W, padx=2)
        phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
        phone_number_entry_box_pickup.warning.configure(text='Requires 9 digits and only digits allowed.')
        return 'break'


    # telling the whole code this is pickup so no charge
    delivery_or_pickup_teller = 0

    # packing display labels
    # Name display packing
    name_display_label.grid(row=0, column=0, pady=(15, 0), padx=(10, 4), sticky='w')
    name_display_label.configure(text=f"PickUp By: {name_entry_box_pickup.entry_box.get().title()}")
    # Phone display packing
    phone_display_label.grid(row=1, column=0, pady=(15, 0), padx=(10, 4), sticky='w')
    phone_display_label.configure(text=f"Phone Number: {phone_number_entry_box_pickup.entry_box.get()}")
    # street name display packing
    address_display_label.grid(row=2, column=0, pady=(15, 0), padx=(10, 4), sticky='w')
    address_display_label.configure(text=f"PickUp From: Henderson Pizza Palace")
    # delivery time display
    delivery_time_display_label.grid(row=3, column=0, pady=(15, 0), padx=(10, 4), sticky='w')
    delivery_time_display_label.configure(text=f"""PickUp Time: {todays_day}/{month}  {update_hours}:{updating_min} {t.strftime("%p")}""")
    # Configure the total cost to 0 dollars as now pickup been added
    total_label.grid(row=4, column=0, pady=(15, 20), padx=(10, 4), sticky='w')
    # adding the total cost in different variabel so it could be changed and this alos the cost that is added but not shown. This the ost before any pizza has been added to the order list
    if delivery_or_pickup_teller == 0:
            Total_cost_order.checker_delivery_or_pickup()
    # Puts the name in the delivery in the menu
    name_entry_box_pickup_display = name_entry_box_pickup.entry_box.get()
    Intro_Frames.page_menu_of3.add_cascade(label=f"PickUp By: {name_entry_box_pickup_display.title()}", font=('Robot',10), menu = pickup_button_displayer )
    pickup_button_displayer.add_command(label="Change", font=('Robot',10), command = Intro_Frames.run_again_delivery_and_pickup)
    # Deleting the frames for pickup and choice frame.
    pickup_frame.destroy()
    frame_for_delivery_pickup.destroy()







# Time and date updates from real time
def timer_set_pcikup():
    hours = t.localtime()
    minutes = t.gmtime()
    updating_min = minutes.tm_min
    update_hours = hours.tm_hour
    updating_min = minutes.tm_min + 40
    adding_together = ""
    if updating_min >= 60:
        update_hours = hours.tm_hour + 1
        updating_min -=  60
        spaces_between_mins = " ".join(str(updating_min))
        removing_space = spaces_between_mins.split(" ")
        if len(removing_space) > 1:
            removing_space.pop(1)
            removing_space.append("0")
            for one_int in removing_space:
                adding_together += one_int
            updating_min = adding_together
        else:
            updating_min = 10
    else:
        spaces_between_mins = " ".join(str(updating_min))
        removing_space = spaces_between_mins.split(" ")
        if len(removing_space) > 1:
            removing_space.pop(1)
            removing_space.append("0")
            for one_int in removing_space:
                adding_together += one_int
            updating_min = adding_together
        else:
            updating_min = 10

    # This is the time in pickup
    today_time_pickup.config(text=f"""{update_hours}:{updating_min} {t.strftime("%p")}""")
    today_time_pickup.after(100, timer_set_pcikup)


# confirm button for pickup
confirm_button_pickup = customtkinter.CTkButton(pickup_frame, text = 'Confirm', text_font=('Bahnschrift SemiBold', 20), cursor='hand2', corner_radius = 6, text_color='white', hover_color ='#858585', fg_color= '#9B9B9B', height=40, width=250, command= add_pickup_details)
confirm_button_pickup.grid(row=4, column=0)

# A mini frame inside the time frame to get a better palcement
now_time_frame_pickup = customtkinter.CTkFrame(time_frame_pickup, borderwidth=0, bg_color='white', fg_color='white')
now_time_frame_pickup.grid(row=0, columnspan=2,column=0, padx=3, pady=5)

# tiny labelframe for order time and order date
date_label_frame_pickup = LabelFrame(now_time_frame_pickup, background='white', width = 450, height=60, borderwidth=0)
date_label_frame_pickup.grid(column=0, row = 1, sticky='w', padx = (2,10), pady = (5,2))


order_date_label_pickup = Label(date_label_frame_pickup, text="Order Date:", font= ('Bahnschrift SemiBold',13), borderwidth=0, background='white', foreground='black')
order_date_label_pickup.grid(row=0, column =0, pady=(3,0), padx=(5, 5), sticky='w')

today_date_pickup = customtkinter.CTkLabel(date_label_frame_pickup, text = f"{todays_day}/{month}/{year}", text_font = ("robot",15), bg_color='white', corner_radius=8, fg_color='#F2F2F2', width=200, height=30)
today_date_pickup.grid(row=1, column =0, pady=(0,3), padx=(5, 5))


#Another mini labelframe on the side in the pickup
time_label_frame_pickup = LabelFrame(now_time_frame_pickup, background='white', width = 450, height=60, borderwidth=0)
time_label_frame_pickup.grid(column=1, row = 1, sticky='w', padx= (2,10), pady=(5,2))

order_time_label_pickup = Label(time_label_frame_pickup, text="Order Time:", font= ('Bahnschrift SemiBold',13), borderwidth=0, background='white', foreground='black')
order_time_label_pickup.grid(row=0, column =1, pady=(3,0), padx=(5, 5), sticky='w')

today_time_pickup = customtkinter.CTkLabel(time_label_frame_pickup, text = f"", text_font = ("robot",15), bg_color='white', corner_radius=8, fg_color='#F2F2F2', width=200, height=30)
today_time_pickup.grid(row=1, column =1, pady=(0,3), padx=(5, 5))



# This is for pickup detai so that is why name entry and phone entry box have been repeated
# Name entry box and all the error telling detail here
name_entry_box_pickup = Entry_generator(mini_pickup_frame,'e.g: Ajay (Max 26  Characters)', 0, 0, 1, "Exceeded max length of 26", "Full Name")



# Function that take of errors in the name entry box and all the detail about name function
def errors_telling_name(e):
    # This the lneght error that could happen in the entry box. So the min is -1, and max is 26
    length_of_name = len(name_entry_box_pickup.entry_box.get() + e.char)
    if length_of_name < 0:
        name_entry_box_pickup.title_of_requirment_outside.configure(foreground='blue')
    elif length_of_name >= 0 and length_of_name < 26:
        name_entry_box_pickup.title_of_requirment_outside.configure(foreground='blue')
        name_entry_box_pickup.warning.grid_forget()
    elif length_of_name > 26:
        name_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
        name_entry_box_pickup.warning.grid(row=2,column=0, sticky=W, padx=2)


def errors_for_backspace_and_delete_name(e):
    # This the lneght error that could happen in the entry box. So the min is -1, and max is 26
    length_of_name = len(name_entry_box_pickup.entry_box.get()  + e.char)
    try:
        selection_length_of_name = len(name_entry_box_pickup.entry_box.selection_get())
        final_length_name = length_of_name - selection_length_of_name
        if length_of_name < 0:
            return 'break'
        elif final_length_name < 29:
            name_entry_box_pickup.title_of_requirment_outside.configure(foreground='blue')
            name_entry_box_pickup.warning.grid_forget()
        elif final_length_name > 27:
            name_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
            name_entry_box_pickup.warning.grid(row=2,column=0, sticky=W, padx=2)
    except TclError:
        if length_of_name < 0:
            return 'break'
        elif length_of_name >= 0 and length_of_name < 29:
            name_entry_box_pickup.title_of_requirment_outside.configure(foreground='blue')
            name_entry_box_pickup.warning.grid_forget()
        elif length_of_name > 27:
            name_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
            name_entry_box_pickup.warning.grid(row=2,column=0, sticky=W, padx=2)


name_entry_box_pickup.entry_box.bind("<Key>", errors_telling_name)
name_entry_box_pickup.entry_box.bind('<BackSpace>', errors_for_backspace_and_delete_name)
name_entry_box_pickup.entry_box.bind('<Delete>', errors_for_backspace_and_delete_name)
name_entry_box_pickup.entry_box.bind("<Control-c>", lambda _: "break")
name_entry_box_pickup.entry_box.bind("<Control-v>", lambda _: "break")




# Phone number entry box and all the error telling detail
phone_number_entry_box_pickup = Entry_generator(mini_pickup_frame,'e.g: 641234242: (Max 9#)', 0, 1, 1, "Requires 9 digits or have gaps.", "Phone Number")


def error_phone(e):
    # Eaching key will be counted and only 9 keyboard entre at once.
    phone_number_entry_box_length = len(phone_number_entry_box_pickup.entry_box.get() + e.char)
    _phone_turn_list = phone_number_entry_box_pickup.entry_box.get() + e.char
    in_list_phone = _phone_turn_list.split(" ")
    if phone_number_entry_box_length < 0:
        phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
    elif phone_number_entry_box_length >= 0 and phone_number_entry_box_length < 9:
        phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='blue')
        phone_number_entry_box_pickup.warning.grid_forget()
        if "" in in_list_phone:
            phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
            phone_number_entry_box_pickup.warning.grid(row=2, column=0, sticky=W, padx=2)
            phone_number_entry_box_pickup.warning.configure(text ="Spaces can not be added")
            return 'break'
    elif phone_number_entry_box_length > 9:
        phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
        phone_number_entry_box_pickup.warning.grid(row=2,column=0, sticky=W, padx=2)
        phone_number_entry_box_pickup.warning.configure(text = "Requires 9 digits or have gaps.")

def error_removing_phone(e):
    # This the lneght error that could happen in the entry box. So the min is -1, and max is 26
    phone_number_entry_box_length = len(phone_number_entry_box_pickup.entry_box.get()  + e.char)
    try:
        selection_length_of_phone = len(phone_number_entry_box_pickup.entry_box.selection_get())
        final_length_phone = phone_number_entry_box_length - selection_length_of_phone
        if phone_number_entry_box_length < 0:
            return "break"
        elif final_length_phone < 11:
            phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='blue')
            phone_number_entry_box_pickup.warning.grid_forget()
        elif final_length_phone > 11:
            phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
            phone_number_entry_box_pickup.warning.grid(row=2, column=0, sticky=W, padx=2)
    except TclError:
        if phone_number_entry_box_length <= -1:
            return "break"
        elif phone_number_entry_box_length >= 0 and phone_number_entry_box_length < 12:
            phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='blue')
            phone_number_entry_box_pickup.warning.grid_forget()
        elif phone_number_entry_box_length > 11:
            phone_number_entry_box_pickup.title_of_requirment_outside.configure(foreground='red')
            phone_number_entry_box_pickup.warning.grid(row=2,column=0, sticky=W, padx=2)

phone_number_entry_box_pickup.entry_box.bind("<Key>", error_phone)
phone_number_entry_box_pickup.entry_box.bind("<BackSpace>", error_removing_phone)
phone_number_entry_box_pickup.entry_box.bind('<Delete>', error_removing_phone)
phone_number_entry_box_pickup.entry_box.bind("<Control-c>", lambda _: "break")
phone_number_entry_box_pickup.entry_box.bind("<Control-v>", lambda _: "break")



# Setting the focus on delivery frame and other frame if the user clicks out of the entry box
pickup_frame.bind("<Button-1>", lambda e: pickup_frame.focus_set())
time_frame_pickup.canvas.bind("<Button-1>", lambda e: time_frame_pickup.focus_set())
mini_pickup_frame.canvas.bind("<Button-1>", lambda e: mini_pickup_frame.focus_set())
confirm_button_pickup.canvas.bind("<Button-1>", lambda e: confirm_button_pickup.focus_set())


# Running the timer set here as now it cover all the area
timer_set()
# Running the same programmer in two form as other label is not label to config
timer_set_pcikup()




# All the Moduels
import importlib
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import Henderson_Pizza_Palace_Tkinter
import helper
import customtkinter
import mouse
import Final_Checkout
import threading


# The window,the title, the icon, and the size
window = Tk()
window.title("Henderson Pizza Palace")
window.iconbitmap(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\pizza_zEj_icon.ico")


# Centering the window according to a display screen
window.update()
width_of_main_window = 1066
height_of_main_window = 600
width_of_screen = window.winfo_screenwidth()
height_of_screen = window.winfo_screenheight()
x = (width_of_screen / 2) - (width_of_main_window / 2)
y = (height_of_screen / 2) - (height_of_main_window / 2)
window.geometry(f'{width_of_main_window}x{height_of_main_window}+{int(x)}+{int(y)}')# these two pulus value are the position of the window
window.resizable(False,False)


# Creating a menu bar
page_menu_of3 = Menu(window)
window.config(menu=page_menu_of3)



# Function that runs the main frame and deletes te collection
def home_page():
    hide_main_frames()
    bring_hiding_fuction_in_menu_page()
    resizing_scroll_bar_home_page()
    home_frame.pack(expand=1,fill=BOTH)


def menu_page():
    hide_main_frames()
    bring_hiding_fuction_in_menu_page()
    menu_frame.pack(expand=1,fill=BOTH)


# This runs the delivery and pick page when the users wants to change to different type of way to getting the pizza
def run_again_delivery_and_pickup():
    if Delivery_or_pickup.frame_for_delivery_pickup.winfo_exists() == True:
        pass
    else:
        # Deleting display information when the user decides to chnage
        Delivery_or_pickup.name_display_label.destroy()
        Delivery_or_pickup.phone_display_label.destroy()
        Delivery_or_pickup.address_display_label.destroy()
        Delivery_or_pickup.delivery_time_display_label.destroy()
        Delivery_or_pickup.delivery_charge_display_label.destroy()
        Delivery_or_pickup.total_label.destroy()
        importlib.reload(Delivery_or_pickup)
        # Deleting the perviou menu display of the delivery to update it to new one
        page_menu_of3.delete(5)
        # reloading the moduel again


def order_list_page():
    hide_main_frames()
    if Delivery_or_pickup.frame_for_delivery_pickup.winfo_exists() == True:
        Delivery_or_pickup.back_to_choice()
    else:
        pass
    bring_hiding_fuction_in_menu_page()
    resizing_scroll_bar_order_page()
    order_list_frame.pack(expand=1, fill=BOTH)


def hide_main_frames():
    home_frame.pack_forget()
    menu_frame.pack_forget()
    order_list_frame.pack_forget()



# Adding title to the menu bar
home_page1 = page_menu_of3
home_page1.add_command(label="Home",font=('Robot',10),command = home_page)
menu_page2 = page_menu_of3
menu_page2.add_command(label='Menu',font=('Robot',10),command=menu_page)
order_list_page3 = page_menu_of3
order_list_page3.add_command(label= 'Order List',font=('Robot',10),command = order_list_page)
help_button = page_menu_of3
help_button.add_command(label="Help",font=('Robot',10), command= helper.helper_slide )



# All the three main frames (home, menu, order)
home_frame = Frame(window,bg = 'white')
home_frame.pack(expand=1,fill=BOTH)
menu_frame = Frame(window,bg='white')
order_list_frame = Frame(window,bg='#F2F2F2')


# Label frame for orders in the order page
order_list = LabelFrame(order_list_frame, text = "Your Order", font=('Bahnschrift SemiBold', 20), background='#F2F2F2', borderwidth=0, width=400)
order_list.pack(expand=1, fill=Y, side=LEFT, padx=(2,20), pady=(10,20))

# A big label frmae to place widget neatly
big_labelFrame_treeview_total_cost = LabelFrame(order_list_frame, borderwidth=0, bg= "#F2F2F2", width=473)
big_labelFrame_treeview_total_cost.pack(side=RIGHT, expand=1, fill=X, anchor='s')

# Total cost and deivery and pickup charge frame
total_cost_frame = customtkinter.CTkFrame(big_labelFrame_treeview_total_cost, border_width=0, bg_color='#F2F2F2', corner_radius=20, fg_color='white')
total_cost_frame.pack(side = BOTTOM,padx=(0,30), pady=20, anchor='w', expand=1, fill=Y)
# Adding a checkout button
check_out_button_image = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\checkout imageeditedresized.png")
checkout_button = customtkinter.CTkButton(total_cost_frame, image= check_out_button_image, text="Check Out", text_font=("Bahnschrift SemiBold", 14), text_color='white', fg_color='#03CC03', hover_color="#03AA03", cursor='hand2', corner_radius=0, height=60, command= Final_Checkout.chect_out, state=DISABLED)
checkout_button.grid( row= 6,column=0, sticky='we', pady=0)
# Diplaying frame and the scroll bar holder frame. This the frame that hodles th pizza in order with picture adn this the frame where all the pizza get put int
displaying_frame = customtkinter.CTkFrame(order_list, fg_color='white',  border=0,  width=400, corner_radius= 20)
displaying_frame.pack(expand=1, fill=Y)



# Iamge for background for home page
home_canvas = Canvas(home_frame, highlightthickness=0)
home_canvas.pack(expand=1,fill=BOTH)
background_image_home_frame = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\1.png")
home_canvas.create_image(0,600,image = background_image_home_frame,anchor = 'sw')


# Animation for the home page to make the app more interactive
image_list = [
    ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\one_image_for_animation.png"),
    ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\fourth combeditedresized.jpg"),
    ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\animation one of the image.png")
]

global count_of_images
count_of_images = -1
home_canvas.create_image(0,0, image = image_list[0], anchor = 'nw')

def next_image():
    global count_of_images
    if count_of_images == 2:
        home_canvas.create_image(0, 0, image=image_list[0], anchor='nw')
        count_of_images = 0
    else:
        home_canvas.create_image(0, 0, image=image_list[count_of_images + 1], anchor='nw')
        count_of_images += 1
    window.after(1000, next_image)

next_image()


# Startup Button
def hover_on(e):
    startup_button.configure(background='#1AFF09',overrelief=SUNKEN,fg = 'white')
def hover_off(e):
    startup_button.configure(bg = '#FFFFF9',overrelief=RAISED,fg = 'black')
startup_button = Button(home_frame,text="Start Ordering",font=("robot",30),pady = 5,padx =5,border=0,bg = '#FFFFF9',activebackground='#1AFF09', activeforeground='white', command=menu_page, cursor = "hand2")
startup_button.place(x = 395,y=380)
startup_button.bind('<Enter>', hover_on)
startup_button.bind('<Leave>',hover_off)


# Scroll Bar for menu frame
menu_canvas = Canvas(menu_frame, highlightthickness=0)
menu_canvas.pack(expand=1,fill=BOTH,side=LEFT)
menu_scroll_bar = ttk.Scrollbar(menu_frame,orient=VERTICAL,command=menu_canvas.yview)
menu_scroll_bar.pack(side=RIGHT,fill=Y)
menu_canvas.configure(yscrollcommand=menu_scroll_bar.set)
menu_canvas.bind('<Configure>',lambda e:menu_canvas.configure(scrollregion=menu_canvas.bbox('all')))
mini_menu_frame = Frame(menu_canvas)
menu_canvas.create_window((0,0),window=mini_menu_frame,anchor='nw',width=1066)
# Background Image for menu frame
image_of_menu_frame = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\backgroundmenuframeimproved.png")
background_image_menu_frame = Label(mini_menu_frame,image=image_of_menu_frame,anchor='nw')
background_image_menu_frame.place(x=0,y=0)





# Importing menu item and order_list_in_text to avoid loop import
import Menu_item
import expanding_pages
#import Order_list_in_text

# Importing frame hiding fuction and putting it in fuction. That is becuase this will allow me to use it anywhere.
def bring_hiding_fuction_in_menu_page():
    expanding_pages.hiding_expanding_frames()
    expanding_pages.Simply_cheese_canvas.yview_moveto(0.0)


# Resizing scrollbar for detail pages when moving back to home page
def resizing_scroll_bar_home_page():
    expanding_pages.Simply_cheese_canvas.yview_moveto(0.0)


# Resizing scrollbar for detail pages when moving back to order page
def resizing_scroll_bar_order_page():
    expanding_pages.Simply_cheese_canvas.yview_moveto(0.0)

# importing Delivery and pickup file here to avoid loop important error
import Delivery_or_pickup



window.mainloop()

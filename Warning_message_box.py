# All the Moduels
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import time
import Intro_Frames
#import Order_list_in_text
import expanding_pages
import Delivery_or_pickup
import Total_cost_order
import mouse
# Importing style makes libaray
import customtkinter
import pyttsx3


# This stoes all the pizza menu items that user had stored
storing_pizzas = []


# Class for mini order list diplay for pizza
class Order_pizza_list:

    # This function that brings a pizza from out so the user know what one they are on
    def __init__(self, image_of_mini_pizza, name_of_pizza, price_of_pizza, remove_command):
        self.order_pizza_frame = customtkinter.CTkFrame(Intro_Frames.displaying_frame, width=150, fg_color='#F2F2F2', border_width=2, border_color='#5E5E5E', bg_color='white')
        self.order_pizza_frame.pack( pady= 1, padx=3, anchor="w")
        self.image_of_mini_pizza_displaying = ImageTk.PhotoImage(file = image_of_mini_pizza)
        self.displaying_mini_pizza = Label(self.order_pizza_frame, image = self.image_of_mini_pizza_displaying,  bg= '#F2F2F2', padx=0, border=0)
        self.displaying_mini_pizza.grid( pady= 6, padx= (6,6), row=0, column=0, sticky='nw', rowspan=2)
        self.displaying_pizza_name = Label(self.order_pizza_frame, text = name_of_pizza , font=("Bahnschrift SemiBold", 13),  bg= '#F2F2F2', padx=0, border=0)
        self.displaying_pizza_name.grid( pady=0, padx= (0,2), row=0, column=1, sticky='s')
        self.displaying_pizza_price = Label(self.order_pizza_frame, text = f"${price_of_pizza}" , font=("Bahnschrift SemiBold", 13),  bg= '#F2F2F2', padx=0, border=0)
        self.displaying_pizza_price.grid(row = 0, column= 2, pady=0, padx= (10,2), sticky='s' )
        self.remove_button = Button(self.order_pizza_frame, text = 'Remove' , font=("Robot", 13),  bg= '#F2F2F2', padx=0, border=0, fg='red', cursor='hand2', activebackground='#F2F2F2', activeforeground='red', command = remove_command)
        self.remove_button.grid( pady=4, padx=3, row=1, column=2, sticky='se')

# Changing the order list label when a pizza is added to order list
def add():
    # This takes the length number of the pizza list and tells the user how many pizza they have in their order.
    Intro_Frames.order_list_page3.entryconfig(3, label=f'Order List  | {len(storing_pizzas)} |')

    # Checking the if the number is 5 if so then a messga will be put out to indicate to the user.
    size_of_list = len(storing_pizzas)


    if size_of_list >= 5:
        custon_message_box = Tk()
        custon_message_box.overrideredirect(True)
        custon_message_box.configure(bg='grey')
        # This makes a specific colour go transparent
        custon_message_box.wm_attributes("-transparent", 'grey')
        custon_message_box.attributes("-topmost", True)
        custon_message_box.transient()
        Intro_Frames.window.attributes('-disabled', True)


        # Centering the message box in middle of the app
        width_of_window = Intro_Frames.window.winfo_width()
        height_of_window = Intro_Frames.window.winfo_height()
        main_position_x = Intro_Frames.window.winfo_x()
        main_position_y = Intro_Frames.window.winfo_y()
        custon_box_postion_x = ((width_of_window / 2) - (400 / 2)) + main_position_x
        custon_box_postion_y = ((96) - (80 / 2)) + main_position_y
        custon_message_box.geometry(f"400x80+{int(custon_box_postion_x)}+{int(custon_box_postion_y)}")


        # Creating a frame for all the button and widgets to be placed in
        custom_message_frame = customtkinter.CTkFrame(custon_message_box,  corner_radius=10,  fg_color='white')
        custom_message_frame.pack(expand=1, fill=BOTH)

        # Telling the message
        message = Label(custom_message_frame, text="You have reached the maximun limited for pizza orders!\nThank you.", background='white', foreground='black', font=('robot', 10, 'bold'))
        message.pack(pady=20, padx=8)


        # Create this function so we could disable the other left
        def destroying_message_box_with_button():
            custon_message_box.destroy()
            # Undisbales the main window
            Intro_Frames.window.attributes('-disabled', False)
            Intro_Frames.window.focus_force()



        # Just a button for style
        exit_button = Button(custom_message_frame, text="OK", font=("Robot", 8, 'bold'), padx=30 , background='#025BC4', activeforeground='white', activebackground='#025BC4', border=0, fg = 'white', cursor= "hand2", command = destroying_message_box_with_button)
        exit_button.place(x=310, y=50)


        # Disabling all the menu button if the value of the list is 5 or greater
        expanding_pages.simply_cheese_page.putting_price_image['state'] = DISABLED
        expanding_pages.simply_cheese_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.american_pepperion_page.putting_price_image['state'] = DISABLED
        expanding_pages.american_pepperion_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.cheesy_gralic_page.putting_price_image['state'] = DISABLED
        expanding_pages.cheesy_gralic_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.chicken_supreme_page.putting_price_image['state'] = DISABLED
        expanding_pages.chicken_supreme_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.ham_cheese_page.putting_price_image['state'] = DISABLED
        expanding_pages.ham_cheese_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.mr_wedge_page.putting_price_image['state'] = DISABLED
        expanding_pages.mr_wedge_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.pepperoni_page.putting_price_image['state'] = DISABLED
        expanding_pages.pepperoni_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.supreme_page.putting_price_image['state'] = DISABLED
        expanding_pages.supreme_page.putting_price_image.configure(cursor= "arrow")

        expanding_pages.apricot_chicken_page.putting_price_image['state'] = DISABLED
        expanding_pages.apricot_chicken_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.chicken_bacon_alioli_page.putting_price_image['state'] = DISABLED
        expanding_pages.chicken_bacon_alioli_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.chicken_and_cheese_page.putting_price_image['state'] = DISABLED
        expanding_pages.chicken_and_cheese_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.mega_meatlover_page.putting_price_image['state'] = DISABLED
        expanding_pages.mega_meatlover_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.peri_peri_chicken_page.putting_price_image['state'] = DISABLED
        expanding_pages.peri_peri_chicken_page.putting_price_image.configure(cursor= "arrow")
        expanding_pages.gralic_prawn_page.putting_price_image['state'] = DISABLED
        expanding_pages.gralic_prawn_page.putting_price_image.configure(cursor= "arrow")


        # keeping the value smae when the order reach 5
        custon_message_box.mainloop()

    # Making the add to cart button normal when the order list has less pizza then 5
    elif size_of_list < 5:
        expanding_pages.simply_cheese_page.putting_price_image['state'] = NORMAL
        expanding_pages.simply_cheese_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.american_pepperion_page.putting_price_image['state'] = NORMAL
        expanding_pages.american_pepperion_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.cheesy_gralic_page.putting_price_image['state'] = NORMAL
        expanding_pages.cheesy_gralic_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.chicken_supreme_page.putting_price_image['state'] = NORMAL
        expanding_pages.chicken_supreme_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.ham_cheese_page.putting_price_image['state'] = NORMAL
        expanding_pages.ham_cheese_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.mr_wedge_page.putting_price_image['state'] = NORMAL
        expanding_pages.mr_wedge_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.pepperoni_page.putting_price_image['state'] = NORMAL
        expanding_pages.pepperoni_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.supreme_page.putting_price_image['state'] = NORMAL
        expanding_pages.supreme_page.putting_price_image.configure(cursor= "hand2")

        expanding_pages.apricot_chicken_page.putting_price_image['state'] = NORMAL
        expanding_pages.apricot_chicken_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.chicken_bacon_alioli_page.putting_price_image['state'] = NORMAL
        expanding_pages.chicken_bacon_alioli_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.chicken_and_cheese_page.putting_price_image['state'] = NORMAL
        expanding_pages.chicken_and_cheese_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.peri_peri_chicken_page.putting_price_image['state'] = NORMAL
        expanding_pages.peri_peri_chicken_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.mega_meatlover_page.putting_price_image['state'] = NORMAL
        expanding_pages.mega_meatlover_page.putting_price_image.configure(cursor= "hand2")
        expanding_pages.gralic_prawn_page.putting_price_image['state'] = NORMAL
        expanding_pages.gralic_prawn_page.putting_price_image.configure(cursor= "hand2")




















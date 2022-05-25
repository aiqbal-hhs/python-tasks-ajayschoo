# All the Moduels
import importlib
from tkinter import *
from tkinter import ttk

import customtkinter
from PIL import ImageTk
import time
import Henderson_Pizza_Palace_Tkinter
import Intro_Frames
import Total_cost_order



# Regular Range
# american pepperion scroll bar
def expanding_American_pepperion():
    hiding_expanding_frames()
    American_pepperion_frame.pack(expand=1,fill=BOTH)
    American_pepperion_canvas.pack(side= LEFT,expand=1,fill=BOTH)
    American_pepperion_scroll_bar.pack(side=RIGHT,fill=Y)
    American_pepperion_canvas.configure(yscrollcommand=American_pepperion_scroll_bar.set)
    American_pepperion_canvas.bind("<Configure>",lambda e:American_pepperion_canvas.configure(scrollregion=American_pepperion_canvas.bbox('all')))
    American_pepperion_canvas.create_window((0,0),window=mini_American_pepperion_frame,width = 1066, height = 1550,anchor='nw')


American_pepperion_frame = Frame(Intro_Frames.window)
American_pepperion_canvas = Canvas(American_pepperion_frame)
American_pepperion_scroll_bar = ttk.Scrollbar(American_pepperion_frame,orient=VERTICAL,command=American_pepperion_canvas.yview)
mini_American_pepperion_frame = Frame(American_pepperion_canvas, bg = '#14141D')


# Cheesy gralic scroll bar and mini frame
def expanding_cheesy_gralic_pizza():
    hiding_expanding_frames()
    Cheesy_gralic_pizza_frame.pack(expand=1,fill=BOTH)
    Cheesy_gralic_pizza_canvas.pack(side=LEFT,expand=1,fill=BOTH)
    Cheesy_gralic_pizza_scroll_bar.pack(side=RIGHT,fill=Y)
    Cheesy_gralic_pizza_canvas.configure(yscrollcommand=Cheesy_gralic_pizza_scroll_bar.set)
    Cheesy_gralic_pizza_canvas.bind("<Configure>",lambda e:Cheesy_gralic_pizza_canvas.configure(scrollregion=Cheesy_gralic_pizza_canvas.bbox('all')))
    Cheesy_gralic_pizza_canvas.create_window((0,0),window=mini_Cheesy_gralic_pizza_frame,width = 1066,anchor='nw')


Cheesy_gralic_pizza_frame = Frame(Intro_Frames.window)
Cheesy_gralic_pizza_canvas = Canvas(Cheesy_gralic_pizza_frame)
Cheesy_gralic_pizza_scroll_bar = ttk.Scrollbar(Cheesy_gralic_pizza_frame, orient=VERTICAL,command=Cheesy_gralic_pizza_canvas.yview)
mini_Cheesy_gralic_pizza_frame = Frame(Cheesy_gralic_pizza_canvas)


# Chicken supreme scroll bar and mini frame
def expanding_chicken_supreme():
    hiding_expanding_frames()
    Chicken_supreme_frame.pack(expand=1,fill=BOTH)
    Chicken_supreme_canvas.pack(side=LEFT,expand=1,fill=BOTH)
    Chicekn_supreme_scroll_bar.pack(fill =Y,side= RIGHT)
    Chicken_supreme_canvas.configure(yscrollcommand = Chicekn_supreme_scroll_bar.set)
    Chicken_supreme_canvas.bind("<Configure>",lambda e:Chicken_supreme_canvas.configure(scrollregion=Chicken_supreme_canvas.bbox('all')))
    Chicken_supreme_canvas.create_window((0,0),window=mini_chicken_supreme_frame,width=1066, anchor='nw')


Chicken_supreme_frame = Frame(Intro_Frames.window)
Chicken_supreme_canvas = Canvas(Chicken_supreme_frame)
Chicekn_supreme_scroll_bar = ttk.Scrollbar(Chicken_supreme_canvas, orient=VERTICAL,command=Chicken_supreme_canvas.yview)
mini_chicken_supreme_frame = Frame(Chicken_supreme_canvas)


# Ham and cheese scroll bar and frame
def expanding_ham_cheese():
    hiding_expanding_frames()
    Ham_and_cheese_frame.pack(expand=1,fill=BOTH)
    Ham_and_cheese_canvas.pack(expand=1,fill=BOTH,side=LEFT)
    Ham_and_cheese_scroll_bar.pack(side = RIGHT,fill=Y)
    Ham_and_cheese_canvas.configure(yscrollcommand=Ham_and_cheese_scroll_bar.set)
    Ham_and_cheese_canvas.bind("<Configure>",lambda e: Ham_and_cheese_canvas.configure(scrollregion=Ham_and_cheese_canvas.bbox('all')))
    Ham_and_cheese_canvas.create_window((0,0),window=mini_ham_and_cheese_frame,width=1066, anchor='nw')


Ham_and_cheese_frame = Frame(Intro_Frames.window)
Ham_and_cheese_canvas = Canvas(Ham_and_cheese_frame)
Ham_and_cheese_scroll_bar = ttk.Scrollbar(Ham_and_cheese_frame, orient=VERTICAL, command=Ham_and_cheese_canvas.yview)
mini_ham_and_cheese_frame = Frame(Ham_and_cheese_canvas)


# Mr wedge frame and scroll
def expanding_mr_wedge():
    hiding_expanding_frames()
    Mr_wedge_frame.pack(expand=1,fill=BOTH)
    Mr_wedge_canvas.pack(fill=BOTH,side=LEFT,expand=1)
    Mr_wedge_scroll_bar.pack(side = RIGHT,fill=Y)
    Mr_wedge_canvas.configure(yscrollcommand=Mr_wedge_scroll_bar.set)
    Mr_wedge_canvas.bind("<Configure>", lambda e: Mr_wedge_canvas.configure(scrollregion=Mr_wedge_canvas.bbox('all')))
    Mr_wedge_canvas.create_window((0,0), window=mini_mr_wedge_frame,width=1066, anchor='nw')


Mr_wedge_frame = Frame(Intro_Frames.window)
Mr_wedge_canvas = Canvas(Mr_wedge_frame)
Mr_wedge_scroll_bar = ttk.Scrollbar(Mr_wedge_frame, orient=VERTICAL, command=Mr_wedge_canvas.yview)
mini_mr_wedge_frame = Frame(Mr_wedge_canvas)


# Pepperion frame and scroll bar
def expanding_pepperion():
    hiding_expanding_frames()
    Pepperion_frame.pack(expand=1,fill=BOTH)
    Pepperion_canvas.pack(side=LEFT,expand=1,fill=BOTH)
    Pepperion_scroll_bar.pack(side=RIGHT,fill=Y)
    Pepperion_canvas.configure(yscrollcommand=Pepperion_scroll_bar.set)
    Pepperion_canvas.bind("<Configure>",lambda e: Pepperion_canvas.configure(scrollregion=Pepperion_canvas.bbox('all')))
    Pepperion_canvas.create_window((0,0),window=mini_Pepperion_frame,width=1066, anchor='nw')


Pepperion_frame = Frame(Intro_Frames.window)
Pepperion_canvas = Canvas(Pepperion_frame)
Pepperion_scroll_bar = ttk.Scrollbar(Pepperion_frame, orient=VERTICAL, command=Pepperion_canvas.yview)
mini_Pepperion_frame = Frame(Pepperion_canvas)


# Simply cheese frame and scroll bar
def expanding_simply_cheese():
    hiding_expanding_frames()
    Simply_cheese_frame.pack(expand=1,fill=BOTH)
    Simply_cheese_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    Simply_cheese_scroll_bar.pack(side=RIGHT,fill=Y)
    Simply_cheese_canvas.configure(yscrollcommand = Simply_cheese_scroll_bar.set)
    Simply_cheese_canvas.bind("<Configure>", lambda e: Simply_cheese_canvas.configure(scrollregion=Simply_cheese_canvas.bbox('all')))
    Simply_cheese_canvas.create_window(((0,0)), window= mini_Simply_cheese_frame, width = 1066, height = 1550, anchor='nw')


Simply_cheese_frame = Frame(Intro_Frames.window)
Simply_cheese_canvas = Canvas(Simply_cheese_frame)
Simply_cheese_scroll_bar = ttk.Scrollbar(Simply_cheese_frame, orient=VERTICAL, command=Simply_cheese_canvas.yview)
mini_Simply_cheese_frame = Frame(Simply_cheese_canvas, bg = '#14141D')


# supreme frame and scroll bar
def expanding_Supreme():
    hiding_expanding_frames()
    Supreme_frame.pack(expand=1,fill=BOTH)
    Supreme_canvas.pack(side = LEFT, fill=BOTH, expand= 1)
    Supreme_scroll_bar.pack(side= RIGHT,fill=Y)
    Supreme_canvas.configure(yscrollcommand=Supreme_scroll_bar.set)
    Supreme_canvas.bind("<Configure>",lambda e: Supreme_canvas.configure(scrollregion= Supreme_canvas.bbox('all')))
    Supreme_canvas.create_window((0,0), window = mini_Supreme_frame, width = 1066, anchor='nw')


Supreme_frame = Frame(Intro_Frames.window)
Supreme_canvas = Canvas(Supreme_frame)
Supreme_scroll_bar = ttk.Scrollbar(Supreme_frame, orient=VERTICAL, command=Supreme_canvas.yview)
mini_Supreme_frame = Frame(Supreme_canvas)



# Gourmet Range
# Apricot frame and scroll bar
def expanding_Apricot():
    hiding_expanding_frames()
    Apricot_frame.pack(expand=1,fill=BOTH)
    Apricot_canvas.pack(side=LEFT,expand=1,fill=BOTH)
    Apricot_scrollbar.pack(fill=Y, side=RIGHT)
    Apricot_canvas.configure(yscrollcommand=Apricot_scrollbar.set)
    Apricot_canvas.bind("<Configure>",lambda e: Apricot_canvas.configure(scrollregion = Apricot_canvas.bbox('all')))
    Apricot_canvas.create_window((0,0),window=mini_Apricot_frame,width=1066, anchor='nw')


Apricot_frame = Frame(Intro_Frames.window)
Apricot_canvas = Canvas(Apricot_frame)
Apricot_scrollbar = ttk.Scrollbar(Apricot_frame,orient=VERTICAL,command=Apricot_canvas.yview)
mini_Apricot_frame = Frame(Apricot_canvas)


# Chicken, Bacon and aioli scrollbar and frame
def expanding_chicken_bacon_aioli():
    hiding_expanding_frames()
    Chicken_supreme_frame.pack(fill=BOTH, expand=1)
    Chicken_bacon_aioli_canvas.pack(side=LEFT, expand=1, fill=BOTH)
    Chicken_bacon_aioli_scroll_bar.pack(side=RIGHT, fill= Y)
    Chicken_bacon_aioli_canvas.configure(yscrollcommand= Chicken_bacon_aioli_scroll_bar.set)
    Chicken_bacon_aioli_canvas.bind("<Configure>", lambda e: Chicken_bacon_aioli_canvas.configure(scrollregion= Chicken_bacon_aioli_canvas.bbox('all')))
    Chicken_bacon_aioli_canvas.create_window((0,0), window= mini_chicken_bacon_aioli, width = 1066, anchor='nw')


Chicken_bacon_aioli_frame = Frame(Intro_Frames.window)
Chicken_bacon_aioli_canvas = Canvas(Chicken_bacon_aioli_frame)
Chicken_bacon_aioli_scroll_bar = ttk.Scrollbar(Chicken_bacon_aioli_frame, orient=VERTICAL,command=Chicken_bacon_aioli_canvas.yview)
mini_chicken_bacon_aioli = Frame(Chicken_bacon_aioli_canvas)


# Chicken and cheese pizza scrollbar and frame
def expand_chicken_cheese():
    hiding_expanding_frames()
    Chicken_cheese_frame.pack(expand=1, fill=BOTH)
    Chicken_cheese_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    Chicken_cheese_scrollbar.pack(side= RIGHT, fill=Y)
    Chicken_cheese_canvas.configure(yscrollcommand = Chicken_cheese_scrollbar.set)
    Chicken_cheese_canvas.bind("<Configure>", lambda e: Chicken_cheese_canvas.configure(scrollregion=Chicken_cheese_canvas.bbox('all')))
    Chicken_cheese_canvas.create_window((0,0), window=mini_chicken_cheese_frame, width = 1066, anchor='nw')


Chicken_cheese_frame = Frame(Intro_Frames.window)
Chicken_cheese_canvas = Canvas(Chicken_cheese_frame)
Chicken_cheese_scrollbar = ttk.Scrollbar(Chicken_cheese_frame, orient= VERTICAL, command= Chicken_cheese_canvas.yview)
mini_chicken_cheese_frame = Frame(Chicken_cheese_canvas)

# Gralic prawn scrollbar and frame
def expanding_gralic_prawn():
    hiding_expanding_frames()
    Gralic_prawn_frame.pack(expand=1, fill= BOTH)
    Gralic_prawn_canvas.pack(side= LEFT, expand=1, fill=BOTH)
    Gralic_prawn_scrollbar.pack(side= RIGHT, fill=Y)
    Gralic_prawn_canvas.configure(yscrollcommand= Gralic_prawn_scrollbar.set)
    Gralic_prawn_canvas.bind("<Configure>", lambda e: Gralic_prawn_canvas.configure(scrollregion= Gralic_prawn_canvas.bbox("all")))
    Gralic_prawn_canvas.create_window((0,0), window=mini_gralic_prawn_frame, width=1066, anchor='nw')


Gralic_prawn_frame = Frame(Intro_Frames.window)
Gralic_prawn_canvas = Canvas(Gralic_prawn_frame)
Gralic_prawn_scrollbar = ttk.Scrollbar(Gralic_prawn_frame, orient=VERTICAL, command=Gralic_prawn_canvas.yview)
mini_gralic_prawn_frame = Frame(Gralic_prawn_canvas)


# Mega meatlover frame and scroll bar
def expanding_mega_meatlover():
    hiding_expanding_frames()
    Mega_meatlover_frame.pack(expand=1, fill=BOTH)
    Mega_meatlover_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    Mega_meatlover_scrollbar.pack(side= RIGHT, fill=Y)
    Mega_meatlover_canvas.configure(yscrollcommand= Mega_meatlover_scrollbar.set)
    Mega_meatlover_canvas.bind("<Configure>", lambda e: Mega_meatlover_canvas.configure(scrollregion= Mega_meatlover_canvas.bbox('all')))
    Mega_meatlover_canvas.create_window((0,0), window=mini_Mega_meatlover_frame,width=1066, anchor='nw')


Mega_meatlover_frame = Frame(Intro_Frames.window)
Mega_meatlover_canvas = Canvas(Mega_meatlover_frame)
Mega_meatlover_scrollbar = ttk.Scrollbar(Mega_meatlover_frame,orient=VERTICAL, command=Mega_meatlover_canvas.yview)
mini_Mega_meatlover_frame = Frame(Mega_meatlover_canvas)


# peri-peri chicken frame and scrollbar
def expanding_peri_peri_chicken():
    hiding_expanding_frames()
    Peri_peri_chicken_frame.pack(expand=1, fill= BOTH)
    Peri_peri_chicken_canvas.pack(side=LEFT, fill= BOTH, expand=1)
    Peri_peri_chicken_scrollbar.pack(side= RIGHT, fill=Y)
    Peri_peri_chicken_canvas.configure(yscrollcommand= Peri_peri_chicken_scrollbar.set)
    Peri_peri_chicken_canvas.bind("<Configure>", lambda e: Peri_peri_chicken_canvas.configure(scrollregion= Peri_peri_chicken_canvas.bbox('all')))
    Peri_peri_chicken_canvas.create_window((0,0),window= mini_Peri_peri_chicken, width = 1066, anchor='nw')


Peri_peri_chicken_frame = Frame(Intro_Frames.window)
Peri_peri_chicken_canvas = Canvas(Peri_peri_chicken_frame)
Peri_peri_chicken_scrollbar = ttk.Scrollbar(Peri_peri_chicken_frame, orient=VERTICAL, command=Peri_peri_chicken_canvas.yview)
mini_Peri_peri_chicken = Frame(Peri_peri_chicken_canvas)


def hiding_expanding_frames():
    Intro_Frames.menu_frame.pack_forget()
    # Regular Range
    American_pepperion_frame.pack_forget()
    Cheesy_gralic_pizza_frame.pack_forget()
    Chicken_supreme_frame.pack_forget()
    Ham_and_cheese_frame.pack_forget()
    Mr_wedge_frame.pack_forget()
    Pepperion_frame.pack_forget()
    Simply_cheese_frame.pack_forget()
    Supreme_frame.pack_forget()
    # Gourmet Range
    Apricot_frame.pack_forget()
    Chicken_bacon_aioli_frame.pack_forget()
    Chicken_cheese_frame.pack_forget()
    Gralic_prawn_frame.pack_forget()
    Mega_meatlover_frame.pack_forget()
    Peri_peri_chicken_frame.pack_forget()


 # Importing the sotring pizza file
import Warning_message_box

# Pizza detail page generator
class Pizza_detail_generator:


    # This the reset of the class which creates and places them in frame correctly
    def allowed_to_checkout(self):
        try:
            if len(Intro_Frames.displaying_frame.winfo_children()) <= 0:
                Intro_Frames.checkout_button.configure(state=DISABLED)
            else:
                Intro_Frames.checkout_button.configure(state=NORMAL)
        except TclError:
            pass

    def __init__(self,pizza_frame,big_pizza_photo, price_photo, pizza_name, pizza_details,going_in_front,going_in_back, adding_pizza):
        self.taking_pizza_image = ImageTk.PhotoImage(file = big_pizza_photo)
        self.taking_price_image = ImageTk.PhotoImage(file = price_photo)
        self.back_button_image = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\back button with pointy arrow.png")
        self.next_button_image = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\next button image.png")
        self.placing_pizza_image = Label(pizza_frame, image= self.taking_pizza_image, bg = '#14141D')
        self.placing_pizza_image.grid(row= 1, column= 0, sticky= 'nw',padx=(30,30), pady = 30)
        self.putting_pizza_name = Label(pizza_frame, text = pizza_name, font = ('robot', 18,'bold'), border=0, bg = '#14141D',fg = 'white', anchor= 'nw')
        self.putting_pizza_name.place(x = 660, y = 30)
        self.putting_detail_of_pizza = Label(pizza_frame, text= pizza_details, font=("Corbel Light", 14), border=0,fg = 'white', bg = '#14141D')
        self.putting_detail_of_pizza.place(x = 660, y = 100)
        self.putting_price_image = Button(pizza_frame, image= self.taking_price_image, bg= "#14141D", border=0, activebackground= "#14141D", command = lambda : [adding_pizza(), self.allowed_to_checkout()], cursor = "hand2")
        self.putting_price_image.place(x = 660, y = 385)
        self.next_button = Button(pizza_frame, image=self.next_button_image,pady =5, padx =5,bg= "#14141D", border=0,activebackground= "#14141D",command =  going_in_front, cursor = "hand2")
        self.next_button.place(x = 905, y = 335.5)
        self.back_button = Button(pizza_frame, image=self.back_button_image,pady =5, padx =5,anchor='nw',bg= "#14141D", border=0, activebackground= "#14141D",command=going_in_back, cursor = "hand2")
        self.back_button.place(y=330, x =660)
        self.topping_labelframe = LabelFrame(pizza_frame, text= 'Customise Your Toppings', font=('robot',22,'bold'), fg = 'white', bg = "#14141D",border=0,pady = 20)
        self.topping_labelframe.grid(row=2,column=0,pady = 60, padx=80,sticky='nw')






# Current topping generator
class Current_topping_generator:
    def __init__(self,current_labelframe, current_topping_photo, current_topping_name,remove_current_topping, constant_column_current, constant_row_current):
        self.taking_current_topping_image = ImageTk.PhotoImage(file = current_topping_photo)
        self.mini_labelframe = LabelFrame(current_labelframe, border=0,background='white', labelanchor='w')
        self.mini_labelframe.grid(padx=12,sticky='w', pady = (0,20), column= constant_column_current, row=constant_row_current)
        self.putting_topping_image = Label(self.mini_labelframe, image= self.taking_current_topping_image, border=0, bg = 'white')
        self.putting_topping_image.grid(row =0, column=0, sticky='n')
        self.name_current_topping = Label(self.mini_labelframe, text = current_topping_name, font=('Helvetica',8), bg = 'white', fg = 'black')
        self.name_current_topping.grid(row = 1, column= 0,sticky='n')
        self.subract_image = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\minise buttoneditedresizedx4.png")
        self.subract_button = Button(self.mini_labelframe, image = self.subract_image ,border=0 ,background='white', activebackground='white', command = remove_current_topping, cursor= 'hand2')
        self.subract_button.grid(row = 0, column=1, sticky='n',padx =0)


# Add on toppings mini labelframe generator
class Add_on_topping_generator:
    def __init__(self, add_on_labelframe, add_on_topping_photo, add_on_topping_name, row_value, column_value,add_to_current):
        self.taking_add_on_topping_image = ImageTk.PhotoImage(file = add_on_topping_photo)
        self.mini_labelframe_add_on_topping = LabelFrame(add_on_labelframe, background= 'white', border = 0)
        self.mini_labelframe_add_on_topping.grid(row = row_value, column = column_value, padx = 20, pady = (0,20))
        self.topping_button = Button(self.mini_labelframe_add_on_topping, image= self.taking_add_on_topping_image,background='white',border=0, command= add_to_current, activebackground='white', cursor= 'hand2')
        self.topping_button.grid(row = 0, column=0, sticky='nw')
        self.add_on_topping_name = Label(self.mini_labelframe_add_on_topping, text = add_on_topping_name,  font=('Helvetica',8), bg = 'white', fg = 'black')
        self.add_on_topping_name.grid(row = 1, column= 0,sticky='n')



# Simply cheese basic information
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def simply_cheese_going_order_list():
    Simply_cheese_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def simply_cheese_going_menu_page():
    Simply_cheese_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


simply_cheese_page = Pizza_detail_generator(mini_Simply_cheese_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Simply Cheese Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\add_cart button_resized.png", "SIMPLY CHEESE", "Lots of mozzarella", simply_cheese_going_order_list, simply_cheese_going_menu_page, lambda : Total_cost_order.simply_cheese_add_order())



# Moduel for putting mini current label frame in the moduel
from Simply_cheese_page import simply_cheese_intro_labelframes, Anchovies, Mozzarella_topping, Paneer_Cheese, Baby_spinach, Camembert_Cheese, Cherry_tomato, Cherry_wood_somked_leg_ham, Chili_Flakes, Capasicum, Feta, Franks_RedHot_Orginal_Hot_Sauce, Fresh_Tomatos, Gralic_base_sauce_swirl, Gralic_Parmesan_Sauce, Ground_beef,\
    Hickory_BBQ_Sauce, Hollandaise_sauce_swirl, Jalapenos, Mayonnaise, Mushroom, Olives, Oregano, Pepperoni, Peri_peri_sauce_swirl, Pineapple, Planet_based_Beef, Prawns, Rasher_Bacon, Red_onion, Seasoned_Chicken, Spring_Onion, Tomato_capsicum_sauce



# Creating a new varibale for the topping list for simlply cheese so it can be used in differnet moduels as the actual files causes import loop error
topping_simply_cheese_list = simply_cheese_intro_labelframes.storing_current_toppings


# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_toppings_simply_cheese():
    for topping_current in simply_cheese_intro_labelframes.current_labelframe_only.winfo_children():
        topping_current.destroy()
        simply_cheese_intro_labelframes.storing_current_toppings.clear()
    simply_cheese_intro_labelframes.storing_current_toppings.append("Mozzarella Cheese")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(Anchovies)
    importlib.reload(Mozzarella_topping)
    importlib.reload(Paneer_Cheese)
    importlib.reload(Baby_spinach)
    importlib.reload(Camembert_Cheese)
    importlib.reload(Cherry_tomato)
    importlib.reload(Cherry_wood_somked_leg_ham)
    importlib.reload(Chili_Flakes)
    importlib.reload(Capasicum)
    importlib.reload(Feta)
    importlib.reload(Franks_RedHot_Orginal_Hot_Sauce)
    importlib.reload(Fresh_Tomatos)
    importlib.reload(Gralic_base_sauce_swirl)
    importlib.reload(Gralic_Parmesan_Sauce)
    importlib.reload(Ground_beef)
    importlib.reload(Hickory_BBQ_Sauce)
    importlib.reload(Hollandaise_sauce_swirl)
    importlib.reload(Jalapenos)
    importlib.reload(Mayonnaise)
    importlib.reload(Mushroom)
    importlib.reload(Olives)
    importlib.reload(Oregano)
    importlib.reload(Pepperoni)
    importlib.reload(Peri_peri_sauce_swirl)
    importlib.reload(Pineapple)
    importlib.reload(Planet_based_Beef)
    importlib.reload(Prawns)
    importlib.reload(Rasher_Bacon)
    importlib.reload(Red_onion)
    importlib.reload(Seasoned_Chicken)
    importlib.reload(Spring_Onion)
    importlib.reload(Tomato_capsicum_sauce)


# American Pepperion Pizza information
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def american_pepperion_going_order_list():
    American_pepperion_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def american_pepperion_going_menu_page():
    American_pepperion_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


american_pepperion_page = Pizza_detail_generator(mini_American_pepperion_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\America Pepperoni Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\add_cart button_resized.png", "AMERICAN PEPPERION", "Loaded with double the amount of\nyour favourite Domino's pepperoni!", american_pepperion_going_order_list, american_pepperion_going_menu_page, lambda : Total_cost_order.american_pepperoni_add_order())


# Moduel for putting mini current label frame in the moduel
from American_Pepperoni_PAGE import American_pepperoni_labelframe as amp
from American_Pepperoni_PAGE import Anchovies as pizza_1_1
from American_Pepperoni_PAGE import Baby_spinach as pizza_1_2
from American_Pepperoni_PAGE import Camembert_Cheese as pizza_1_3
from American_Pepperoni_PAGE import Cherry_tomato as pizza_1_4
from American_Pepperoni_PAGE import Cherry_wood_somked_leg_ham as pizza_1_5
from American_Pepperoni_PAGE import Chili_Flakes as pizza_1_6
from American_Pepperoni_PAGE import Capasicum as pizza_1_7
from American_Pepperoni_PAGE import Feta as pizza_1_8
from American_Pepperoni_PAGE import Franks_RedHot_Orginal_Hot_Sauce as pizza_1_9
from American_Pepperoni_PAGE import Fresh_Tomatos as pizza_1_10
from American_Pepperoni_PAGE import Gralic_base_sauce_swirl as pizza_1_11
from American_Pepperoni_PAGE import Gralic_Parmesan_Sauce as pizza_1_12
from American_Pepperoni_PAGE import Ground_beef as pizza_1_13
from American_Pepperoni_PAGE import Hickory_BBQ_Sauce as pizza_1_14
from American_Pepperoni_PAGE import Hollandaise_sauce_swirl as pizza_1_15
from American_Pepperoni_PAGE import Jalapenos as pizza_1_16
from American_Pepperoni_PAGE import Mayonnaise as pizza_1_17
from American_Pepperoni_PAGE import Mozzarella_topping as pizza_1_18
from American_Pepperoni_PAGE import Mushroom as pizza_1_19
from American_Pepperoni_PAGE import Olives as pizza_1_20
from American_Pepperoni_PAGE import Oregano as pizza_1_21
from American_Pepperoni_PAGE import Paneer_Cheese as pizza_1_22
from American_Pepperoni_PAGE import Pepperoni as pizza_1_23
from American_Pepperoni_PAGE import Peri_peri_sauce_swirl as pizza_1_24
from American_Pepperoni_PAGE import Pineapple as pizza_1_25
from American_Pepperoni_PAGE import Planet_based_Beef as pizza_1_26
from American_Pepperoni_PAGE import Prawns as pizza_1_27
from American_Pepperoni_PAGE import Rasher_Bacon as pizza_1_28
from American_Pepperoni_PAGE import Red_onion as pizza_1_29
from American_Pepperoni_PAGE import Seasoned_Chicken as pizza_1_30
from American_Pepperoni_PAGE import Spring_Onion as pizza_1_31
from American_Pepperoni_PAGE import Tomato_capsicum_sauce as pizza_1_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_toppings_american_pepperoni():
    for topping_current in amp.current_labelframe_only.winfo_children():
        topping_current.destroy()
        amp.storing_current_toppings.clear()
    amp.storing_current_toppings.append("Mozzarella Cheese")
    amp.storing_current_toppings.append("Pepperoni")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_1_1)
    importlib.reload(pizza_1_2)
    importlib.reload(pizza_1_3)
    importlib.reload(pizza_1_4)
    importlib.reload(pizza_1_5)
    importlib.reload(pizza_1_6)
    importlib.reload(pizza_1_7)
    importlib.reload(pizza_1_8)
    importlib.reload(pizza_1_9)
    importlib.reload(pizza_1_10)
    importlib.reload(pizza_1_11)
    importlib.reload(pizza_1_12)
    importlib.reload(pizza_1_13)
    importlib.reload(pizza_1_14)
    importlib.reload(pizza_1_15)
    importlib.reload(pizza_1_16)
    importlib.reload(pizza_1_17)
    importlib.reload(pizza_1_18)
    importlib.reload(pizza_1_19)
    importlib.reload(pizza_1_20)
    importlib.reload(pizza_1_21)
    importlib.reload(pizza_1_22)
    importlib.reload(pizza_1_23)
    importlib.reload(pizza_1_24)
    importlib.reload(pizza_1_25)
    importlib.reload(pizza_1_26)
    importlib.reload(pizza_1_27)
    importlib.reload(pizza_1_28)
    importlib.reload(pizza_1_29)
    importlib.reload(pizza_1_30)
    importlib.reload(pizza_1_31)
    importlib.reload(pizza_1_32)


# Creating a new varibale for the topping list for simlply cheese so it can be used in differnet moduels as the actual files causes import loop error
topping_american_pepperoni_list = amp.storing_current_toppings
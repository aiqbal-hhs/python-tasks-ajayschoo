# All the Moduels
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import expanding_pages


# storing current topping list
storing_current_toppings = ['Mozzarella Cheese', 'Gralic Base Sauce Swirl', 'Oregano']




# checking if the length of the storing list is greater than 1 if not than we delete the frame and destroy the space for bettter looks
def reszing():
    if len(storing_current_toppings) < 1:
        current_labelframe_only.configure(height=1)
    else:
        pass


# Background for customis toppings to differenist
topping_background_frame = Frame(expanding_pages.cheesy_gralic_page.topping_labelframe,bg='white', highlightcolor='white', highlightthickness=0)
topping_background_frame.pack(expand=1,fill=BOTH)

# Toppings that are added to the pizza are current toppings
current_topping_labelframe = LabelFrame(topping_background_frame, text = "Current Toppings", font=('robot',16, 'bold'),fg= 'black', bg = 'white',border=0 ,pady = 1,labelanchor='nw')
current_topping_labelframe.grid(row=0, column=0, pady = (10,10), sticky='nw')


# information label frame
information_label_frame = Frame(current_topping_labelframe, background='white', border=0)
information_label_frame.grid(row=0,column = 0, sticky='w', pady = (1,10))


# Subheading for current toppings
information_current_topping  = Label(information_label_frame, text = "10 maximun toppings allowed per pizza (including current toppings).", font=('robot', 11), fg = 'black', border=0,bg ='white')
information_current_topping.grid(row=0, column = 0, sticky='nw', padx=(0,278))


information2_current_topping  = Label(information_label_frame, text = "Tap ", font=('robot', 11), fg = 'black', border=0,bg ='white')
information2_current_topping.grid(row=0, column=2, sticky='ne', padx=0)


information2_continue_image = ImageTk.PhotoImage(file = r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\minise buttoneditedresizedx4.png")
information2_continue_label = Label(information_label_frame, image = information2_continue_image,border = 0, background='white')
information2_continue_label.grid(row=0, column= 3, sticky='ne')


information3_label = Label(information_label_frame, text = " to remove a topping.", font=("robot",11),fg = 'black', background='white', border = 0)
information3_label.grid(row=0, column=4, sticky='ne')


# new and only for current topping labelframe. Other writing stuff is being kept out
current_labelframe_only = LabelFrame(current_topping_labelframe, border=0, background='white', padx = 8 )
current_labelframe_only.grid(row=1, column=0, sticky='w', pady = (10,0))


# Add topping labelfram, has all the topping that could be added to your pizza
add_topping_labelframe = LabelFrame(topping_background_frame, text = 'Add on Toppings', font = ("robot",16, 'bold'), fg = 'black', bg = 'white', border = 0, pady =  1)
add_topping_labelframe.grid(row=1, column= 0)


# information labeframe for add on toppings
informatio_labelframe2 = LabelFrame(add_topping_labelframe,background='white', border=0,labelanchor='w')
informatio_labelframe2.grid(row=0,column = 0, sticky='w', pady = (0,20))


# Information for add on toppings
information1_add_on_toppings = Label(informatio_labelframe2, text = "Maximun of 1 serve of any single topping ($0.50 per topping).", font=("robot",11),fg = 'black', background='white', border = 0 )
information1_add_on_toppings.grid(row = 0,column = 0,sticky='nw')


information2_add_on_toppings = Label(informatio_labelframe2, text= "Tap on topping's image to add.", font=("robot",11),fg = 'black', background='white', border = 0 )
information2_add_on_toppings.grid(row = 0,column = 4,sticky='ne',padx=(310,0))


# creating another labeframe for toppings
add_on_topping_labelframe_only = LabelFrame(add_topping_labelframe, background='white', border=0, padx=10)
add_on_topping_labelframe_only.grid(row=1, column=0, sticky='w')








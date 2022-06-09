from tkinter import *
from tkinter import ttk
from PIL import ImageTk


# Generator menu pages or menu items
class Meun_item_geneartor:

    def __init__(self,master_frame,pizza_image,add_button_image,row_num,column_num,y_value,x_value,name_of_pizza,detail_pizza,detail_pizza1,detail_pizza2,expand_menu_item):
        self.pizza_photo = ImageTk.PhotoImage(file = pizza_image)
        self.add_button_photo = ImageTk.PhotoImage(file = add_button_image)
        self.mini_pizza_item_frame = Frame(master_frame,bg='white')
        self.mini_pizza_item_frame.grid(row = row_num,column=column_num,padx=x_value,pady=(y_value,40))
        self.packing_pizza_image = Label(self.mini_pizza_item_frame,image=self.pizza_photo,background='white',anchor='nw',border=0)
        self.packing_pizza_image.grid(row =0,column=0,pady=0,padx=0)
        self.pizza_name = Label(self.mini_pizza_item_frame,text = name_of_pizza,font = ('Bahnschrift SemiBold',14),background='white')
        self.pizza_name.grid(row =1,column=0,pady = (5,10),sticky='nw',padx=8)
        self.detail_of_pizza = Label(self.mini_pizza_item_frame,text = detail_pizza, font=('Corbel Light',10),background='white',fg ='black',pady=0)
        self.detail_of_pizza.grid(row =2,column=0,sticky='nw',pady=(3,0),padx =8)
        self.detail_of_pizza1 = Label(self.mini_pizza_item_frame, text=detail_pizza1, font=('Corbel Light', 10),background='white', fg='black',pady=0)
        self.detail_of_pizza1.grid(row=3, column=0, sticky='nw',pady=0,padx =8)
        self.detail_of_pizza2 = Label(self.mini_pizza_item_frame, text=detail_pizza2, font=('Corbel Light', 10),background='white', fg='black',pady=0)
        self.detail_of_pizza2.grid(row=4, column=0, sticky='nw',pady=(0,5),padx =8)
        self.packing_add_button = Button(self.mini_pizza_item_frame,image=self.add_button_photo,border=0,background='white',activebackground='white',command=expand_menu_item, cursor = "hand2")
        self.packing_add_button.grid(row = 5,column=0,pady=(15,0))


# Import staring frames here to avoid loop imports
import Intro_Frames
















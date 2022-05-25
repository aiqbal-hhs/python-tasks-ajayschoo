import Delivery_or_pickup
import expanding_pages
import Intro_Frames
from tkinter import *
import customtkinter
from PIL import ImageTk
import Warning_message_box
import Delivery_or_pickup


# Class for mini order list diplay for pizza
class Order_pizza_list:

    # This function that brings a pizza from out so the user know what one they are on
    def __init__(self, image_of_mini_pizza, name_of_pizza, price_of_pizza, remove_command):
        self.order_pizza_frame = customtkinter.CTkFrame(Intro_Frames.displaying_frame, fg_color='#F2F2F2', border_width=2, border_color='#5E5E5E', bg_color='white')
        self.order_pizza_frame.pack( pady= 1, padx=3, anchor="w", fill = X)
        self.image_of_mini_pizza_displaying = ImageTk.PhotoImage(file = image_of_mini_pizza)
        self.displaying_mini_pizza = Label(self.order_pizza_frame, image = self.image_of_mini_pizza_displaying,  bg= '#F2F2F2', padx=0, border=0)
        self.displaying_mini_pizza.grid( pady= 6, padx= (6,6), row=0, column=0, sticky='nw', rowspan=2)
        self.displaying_pizza_name = Label(self.order_pizza_frame, text = name_of_pizza , font=("Bahnschrift SemiBold", 13),  bg= '#F2F2F2', padx=0, border=0)
        self.displaying_pizza_name.grid( pady=0, padx= (0,2), row=0, column=1, sticky='s')
        self.displaying_pizza_price = Label(self.order_pizza_frame, text = f"${price_of_pizza}" , font=("Bahnschrift SemiBold", 13),  bg= '#F2F2F2', padx=0, border=0)
        self.displaying_pizza_price.grid(row = 0, column= 2, pady=0, padx= (10,2) )
        self.remove_button = Button(self.order_pizza_frame, text = 'Remove' , font=("Robot", 13),  bg= '#F2F2F2', padx=0, border=0, fg='red', cursor='hand2', activebackground='#F2F2F2', activeforeground='red', command = remove_command)
        self.remove_button.grid( pady=4, padx=3, row=1, column=2, sticky='se')


# Making total amount in this moduelso it can be used globally in this moduel and this variable also carries the pickup and delivery charge
global total_cost_for_all_pizzas
total_cost_for_all_pizzas = 0

# two list that are for pickup and delivery
total_cost_list = [0,0]


def checker_delivery_or_pickup():
    global total_cost_for_all_pizzas, final_cost_with_delivery, final_cost_pickup, total_cost_list
    if Delivery_or_pickup.delivery_or_pickup_teller == 1:
        total_cost_list.clear()
        total_cost_list.append(total_cost_for_all_pizzas)
        total_cost_list.append(3)
        Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    elif Delivery_or_pickup.delivery_or_pickup_teller == 0:
        total_cost_list.clear()
        total_cost_list.append(total_cost_for_all_pizzas)
        total_cost_list.append(0)
        Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")

# This a gloabl counter all pizzas and it will decided what number to put a specific thing in treeview
global pizza_counter
pizza_counter = 0



# This all for simply cheese pizza
# This is simply cheese counter so everytime the button is clicked on simply cheese it updates
global overall_SC_counter
overall_SC_counter = 1


global SC_in_or_out_1, SC_in_or_out_2, SC_in_or_out_3, SC_in_or_out_4, SC_in_or_out_5
# 0 means a simply cheese pizza is not in the order list whereas one measn the pizza is in the list
SC_in_or_out_1 = 0
SC_in_or_out_2 = 0
SC_in_or_out_3 = 0
SC_in_or_out_4 = 0
SC_in_or_out_5 = 0


# Function that checks if the order list is fill if so then it will make the check out button normal. Whereas, if the order list is empty the check out button will br disable
def allowed_to_checkout():
    if len(Intro_Frames.displaying_frame.winfo_children()) <= 1:
        Intro_Frames.checkout_button.configure(state=DISABLED)
    else:
        Intro_Frames.checkout_button.configure(state=NORMAL)


# This where everything get remove for simply cheese
def removing_simply_cheese_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_SC1, SC_in_or_out_1
    allowed_to_checkout()
    simply_cheese_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_SC1) * 0.50 + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Simply Cheese")
    show_topping_frame_SC1.destroy()
    # updating the in and out Simply cheese pizza
    SC_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove for simply cheese
def removing_simply_cheese_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_SC2, SC_in_or_out_2
    allowed_to_checkout()
    simply_cheese_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_SC2 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Simply Cheese")
    show_topping_frame_SC2.destroy()
    # updating the in and out Simply cheese pizza
    SC_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove for simply cheese
def removing_simply_cheese_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_SC3, SC_in_or_out_3
    allowed_to_checkout()
    simply_cheese_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_SC3) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Simply Cheese")
    show_topping_frame_SC3.destroy()
    # updating the in and out Simply cheese pizza
    SC_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove for simply cheese
def removing_simply_cheese_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_SC4, SC_in_or_out_4
    allowed_to_checkout()
    simply_cheese_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_SC4 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Simply Cheese")
    show_topping_frame_SC4.destroy()
    # updating the in and out Simply cheese pizza
    SC_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove for simply cheese
def removing_simply_cheese_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_SC5, SC_in_or_out_5
    allowed_to_checkout()
    simply_cheese_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_SC5) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Simply Cheese")
    show_topping_frame_SC5.destroy()
    # updating the in and out Simply cheese pizza
    SC_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types of simply cheese get add iwht it toppings
def adding_simply_cheese_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global simply_cheese_1, total_cost_for_all_pizzas,show_topping_frame_SC1, length_SC1, SC_in_or_out_1, total_cost_list
    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_SC1 = len(expanding_pages.topping_simply_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    simply_cheese_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\SIMPLY CHEESE Resized for order list.jpg", "Simply\nCheese", f"{((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50):.2f}", removing_simply_cheese_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_SC1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_SC1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_SC1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_SC1, text = "Simply Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_SC1, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_simply_cheese_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_SC1 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text = topping_SC1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC1, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_SC(e):
        show_topping_frame_SC1.place(x = 440, y= 40)
    def hide_topping_SC(e):
        show_topping_frame_SC1.place_forget()

    simply_cheese_1.order_pizza_frame.bind('<Enter>', show_topping_SC)
    simply_cheese_1.order_pizza_frame.bind("<Leave>", hide_topping_SC)

    # updating the in and out Simply cheese pizza
    SC_in_or_out_1 = 1



# This where all types of simply cheese get add iwht it toppings
def adding_simply_cheese_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global simply_cheese_2, total_cost_for_all_pizzas, show_topping_frame_SC2, length_SC2, SC_in_or_out_2, total_cost_list

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_SC2 = len(expanding_pages.topping_simply_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    simply_cheese_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\SIMPLY CHEESE Resized for order list.jpg", "Simply\nCheese", f"{((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50):.2f}", removing_simply_cheese_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_SC2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_SC2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_SC2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_SC2, text = "Simply Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_SC2, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_simply_cheese_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_SC2 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text = topping_SC2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC2, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_SC(e):
        show_topping_frame_SC2.place(x = 440, y= 40)
    def hide_topping_SC(e):
        show_topping_frame_SC2.place_forget()

    simply_cheese_2.order_pizza_frame.bind('<Enter>', show_topping_SC)
    simply_cheese_2.order_pizza_frame.bind("<Leave>", hide_topping_SC)

    # updating the in and out Simply cheese pizza
    SC_in_or_out_2 = 1




# This where all types of simply cheese get add iwht it toppings
def adding_simply_cheese_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global simply_cheese_3, total_cost_for_all_pizzas, show_topping_frame_SC3, length_SC3, SC_in_or_out_3, total_cost_list

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_SC3 = len(expanding_pages.topping_simply_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    simply_cheese_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\SIMPLY CHEESE Resized for order list.jpg", "Simply\nCheese", f"{((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50):.2f}", removing_simply_cheese_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_SC3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_SC3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_SC3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_SC3, text = "Simply Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_SC3, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_simply_cheese_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_SC3 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text = topping_SC3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC3, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_SC(e):
        show_topping_frame_SC3.place(x = 440, y= 40)
    def hide_topping_SC(e):
        show_topping_frame_SC3.place_forget()

    simply_cheese_3.order_pizza_frame.bind('<Enter>', show_topping_SC)
    simply_cheese_3.order_pizza_frame.bind("<Leave>", hide_topping_SC)

    # updating the in and out Simply cheese pizza
    SC_in_or_out_3 = 1



# This where all types of simply cheese get add iwht it toppings
def adding_simply_cheese_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global simply_cheese_4, total_cost_for_all_pizzas, show_topping_frame_SC4, length_SC4, SC_in_or_out_4, total_cost_list

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_SC4 = len(expanding_pages.topping_simply_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    simply_cheese_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\SIMPLY CHEESE Resized for order list.jpg", "Simply\nCheese", f"{((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50):.2f}", removing_simply_cheese_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_SC4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_SC4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_SC4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_SC4, text = "Simply Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_SC4, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_simply_cheese_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_SC4 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text = topping_SC4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC4, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_SC(e):
        show_topping_frame_SC4.place(x = 440, y= 40)
    def hide_topping_SC(e):
        show_topping_frame_SC4.place_forget()

    simply_cheese_4.order_pizza_frame.bind('<Enter>', show_topping_SC)
    simply_cheese_4.order_pizza_frame.bind("<Leave>", hide_topping_SC)

    # updating the in and out Simply cheese pizza
    SC_in_or_out_4 = 1


# This where all types of simply cheese get add iwht it toppings
def adding_simply_cheese_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global simply_cheese_5, total_cost_for_all_pizzas, show_topping_frame_SC5, length_SC5, SC_in_or_out_5, total_cost_list

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_SC5 = len(expanding_pages.topping_simply_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    simply_cheese_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\SIMPLY CHEESE Resized for order list.jpg", "Simply\nCheese", f"{((len(expanding_pages.topping_simply_cheese_list) * 0.50) + 8.50):.2f}", removing_simply_cheese_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_SC5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_SC5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_SC5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_SC5, text = "Simply Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_SC5, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_simply_cheese_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_SC5 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text = topping_SC5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC5, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_SC(e):
        show_topping_frame_SC5.place(x = 440, y= 40)
    def hide_topping_SC(e):
        show_topping_frame_SC5.place_forget()

    simply_cheese_5.order_pizza_frame.bind('<Enter>', show_topping_SC)
    simply_cheese_5.order_pizza_frame.bind("<Leave>", hide_topping_SC)

    # updating the in and out Simply cheese pizza
    SC_in_or_out_5 = 1



# This take of the simply cheese adding in the order list
def simply_cheese_add_order():
    global overall_SC_counter, SC_in_or_out_1, SC_in_or_out_2, SC_in_or_out_3, SC_in_or_out_4, SC_in_or_out_5

    # Telling the the counter that simply cheese has been added or display a number
    Warning_message_box.storing_pizzas.append("Simply Cheese")

    if SC_in_or_out_1 == 2:
        SC_in_or_out_1 = 0
        overall_SC_counter = 1

    elif SC_in_or_out_2 == 2:
        SC_in_or_out_2 = 0
        overall_SC_counter = 2

    elif SC_in_or_out_3 == 2:
        SC_in_or_out_3 = 0
        overall_SC_counter = 3

    elif SC_in_or_out_4 == 2:
        SC_in_or_out_4 = 0
        overall_SC_counter = 4

    elif SC_in_or_out_5 == 2:
        SC_in_or_out_5 = 0
        overall_SC_counter = 5



    if overall_SC_counter == 1:
        if SC_in_or_out_1 == 0:
            adding_simply_cheese_1()



    elif overall_SC_counter == 2:
        if SC_in_or_out_2 == 0:
            adding_simply_cheese_2()


    elif overall_SC_counter == 3:
        if SC_in_or_out_3 == 0:
            adding_simply_cheese_3()


    elif overall_SC_counter== 4:
        if SC_in_or_out_4 == 0:
            adding_simply_cheese_4()


    elif overall_SC_counter == 5:
        overall_SC_counter = 0
        if SC_in_or_out_5 == 0:
            adding_simply_cheese_5()



    # This the counter for all five simply cheese pizza
    overall_SC_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_toppings_simply_cheese()
    Warning_message_box.add()




# AM means the American pepperion and all the adding for american pepperoni
# This all for American Pepperoni pizza
# This is American Pepperoni counter so everytime the button is clicked on American Pepperoni it updates
global overall_AM_counter
overall_AM_counter = 1


global AM_in_or_out_1, AM_in_or_out_2, AM_in_or_out_3, AM_in_or_out_4, AM_in_or_out_5
# 0 means a American Pepperoni pizza is not in the order list whereas one measn the pizza is in the list
AM_in_or_out_1 = 0
AM_in_or_out_2 = 0
AM_in_or_out_3 = 0
AM_in_or_out_4 = 0
AM_in_or_out_5 = 0



# This where everything get remove for American Pepperoni
def removing_american_pepperoni_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AM1, AM_in_or_out_1
    allowed_to_checkout()
    american_pepperoni_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_AM1) * 0.50 + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("American Pepperoni")
    show_topping_frame_AM1.destroy()
    # updating the in and out American Pepperoni pizza
    AM_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove for American Pepperoni
def removing_american_pepperoni_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AM2, AM_in_or_out_2
    allowed_to_checkout()
    american_pepperoni_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_AM2 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("American Pepperoni")
    show_topping_frame_AM2.destroy()
    # updating the in and out American Pepperoni pizza
    AM_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove for American Pepperoni
def removing_american_pepperoni_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AM3, AM_in_or_out_3
    allowed_to_checkout()
    american_pepperoni_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_AM3) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("American Pepperoni")
    show_topping_frame_AM3.destroy()
    # updating the in and out American Pepperoni pizza
    AM_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove for American Pepperoni
def removing_american_pepperoni_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AM4, AM_in_or_out_4
    allowed_to_checkout()
    american_pepperoni_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_AM4 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("American Pepperoni")
    show_topping_frame_AM4.destroy()
    # updating the in and out American Pepperoni pizza
    AM_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove for American Pepperoni
def removing_american_pepperoni_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AM5, AM_in_or_out_5
    allowed_to_checkout()
    american_pepperoni_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_AM5) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("American Pepperoni")
    show_topping_frame_AM5.destroy()
    # updating the in and out American Pepperoni pizza
    AM_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types of American Pepperoni get add iwht it toppings
def adding_american_pepperoni_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global american_pepperoni_1, total_cost_for_all_pizzas,show_topping_frame_AM1, length_AM1, AM_in_or_out_1, total_cost_list
    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AM1 = len(expanding_pages.topping_american_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    american_pepperoni_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\America Pepperoni Resized order list.png", "American\nPepperoni", f"{((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50):.2f}", removing_american_pepperoni_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AM1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AM1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AM1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AM1, text = "American Pepperoni", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AM1, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_american_pepperoni_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_AM1 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM1, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_AM(e):
        show_topping_frame_AM1.place(x = 440, y= 40)
    def hide_topping_AM(e):
        show_topping_frame_AM1.place_forget()

    american_pepperoni_1.order_pizza_frame.bind('<Enter>', show_topping_AM)
    american_pepperoni_1.order_pizza_frame.bind("<Leave>", hide_topping_AM)

    # updating the in and out American Pepperoni pizza
    AM_in_or_out_1 = 1



# This where all types of American Pepperoni get add iwht it toppings
def adding_american_pepperoni_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global american_pepperoni_2, total_cost_for_all_pizzas, show_topping_frame_AM2, length_AM2, AM_in_or_out_2, total_cost_list

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AM2 = len(expanding_pages.topping_american_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    american_pepperoni_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\America Pepperoni Resized order list.png", "American\nPepperoni", f"{((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50):.2f}", removing_american_pepperoni_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AM2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AM2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AM2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AM2, text = "American Pepperoni", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AM2, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_american_pepperoni_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_AM2 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM2, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_AM(e):
        show_topping_frame_AM2.place(x = 440, y= 40)
    def hide_topping_AM(e):
        show_topping_frame_AM2.place_forget()

    american_pepperoni_2.order_pizza_frame.bind('<Enter>', show_topping_AM)
    american_pepperoni_2.order_pizza_frame.bind("<Leave>", hide_topping_AM)

    # updating the in and out American Pepperoni pizza
    AM_in_or_out_2 = 1




# This where all types of American Pepperoni get add iwht it toppings
def adding_american_pepperoni_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global american_pepperoni_3, total_cost_for_all_pizzas, show_topping_frame_AM3, length_AM3, AM_in_or_out_3, total_cost_list

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AM3 = len(expanding_pages.topping_american_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    american_pepperoni_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\America Pepperoni Resized order list.png", "American\nPepperoni", f"{((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50):.2f}", removing_american_pepperoni_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AM3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AM3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AM3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AM3, text = "American Pepperoni", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AM3, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_american_pepperoni_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_AM3 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM3, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_AM(e):
        show_topping_frame_AM3.place(x = 440, y= 40)
    def hide_topping_AM(e):
        show_topping_frame_AM3.place_forget()

    american_pepperoni_3.order_pizza_frame.bind('<Enter>', show_topping_AM)
    american_pepperoni_3.order_pizza_frame.bind("<Leave>", hide_topping_AM)

    # updating the in and out American Pepperoni pizza
    AM_in_or_out_3 = 1



# This where all types of American Pepperoni get add iwht it toppings
def adding_american_pepperoni_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global american_pepperoni_4, total_cost_for_all_pizzas, show_topping_frame_AM4, length_AM4, AM_in_or_out_4, total_cost_list

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AM4 = len(expanding_pages.topping_american_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    american_pepperoni_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\America Pepperoni Resized order list.png", "American\nPepperoni", f"{((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50):.2f}", removing_american_pepperoni_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AM4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AM4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AM4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AM4, text = "American Pepperoni", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AM4, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_american_pepperoni_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_AM4 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM4, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_AM(e):
        show_topping_frame_AM4.place(x = 440, y= 40)
    def hide_topping_AM(e):
        show_topping_frame_AM4.place_forget()

    american_pepperoni_4.order_pizza_frame.bind('<Enter>', show_topping_AM)
    american_pepperoni_4.order_pizza_frame.bind("<Leave>", hide_topping_AM)

    # updating the in and out American Pepperoni pizza
    AM_in_or_out_4 = 1


# This where all types of American Pepperoni get add iwht it toppings
def adding_american_pepperoni_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global american_pepperoni_5, total_cost_for_all_pizzas, show_topping_frame_AM5, length_AM5, AM_in_or_out_5, total_cost_list

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AM5 = len(expanding_pages.topping_american_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    american_pepperoni_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\America Pepperoni Resized order list.png", "American\nPepperoni", f"{((len(expanding_pages.topping_american_pepperoni_list) * 0.50) + 8.50):.2f}", removing_american_pepperoni_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AM5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AM5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AM5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AM5, text = "American Pepperoni", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AM5, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    count_topping = 1
    if len(expanding_pages.topping_american_pepperoni_list) == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for topping_AM5 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM5, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)


    def show_topping_AM(e):
        show_topping_frame_AM5.place(x = 440, y= 40)
    def hide_topping_AM(e):
        show_topping_frame_AM5.place_forget()

    american_pepperoni_5.order_pizza_frame.bind('<Enter>', show_topping_AM)
    american_pepperoni_5.order_pizza_frame.bind("<Leave>", hide_topping_AM)

    # updating the in and out American Pepperoni pizza
    AM_in_or_out_5 = 1



# This take of the American Pepperoni adding in the order list
def american_pepperoni_add_order():
    global overall_AM_counter, AM_in_or_out_1, AM_in_or_out_2, AM_in_or_out_3, AM_in_or_out_4, AM_in_or_out_5

    # Telling the the counter that American Pepperoni has been added or display a number
    Warning_message_box.storing_pizzas.append("American Pepperoni")

    if AM_in_or_out_1 == 2:
        AM_in_or_out_1 = 0
        overall_AM_counter = 1

    elif AM_in_or_out_2 == 2:
        AM_in_or_out_2 = 0
        overall_AM_counter = 2

    elif AM_in_or_out_3 == 2:
        AM_in_or_out_3 = 0
        overall_AM_counter = 3

    elif AM_in_or_out_4 == 2:
        AM_in_or_out_4 = 0
        overall_AM_counter = 4

    elif AM_in_or_out_5 == 2:
        AM_in_or_out_5 = 0
        overall_AM_counter = 5



    if overall_AM_counter == 1:
        if AM_in_or_out_1 == 0:
            adding_american_pepperoni_1()



    elif overall_AM_counter == 2:
        if AM_in_or_out_2 == 0:
            adding_american_pepperoni_2()


    elif overall_AM_counter == 3:
        if AM_in_or_out_3 == 0:
            adding_american_pepperoni_3()


    elif overall_AM_counter== 4:
        if AM_in_or_out_4 == 0:
            adding_american_pepperoni_4()


    elif overall_AM_counter == 5:
        overall_AM_counter = 0
        if AM_in_or_out_5 == 0:
            adding_american_pepperoni_5()



    # This the counter for all five American Pepperoni pizza
    overall_AM_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_toppings_american_pepperoni()
    Warning_message_box.add()
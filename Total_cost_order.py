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
# SC stands for Simply Cheese
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

    # Here is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_simply_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_simply_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_simply_cheese_list[0])
        expanding_pages.topping_simply_cheese_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text=no_charge_topping, background='white',font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column=0,sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_SC1 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text = topping_SC1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC1, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1, padx= (3,0))


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

    # Here is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_simply_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_simply_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_simply_cheese_list[0])
        expanding_pages.topping_simply_cheese_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text=no_charge_topping, background='white',font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column=0,sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_SC2 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text = topping_SC2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC2, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1, padx= (3,0))


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

    # Here is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_simply_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_simply_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_simply_cheese_list[0])
        expanding_pages.topping_simply_cheese_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text=no_charge_topping, background='white',font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column=0,sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_SC3 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text = topping_SC3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC3, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1, padx= (3,0))


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

    # Here is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_simply_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_simply_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_simply_cheese_list[0])
        expanding_pages.topping_simply_cheese_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text=no_charge_topping, background='white',font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column=0,sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_SC4 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text = topping_SC4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC4, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1, padx= (3,0))


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

    # Here is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_simply_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_simply_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_simply_cheese_list[0])
        expanding_pages.topping_simply_cheese_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_SC5 in expanding_pages.topping_simply_cheese_list:
            Label(show_topping_name_frame, text=topping_SC5, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_SC5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_SC5, text = f"${8.50 + len(expanding_pages.topping_simply_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1, padx= (3,0))


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

    # This tell the code that If any Simply Cheese have been delete if so then it will first will that gap.
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
# AM stand for American Pepperoni
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

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_american_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM1 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM1, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
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

    # Here is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_american_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM2 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM2, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
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

    # Here is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_american_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM3 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM3, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
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

    # Here is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_american_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM4 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM4, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
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

    # Here is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_american_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)
    if len(expanding_pages.topping_american_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_american_pepperoni_list[0])
        expanding_pages.topping_american_pepperoni_list.pop(0)

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
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM5 in expanding_pages.topping_american_pepperoni_list:
            Label(show_topping_name_frame, text = topping_AM5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AM5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AM5, text = f"${8.50 + len(expanding_pages.topping_american_pepperoni_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
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
    # This part add a number overall_AM_counter when the AMerican Pepperoni add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("American Pepperoni")

    # This parts checks any American Pepperoni have been delete if so then it will fill that gap
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







# AM means the American pepperion and all the adding for Cheesy Gralic
# This all for Cheesy Gralic pizza
# This is Cheesy Gralic counter so everytime the button is clicked on Cheesy Gralic it updates
# CG Stands for Cheesy Gralic
global overall_CG_counter
overall_CG_counter = 1


global CG_in_or_out_1, CG_in_or_out_2, CG_in_or_out_3, CG_in_or_out_4, CG_in_or_out_5
# 0 means a Cheesy Gralic pizza is not in the order list whereas one measn the pizza is in the list
CG_in_or_out_1 = 0
CG_in_or_out_2 = 0
CG_in_or_out_3 = 0
CG_in_or_out_4 = 0
CG_in_or_out_5 = 0



# This where everything get remove for Cheesy Gralic
def removing_cheesy_gralic_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CG1, CG_in_or_out_1
    allowed_to_checkout()
    cheesy_gralic_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_CG1) * 0.50 + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Cheesy Gralic")
    show_topping_frame_CG1.destroy()
    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove for Cheesy Gralic
def removing_cheesy_gralic_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CG2, CG_in_or_out_2
    allowed_to_checkout()
    cheesy_gralic_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CG2 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Cheesy Gralic")
    show_topping_frame_CG2.destroy()
    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove for Cheesy Gralic
def removing_cheesy_gralic_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CG3, CG_in_or_out_3
    allowed_to_checkout()
    cheesy_gralic_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CG3) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Cheesy Gralic")
    show_topping_frame_CG3.destroy()
    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove for Cheesy Gralic
def removing_cheesy_gralic_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CG4, CG_in_or_out_4
    allowed_to_checkout()
    cheesy_gralic_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CG4 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Cheesy Gralic")
    show_topping_frame_CG4.destroy()
    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove for Cheesy Gralic
def removing_cheesy_gralic_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CG5, CG_in_or_out_5
    allowed_to_checkout()
    cheesy_gralic_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CG5) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Cheesy Gralic")
    show_topping_frame_CG5.destroy()
    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types of Cheesy Gralic get add iwht it toppings
def adding_cheesy_gralic_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global cheesy_gralic_1, total_cost_for_all_pizzas,show_topping_frame_CG1, length_CG1, CG_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_cheesy_gralic_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CG1 = len(expanding_pages.topping_cheesy_gralic_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    cheesy_gralic_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Cheesy Gralic Pizza Resized order list.png", "Cheesy Gralic\nPizza", f"{((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50):.2f}", removing_cheesy_gralic_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CG1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CG1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CG1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CG1, text = "Cheesy Gralic Pizza", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CG1, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CG1 in expanding_pages.topping_cheesy_gralic_list:
            Label(show_topping_name_frame, text = topping_CG1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CG1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CG1, text = f"${8.50 + len(expanding_pages.topping_cheesy_gralic_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CG(e):
        show_topping_frame_CG1.place(x = 440, y= 40)
    def hide_topping_CG(e):
        show_topping_frame_CG1.place_forget()

    cheesy_gralic_1.order_pizza_frame.bind('<Enter>', show_topping_CG)
    cheesy_gralic_1.order_pizza_frame.bind("<Leave>", hide_topping_CG)

    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_1 = 1



# This where all types of Cheesy Gralic get add iwht it toppings
def adding_cheesy_gralic_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global cheesy_gralic_2, total_cost_for_all_pizzas, show_topping_frame_CG2, length_CG2, CG_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_cheesy_gralic_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CG2 = len(expanding_pages.topping_cheesy_gralic_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    cheesy_gralic_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Cheesy Gralic Pizza Resized order list.png", "Cheesy Gralic\nPizza", f"{((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50):.2f}", removing_cheesy_gralic_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CG2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CG2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CG2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CG2, text = "Cheesy Gralic Pizza", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CG2, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CG2 in expanding_pages.topping_cheesy_gralic_list:
            Label(show_topping_name_frame, text = topping_CG2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CG2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CG2, text = f"${8.50 + len(expanding_pages.topping_cheesy_gralic_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CG(e):
        show_topping_frame_CG2.place(x = 440, y= 40)
    def hide_topping_CG(e):
        show_topping_frame_CG2.place_forget()

    cheesy_gralic_2.order_pizza_frame.bind('<Enter>', show_topping_CG)
    cheesy_gralic_2.order_pizza_frame.bind("<Leave>", hide_topping_CG)

    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_2 = 1




# This where all types of Cheesy Gralic get add iwht it toppings
def adding_cheesy_gralic_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global cheesy_gralic_3, total_cost_for_all_pizzas, show_topping_frame_CG3, length_CG3, CG_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_cheesy_gralic_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CG3 = len(expanding_pages.topping_cheesy_gralic_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    cheesy_gralic_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Cheesy Gralic Pizza Resized order list.png", "Cheesy Gralic\nPizza", f"{((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50):.2f}", removing_cheesy_gralic_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CG3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CG3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CG3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CG3, text = "Cheesy Gralic Pizza", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CG3, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CG3 in expanding_pages.topping_cheesy_gralic_list:
            Label(show_topping_name_frame, text = topping_CG3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CG3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CG3, text = f"${8.50 + len(expanding_pages.topping_cheesy_gralic_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CG(e):
        show_topping_frame_CG3.place(x = 440, y= 40)
    def hide_topping_CG(e):
        show_topping_frame_CG3.place_forget()

    cheesy_gralic_3.order_pizza_frame.bind('<Enter>', show_topping_CG)
    cheesy_gralic_3.order_pizza_frame.bind("<Leave>", hide_topping_CG)

    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_3 = 1



# This where all types of Cheesy Gralic get add iwht it toppings
def adding_cheesy_gralic_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global cheesy_gralic_4, total_cost_for_all_pizzas, show_topping_frame_CG4, length_CG4, CG_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_cheesy_gralic_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CG4 = len(expanding_pages.topping_cheesy_gralic_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    cheesy_gralic_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Cheesy Gralic Pizza Resized order list.png", "Cheesy Gralic\nPizza", f"{((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50):.2f}", removing_cheesy_gralic_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CG4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CG4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CG4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CG4, text = "Cheesy Gralic Pizza", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CG4, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM4 in expanding_pages.topping_cheesy_gralic_list:
            Label(show_topping_name_frame, text = topping_AM4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CG4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CG4, text = f"${8.50 + len(expanding_pages.topping_cheesy_gralic_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_CG(e):
        show_topping_frame_CG4.place(x = 440, y= 40)
    def hide_topping_CG(e):
        show_topping_frame_CG4.place_forget()

    cheesy_gralic_4.order_pizza_frame.bind('<Enter>', show_topping_CG)
    cheesy_gralic_4.order_pizza_frame.bind("<Leave>", hide_topping_CG)

    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_4 = 1


# This where all types of Cheesy Gralic get add iwht it toppings
def adding_cheesy_gralic_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global cheesy_gralic_5, total_cost_for_all_pizzas, show_topping_frame_CG5, length_CG5, CG_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_cheesy_gralic_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)
    if len(expanding_pages.topping_cheesy_gralic_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_cheesy_gralic_list[0])
        expanding_pages.topping_cheesy_gralic_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CG5 = len(expanding_pages.topping_cheesy_gralic_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    cheesy_gralic_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Cheesy Gralic Pizza Resized order list.png", "Cheesy Gralic\nPizza", f"{((len(expanding_pages.topping_cheesy_gralic_list) * 0.50) + 8.50):.2f}", removing_cheesy_gralic_5)


    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CG5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CG5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CG5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CG5, text = "Cheesy Gralic Pizza", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CG5, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CG5 in expanding_pages.topping_cheesy_gralic_list:
            Label(show_topping_name_frame, text = topping_CG5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CG5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CG5, text = f"${8.50 + len(expanding_pages.topping_cheesy_gralic_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CG(e):
        show_topping_frame_CG5.place(x = 440, y= 40)
    def hide_topping_CG(e):
        show_topping_frame_CG5.place_forget()

    cheesy_gralic_5.order_pizza_frame.bind('<Enter>', show_topping_CG)
    cheesy_gralic_5.order_pizza_frame.bind("<Leave>", hide_topping_CG)

    # updating the in and out Cheesy Gralic pizza
    CG_in_or_out_5 = 1



# This take of the Cheesy Gralic adding in the order list
def cheesy_gralic_add_order():
    global overall_CG_counter, CG_in_or_out_1, CG_in_or_out_2, CG_in_or_out_3, CG_in_or_out_4, CG_in_or_out_5

    # Telling the the counter that Cheesy Gralic has been added or display a number
    # This part add a number overall_CG_counter when the Cheesy Gralic add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Cheesy Gralic")

    # This parts chekc any Cheesy gralic have been delete if so then it will fill that gap
    if CG_in_or_out_1 == 2:
        CG_in_or_out_1 = 0
        overall_CG_counter = 1

    elif CG_in_or_out_2 == 2:
        CG_in_or_out_2 = 0
        overall_CG_counter = 2

    elif CG_in_or_out_3 == 2:
        CG_in_or_out_3 = 0
        overall_CG_counter = 3

    elif CG_in_or_out_4 == 2:
        CG_in_or_out_4 = 0
        overall_CG_counter = 4

    elif CG_in_or_out_5 == 2:
        CG_in_or_out_5 = 0
        overall_CG_counter = 5



    if overall_CG_counter == 1:
        if CG_in_or_out_1 == 0:
            adding_cheesy_gralic_1()



    elif overall_CG_counter == 2:
        if CG_in_or_out_2 == 0:
            adding_cheesy_gralic_2()


    elif overall_CG_counter == 3:
        if CG_in_or_out_3 == 0:
            adding_cheesy_gralic_3()


    elif overall_CG_counter== 4:
        if CG_in_or_out_4 == 0:
            adding_cheesy_gralic_4()


    elif overall_CG_counter == 5:
        overall_CG_counter = 0
        if CG_in_or_out_5 == 0:
            adding_cheesy_gralic_5()



    # This the counter for all five Cheesy Gralic pizza
    overall_CG_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_toppings_cheesy_gralic()
    Warning_message_box.add()




# CS means the Chicken Supreme and all the adding for Chicken Supreme
# This all for Chicken Supreme pizza
# This is Chicken Supreme counter so everytime the button is clicked on Chicken Supreme it updates
global overall_CS_counter
overall_CS_counter = 1


global CS_in_or_out_1, CS_in_or_out_2, CS_in_or_out_3, CS_in_or_out_4, CS_in_or_out_5
# 0 means a Chicken Supreme pizza is not in the order list whereas one measn the pizza is in the list
CS_in_or_out_1 = 0
CS_in_or_out_2 = 0
CS_in_or_out_3 = 0
CS_in_or_out_4 = 0
CS_in_or_out_5 = 0



# This where everything get remove for Chicken Supreme
def removing_chicken_supreme_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CS1, CS_in_or_out_1
    allowed_to_checkout()
    chicken_supreme_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_CS1) * 0.50 + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Supreme")
    show_topping_frame_CS1.destroy()
    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove for Chicken Supreme
def removing_chicken_supreme_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CS2, CS_in_or_out_2
    allowed_to_checkout()
    chicken_supreme_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CS2 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Supreme")
    show_topping_frame_CS2.destroy()
    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove for Chicken Supreme
def removing_chicken_supreme_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CS3, CS_in_or_out_3
    allowed_to_checkout()
    chicken_supreme_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CS3) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Supreme")
    show_topping_frame_CS3.destroy()
    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove for Chicken Supreme
def removing_chicken_supreme_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CS4, CS_in_or_out_4
    allowed_to_checkout()
    chicken_supreme_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CS4 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Supreme")
    show_topping_frame_CS4.destroy()
    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove for Chicken Supreme
def removing_chicken_supreme_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CS5, CS_in_or_out_5
    allowed_to_checkout()
    chicken_supreme_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CS5) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Supreme")
    show_topping_frame_CS5.destroy()
    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types of Chicken Supreme get add iwht it toppings
def adding_chicken_supreme_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_supreme_1, total_cost_for_all_pizzas,show_topping_frame_CS1, length_CS1, CS_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CS1 = len(expanding_pages.topping_chicken_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_supreme_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken Supreme Resized order list.png", "Chicken\nSupreme", f"{((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50):.2f}", removing_chicken_supreme_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CS1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CS1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CS1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CS1, text = "Chicken Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CS1, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)

    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CS1 in expanding_pages.topping_chicken_supreme_list:
            Label(show_topping_name_frame, text = topping_CS1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CS1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CS1, text = f"${8.50 + len(expanding_pages.topping_chicken_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CS(e):
        show_topping_frame_CS1.place(x = 440, y= 40)
    def hide_topping_CS(e):
        show_topping_frame_CS1.place_forget()

    chicken_supreme_1.order_pizza_frame.bind('<Enter>', show_topping_CS)
    chicken_supreme_1.order_pizza_frame.bind("<Leave>", hide_topping_CS)

    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_1 = 1



# This where all types of Chicken Supreme get add iwht it toppings
def adding_chicken_supreme_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_supreme_2, total_cost_for_all_pizzas, show_topping_frame_CS2, length_CS2, CS_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CS2 = len(expanding_pages.topping_chicken_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_supreme_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken Supreme Resized order list.png", "Chicken\nSupreme", f"{((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50):.2f}", removing_chicken_supreme_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CS2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CS2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CS2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CS2, text = "Chicken Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CS2, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CS2 in expanding_pages.topping_chicken_supreme_list:
            Label(show_topping_name_frame, text = topping_CS2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CS2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CS2, text = f"${8.50 + len(expanding_pages.topping_chicken_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CS(e):
        show_topping_frame_CS2.place(x = 440, y= 40)
    def hide_topping_CS(e):
        show_topping_frame_CS2.place_forget()

    chicken_supreme_2.order_pizza_frame.bind('<Enter>', show_topping_CS)
    chicken_supreme_2.order_pizza_frame.bind("<Leave>", hide_topping_CS)

    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_2 = 1




# This where all types of Chicken Supreme get add iwht it toppings
def adding_chicken_supreme_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_supreme_3, total_cost_for_all_pizzas, show_topping_frame_CS3, length_CS3, CS_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CS3 = len(expanding_pages.topping_chicken_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_supreme_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken Supreme Resized order list.png", "Chicken\nSupreme", f"{((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50):.2f}", removing_chicken_supreme_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CS3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CS3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CS3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CS3, text = "Chicken Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CS3, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CS3 in expanding_pages.topping_chicken_supreme_list:
            Label(show_topping_name_frame, text = topping_CS3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CS3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CS3, text = f"${8.50 + len(expanding_pages.topping_chicken_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CS(e):
        show_topping_frame_CS3.place(x = 440, y= 40)
    def hide_topping_CS(e):
        show_topping_frame_CS3.place_forget()

    chicken_supreme_3.order_pizza_frame.bind('<Enter>', show_topping_CS)
    chicken_supreme_3.order_pizza_frame.bind("<Leave>", hide_topping_CS)

    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_3 = 1



# This where all types of Chicken Supreme get add iwht it toppings
def adding_chicken_supreme_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_supreme_4, total_cost_for_all_pizzas, show_topping_frame_CS4, length_CS4, CS_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CS4 = len(expanding_pages.topping_chicken_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_supreme_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken Supreme Resized order list.png", "Chicken\nSupreme", f"{((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50):.2f}", removing_chicken_supreme_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CS4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CS4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CS4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CS4, text = "Chicken Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CS4, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM4 in expanding_pages.topping_chicken_supreme_list:
            Label(show_topping_name_frame, text = topping_AM4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CS4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CS4, text = f"${8.50 + len(expanding_pages.topping_chicken_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_CS(e):
        show_topping_frame_CS4.place(x = 440, y= 40)
    def hide_topping_CS(e):
        show_topping_frame_CS4.place_forget()

    chicken_supreme_4.order_pizza_frame.bind('<Enter>', show_topping_CS)
    chicken_supreme_4.order_pizza_frame.bind("<Leave>", hide_topping_CS)

    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_4 = 1


# This where all types of Chicken Supreme get add iwht it toppings
def adding_chicken_supreme_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_supreme_5, total_cost_for_all_pizzas, show_topping_frame_CS5, length_CS5, CS_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)
    if len(expanding_pages.topping_chicken_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_supreme_list[0])
        expanding_pages.topping_chicken_supreme_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CS5 = len(expanding_pages.topping_chicken_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_supreme_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken Supreme Resized order list.png", "Chicken\nSupreme", f"{((len(expanding_pages.topping_chicken_supreme_list) * 0.50) + 8.50):.2f}", removing_chicken_supreme_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CS5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CS5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CS5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CS5, text = "Chicken Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CS5, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)

    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CS5 in expanding_pages.topping_chicken_supreme_list:
            Label(show_topping_name_frame, text = topping_CS5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CS5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CS5, text = f"${8.50 + len(expanding_pages.topping_chicken_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CS(e):
        show_topping_frame_CS5.place(x = 440, y= 40)
    def hide_topping_CS(e):
        show_topping_frame_CS5.place_forget()

    chicken_supreme_5.order_pizza_frame.bind('<Enter>', show_topping_CS)
    chicken_supreme_5.order_pizza_frame.bind("<Leave>", hide_topping_CS)

    # updating the in and out Chicken Supreme pizza
    CS_in_or_out_5 = 1



# This take of the Chicken Supreme adding in the order list
def chicken_supreme_add_order():
    global overall_CS_counter, CS_in_or_out_1, CS_in_or_out_2, CS_in_or_out_3, CS_in_or_out_4, CS_in_or_out_5

    # Telling the the counter that Chicken Supreme has been added or display a number
    # This part add a number overall_CS_counter when the Chicken Supreme add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Chicken Supreme")

    if CS_in_or_out_1 == 2:
        CS_in_or_out_1 = 0
        overall_CS_counter = 1

    elif CS_in_or_out_2 == 2:
        CS_in_or_out_2 = 0
        overall_CS_counter = 2

    elif CS_in_or_out_3 == 2:
        CS_in_or_out_3 = 0
        overall_CS_counter = 3

    elif CS_in_or_out_4 == 2:
        CS_in_or_out_4 = 0
        overall_CS_counter = 4

    elif CS_in_or_out_5 == 2:
        CS_in_or_out_5 = 0
        overall_CS_counter = 5



    if overall_CS_counter == 1:
        if CS_in_or_out_1 == 0:
            adding_chicken_supreme_1()



    elif overall_CS_counter == 2:
        if CS_in_or_out_2 == 0:
            adding_chicken_supreme_2()


    elif overall_CS_counter == 3:
        if CS_in_or_out_3 == 0:
            adding_chicken_supreme_3()


    elif overall_CS_counter== 4:
        if CS_in_or_out_4 == 0:
            adding_chicken_supreme_4()


    elif overall_CS_counter == 5:
        overall_CS_counter = 0
        if CS_in_or_out_5 == 0:
            adding_chicken_supreme_5()



    # This the counter for all five Chicken Supreme pizza
    overall_CS_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_toppings_chicken_supreme()
    Warning_message_box.add()





# HC means the Ham and Cheese and all the adding for Ham and Cheese
# This all for Ham and Cheese pizza
# This is Ham and Cheese counter so everytime the button is clicked on Ham and Cheese it updates
global overall_HC_counter
overall_HC_counter = 1


global HC_in_or_out_1, HC_in_or_out_2, HC_in_or_out_3, HC_in_or_out_4, HC_in_or_out_5
# 0 means a Ham and Cheese pizza is not in the order list whereas one measn the pizza is in the list
HC_in_or_out_1 = 0
HC_in_or_out_2 = 0
HC_in_or_out_3 = 0
HC_in_or_out_4 = 0
HC_in_or_out_5 = 0



# This where everything get remove for Ham and Cheese
def removing_ham_and_cheese_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_HC1, HC_in_or_out_1
    allowed_to_checkout()
    ham_and_cheese_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_HC1) * 0.50 + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Ham and Cheese")
    show_topping_frame_HC1.destroy()
    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove for Ham and Cheese
def removing_ham_and_cheese_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_HC2, HC_in_or_out_2
    allowed_to_checkout()
    ham_and_cheese_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_HC2 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Ham and Cheese")
    show_topping_frame_HC2.destroy()
    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove for Ham and Cheese
def removing_ham_and_cheese_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_HC3, HC_in_or_out_3
    allowed_to_checkout()
    ham_and_cheese_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_HC3) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Ham and Cheese")
    show_topping_frame_HC3.destroy()
    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove for Ham and Cheese
def removing_ham_and_cheese_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_HC4, HC_in_or_out_4
    allowed_to_checkout()
    ham_and_cheese_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_HC4 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Ham and Cheese")
    show_topping_frame_HC4.destroy()
    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove for Ham and Cheese
def removing_ham_and_cheese_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_HC5, HC_in_or_out_5
    allowed_to_checkout()
    ham_and_cheese_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_HC5) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Ham and Cheese")
    show_topping_frame_HC5.destroy()
    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types of Ham and Cheese get add iwht it toppings
def adding_ham_and_cheese_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global ham_and_cheese_1, total_cost_for_all_pizzas,show_topping_frame_HC1, length_HC1, HC_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_ham_and_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_HC1 = len(expanding_pages.topping_ham_and_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    ham_and_cheese_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Ham and Cheese Resized order list.png", "Ham and\nCheese", f"{((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50):.2f}", removing_ham_and_cheese_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_HC1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_HC1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_HC1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_HC1, text = "Ham and Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_HC1, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_HC1 in expanding_pages.topping_ham_and_cheese_list:
            Label(show_topping_name_frame, text = topping_HC1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_HC1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_HC1, text = f"${8.50 + len(expanding_pages.topping_ham_and_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_HC(e):
        show_topping_frame_HC1.place(x = 440, y= 40)
    def hide_topping_HC(e):
        show_topping_frame_HC1.place_forget()

    ham_and_cheese_1.order_pizza_frame.bind('<Enter>', show_topping_HC)
    ham_and_cheese_1.order_pizza_frame.bind("<Leave>", hide_topping_HC)

    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_1 = 1



# This where all types of Ham and Cheese get add iwht it toppings
def adding_ham_and_cheese_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global ham_and_cheese_2, total_cost_for_all_pizzas, show_topping_frame_HC2, length_HC2, HC_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_ham_and_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_HC2 = len(expanding_pages.topping_ham_and_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    ham_and_cheese_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Ham and Cheese Resized order list.png", "Ham and\nCheese", f"{((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50):.2f}", removing_ham_and_cheese_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_HC2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_HC2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_HC2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_HC2, text = "Ham and Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_HC2, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_HC2 in expanding_pages.topping_ham_and_cheese_list:
            Label(show_topping_name_frame, text = topping_HC2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_HC2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_HC2, text = f"${8.50 + len(expanding_pages.topping_ham_and_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_HC(e):
        show_topping_frame_HC2.place(x = 440, y= 40)
    def hide_topping_HC(e):
        show_topping_frame_HC2.place_forget()

    ham_and_cheese_2.order_pizza_frame.bind('<Enter>', show_topping_HC)
    ham_and_cheese_2.order_pizza_frame.bind("<Leave>", hide_topping_HC)

    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_2 = 1




# This where all types of Ham and Cheese get add iwht it toppings
def adding_ham_and_cheese_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global ham_and_cheese_3, total_cost_for_all_pizzas, show_topping_frame_HC3, length_HC3, HC_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_ham_and_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_HC3 = len(expanding_pages.topping_ham_and_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    ham_and_cheese_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Ham and Cheese Resized order list.png", "Ham and\nCheese", f"{((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50):.2f}", removing_ham_and_cheese_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_HC3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_HC3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_HC3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_HC3, text = "Ham and Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_HC3, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_HC3 in expanding_pages.topping_ham_and_cheese_list:
            Label(show_topping_name_frame, text = topping_HC3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_HC3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_HC3, text = f"${8.50 + len(expanding_pages.topping_ham_and_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_HC(e):
        show_topping_frame_HC3.place(x = 440, y= 40)
    def hide_topping_HC(e):
        show_topping_frame_HC3.place_forget()

    ham_and_cheese_3.order_pizza_frame.bind('<Enter>', show_topping_HC)
    ham_and_cheese_3.order_pizza_frame.bind("<Leave>", hide_topping_HC)

    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_3 = 1



# This where all types of Ham and Cheese get add iwht it toppings
def adding_ham_and_cheese_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global ham_and_cheese_4, total_cost_for_all_pizzas, show_topping_frame_HC4, length_HC4, HC_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_ham_and_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_HC4 = len(expanding_pages.topping_ham_and_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    ham_and_cheese_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Ham and Cheese Resized order list.png", "Ham and\nCheese", f"{((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50):.2f}", removing_ham_and_cheese_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_HC4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_HC4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_HC4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_HC4, text = "Ham and Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_HC4, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM4 in expanding_pages.topping_ham_and_cheese_list:
            Label(show_topping_name_frame, text = topping_AM4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_HC4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_HC4, text = f"${8.50 + len(expanding_pages.topping_ham_and_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_HC(e):
        show_topping_frame_HC4.place(x = 440, y= 40)
    def hide_topping_HC(e):
        show_topping_frame_HC4.place_forget()

    ham_and_cheese_4.order_pizza_frame.bind('<Enter>', show_topping_HC)
    ham_and_cheese_4.order_pizza_frame.bind("<Leave>", hide_topping_HC)

    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_4 = 1


# This where all types of Ham and Cheese get add iwht it toppings
def adding_ham_and_cheese_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global ham_and_cheese_5, total_cost_for_all_pizzas, show_topping_frame_HC5, length_HC5, HC_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_ham_and_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)
    if len(expanding_pages.topping_ham_and_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_ham_and_cheese_list[0])
        expanding_pages.topping_ham_and_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_HC5 = len(expanding_pages.topping_ham_and_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    ham_and_cheese_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Ham and Cheese Resized order list.png", "Ham and\nCheese", f"{((len(expanding_pages.topping_ham_and_cheese_list) * 0.50) + 8.50):.2f}", removing_ham_and_cheese_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_HC5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_HC5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_HC5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_HC5, text = "Ham and Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_HC5, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_HC5 in expanding_pages.topping_ham_and_cheese_list:
            Label(show_topping_name_frame, text = topping_HC5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_HC5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_HC5, text = f"${8.50 + len(expanding_pages.topping_ham_and_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_HC(e):
        show_topping_frame_HC5.place(x = 440, y= 40)
    def hide_topping_HC(e):
        show_topping_frame_HC5.place_forget()

    ham_and_cheese_5.order_pizza_frame.bind('<Enter>', show_topping_HC)
    ham_and_cheese_5.order_pizza_frame.bind("<Leave>", hide_topping_HC)

    # updating the in and out Ham and Cheese pizza
    HC_in_or_out_5 = 1



# This take of the Ham and Cheese adding in the order list
def ham_and_cheese_add_order():
    global overall_HC_counter, HC_in_or_out_1, HC_in_or_out_2, HC_in_or_out_3, HC_in_or_out_4, HC_in_or_out_5

    # Telling the the counter that Ham and Cheese has been added or display a number
    # This part add a number overall_HC_counter when the Ham and Cheese add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Ham and Cheese")

    if HC_in_or_out_1 == 2:
        HC_in_or_out_1 = 0
        overall_HC_counter = 1

    elif HC_in_or_out_2 == 2:
        HC_in_or_out_2 = 0
        overall_HC_counter = 2

    elif HC_in_or_out_3 == 2:
        HC_in_or_out_3 = 0
        overall_HC_counter = 3

    elif HC_in_or_out_4 == 2:
        HC_in_or_out_4 = 0
        overall_HC_counter = 4

    elif HC_in_or_out_5 == 2:
        HC_in_or_out_5 = 0
        overall_HC_counter = 5



    if overall_HC_counter == 1:
        if HC_in_or_out_1 == 0:
            adding_ham_and_cheese_1()



    elif overall_HC_counter == 2:
        if HC_in_or_out_2 == 0:
            adding_ham_and_cheese_2()


    elif overall_HC_counter == 3:
        if HC_in_or_out_3 == 0:
            adding_ham_and_cheese_3()


    elif overall_HC_counter== 4:
        if HC_in_or_out_4 == 0:
            adding_ham_and_cheese_4()


    elif overall_HC_counter == 5:
        overall_HC_counter = 0
        if HC_in_or_out_5 == 0:
            adding_ham_and_cheese_5()



    # This the counter for all five Ham and Cheese pizza
    overall_HC_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_toppings_ham_and_cheese()
    Warning_message_box.add()





# MW means the Mr Wedge and all the adding foe Mr Wedge
# This all for Mr Wedge pizza
# This ie Mr Wedge counter so everytime the button is clicked oe Mr Wedge it updates
global overall_MW_counter
overall_MW_counter = 1


global MW_in_or_out_1, MW_in_or_out_2, MW_in_or_out_3, MW_in_or_out_4, MW_in_or_out_5
# 0 means a Mr Wedge pizza is not in the order list whereas one measn the pizza is in the list
MW_in_or_out_1 = 0
MW_in_or_out_2 = 0
MW_in_or_out_3 = 0
MW_in_or_out_4 = 0
MW_in_or_out_5 = 0



# This where everything get remove foe Mr Wedge
def removing_mr_wedge_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_MW1, MW_in_or_out_1
    allowed_to_checkout()
    mr_wedge_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_MW1) * 0.50 + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mr Wedge")
    show_topping_frame_MW1.destroy()
    # updating the in and out Mr Wedge pizza
    MW_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove foe Mr Wedge
def removing_mr_wedge_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_MW2, MW_in_or_out_2
    allowed_to_checkout()
    mr_wedge_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_MW2 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mr Wedge")
    show_topping_frame_MW2.destroy()
    # updating the in and out Mr Wedge pizza
    MW_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove foe Mr Wedge
def removing_mr_wedge_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_MW3, MW_in_or_out_3
    allowed_to_checkout()
    mr_wedge_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_MW3) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mr Wedge")
    show_topping_frame_MW3.destroy()
    # updating the in and out Mr Wedge pizza
    MW_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove foe Mr Wedge
def removing_mr_wedge_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_MW4, MW_in_or_out_4
    allowed_to_checkout()
    mr_wedge_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_MW4 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mr Wedge")
    show_topping_frame_MW4.destroy()
    # updating the in and out Mr Wedge pizza
    MW_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove foe Mr Wedge
def removing_mr_wedge_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_MW5, MW_in_or_out_5
    allowed_to_checkout()
    mr_wedge_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_MW5) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mr Wedge")
    show_topping_frame_MW5.destroy()
    # updating the in and out Mr Wedge pizza
    MW_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types oe Mr Wedge get add iwht it toppings
def adding_mr_wedge_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global mr_wedge_1, total_cost_for_all_pizzas,show_topping_frame_MW1, length_MW1, MW_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mr_wedge_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MW1 = len(expanding_pages.topping_mr_wedge_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mr_wedge_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mr Wedge Resized order list.png", "MR Wedge\n", f"{((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50):.2f}", removing_mr_wedge_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MW1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MW1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MW1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MW1, text = "Mr Wedge", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MW1, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_MW1 in expanding_pages.topping_mr_wedge_list:
            Label(show_topping_name_frame, text = topping_MW1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MW1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MW1, text = f"${8.50 + len(expanding_pages.topping_mr_wedge_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_MW(e):
        show_topping_frame_MW1.place(x = 440, y= 40)
    def hide_topping_MW(e):
        show_topping_frame_MW1.place_forget()

    mr_wedge_1.order_pizza_frame.bind('<Enter>', show_topping_MW)
    mr_wedge_1.order_pizza_frame.bind("<Leave>", hide_topping_MW)

    # updating the in and out Mr Wedge pizza
    MW_in_or_out_1 = 1



# This where all types oe Mr Wedge get add iwht it toppings
def adding_mr_wedge_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global mr_wedge_2, total_cost_for_all_pizzas, show_topping_frame_MW2, length_MW2, MW_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mr_wedge_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MW2 = len(expanding_pages.topping_mr_wedge_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mr_wedge_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mr Wedge Resized order list.png", "MR Wedge\n", f"{((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50):.2f}", removing_mr_wedge_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MW2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MW2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MW2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MW2, text = "Mr Wedge", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MW2, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_MW2 in expanding_pages.topping_mr_wedge_list:
            Label(show_topping_name_frame, text = topping_MW2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MW2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MW2, text = f"${8.50 + len(expanding_pages.topping_mr_wedge_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_MW(e):
        show_topping_frame_MW2.place(x = 440, y= 40)
    def hide_topping_MW(e):
        show_topping_frame_MW2.place_forget()

    mr_wedge_2.order_pizza_frame.bind('<Enter>', show_topping_MW)
    mr_wedge_2.order_pizza_frame.bind("<Leave>", hide_topping_MW)

    # updating the in and out Mr Wedge pizza
    MW_in_or_out_2 = 1




# This where all types oe Mr Wedge get add iwht it toppings
def adding_mr_wedge_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global mr_wedge_3, total_cost_for_all_pizzas, show_topping_frame_MW3, length_MW3, MW_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mr_wedge_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MW3 = len(expanding_pages.topping_mr_wedge_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mr_wedge_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mr Wedge Resized order list.png", "MR Wedge\n", f"{((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50):.2f}", removing_mr_wedge_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MW3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MW3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MW3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MW3, text = "Mr Wedge", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MW3, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_MW3 in expanding_pages.topping_mr_wedge_list:
            Label(show_topping_name_frame, text = topping_MW3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MW3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MW3, text = f"${8.50 + len(expanding_pages.topping_mr_wedge_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_MW(e):
        show_topping_frame_MW3.place(x = 440, y= 40)
    def hide_topping_MW(e):
        show_topping_frame_MW3.place_forget()

    mr_wedge_3.order_pizza_frame.bind('<Enter>', show_topping_MW)
    mr_wedge_3.order_pizza_frame.bind("<Leave>", hide_topping_MW)

    # updating the in and out Mr Wedge pizza
    MW_in_or_out_3 = 1



# This where all types oe Mr Wedge get add iwht it toppings
def adding_mr_wedge_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global mr_wedge_4, total_cost_for_all_pizzas, show_topping_frame_MW4, length_MW4, MW_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mr_wedge_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MW4 = len(expanding_pages.topping_mr_wedge_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mr_wedge_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mr Wedge Resized order list.png", "MR Wedge\n", f"{((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50):.2f}", removing_mr_wedge_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MW4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MW4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MW4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MW4, text = "Mr Wedge", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MW4, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM4 in expanding_pages.topping_mr_wedge_list:
            Label(show_topping_name_frame, text = topping_AM4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MW4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MW4, text = f"${8.50 + len(expanding_pages.topping_mr_wedge_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_MW(e):
        show_topping_frame_MW4.place(x = 440, y= 40)
    def hide_topping_MW(e):
        show_topping_frame_MW4.place_forget()

    mr_wedge_4.order_pizza_frame.bind('<Enter>', show_topping_MW)
    mr_wedge_4.order_pizza_frame.bind("<Leave>", hide_topping_MW)

    # updating the in and out Mr Wedge pizza
    MW_in_or_out_4 = 1


# This where all types oe Mr Wedge get add iwht it toppings
def adding_mr_wedge_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global mr_wedge_5, total_cost_for_all_pizzas, show_topping_frame_MW5, length_MW5, MW_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mr_wedge_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)
    if len(expanding_pages.topping_mr_wedge_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mr_wedge_list[0])
        expanding_pages.topping_mr_wedge_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MW5 = len(expanding_pages.topping_mr_wedge_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mr_wedge_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mr Wedge Resized order list.png", "MR Wedge\n", f"{((len(expanding_pages.topping_mr_wedge_list) * 0.50) + 8.50):.2f}", removing_mr_wedge_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MW5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MW5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MW5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MW5, text = "Mr Wedge", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MW5, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_MW5 in expanding_pages.topping_mr_wedge_list:
            Label(show_topping_name_frame, text = topping_MW5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MW5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MW5, text = f"${8.50 + len(expanding_pages.topping_mr_wedge_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_MW(e):
        show_topping_frame_MW5.place(x = 440, y= 40)
    def hide_topping_MW(e):
        show_topping_frame_MW5.place_forget()

    mr_wedge_5.order_pizza_frame.bind('<Enter>', show_topping_MW)
    mr_wedge_5.order_pizza_frame.bind("<Leave>", hide_topping_MW)

    # updating the in and out Mr Wedge pizza
    MW_in_or_out_5 = 1



# This take of the Mr Wedge adding in the order list
def mr_wedge_add_order():
    global overall_MW_counter, MW_in_or_out_1, MW_in_or_out_2, MW_in_or_out_3, MW_in_or_out_4, MW_in_or_out_5

    # Telling the the counter thae Mr Wedge has been added or display a number
    # This part add a number overall_MW_counter when the Mr Wedge add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Mr Wedge")

    if MW_in_or_out_1 == 2:
        MW_in_or_out_1 = 0
        overall_MW_counter = 1

    elif MW_in_or_out_2 == 2:
        MW_in_or_out_2 = 0
        overall_MW_counter = 2

    elif MW_in_or_out_3 == 2:
        MW_in_or_out_3 = 0
        overall_MW_counter = 3

    elif MW_in_or_out_4 == 2:
        MW_in_or_out_4 = 0
        overall_MW_counter = 4

    elif MW_in_or_out_5 == 2:
        MW_in_or_out_5 = 0
        overall_MW_counter = 5



    if overall_MW_counter == 1:
        if MW_in_or_out_1 == 0:
            adding_mr_wedge_1()



    elif overall_MW_counter == 2:
        if MW_in_or_out_2 == 0:
            adding_mr_wedge_2()


    elif overall_MW_counter == 3:
        if MW_in_or_out_3 == 0:
            adding_mr_wedge_3()


    elif overall_MW_counter== 4:
        if MW_in_or_out_4 == 0:
            adding_mr_wedge_4()


    elif overall_MW_counter == 5:
        overall_MW_counter = 0
        if MW_in_or_out_5 == 0:
            adding_mr_wedge_5()



    # This the counter for all five Mr Wedge pizza
    overall_MW_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_topping_mr_wedge()
    Warning_message_box.add()

# Pe means the Pepperoni and all the adding foe Pepperoni
# This all for Pepperoni pizza
# This ie Pepperoni counter so everytime the button is clicked oe Pepperoni it updates
global overall_Pe_counter
overall_Pe_counter = 1

global Pe_in_or_out_1, Pe_in_or_out_2, Pe_in_or_out_3, Pe_in_or_out_4, Pe_in_or_out_5
# 0 means a Pepperoni pizza is not in the order list whereas one measn the pizza is in the list
Pe_in_or_out_1 = 0
Pe_in_or_out_2 = 0
Pe_in_or_out_3 = 0
Pe_in_or_out_4 = 0
Pe_in_or_out_5 = 0

# This where everything get remove foe Pepperoni
def removing_pepperoni_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Pe1, Pe_in_or_out_1
    allowed_to_checkout()
    pepperoni_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_Pe1) * 0.50 + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Pepperoni")
    show_topping_frame_Pe1.destroy()
    # updating the in and out Pepperoni pizza
    Pe_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove foe Pepperoni
def removing_pepperoni_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Pe2, Pe_in_or_out_2
    allowed_to_checkout()
    pepperoni_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_Pe2 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Pepperoni")
    show_topping_frame_Pe2.destroy()
    # updating the in and out Pepperoni pizza
    Pe_in_or_out_2 = 2
    Warning_message_box.add()

# This where everything get remove foe Pepperoni
def removing_pepperoni_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Pe3, Pe_in_or_out_3
    allowed_to_checkout()
    pepperoni_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_Pe3) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Pepperoni")
    show_topping_frame_Pe3.destroy()
    # updating the in and out Pepperoni pizza
    Pe_in_or_out_3 = 2
    Warning_message_box.add()

# This where everything get remove foe Pepperoni
def removing_pepperoni_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Pe4, Pe_in_or_out_4
    allowed_to_checkout()
    pepperoni_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_Pe4 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Pepperoni")
    show_topping_frame_Pe4.destroy()
    # updating the in and out Pepperoni pizza
    Pe_in_or_out_4 = 2
    Warning_message_box.add()

# This where everything get remove foe Pepperoni
def removing_pepperoni_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Pe5, Pe_in_or_out_5
    allowed_to_checkout()
    pepperoni_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_Pe5) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Pepperoni")
    show_topping_frame_Pe5.destroy()
    # updating the in and out Pepperoni pizza
    Pe_in_or_out_5 = 2
    Warning_message_box.add()

# This where all types oe Pepperoni get add iwht it toppings
def adding_pepperoni_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global pepperoni_1, total_cost_for_all_pizzas, show_topping_frame_Pe1, length_Pe1, Pe_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Pe1 = len(expanding_pages.topping_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    pepperoni_1 = Order_pizza_list(
        r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Pepperion Resized order list.png",
        "Pepperoni\n", f"{((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50):.2f}", removing_pepperoni_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Pe1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white',
                                                    bg_color='#F2F2F2', corner_radius=20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Pe1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Pe1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10, 5))
    pizza_name_display = Label(show_topping_frame_Pe1, text="Pepperoni", background='white',
                               font=("Bahnschrift SemiBold", 12), border=0, pady=5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Pe1, text="$8.50",
                                                 text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30,
                                                 fg_color='white', text_color='black')
    pizza_price_display.grid(row=0, column=1, padx=(10, 5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text=no_charge_topping, background='white',
                  font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column=0,
                                                                                        sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_Pe1 in expanding_pages.topping_pepperoni_list:
            Label(show_topping_name_frame, text=topping_Pe1, background='white', font=("Bahnschrift SemiLight", 8),
                  border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Pe1, text="Total Price:",
                                                         fg_color='white', text_font=("Bahnschrift SemiBold", 12),
                                                         corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx=(14, 10), pady=(5, 0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Pe1,
                                   text=f"${8.50 + len(expanding_pages.topping_pepperoni_list) * 0.50:.2f}",
                                   background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10,
                                   foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5, 0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_Pe(e):
        show_topping_frame_Pe1.place(x=440, y=40)

    def hide_topping_Pe(e):
        show_topping_frame_Pe1.place_forget()

    pepperoni_1.order_pizza_frame.bind('<Enter>', show_topping_Pe)
    pepperoni_1.order_pizza_frame.bind("<Leave>", hide_topping_Pe)

    # updating the in and out Pepperoni pizza
    Pe_in_or_out_1 = 1

# This where all types oe Pepperoni get add iwht it toppings
def adding_pepperoni_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global pepperoni_2, total_cost_for_all_pizzas, show_topping_frame_Pe2, length_Pe2, Pe_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Pe2 = len(expanding_pages.topping_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    pepperoni_2 = Order_pizza_list(
        r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Pepperion Resized order list.png",
        "Pepperoni\n", f"{((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50):.2f}", removing_pepperoni_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Pe2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white',
                                                    bg_color='#F2F2F2', corner_radius=20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Pe2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Pe2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10, 5))
    pizza_name_display = Label(show_topping_frame_Pe2, text="Pepperoni", background='white',
                               font=("Bahnschrift SemiBold", 12), border=0, pady=5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Pe2, text="$8.50",
                                                 text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30,
                                                 fg_color='white', text_color='black')
    pizza_price_display.grid(row=0, column=1, padx=(10, 5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text=no_charge_topping, background='white',
                  font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column=0,
                                                                                        sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_Pe2 in expanding_pages.topping_pepperoni_list:
            Label(show_topping_name_frame, text=topping_Pe2, background='white', font=("Bahnschrift SemiLight", 8),
                  border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Pe2, text="Total Price:",
                                                         fg_color='white', text_font=("Bahnschrift SemiBold", 12),
                                                         corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx=(14, 10), pady=(5, 0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Pe2,
                                   text=f"${8.50 + len(expanding_pages.topping_pepperoni_list) * 0.50:.2f}",
                                   background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10,
                                   foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5, 0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_Pe(e):
        show_topping_frame_Pe2.place(x=440, y=40)

    def hide_topping_Pe(e):
        show_topping_frame_Pe2.place_forget()

    pepperoni_2.order_pizza_frame.bind('<Enter>', show_topping_Pe)
    pepperoni_2.order_pizza_frame.bind("<Leave>", hide_topping_Pe)

    # updating the in and out Pepperoni pizza
    Pe_in_or_out_2 = 1

# This where all types oe Pepperoni get add iwht it toppings
def adding_pepperoni_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global pepperoni_3, total_cost_for_all_pizzas, show_topping_frame_Pe3, length_Pe3, Pe_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Pe3 = len(expanding_pages.topping_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    pepperoni_3 = Order_pizza_list(
        r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Pepperion Resized order list.png",
        "Pepperoni\n", f"{((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50):.2f}", removing_pepperoni_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Pe3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white',
                                                    bg_color='#F2F2F2', corner_radius=20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Pe3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Pe3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10, 5))
    pizza_name_display = Label(show_topping_frame_Pe3, text="Pepperoni", background='white',
                               font=("Bahnschrift SemiBold", 12), border=0, pady=5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Pe3, text="$8.50",
                                                 text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30,
                                                 fg_color='white', text_color='black')
    pizza_price_display.grid(row=0, column=1, padx=(10, 5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text=no_charge_topping, background='white',
                  font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column=0,
                                                                                        sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_Pe3 in expanding_pages.topping_pepperoni_list:
            Label(show_topping_name_frame, text=topping_Pe3, background='white', font=("Bahnschrift SemiLight", 8),
                  border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Pe3, text="Total Price:",
                                                         fg_color='white', text_font=("Bahnschrift SemiBold", 12),
                                                         corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx=(14, 10), pady=(5, 0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Pe3,
                                   text=f"${8.50 + len(expanding_pages.topping_pepperoni_list) * 0.50:.2f}",
                                   background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10,
                                   foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5, 0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_Pe(e):
        show_topping_frame_Pe3.place(x=440, y=40)

    def hide_topping_Pe(e):
        show_topping_frame_Pe3.place_forget()

    pepperoni_3.order_pizza_frame.bind('<Enter>', show_topping_Pe)
    pepperoni_3.order_pizza_frame.bind("<Leave>", hide_topping_Pe)

    # updating the in and out Pepperoni pizza
    Pe_in_or_out_3 = 1

# This where all types oe Pepperoni get add iwht it toppings
def adding_pepperoni_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global pepperoni_4, total_cost_for_all_pizzas, show_topping_frame_Pe4, length_Pe4, Pe_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Pe4 = len(expanding_pages.topping_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    pepperoni_4 = Order_pizza_list(
        r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Pepperion Resized order list.png",
        "Pepperoni\n", f"{((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50):.2f}", removing_pepperoni_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Pe4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white',
                                                    bg_color='#F2F2F2', corner_radius=20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Pe4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Pe4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10, 5))
    pizza_name_display = Label(show_topping_frame_Pe4, text="Pepperoni", background='white',
                               font=("Bahnschrift SemiBold", 12), border=0, pady=5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Pe4, text="$8.50",
                                                 text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30,
                                                 fg_color='white', text_color='black')
    pizza_price_display.grid(row=0, column=1, padx=(10, 5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text=no_charge_topping, background='white',
                  font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column=0,
                                                                                        sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM4 in expanding_pages.topping_pepperoni_list:
            Label(show_topping_name_frame, text=topping_AM4, background='white', font=("Bahnschrift SemiLight", 8),
                  border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Pe4, text="Total Price:",
                                                         fg_color='white', text_font=("Bahnschrift SemiBold", 12),
                                                         corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx=(14, 10), pady=(5, 0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Pe4,
                                   text=f"${8.50 + len(expanding_pages.topping_pepperoni_list) * 0.50:.2f}",
                                   background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10,
                                   foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5, 0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_Pe(e):
        show_topping_frame_Pe4.place(x=440, y=40)

    def hide_topping_Pe(e):
        show_topping_frame_Pe4.place_forget()

    pepperoni_4.order_pizza_frame.bind('<Enter>', show_topping_Pe)
    pepperoni_4.order_pizza_frame.bind("<Leave>", hide_topping_Pe)

    # updating the in and out Pepperoni pizza
    Pe_in_or_out_4 = 1

# This where all types oe Pepperoni get add iwht it toppings
def adding_pepperoni_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global pepperoni_5, total_cost_for_all_pizzas, show_topping_frame_Pe5, length_Pe5, Pe_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_pepperoni_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)
    if len(expanding_pages.topping_pepperoni_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_pepperoni_list[0])
        expanding_pages.topping_pepperoni_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Pe5 = len(expanding_pages.topping_pepperoni_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    pepperoni_5 = Order_pizza_list(
        r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Pepperion Resized order list.png",
        "Pepperoni\n", f"{((len(expanding_pages.topping_pepperoni_list) * 0.50) + 8.50):.2f}", removing_pepperoni_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Pe5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white',
                                                    bg_color='#F2F2F2', corner_radius=20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Pe5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Pe5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10, 5))
    pizza_name_display = Label(show_topping_frame_Pe5, text="Pepperoni", background='white',
                               font=("Bahnschrift SemiBold", 12), border=0, pady=5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Pe5, text="$8.50",
                                                 text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30,
                                                 fg_color='white', text_color='black')
    pizza_price_display.grid(row=0, column=1, padx=(10, 5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text=no_charge_topping, background='white',
                  font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column=0,
                                                                                        sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_Pe5 in expanding_pages.topping_pepperoni_list:
            Label(show_topping_name_frame, text=topping_Pe5, background='white', font=("Bahnschrift SemiLight", 8),
                  border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8),
                  border=0, foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Pe5, text="Total Price:",
                                                         fg_color='white', text_font=("Bahnschrift SemiBold", 12),
                                                         corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx=(14, 10), pady=(5, 0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Pe5,
                                   text=f"${8.50 + len(expanding_pages.topping_pepperoni_list) * 0.50:.2f}",
                                   background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10,
                                   foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5, 0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_Pe(e):
        show_topping_frame_Pe5.place(x=440, y=40)

    def hide_topping_Pe(e):
        show_topping_frame_Pe5.place_forget()

    pepperoni_5.order_pizza_frame.bind('<Enter>', show_topping_Pe)
    pepperoni_5.order_pizza_frame.bind("<Leave>", hide_topping_Pe)

    # updating the in and out Pepperoni pizza
    Pe_in_or_out_5 = 1

# This take of the Pepperoni adding in the order list
def pepperoni_add_order():
    global overall_Pe_counter, Pe_in_or_out_1, Pe_in_or_out_2, Pe_in_or_out_3, Pe_in_or_out_4, Pe_in_or_out_5

    # Telling the the counter thae Pepperoni has been added or display a number
    # This part add a number overall_Pe_counter when the Pepperoni add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Pepperoni")

    if Pe_in_or_out_1 == 2:
        Pe_in_or_out_1 = 0
        overall_Pe_counter = 1

    elif Pe_in_or_out_2 == 2:
        Pe_in_or_out_2 = 0
        overall_Pe_counter = 2

    elif Pe_in_or_out_3 == 2:
        Pe_in_or_out_3 = 0
        overall_Pe_counter = 3

    elif Pe_in_or_out_4 == 2:
        Pe_in_or_out_4 = 0
        overall_Pe_counter = 4

    elif Pe_in_or_out_5 == 2:
        Pe_in_or_out_5 = 0
        overall_Pe_counter = 5

    if overall_Pe_counter == 1:
        if Pe_in_or_out_1 == 0:
            adding_pepperoni_1()



    elif overall_Pe_counter == 2:
        if Pe_in_or_out_2 == 0:
            adding_pepperoni_2()


    elif overall_Pe_counter == 3:
        if Pe_in_or_out_3 == 0:
            adding_pepperoni_3()


    elif overall_Pe_counter == 4:
        if Pe_in_or_out_4 == 0:
            adding_pepperoni_4()


    elif overall_Pe_counter == 5:
        overall_Pe_counter = 0
        if Pe_in_or_out_5 == 0:
            adding_pepperoni_5()

    # This the counter for all five Pepperoni pizza
    overall_Pe_counter += 1

    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_topping_pepperoni()
    Warning_message_box.add()



# Sp means the Supreme and all the adding foe Supreme
# This all for Supreme pizza
# This ie Supreme counter so everytime the button is clicked oe Supreme it updates
global overall_Sp_counter
overall_Sp_counter = 1


global Sp_in_or_out_1, Sp_in_or_out_2, Sp_in_or_out_3, Sp_in_or_out_4, Sp_in_or_out_5
# 0 means a Supreme pizza is not in the order list whereas one measn the pizza is in the list
Sp_in_or_out_1 = 0
Sp_in_or_out_2 = 0
Sp_in_or_out_3 = 0
Sp_in_or_out_4 = 0
Sp_in_or_out_5 = 0



# This where everything get remove foe Supreme
def removing_supreme_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Sp1, Sp_in_or_out_1
    allowed_to_checkout()
    supreme_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_Sp1) * 0.50 + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Supreme")
    show_topping_frame_Sp1.destroy()
    # updating the in and out Supreme pizza
    Sp_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove foe Supreme
def removing_supreme_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Sp2, Sp_in_or_out_2
    allowed_to_checkout()
    supreme_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_Sp2 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Supreme")
    show_topping_frame_Sp2.destroy()
    # updating the in and out Supreme pizza
    Sp_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove foe Supreme
def removing_supreme_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Sp3, Sp_in_or_out_3
    allowed_to_checkout()
    supreme_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_Sp3) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Supreme")
    show_topping_frame_Sp3.destroy()
    # updating the in and out Supreme pizza
    Sp_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove foe Supreme
def removing_supreme_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Sp4, Sp_in_or_out_4
    allowed_to_checkout()
    supreme_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_Sp4 * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Supreme")
    show_topping_frame_Sp4.destroy()
    # updating the in and out Supreme pizza
    Sp_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove foe Supreme
def removing_supreme_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_Sp5, Sp_in_or_out_5
    allowed_to_checkout()
    supreme_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_Sp5) * 0.50) + 8.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Supreme")
    show_topping_frame_Sp5.destroy()
    # updating the in and out Supreme pizza
    Sp_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types oe Supreme get add iwht it toppings
def adding_supreme_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global supreme_1, total_cost_for_all_pizzas,show_topping_frame_Sp1, length_Sp1, Sp_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)


    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Sp1 = len(expanding_pages.topping_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    supreme_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Supreme Resized order list.png", "Supreme\n", f"{((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50):.2f}", removing_supreme_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Sp1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Sp1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Sp1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_Sp1, text = "Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Sp1, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_Sp1 in expanding_pages.topping_supreme_list:
            Label(show_topping_name_frame, text = topping_Sp1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Sp1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Sp1, text = f"${8.50 + len(expanding_pages.topping_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_Sp(e):
        show_topping_frame_Sp1.place(x = 440, y= 40)
    def hide_topping_Sp(e):
        show_topping_frame_Sp1.place_forget()

    supreme_1.order_pizza_frame.bind('<Enter>', show_topping_Sp)
    supreme_1.order_pizza_frame.bind("<Leave>", hide_topping_Sp)

    # updating the in and out Supreme pizza
    Sp_in_or_out_1 = 1



# This where all types oe Supreme get add iwht it toppings
def adding_supreme_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global supreme_2, total_cost_for_all_pizzas, show_topping_frame_Sp2, length_Sp2, Sp_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Sp2 = len(expanding_pages.topping_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    supreme_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Supreme Resized order list.png", "Supreme\n", f"{((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50):.2f}", removing_supreme_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Sp2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Sp2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Sp2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_Sp2, text = "Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Sp2, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_Sp2 in expanding_pages.topping_supreme_list:
            Label(show_topping_name_frame, text = topping_Sp2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Sp2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Sp2, text = f"${8.50 + len(expanding_pages.topping_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_Sp(e):
        show_topping_frame_Sp2.place(x = 440, y= 40)
    def hide_topping_Sp(e):
        show_topping_frame_Sp2.place_forget()

    supreme_2.order_pizza_frame.bind('<Enter>', show_topping_Sp)
    supreme_2.order_pizza_frame.bind("<Leave>", hide_topping_Sp)

    # updating the in and out Supreme pizza
    Sp_in_or_out_2 = 1




# This where all types oe Supreme get add iwht it toppings
def adding_supreme_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global supreme_3, total_cost_for_all_pizzas, show_topping_frame_Sp3, length_Sp3, Sp_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Sp3 = len(expanding_pages.topping_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    supreme_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Supreme Resized order list.png", "Supreme\n", f"{((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50):.2f}", removing_supreme_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Sp3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Sp3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Sp3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_Sp3, text = "Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Sp3, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_Sp3 in expanding_pages.topping_supreme_list:
            Label(show_topping_name_frame, text = topping_Sp3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Sp3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Sp3, text = f"${8.50 + len(expanding_pages.topping_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_Sp(e):
        show_topping_frame_Sp3.place(x = 440, y= 40)
    def hide_topping_Sp(e):
        show_topping_frame_Sp3.place_forget()

    supreme_3.order_pizza_frame.bind('<Enter>', show_topping_Sp)
    supreme_3.order_pizza_frame.bind("<Leave>", hide_topping_Sp)

    # updating the in and out Supreme pizza
    Sp_in_or_out_3 = 1



# This where all types oe Supreme get add iwht it toppings
def adding_supreme_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global supreme_4, total_cost_for_all_pizzas, show_topping_frame_Sp4, length_Sp4, Sp_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Sp4 = len(expanding_pages.topping_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    supreme_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Supreme Resized order list.png", "Supreme\n", f"{((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50):.2f}", removing_supreme_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Sp4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Sp4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Sp4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_Sp4, text = "Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Sp4, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AM4 in expanding_pages.topping_supreme_list:
            Label(show_topping_name_frame, text = topping_AM4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Sp4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Sp4, text = f"${8.50 + len(expanding_pages.topping_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_Sp(e):
        show_topping_frame_Sp4.place(x = 440, y= 40)
    def hide_topping_Sp(e):
        show_topping_frame_Sp4.place_forget()

    supreme_4.order_pizza_frame.bind('<Enter>', show_topping_Sp)
    supreme_4.order_pizza_frame.bind("<Leave>", hide_topping_Sp)

    # updating the in and out Supreme pizza
    Sp_in_or_out_4 = 1


# This where all types oe Supreme get add iwht it toppings
def adding_supreme_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global supreme_5, total_cost_for_all_pizzas, show_topping_frame_Sp5, length_Sp5, Sp_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_supreme_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)
    if len(expanding_pages.topping_supreme_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_supreme_list[0])
        expanding_pages.topping_supreme_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_Sp5 = len(expanding_pages.topping_supreme_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    supreme_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Supreme Resized order list.png", "Supreme\n", f"{((len(expanding_pages.topping_supreme_list) * 0.50) + 8.50):.2f}", removing_supreme_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_Sp5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_Sp5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_Sp5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_Sp5, text = "Supreme", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_Sp5, text = "$8.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_Sp5 in expanding_pages.topping_supreme_list:
            Label(show_topping_name_frame, text = topping_Sp5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_Sp5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_Sp5, text = f"${8.50 + len(expanding_pages.topping_supreme_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_Sp(e):
        show_topping_frame_Sp5.place(x = 440, y= 40)
    def hide_topping_Sp(e):
        show_topping_frame_Sp5.place_forget()

    supreme_5.order_pizza_frame.bind('<Enter>', show_topping_Sp)
    supreme_5.order_pizza_frame.bind("<Leave>", hide_topping_Sp)

    # updating the in and out Supreme pizza
    Sp_in_or_out_5 = 1



# This take of the Supreme adding in the order list
def Supreme_add_order():
    global overall_Sp_counter, Sp_in_or_out_1, Sp_in_or_out_2, Sp_in_or_out_3, Sp_in_or_out_4, Sp_in_or_out_5

    # Telling the the counter thae Supreme has been added or display a number
    # This part add a number overall_Sp_counter when the Supreme add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Supreme")

    if Sp_in_or_out_1 == 2:
        Sp_in_or_out_1 = 0
        overall_Sp_counter = 1

    elif Sp_in_or_out_2 == 2:
        Sp_in_or_out_2 = 0
        overall_Sp_counter = 2

    elif Sp_in_or_out_3 == 2:
        Sp_in_or_out_3 = 0
        overall_Sp_counter = 3

    elif Sp_in_or_out_4 == 2:
        Sp_in_or_out_4 = 0
        overall_Sp_counter = 4

    elif Sp_in_or_out_5 == 2:
        Sp_in_or_out_5 = 0
        overall_Sp_counter = 5



    if overall_Sp_counter == 1:
        if Sp_in_or_out_1 == 0:
            adding_supreme_1()



    elif overall_Sp_counter == 2:
        if Sp_in_or_out_2 == 0:
            adding_supreme_2()


    elif overall_Sp_counter == 3:
        if Sp_in_or_out_3 == 0:
            adding_supreme_3()


    elif overall_Sp_counter== 4:
        if Sp_in_or_out_4 == 0:
            adding_supreme_4()


    elif overall_Sp_counter == 5:
        overall_Sp_counter = 0
        if Sp_in_or_out_5 == 0:
            adding_supreme_5()



    # This the counter for all five Supreme pizza
    overall_Sp_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_topping_supreme()
    Warning_message_box.add()


# AC means the Aprciot Chicken and all the adding foe aprciot_chicken
# This all for aprciot_chicken pizza
# This ie aprciot_chicken counter so everytime the button is clicked oe aprciot_chicken it updates
global overall_AC_counter
overall_AC_counter = 1


global AC_in_or_out_1, AC_in_or_out_2, AC_in_or_out_3, AC_in_or_out_4, AC_in_or_out_5
# 0 means a aprciot_chicken pizza is not in the order list whereas one measn the pizza is in the list
AC_in_or_out_1 = 0
AC_in_or_out_2 = 0
AC_in_or_out_3 = 0
AC_in_or_out_4 = 0
AC_in_or_out_5 = 0



# This where everything get remove foe aprciot_chicken
def removing_aprciot_chicken_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AC1, AC_in_or_out_1
    allowed_to_checkout()
    apricot_chicken_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_AC1) * 0.50 + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Aprciot Chicken")
    show_topping_frame_AC1.destroy()
    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove foe aprciot_chicken
def removing_aprciot_chicken_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AC2, AC_in_or_out_2
    allowed_to_checkout()
    apricot_chicken_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_AC2 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Aprciot Chicken")
    show_topping_frame_AC2.destroy()
    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove foe aprciot_chicken
def removing_aprciot_chicken_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AC3, AC_in_or_out_3
    allowed_to_checkout()
    apricot_chicken_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_AC3) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Aprciot Chicken")
    show_topping_frame_AC3.destroy()
    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove foe aprciot_chicken
def removing_aprciot_chicken_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AC4, AC_in_or_out_4
    allowed_to_checkout()
    apricot_chicken_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_AC4 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Aprciot Chicken")
    show_topping_frame_AC4.destroy()
    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove foe aprciot_chicken
def removing_aprciot_chicken_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_AC5, AC_in_or_out_5
    allowed_to_checkout()
    apricot_chicken_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_AC5) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Aprciot Chicken")
    show_topping_frame_AC5.destroy()
    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types oe aprciot_chicken get add iwht it toppings
def adding_apricot_chicken_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global apricot_chicken_1, total_cost_for_all_pizzas,show_topping_frame_AC1, length_AC1, AC_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_apricot_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AC1 = len(expanding_pages.topping_apricot_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    apricot_chicken_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Apriot Chicken Resized order list.png", "Aprciot\nChicken", f"{((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50):.2f}", removing_aprciot_chicken_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AC1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AC1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AC1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AC1, text = "Aprciot Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AC1, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AC1 in expanding_pages.topping_apricot_chicken_list:
            Label(show_topping_name_frame, text = topping_AC1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AC1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AC1, text = f"${13.50 + len(expanding_pages.topping_apricot_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_AC(e):
        show_topping_frame_AC1.place(x = 440, y= 40)
    def hide_topping_AC(e):
        show_topping_frame_AC1.place_forget()

    apricot_chicken_1.order_pizza_frame.bind('<Enter>', show_topping_AC)
    apricot_chicken_1.order_pizza_frame.bind("<Leave>", hide_topping_AC)

    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_1 = 1



# This where all types oe aprciot_chicken get add iwht it toppings
def adding_apricot_chicken_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global apricot_chicken_2, total_cost_for_all_pizzas, show_topping_frame_AC2, length_AC2, AC_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_apricot_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AC2 = len(expanding_pages.topping_apricot_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    apricot_chicken_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Apriot Chicken Resized order list.png", "Aprciot\nChicken", f"{((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50):.2f}", removing_aprciot_chicken_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AC2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AC2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AC2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AC2, text = "Aprciot Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AC2, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AC2 in expanding_pages.topping_apricot_chicken_list:
            Label(show_topping_name_frame, text = topping_AC2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AC2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AC2, text = f"${13.50 + len(expanding_pages.topping_apricot_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_AC(e):
        show_topping_frame_AC2.place(x = 440, y= 40)
    def hide_topping_AC(e):
        show_topping_frame_AC2.place_forget()

    apricot_chicken_2.order_pizza_frame.bind('<Enter>', show_topping_AC)
    apricot_chicken_2.order_pizza_frame.bind("<Leave>", hide_topping_AC)

    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_2 = 1




# This where all types oe aprciot_chicken get add iwht it toppings
def adding_apricot_chicken_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global apricot_chicken_3, total_cost_for_all_pizzas, show_topping_frame_AC3, length_AC3, AC_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_apricot_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AC3 = len(expanding_pages.topping_apricot_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    apricot_chicken_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Apriot Chicken Resized order list.png", "Aprciot\nChicken", f"{((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50):.2f}", removing_aprciot_chicken_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AC3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AC3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AC3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AC3, text = "Aprciot Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AC3, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AC3 in expanding_pages.topping_apricot_chicken_list:
            Label(show_topping_name_frame, text = topping_AC3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AC3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AC3, text = f"${13.50 + len(expanding_pages.topping_apricot_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_AC(e):
        show_topping_frame_AC3.place(x = 440, y= 40)
    def hide_topping_AC(e):
        show_topping_frame_AC3.place_forget()

    apricot_chicken_3.order_pizza_frame.bind('<Enter>', show_topping_AC)
    apricot_chicken_3.order_pizza_frame.bind("<Leave>", hide_topping_AC)

    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_3 = 1



# This where all types oe aprciot_chicken get add iwht it toppings
def adding_apricot_chicken_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global apricot_chicken_4, total_cost_for_all_pizzas, show_topping_frame_AC4, length_AC4, AC_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_apricot_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AC4 = len(expanding_pages.topping_apricot_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    apricot_chicken_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Apriot Chicken Resized order list.png", "Aprciot\nChicken", f"{((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50):.2f}", removing_aprciot_chicken_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AC4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AC4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AC4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AC4, text = "Aprciot Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AC4, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AC4 in expanding_pages.topping_apricot_chicken_list:
            Label(show_topping_name_frame, text = topping_AC4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AC4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AC4, text = f"${13.50 + len(expanding_pages.topping_apricot_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_AC(e):
        show_topping_frame_AC4.place(x = 440, y= 40)
    def hide_topping_AC(e):
        show_topping_frame_AC4.place_forget()

    apricot_chicken_4.order_pizza_frame.bind('<Enter>', show_topping_AC)
    apricot_chicken_4.order_pizza_frame.bind("<Leave>", hide_topping_AC)

    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_4 = 1


# This where all types oe aprciot_chicken get add iwht it toppings
def adding_apricot_chicken_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global apricot_chicken_5, total_cost_for_all_pizzas, show_topping_frame_AC5, length_AC5, AC_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_apricot_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)
    if len(expanding_pages.topping_apricot_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_apricot_chicken_list[0])
        expanding_pages.topping_apricot_chicken_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_AC5 = len(expanding_pages.topping_apricot_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    apricot_chicken_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Apriot Chicken Resized order list.png", "Aprciot\nChicken", f"{((len(expanding_pages.topping_apricot_chicken_list) * 0.50) + 13.50):.2f}", removing_aprciot_chicken_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_AC5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_AC5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_AC5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_AC5, text = "Aprciot Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_AC5, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_AC5 in expanding_pages.topping_apricot_chicken_list:
            Label(show_topping_name_frame, text = topping_AC5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_AC5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_AC5, text = f"${13.50 + len(expanding_pages.topping_apricot_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_AC(e):
        show_topping_frame_AC5.place(x = 440, y= 40)
    def hide_topping_AC(e):
        show_topping_frame_AC5.place_forget()

    apricot_chicken_5.order_pizza_frame.bind('<Enter>', show_topping_AC)
    apricot_chicken_5.order_pizza_frame.bind("<Leave>", hide_topping_AC)

    # updating the in and out aprciot_chicken pizza
    AC_in_or_out_5 = 1



# This take of the aprciot_chicken adding in the order list
def apricot_chicken_add_order():
    global overall_AC_counter, AC_in_or_out_1, AC_in_or_out_2, AC_in_or_out_3, AC_in_or_out_4, AC_in_or_out_5

    # Telling the the counter thae aprciot_chicken has been added or display a number
    # This part add a number overall_AC_counter when the aprciot_chicken add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Aprciot Chicken")

    if AC_in_or_out_1 == 2:
        AC_in_or_out_1 = 0
        overall_AC_counter = 1

    elif AC_in_or_out_2 == 2:
        AC_in_or_out_2 = 0
        overall_AC_counter = 2

    elif AC_in_or_out_3 == 2:
        AC_in_or_out_3 = 0
        overall_AC_counter = 3

    elif AC_in_or_out_4 == 2:
        AC_in_or_out_4 = 0
        overall_AC_counter = 4

    elif AC_in_or_out_5 == 2:
        AC_in_or_out_5 = 0
        overall_AC_counter = 5



    if overall_AC_counter == 1:
        if AC_in_or_out_1 == 0:
            adding_apricot_chicken_1()



    elif overall_AC_counter == 2:
        if AC_in_or_out_2 == 0:
            adding_apricot_chicken_2()


    elif overall_AC_counter == 3:
        if AC_in_or_out_3 == 0:
            adding_apricot_chicken_3()


    elif overall_AC_counter== 4:
        if AC_in_or_out_4 == 0:
            adding_apricot_chicken_4()


    elif overall_AC_counter == 5:
        overall_AC_counter = 0
        if AC_in_or_out_5 == 0:
            adding_apricot_chicken_5()



    # This the counter for all five aprciot_chicken pizza
    overall_AC_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_topping_aprciot_chicken()
    Warning_message_box.add()


# CBA means the Chicken, Bacon and Aioli and all the adding foe bacon_aioli
# This all for bacon_aioli pizza
# This ie bacon_aioli counter so everytime the button is clicked oe bacon_aioli it updates
global overall_CBA_counter
overall_CBA_counter = 1


global CBA_in_or_out_1, CBA_in_or_out_2, CBA_in_or_out_3, CBA_in_or_out_4, CBA_in_or_out_5
# 0 means a bacon_aioli pizza is not in the order list whereas one measn the pizza is in the list
CBA_in_or_out_1 = 0
CBA_in_or_out_2 = 0
CBA_in_or_out_3 = 0
CBA_in_or_out_4 = 0
CBA_in_or_out_5 = 0



# This where everything get remove foe bacon_aioli
def removing_bacon_aioli_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CBA1, CBA_in_or_out_1
    allowed_to_checkout()
    bacon_aioli_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_CBA1) * 0.50 + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Bacon & Aioli")
    show_topping_frame_CBA1.destroy()
    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove foe bacon_aioli
def removing_bacon_aioli_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CBA2, CBA_in_or_out_2
    allowed_to_checkout()
    bacon_aioli_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CBA2 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Bacon & Aioli")
    show_topping_frame_CBA2.destroy()
    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove foe bacon_aioli
def removing_bacon_aioli_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CBA3, CBA_in_or_out_3
    allowed_to_checkout()
    bacon_aioli_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CBA3) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Bacon & Aioli")
    show_topping_frame_CBA3.destroy()
    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove foe bacon_aioli
def removing_bacon_aioli_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CBA4, CBA_in_or_out_4
    allowed_to_checkout()
    bacon_aioli_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CBA4 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Bacon & Aioli")
    show_topping_frame_CBA4.destroy()
    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove foe bacon_aioli
def removing_bacon_aioli_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CBA5, CBA_in_or_out_5
    allowed_to_checkout()
    bacon_aioli_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CBA5) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Bacon & Aioli")
    show_topping_frame_CBA5.destroy()
    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types oe bacon_aioli get add iwht it toppings
def adding_bacon_aioli_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global bacon_aioli_1, total_cost_for_all_pizzas,show_topping_frame_CBA1, length_CBA1, CBA_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_bacon_aioli_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CBA1 = len(expanding_pages.topping_bacon_aioli_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    bacon_aioli_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken, Bacon and Aloli order list.png", "Bacon &\nAioli", f"{((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50):.2f}", removing_bacon_aioli_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CBA1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CBA1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CBA1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CBA1, text = "Bacon & Aioli", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CBA1, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CBA1 in expanding_pages.topping_bacon_aioli_list:
            Label(show_topping_name_frame, text = topping_CBA1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CBA1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CBA1, text = f"${13.50 + len(expanding_pages.topping_bacon_aioli_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CBA(e):
        show_topping_frame_CBA1.place(x = 440, y= 40)
    def hide_topping_CBA(e):
        show_topping_frame_CBA1.place_forget()

    bacon_aioli_1.order_pizza_frame.bind('<Enter>', show_topping_CBA)
    bacon_aioli_1.order_pizza_frame.bind("<Leave>", hide_topping_CBA)

    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_1 = 1



# This where all types oe bacon_aioli get add iwht it toppings
def adding_bacon_aioli_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global bacon_aioli_2, total_cost_for_all_pizzas, show_topping_frame_CBA2, length_CBA2, CBA_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_bacon_aioli_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CBA2 = len(expanding_pages.topping_bacon_aioli_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    bacon_aioli_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken, Bacon and Aloli order list.png", "Bacon &\nAioli", f"{((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50):.2f}", removing_bacon_aioli_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CBA2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CBA2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CBA2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CBA2, text = "Bacon & Aioli", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CBA2, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CBA2 in expanding_pages.topping_bacon_aioli_list:
            Label(show_topping_name_frame, text = topping_CBA2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CBA2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CBA2, text = f"${13.50 + len(expanding_pages.topping_bacon_aioli_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CBA(e):
        show_topping_frame_CBA2.place(x = 440, y= 40)
    def hide_topping_CBA(e):
        show_topping_frame_CBA2.place_forget()

    bacon_aioli_2.order_pizza_frame.bind('<Enter>', show_topping_CBA)
    bacon_aioli_2.order_pizza_frame.bind("<Leave>", hide_topping_CBA)

    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_2 = 1




# This where all types oe bacon_aioli get add iwht it toppings
def adding_bacon_aioli_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global bacon_aioli_3, total_cost_for_all_pizzas, show_topping_frame_CBA3, length_CBA3, CBA_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_bacon_aioli_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CBA3 = len(expanding_pages.topping_bacon_aioli_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    bacon_aioli_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken, Bacon and Aloli order list.png", "Bacon &\nAioli", f"{((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50):.2f}", removing_bacon_aioli_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CBA3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CBA3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CBA3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CBA3, text = "Bacon & Aioli", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CBA3, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CBA3 in expanding_pages.topping_bacon_aioli_list:
            Label(show_topping_name_frame, text = topping_CBA3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CBA3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CBA3, text = f"${13.50 + len(expanding_pages.topping_bacon_aioli_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CBA(e):
        show_topping_frame_CBA3.place(x = 440, y= 40)
    def hide_topping_CBA(e):
        show_topping_frame_CBA3.place_forget()

    bacon_aioli_3.order_pizza_frame.bind('<Enter>', show_topping_CBA)
    bacon_aioli_3.order_pizza_frame.bind("<Leave>", hide_topping_CBA)

    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_3 = 1



# This where all types oe bacon_aioli get add iwht it toppings
def adding_bacon_aioli_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global bacon_aioli_4, total_cost_for_all_pizzas, show_topping_frame_CBA4, length_CBA4, CBA_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_bacon_aioli_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CBA4 = len(expanding_pages.topping_bacon_aioli_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    bacon_aioli_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken, Bacon and Aloli order list.png", "Bacon &\nAioli", f"{((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50):.2f}", removing_bacon_aioli_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CBA4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CBA4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CBA4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CBA4, text = "Bacon & Aioli", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CBA4, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CBA4 in expanding_pages.topping_bacon_aioli_list:
            Label(show_topping_name_frame, text = topping_CBA4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CBA4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CBA4, text = f"${13.50 + len(expanding_pages.topping_bacon_aioli_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_CBA(e):
        show_topping_frame_CBA4.place(x = 440, y= 40)
    def hide_topping_CBA(e):
        show_topping_frame_CBA4.place_forget()

    bacon_aioli_4.order_pizza_frame.bind('<Enter>', show_topping_CBA)
    bacon_aioli_4.order_pizza_frame.bind("<Leave>", hide_topping_CBA)

    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_4 = 1


# This where all types oe bacon_aioli get add iwht it toppings
def adding_bacon_aioli_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global bacon_aioli_5, total_cost_for_all_pizzas, show_topping_frame_CBA5, length_CBA5, CBA_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_bacon_aioli_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)
    if len(expanding_pages.topping_bacon_aioli_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_bacon_aioli_list[0])
        expanding_pages.topping_bacon_aioli_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CBA5 = len(expanding_pages.topping_bacon_aioli_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    bacon_aioli_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken, Bacon and Aloli order list.png", "Bacon &\nAioli", f"{((len(expanding_pages.topping_bacon_aioli_list) * 0.50) + 13.50):.2f}", removing_bacon_aioli_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CBA5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CBA5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CBA5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CBA5, text = "Bacon & Aioli", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CBA5, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CBA5 in expanding_pages.topping_bacon_aioli_list:
            Label(show_topping_name_frame, text = topping_CBA5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CBA5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CBA5, text = f"${13.50 + len(expanding_pages.topping_bacon_aioli_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CBA(e):
        show_topping_frame_CBA5.place(x = 440, y= 40)
    def hide_topping_CBA(e):
        show_topping_frame_CBA5.place_forget()

    bacon_aioli_5.order_pizza_frame.bind('<Enter>', show_topping_CBA)
    bacon_aioli_5.order_pizza_frame.bind("<Leave>", hide_topping_CBA)

    # updating the in and out bacon_aioli pizza
    CBA_in_or_out_5 = 1



# This take of the bacon_aioli adding in the order list
def bacon_aioli_add_order():
    global overall_CBA_counter, CBA_in_or_out_1, CBA_in_or_out_2, CBA_in_or_out_3, CBA_in_or_out_4, CBA_in_or_out_5

    # Telling the the counter thae bacon_aioli has been added or display a number
    # This part add a number overall_CBA_counter when the bacon_aioli add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Bacon & Aioli")

    if CBA_in_or_out_1 == 2:
        CBA_in_or_out_1 = 0
        overall_CBA_counter = 1

    elif CBA_in_or_out_2 == 2:
        CBA_in_or_out_2 = 0
        overall_CBA_counter = 2

    elif CBA_in_or_out_3 == 2:
        CBA_in_or_out_3 = 0
        overall_CBA_counter = 3

    elif CBA_in_or_out_4 == 2:
        CBA_in_or_out_4 = 0
        overall_CBA_counter = 4

    elif CBA_in_or_out_5 == 2:
        CBA_in_or_out_5 = 0
        overall_CBA_counter = 5



    if overall_CBA_counter == 1:
        if CBA_in_or_out_1 == 0:
            adding_bacon_aioli_1()



    elif overall_CBA_counter == 2:
        if CBA_in_or_out_2 == 0:
            adding_bacon_aioli_2()


    elif overall_CBA_counter == 3:
        if CBA_in_or_out_3 == 0:
            adding_bacon_aioli_3()


    elif overall_CBA_counter== 4:
        if CBA_in_or_out_4 == 0:
            adding_bacon_aioli_4()


    elif overall_CBA_counter == 5:
        overall_CBA_counter = 0
        if CBA_in_or_out_5 == 0:
            adding_bacon_aioli_5()



    # This the counter for all five bacon_aioli pizza
    overall_CBA_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_topping_bacon_aioli()
    Warning_message_box.add()


# CC means the Chicken, chicken Cheese and all the adding foe chicken_cheese
# This all for chicken_cheese pizza
# This ie chicken_cheese counter so everytime the button is clicked oe chicken_cheese it updates
global overall_CC_counter
overall_CC_counter = 1


global CC_in_or_out_1, CC_in_or_out_2, CC_in_or_out_3, CC_in_or_out_4, CC_in_or_out_5
# 0 means a chicken_cheese pizza is not in the order list whereas one measn the pizza is in the list
CC_in_or_out_1 = 0
CC_in_or_out_2 = 0
CC_in_or_out_3 = 0
CC_in_or_out_4 = 0
CC_in_or_out_5 = 0



# This where everything get remove foe chicken_cheese
def removing_chicken_cheese_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CC1, CC_in_or_out_1
    allowed_to_checkout()
    chicken_cheese_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_CC1) * 0.50 + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Cheese")
    show_topping_frame_CC1.destroy()
    # updating the in and out chicken_cheese pizza
    CC_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove foe chicken_cheese
def removing_chicken_cheese_2():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CC2, CC_in_or_out_2
    allowed_to_checkout()
    chicken_cheese_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CC2 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Cheese")
    show_topping_frame_CC2.destroy()
    # updating the in and out chicken_cheese pizza
    CC_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove foe chicken_cheese
def removing_chicken_cheese_3():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CC3, CC_in_or_out_3
    allowed_to_checkout()
    chicken_cheese_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CC3) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Cheese")
    show_topping_frame_CC3.destroy()
    # updating the in and out chicken_cheese pizza
    CC_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove foe chicken_cheese
def removing_chicken_cheese_4():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CC4, CC_in_or_out_4
    allowed_to_checkout()
    chicken_cheese_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CC4 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Cheese")
    show_topping_frame_CC4.destroy()
    # updating the in and out chicken_cheese pizza
    CC_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove foe chicken_cheese
def removing_chicken_cheese_5():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_CC5, CC_in_or_out_5
    allowed_to_checkout()
    chicken_cheese_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_CC5) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Chicken Cheese")
    show_topping_frame_CC5.destroy()
    # updating the in and out chicken_cheese pizza
    CC_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types oe chicken_cheese get add iwht it toppings
def adding_chicken_cheese_1():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_cheese_1, total_cost_for_all_pizzas,show_topping_frame_CC1, length_CC1, CC_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CC1 = len(expanding_pages.topping_chicken_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_cheese_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken & Camembert Resized order list.png", "Chicken\nCheese", f"{((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50):.2f}", removing_chicken_cheese_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CC1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CC1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CC1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CC1, text = "Chicken Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CC1, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CC1 in expanding_pages.topping_chicken_cheese_list:
            Label(show_topping_name_frame, text = topping_CC1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CC1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CC1, text = f"${13.50 + len(expanding_pages.topping_chicken_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CC(e):
        show_topping_frame_CC1.place(x = 440, y= 40)
    def hide_topping_CC(e):
        show_topping_frame_CC1.place_forget()

    chicken_cheese_1.order_pizza_frame.bind('<Enter>', show_topping_CC)
    chicken_cheese_1.order_pizza_frame.bind("<Leave>", hide_topping_CC)

    # updating the in and out chicken_cheese pizza
    CC_in_or_out_1 = 1



# This where all types oe chicken_cheese get add iwht it toppings
def adding_chicken_cheese_2():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_cheese_2, total_cost_for_all_pizzas, show_topping_frame_CC2, length_CC2, CC_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CC2 = len(expanding_pages.topping_chicken_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_cheese_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken & Camembert Resized order list.png", "Chicken\nCheese", f"{((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50):.2f}", removing_chicken_cheese_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CC2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CC2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CC2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CC2, text = "Chicken Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CC2, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CC2 in expanding_pages.topping_chicken_cheese_list:
            Label(show_topping_name_frame, text = topping_CC2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CC2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CC2, text = f"${13.50 + len(expanding_pages.topping_chicken_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CC(e):
        show_topping_frame_CC2.place(x = 440, y= 40)
    def hide_topping_CC(e):
        show_topping_frame_CC2.place_forget()

    chicken_cheese_2.order_pizza_frame.bind('<Enter>', show_topping_CC)
    chicken_cheese_2.order_pizza_frame.bind("<Leave>", hide_topping_CC)

    # updating the in and out chicken_cheese pizza
    CC_in_or_out_2 = 1




# This where all types oe chicken_cheese get add iwht it toppings
def adding_chicken_cheese_3():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_cheese_3, total_cost_for_all_pizzas, show_topping_frame_CC3, length_CC3, CC_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CC3 = len(expanding_pages.topping_chicken_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_cheese_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken & Camembert Resized order list.png", "Chicken\nCheese", f"{((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50):.2f}", removing_chicken_cheese_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CC3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CC3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CC3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CC3, text = "Chicken Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CC3, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CC3 in expanding_pages.topping_chicken_cheese_list:
            Label(show_topping_name_frame, text = topping_CC3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CC3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CC3, text = f"${13.50 + len(expanding_pages.topping_chicken_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CC(e):
        show_topping_frame_CC3.place(x = 440, y= 40)
    def hide_topping_CC(e):
        show_topping_frame_CC3.place_forget()

    chicken_cheese_3.order_pizza_frame.bind('<Enter>', show_topping_CC)
    chicken_cheese_3.order_pizza_frame.bind("<Leave>", hide_topping_CC)

    # updating the in and out chicken_cheese pizza
    CC_in_or_out_3 = 1



# This where all types oe chicken_cheese get add iwht it toppings
def adding_chicken_cheese_4():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_cheese_4, total_cost_for_all_pizzas, show_topping_frame_CC4, length_CC4, CC_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CC4 = len(expanding_pages.topping_chicken_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_cheese_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken & Camembert Resized order list.png", "Chicken\nCheese", f"{((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50):.2f}", removing_chicken_cheese_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CC4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CC4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CC4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CC4, text = "Chicken Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CC4, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CC4 in expanding_pages.topping_chicken_cheese_list:
            Label(show_topping_name_frame, text = topping_CC4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CC4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CC4, text = f"${13.50 + len(expanding_pages.topping_chicken_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_CC(e):
        show_topping_frame_CC4.place(x = 440, y= 40)
    def hide_topping_CC(e):
        show_topping_frame_CC4.place_forget()

    chicken_cheese_4.order_pizza_frame.bind('<Enter>', show_topping_CC)
    chicken_cheese_4.order_pizza_frame.bind("<Leave>", hide_topping_CC)

    # updating the in and out chicken_cheese pizza
    CC_in_or_out_4 = 1


# This where all types oe chicken_cheese get add iwht it toppings
def adding_chicken_cheese_5():
    # setting a global variable so it can be updated and alos can be accesded outsidr os this function to be updated
    global chicken_cheese_5, total_cost_for_all_pizzas, show_topping_frame_CC5, length_CC5, CC_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the accurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_chicken_cheese_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)
    if len(expanding_pages.topping_chicken_cheese_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_chicken_cheese_list[0])
        expanding_pages.topping_chicken_cheese_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_CC5 = len(expanding_pages.topping_chicken_cheese_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    chicken_cheese_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken & Camembert Resized order list.png", "Chicken\nCheese", f"{((len(expanding_pages.topping_chicken_cheese_list) * 0.50) + 13.50):.2f}", removing_chicken_cheese_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_CC5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_CC5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_CC5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_CC5, text = "Chicken Cheese", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_CC5, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_CC5 in expanding_pages.topping_chicken_cheese_list:
            Label(show_topping_name_frame, text = topping_CC5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_CC5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_CC5, text = f"${13.50 + len(expanding_pages.topping_chicken_cheese_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_CC(e):
        show_topping_frame_CC5.place(x = 440, y= 40)
    def hide_topping_CC(e):
        show_topping_frame_CC5.place_forget()

    chicken_cheese_5.order_pizza_frame.bind('<Enter>', show_topping_CC)
    chicken_cheese_5.order_pizza_frame.bind("<Leave>", hide_topping_CC)

    # updating the in and out chicken_cheese pizza
    CC_in_or_out_5 = 1



# This take of the chicken_cheese adding in the order list
def chicken_cheese_add_order():
    global overall_CC_counter, CC_in_or_out_1, CC_in_or_out_2, CC_in_or_out_3, CC_in_or_out_4, CC_in_or_out_5

    # Telling the the counter thae chicken_cheese has been added or display a number
    # This part add a number overall_CC_counter when the chicken_cheese add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Chicken Cheese")

    if CC_in_or_out_1 == 2:
        CC_in_or_out_1 = 0
        overall_CC_counter = 1

    elif CC_in_or_out_2 == 2:
        CC_in_or_out_2 = 0
        overall_CC_counter = 2

    elif CC_in_or_out_3 == 2:
        CC_in_or_out_3 = 0
        overall_CC_counter = 3

    elif CC_in_or_out_4 == 2:
        CC_in_or_out_4 = 0
        overall_CC_counter = 4

    elif CC_in_or_out_5 == 2:
        CC_in_or_out_5 = 0
        overall_CC_counter = 5



    if overall_CC_counter == 1:
        if CC_in_or_out_1 == 0:
            adding_chicken_cheese_1()



    elif overall_CC_counter == 2:
        if CC_in_or_out_2 == 0:
            adding_chicken_cheese_2()


    elif overall_CC_counter == 3:
        if CC_in_or_out_3 == 0:
            adding_chicken_cheese_3()


    elif overall_CC_counter== 4:
        if CC_in_or_out_4 == 0:
            adding_chicken_cheese_4()


    elif overall_CC_counter == 5:
        overall_CC_counter = 0
        if CC_in_or_out_5 == 0:
            adding_chicken_cheese_5()



    # This the counter for all five chicken_cheese pizza
    overall_CC_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_topping_chicken_cheese()
    Warning_message_box.add()


# GP means the Gralic Prawn, and all the adding for gralic prawns
# This all for gralic prawns pizza
# This ie gralic prawns counter so everytime the button is clicked oe gralic prawns it updates
global overall_GP_counter
overall_GP_counter = 1


global GP_in_or_out_1, GP_in_or_out_2, GP_in_or_out_3, GP_in_or_out_4, GP_in_or_out_5
# 0 means a gralic prawns pizza is not in the order list whereas one measn the pizza is in the list
GP_in_or_out_1 = 0
GP_in_or_out_2 = 0
GP_in_or_out_3 = 0
GP_in_or_out_4 = 0
GP_in_or_out_5 = 0



# This where everything get remove foe gralic prawns
def removing_gralic_prawn_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_GP1, GP_in_or_out_1
    allowed_to_checkout()
    gralic_prawns_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_GP1) * 0.50 + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Gralic Prawn")
    show_topping_frame_GP1.destroy()
    # updating the in and out gralic prawns pizza
    GP_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove foe gralic prawns
def removing_gralic_prawn_2():
    # setting a global statement so other variabel can get updated aGPording to remove fucntion
    global total_cost_for_all_pizzas, length_GP2, GP_in_or_out_2
    allowed_to_checkout()
    gralic_prawns_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_GP2 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Gralic Prawn")
    show_topping_frame_GP2.destroy()
    # updating the in and out gralic prawns pizza
    GP_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove foe gralic prawns
def removing_gralic_prawn_3():
    # setting a global statement so other variabel can get updated aGPording to remove fucntion
    global total_cost_for_all_pizzas, length_GP3, GP_in_or_out_3
    allowed_to_checkout()
    gralic_prawns_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_GP3) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Gralic Prawn")
    show_topping_frame_GP3.destroy()
    # updating the in and out gralic prawns pizza
    GP_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove foe gralic prawns
def removing_gralic_prawn_4():
    # setting a global statement so other variabel can get updated aGPording to remove fucntion
    global total_cost_for_all_pizzas, length_GP4, GP_in_or_out_4
    allowed_to_checkout()
    gralic_prawns_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_GP4 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Gralic Prawn")
    show_topping_frame_GP4.destroy()
    # updating the in and out gralic prawns pizza
    GP_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove foe gralic prawns
def removing_gralic_prawn_5():
    # setting a global statement so other variabel can get updated aGPording to remove fucntion
    global total_cost_for_all_pizzas, length_GP5, GP_in_or_out_5
    allowed_to_checkout()
    gralic_prawns_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_GP5) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Gralic Prawn")
    show_topping_frame_GP5.destroy()
    # updating the in and out gralic prawns pizza
    GP_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types oe gralic prawns get add iwht it toppings
def adding_gralic_prawns_1():
    # setting a global variable so it can be updated and alos can be aGPesded outsidr os this function to be updated
    global gralic_prawns_1, total_cost_for_all_pizzas,show_topping_frame_GP1, length_GP1, GP_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aGPurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_gralic_prawns_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_GP1 = len(expanding_pages.topping_gralic_prawns_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    gralic_prawns_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Gralice Prawn Resized order list.png", "Gralic\nPrawms", f"{((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50):.2f}", removing_gralic_prawn_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_GP1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_GP1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_GP1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_GP1, text = "Gralic Prawn", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_GP1, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_GP1 in expanding_pages.topping_gralic_prawns_list:
            Label(show_topping_name_frame, text = topping_GP1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_GP1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_GP1, text = f"${13.50 + len(expanding_pages.topping_gralic_prawns_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_GP(e):
        show_topping_frame_GP1.place(x = 440, y= 40)
    def hide_topping_GP(e):
        show_topping_frame_GP1.place_forget()

    gralic_prawns_1.order_pizza_frame.bind('<Enter>', show_topping_GP)
    gralic_prawns_1.order_pizza_frame.bind("<Leave>", hide_topping_GP)

    # updating the in and out gralic prawns pizza
    GP_in_or_out_1 = 1



# This where all types oe gralic prawns get add iwht it toppings
def adding_gralic_prawns_2():
    # setting a global variable so it can be updated and alos can be aGPesded outsidr os this function to be updated
    global gralic_prawns_2, total_cost_for_all_pizzas, show_topping_frame_GP2, length_GP2, GP_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aGPurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_gralic_prawns_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_GP2 = len(expanding_pages.topping_gralic_prawns_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    gralic_prawns_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Gralice Prawn Resized order list.png", "Gralic\nPrawms", f"{((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50):.2f}", removing_gralic_prawn_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_GP2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_GP2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_GP2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_GP2, text = "Gralic Prawn", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_GP2, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_GP2 in expanding_pages.topping_gralic_prawns_list:
            Label(show_topping_name_frame, text = topping_GP2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_GP2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_GP2, text = f"${13.50 + len(expanding_pages.topping_gralic_prawns_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_GP(e):
        show_topping_frame_GP2.place(x = 440, y= 40)
    def hide_topping_GP(e):
        show_topping_frame_GP2.place_forget()

    gralic_prawns_2.order_pizza_frame.bind('<Enter>', show_topping_GP)
    gralic_prawns_2.order_pizza_frame.bind("<Leave>", hide_topping_GP)

    # updating the in and out gralic prawns pizza
    GP_in_or_out_2 = 1




# This where all types oe gralic prawns get add iwht it toppings
def adding_gralic_prawns_3():
    # setting a global variable so it can be updated and alos can be aGPesded outsidr os this function to be updated
    global gralic_prawns_3, total_cost_for_all_pizzas, show_topping_frame_GP3, length_GP3, GP_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aGPurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_gralic_prawns_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_GP3 = len(expanding_pages.topping_gralic_prawns_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    gralic_prawns_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Gralice Prawn Resized order list.png", "Gralic\nPrawms", f"{((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50):.2f}", removing_gralic_prawn_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_GP3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_GP3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_GP3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_GP3, text = "Gralic Prawn", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_GP3, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_GP3 in expanding_pages.topping_gralic_prawns_list:
            Label(show_topping_name_frame, text = topping_GP3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_GP3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_GP3, text = f"${13.50 + len(expanding_pages.topping_gralic_prawns_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_GP(e):
        show_topping_frame_GP3.place(x = 440, y= 40)
    def hide_topping_GP(e):
        show_topping_frame_GP3.place_forget()

    gralic_prawns_3.order_pizza_frame.bind('<Enter>', show_topping_GP)
    gralic_prawns_3.order_pizza_frame.bind("<Leave>", hide_topping_GP)

    # updating the in and out gralic prawns pizza
    GP_in_or_out_3 = 1



# This where all types oe gralic prawns get add iwht it toppings
def adding_gralic_prawns_4():
    # setting a global variable so it can be updated and alos can be aGPesded outsidr os this function to be updated
    global gralic_prawns_4, total_cost_for_all_pizzas, show_topping_frame_GP4, length_GP4, GP_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aGPurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_gralic_prawns_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_GP4 = len(expanding_pages.topping_gralic_prawns_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    gralic_prawns_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Gralice Prawn Resized order list.png", "Gralic\nPrawms", f"{((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50):.2f}", removing_gralic_prawn_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_GP4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_GP4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_GP4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_GP4, text = "Gralic Prawn", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_GP4, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_GP4 in expanding_pages.topping_gralic_prawns_list:
            Label(show_topping_name_frame, text = topping_GP4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_GP4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_GP4, text = f"${13.50 + len(expanding_pages.topping_gralic_prawns_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_GP(e):
        show_topping_frame_GP4.place(x = 440, y= 40)
    def hide_topping_GP(e):
        show_topping_frame_GP4.place_forget()

    gralic_prawns_4.order_pizza_frame.bind('<Enter>', show_topping_GP)
    gralic_prawns_4.order_pizza_frame.bind("<Leave>", hide_topping_GP)

    # updating the in and out gralic prawns pizza
    GP_in_or_out_4 = 1


# This where all types oe gralic prawns get add iwht it toppings
def adding_gralic_prawns_5():
    # setting a global variable so it can be updated and alos can be aGPesded outsidr os this function to be updated
    global gralic_prawns_5, total_cost_for_all_pizzas, show_topping_frame_GP5, length_GP5, GP_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aGPurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_gralic_prawns_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)
    if len(expanding_pages.topping_gralic_prawns_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_gralic_prawns_list[0])
        expanding_pages.topping_gralic_prawns_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_GP5 = len(expanding_pages.topping_gralic_prawns_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    gralic_prawns_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Gralice Prawn Resized order list.png", "Gralic\nPrawms", f"{((len(expanding_pages.topping_gralic_prawns_list) * 0.50) + 13.50):.2f}", removing_gralic_prawn_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_GP5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_GP5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_GP5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_GP5, text = "Gralic Prawn", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_GP5, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_GP5 in expanding_pages.topping_gralic_prawns_list:
            Label(show_topping_name_frame, text = topping_GP5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_GP5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_GP5, text = f"${13.50 + len(expanding_pages.topping_gralic_prawns_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_GP(e):
        show_topping_frame_GP5.place(x = 440, y= 40)
    def hide_topping_GP(e):
        show_topping_frame_GP5.place_forget()

    gralic_prawns_5.order_pizza_frame.bind('<Enter>', show_topping_GP)
    gralic_prawns_5.order_pizza_frame.bind("<Leave>", hide_topping_GP)

    # updating the in and out gralic prawns pizza
    GP_in_or_out_5 = 1



# This take of the gralic prawns adding in the order list
def gralic_prawns_add_order():
    global overall_GP_counter, GP_in_or_out_1, GP_in_or_out_2, GP_in_or_out_3, GP_in_or_out_4, GP_in_or_out_5

    # Telling the the counter thae gralic prawns has been added or display a number
    # This part add a number overall_GP_counter when the gralic prawns add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Gralic Prawn")

    if GP_in_or_out_1 == 2:
        GP_in_or_out_1 = 0
        overall_GP_counter = 1

    elif GP_in_or_out_2 == 2:
        GP_in_or_out_2 = 0
        overall_GP_counter = 2

    elif GP_in_or_out_3 == 2:
        GP_in_or_out_3 = 0
        overall_GP_counter = 3

    elif GP_in_or_out_4 == 2:
        GP_in_or_out_4 = 0
        overall_GP_counter = 4

    elif GP_in_or_out_5 == 2:
        GP_in_or_out_5 = 0
        overall_GP_counter = 5



    if overall_GP_counter == 1:
        if GP_in_or_out_1 == 0:
            adding_gralic_prawns_1()



    elif overall_GP_counter == 2:
        if GP_in_or_out_2 == 0:
            adding_gralic_prawns_2()


    elif overall_GP_counter == 3:
        if GP_in_or_out_3 == 0:
            adding_gralic_prawns_3()


    elif overall_GP_counter== 4:
        if GP_in_or_out_4 == 0:
            adding_gralic_prawns_4()


    elif overall_GP_counter == 5:
        overall_GP_counter = 0
        if GP_in_or_out_5 == 0:
            adding_gralic_prawns_5()



    # This the counter for all five gralic prawns pizza
    overall_GP_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_topping_gralic_prawns()
    Warning_message_box.add()




# MML means the Mega MeatLover, and all the adding for Mega MeatLover
# This all for Mega MeatLover pizza
# This ie Mega MeatLover counter so everytime the button is clicked oe Mega MeatLover it updates
global overall_MML_counter
overall_MML_counter = 1


global MML_in_or_out_1, MML_in_or_out_2, MML_in_or_out_3, MML_in_or_out_4, MML_in_or_out_5
# 0 means a Mega MeatLover pizza is not in the order list whereas one measn the pizza is in the list
MML_in_or_out_1 = 0
MML_in_or_out_2 = 0
MML_in_or_out_3 = 0
MML_in_or_out_4 = 0
MML_in_or_out_5 = 0



# This where everything get remove foe Mega MeatLover
def removing_mega_meatlover_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_MML1, MML_in_or_out_1
    allowed_to_checkout()
    mega_meatlover_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_MML1) * 0.50 + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mega MeatLover")
    show_topping_frame_MML1.destroy()
    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove foe Mega MeatLover
def removing_mega_meatlover_2():
    # setting a global statement so other variabel can get updated aMMLording to remove fucntion
    global total_cost_for_all_pizzas, length_MML2, MML_in_or_out_2
    allowed_to_checkout()
    mega_meatlover_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_MML2 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mega MeatLover")
    show_topping_frame_MML2.destroy()
    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove foe Mega MeatLover
def removing_mega_meatlover_3():
    # setting a global statement so other variabel can get updated aMMLording to remove fucntion
    global total_cost_for_all_pizzas, length_MML3, MML_in_or_out_3
    allowed_to_checkout()
    mega_meatlover_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_MML3) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mega MeatLover")
    show_topping_frame_MML3.destroy()
    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove foe Mega MeatLover
def removing_mega_meatlover_4():
    # setting a global statement so other variabel can get updated aMMLording to remove fucntion
    global total_cost_for_all_pizzas, length_MML4, MML_in_or_out_4
    allowed_to_checkout()
    mega_meatlover_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_MML4 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mega MeatLover")
    show_topping_frame_MML4.destroy()
    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove foe Mega MeatLover
def removing_mega_meatlover_5():
    # setting a global statement so other variabel can get updated aMMLording to remove fucntion
    global total_cost_for_all_pizzas, length_MML5, MML_in_or_out_5
    allowed_to_checkout()
    mega_meatlover_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_MML5) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Mega MeatLover")
    show_topping_frame_MML5.destroy()
    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types oe Mega MeatLover get add iwht it toppings
def adding_mega_meatlover_1():
    # setting a global variable so it can be updated and alos can be aMMLesded outsidr os this function to be updated
    global mega_meatlover_1, total_cost_for_all_pizzas,show_topping_frame_MML1, length_MML1, MML_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aMMLurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mega_meatlover_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MML1 = len(expanding_pages.topping_mega_meatlover_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mega_meatlover_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mega MeatLover Resized order list.png", "Mega\nMeatLover", f"{((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50):.2f}", removing_mega_meatlover_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MML1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MML1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MML1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MML1, text = "Mega MeatLover", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MML1, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_MML1 in expanding_pages.topping_mega_meatlover_list:
            Label(show_topping_name_frame, text = topping_MML1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MML1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MML1, text = f"${13.50 + len(expanding_pages.topping_mega_meatlover_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_MML(e):
        show_topping_frame_MML1.place(x = 440, y= 40)
    def hide_topping_MML(e):
        show_topping_frame_MML1.place_forget()

    mega_meatlover_1.order_pizza_frame.bind('<Enter>', show_topping_MML)
    mega_meatlover_1.order_pizza_frame.bind("<Leave>", hide_topping_MML)

    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_1 = 1



# This where all types oe Mega MeatLover get add iwht it toppings
def adding_mega_meatlover_2():
    # setting a global variable so it can be updated and alos can be aMMLesded outsidr os this function to be updated
    global mega_meatlover_2, total_cost_for_all_pizzas, show_topping_frame_MML2, length_MML2, MML_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aMMLurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mega_meatlover_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MML2 = len(expanding_pages.topping_mega_meatlover_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mega_meatlover_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mega MeatLover Resized order list.png", "Mega\nMeatLover", f"{((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50):.2f}", removing_mega_meatlover_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MML2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MML2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MML2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MML2, text = "Mega MeatLover", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MML2, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_MML2 in expanding_pages.topping_mega_meatlover_list:
            Label(show_topping_name_frame, text = topping_MML2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MML2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MML2, text = f"${13.50 + len(expanding_pages.topping_mega_meatlover_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_MML(e):
        show_topping_frame_MML2.place(x = 440, y= 40)
    def hide_topping_MML(e):
        show_topping_frame_MML2.place_forget()

    mega_meatlover_2.order_pizza_frame.bind('<Enter>', show_topping_MML)
    mega_meatlover_2.order_pizza_frame.bind("<Leave>", hide_topping_MML)

    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_2 = 1




# This where all types oe Mega MeatLover get add iwht it toppings
def adding_mega_meatlover_3():
    # setting a global variable so it can be updated and alos can be aMMLesded outsidr os this function to be updated
    global mega_meatlover_3, total_cost_for_all_pizzas, show_topping_frame_MML3, length_MML3, MML_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aMMLurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mega_meatlover_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MML3 = len(expanding_pages.topping_mega_meatlover_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mega_meatlover_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mega MeatLover Resized order list.png", "Mega\nMeatLover", f"{((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50):.2f}", removing_mega_meatlover_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MML3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MML3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MML3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MML3, text = "Mega MeatLover", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MML3, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_MML3 in expanding_pages.topping_mega_meatlover_list:
            Label(show_topping_name_frame, text = topping_MML3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MML3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MML3, text = f"${13.50 + len(expanding_pages.topping_mega_meatlover_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_MML(e):
        show_topping_frame_MML3.place(x = 440, y= 40)
    def hide_topping_MML(e):
        show_topping_frame_MML3.place_forget()

    mega_meatlover_3.order_pizza_frame.bind('<Enter>', show_topping_MML)
    mega_meatlover_3.order_pizza_frame.bind("<Leave>", hide_topping_MML)

    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_3 = 1



# This where all types oe Mega MeatLover get add iwht it toppings
def adding_mega_meatlover_4():
    # setting a global variable so it can be updated and alos can be aMMLesded outsidr os this function to be updated
    global mega_meatlover_4, total_cost_for_all_pizzas, show_topping_frame_MML4, length_MML4, MML_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aMMLurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mega_meatlover_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MML4 = len(expanding_pages.topping_mega_meatlover_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mega_meatlover_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mega MeatLover Resized order list.png", "Mega\nMeatLover", f"{((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50):.2f}", removing_mega_meatlover_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MML4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MML4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MML4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MML4, text = "Mega MeatLover", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MML4, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_MML4 in expanding_pages.topping_mega_meatlover_list:
            Label(show_topping_name_frame, text = topping_MML4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MML4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MML4, text = f"${13.50 + len(expanding_pages.topping_mega_meatlover_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_MML(e):
        show_topping_frame_MML4.place(x = 440, y= 40)
    def hide_topping_MML(e):
        show_topping_frame_MML4.place_forget()

    mega_meatlover_4.order_pizza_frame.bind('<Enter>', show_topping_MML)
    mega_meatlover_4.order_pizza_frame.bind("<Leave>", hide_topping_MML)

    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_4 = 1


# This where all types oe Mega MeatLover get add iwht it toppings
def adding_mega_meatlover_5():
    # setting a global variable so it can be updated and alos can be aMMLesded outsidr os this function to be updated
    global mega_meatlover_5, total_cost_for_all_pizzas, show_topping_frame_MML5, length_MML5, MML_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aMMLurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_mega_meatlover_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)
    if len(expanding_pages.topping_mega_meatlover_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_mega_meatlover_list[0])
        expanding_pages.topping_mega_meatlover_list.pop(0)

    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_MML5 = len(expanding_pages.topping_mega_meatlover_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    mega_meatlover_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mega MeatLover Resized order list.png", "Mega\nMeatLover", f"{((len(expanding_pages.topping_mega_meatlover_list) * 0.50) + 13.50):.2f}", removing_mega_meatlover_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_MML5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_MML5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_MML5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_MML5, text = "Mega MeatLover", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_MML5, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_MML5 in expanding_pages.topping_mega_meatlover_list:
            Label(show_topping_name_frame, text = topping_MML5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_MML5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_MML5, text = f"${13.50 + len(expanding_pages.topping_mega_meatlover_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_MML(e):
        show_topping_frame_MML5.place(x = 440, y= 40)
    def hide_topping_MML(e):
        show_topping_frame_MML5.place_forget()

    mega_meatlover_5.order_pizza_frame.bind('<Enter>', show_topping_MML)
    mega_meatlover_5.order_pizza_frame.bind("<Leave>", hide_topping_MML)

    # updating the in and out Mega MeatLover pizza
    MML_in_or_out_5 = 1



# This take of the Mega MeatLover adding in the order list
def mega_meatlover_add_order():
    global overall_MML_counter, MML_in_or_out_1, MML_in_or_out_2, MML_in_or_out_3, MML_in_or_out_4, MML_in_or_out_5

    # Telling the the counter thae Mega MeatLover has been added or display a number
    # This part add a number overall_MML_counter when the Mega MeatLover add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Mega MeatLover")

    if MML_in_or_out_1 == 2:
        MML_in_or_out_1 = 0
        overall_MML_counter = 1

    elif MML_in_or_out_2 == 2:
        MML_in_or_out_2 = 0
        overall_MML_counter = 2

    elif MML_in_or_out_3 == 2:
        MML_in_or_out_3 = 0
        overall_MML_counter = 3

    elif MML_in_or_out_4 == 2:
        MML_in_or_out_4 = 0
        overall_MML_counter = 4

    elif MML_in_or_out_5 == 2:
        MML_in_or_out_5 = 0
        overall_MML_counter = 5



    if overall_MML_counter == 1:
        if MML_in_or_out_1 == 0:
            adding_mega_meatlover_1()



    elif overall_MML_counter == 2:
        if MML_in_or_out_2 == 0:
            adding_mega_meatlover_2()


    elif overall_MML_counter == 3:
        if MML_in_or_out_3 == 0:
            adding_mega_meatlover_3()


    elif overall_MML_counter== 4:
        if MML_in_or_out_4 == 0:
            adding_mega_meatlover_4()


    elif overall_MML_counter == 5:
        overall_MML_counter = 0
        if MML_in_or_out_5 == 0:
            adding_mega_meatlover_5()



    # This the counter for all five Mega MeatLover pizza
    overall_MML_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_topping_mega_meatlover()
    Warning_message_box.add()


# PPC means the Peri Peri Chicken, and all the adding for Peri Peri Chicken
# This all for Peri peri chicken pizza
# This ie Peri peri chicken counter so everytime the button is clicked oe Peri peri chicken it updates
global overall_PPC_counter
overall_PPC_counter = 1


global PPC_in_or_out_1, PPC_in_or_out_2, PPC_in_or_out_3, PPC_in_or_out_4, PPC_in_or_out_5
# 0 means a Peri peri chicken pizza is not in the order list whereas one measn the pizza is in the list
PPC_in_or_out_1 = 0
PPC_in_or_out_2 = 0
PPC_in_or_out_3 = 0
PPC_in_or_out_4 = 0
PPC_in_or_out_5 = 0



# This where everything get remove foe Peri peri chicken
def removing_peri_peri_chicken_1():
    # setting a global statement so other variabel can get updated according to remove fucntion
    global total_cost_for_all_pizzas, length_PPC1, PPC_in_or_out_1
    allowed_to_checkout()
    peri_peri_chicken_1.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= (length_PPC1) * 0.50 + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Peri Peri Chicken")
    show_topping_frame_PPC1.destroy()
    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_1 = 2
    Warning_message_box.add()

# This where everything get remove foe Peri peri chicken
def removing_peri_peri_chicken_2():
    # setting a global statement so other variabel can get updated aPPCording to remove fucntion
    global total_cost_for_all_pizzas, length_PPC2, PPC_in_or_out_2
    allowed_to_checkout()
    peri_peri_chicken_2.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_PPC2 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Peri Peri Chicken")
    show_topping_frame_PPC2.destroy()
    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_2 = 2
    Warning_message_box.add()


# This where everything get remove foe Peri peri chicken
def removing_peri_peri_chicken_3():
    # setting a global statement so other variabel can get updated aPPCording to remove fucntion
    global total_cost_for_all_pizzas, length_PPC3, PPC_in_or_out_3
    allowed_to_checkout()
    peri_peri_chicken_3.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_PPC3) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Peri Peri Chicken")
    show_topping_frame_PPC3.destroy()
    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_3 = 2
    Warning_message_box.add()


# This where everything get remove foe Peri peri chicken
def removing_peri_peri_chicken_4():
    # setting a global statement so other variabel can get updated aPPCording to remove fucntion
    global total_cost_for_all_pizzas, length_PPC4, PPC_in_or_out_4
    allowed_to_checkout()
    peri_peri_chicken_4.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_PPC4 * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Peri Peri Chicken")
    show_topping_frame_PPC4.destroy()
    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_4 = 2
    Warning_message_box.add()


# This where everything get remove foe Peri peri chicken
def removing_peri_peri_chicken_5():
    # setting a global statement so other variabel can get updated aPPCording to remove fucntion
    global total_cost_for_all_pizzas, length_PPC5, PPC_in_or_out_5
    allowed_to_checkout()
    peri_peri_chicken_5.order_pizza_frame.destroy()
    total_cost_for_all_pizzas -= ((length_PPC5) * 0.50) + 13.50
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    Warning_message_box.storing_pizzas.remove("Peri Peri Chicken")
    show_topping_frame_PPC5.destroy()
    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_5 = 2
    Warning_message_box.add()


# This where all types oe Peri peri chicken get add iwht it toppings
def adding_peri_peri_chicken_1():
    # setting a global variable so it can be updated and alos can be aPPCesded outsidr os this function to be updated
    global peri_peri_chicken_1, total_cost_for_all_pizzas,show_topping_frame_PPC1, length_PPC1, PPC_in_or_out_1, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aPPCurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_peri_peri_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)


    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_PPC1 = len(expanding_pages.topping_peri_peri_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0,total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    peri_peri_chicken_1 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Peri_Peri_chicken Resized order list.png", "Peri Peri\nChicken", f"{((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50):.2f}", removing_peri_peri_chicken_1)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_PPC1 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_PPC1, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_PPC1, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_PPC1, text = "Peri Peri Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_PPC1, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_PPC1 in expanding_pages.topping_peri_peri_chicken_list:
            Label(show_topping_name_frame, text = topping_PPC1, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiBold", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_PPC1, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_PPC1, text = f"${13.50 + len(expanding_pages.topping_peri_peri_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_PPC(e):
        show_topping_frame_PPC1.place(x = 440, y= 40)
    def hide_topping_PPC(e):
        show_topping_frame_PPC1.place_forget()

    peri_peri_chicken_1.order_pizza_frame.bind('<Enter>', show_topping_PPC)
    peri_peri_chicken_1.order_pizza_frame.bind("<Leave>", hide_topping_PPC)

    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_1 = 1



# This where all types oe Peri peri chicken get add iwht it toppings
def adding_peri_peri_chicken_2():
    # setting a global variable so it can be updated and alos can be aPPCesded outsidr os this function to be updated
    global peri_peri_chicken_2, total_cost_for_all_pizzas, show_topping_frame_PPC2, length_PPC2, PPC_in_or_out_2, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aPPCurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_peri_peri_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)


    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_PPC2 = len(expanding_pages.topping_peri_peri_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    peri_peri_chicken_2 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Peri_Peri_chicken Resized order list.png", "Peri Peri\nChicken", f"{((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50):.2f}", removing_peri_peri_chicken_2)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_PPC2 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_PPC2, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_PPC2, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_PPC2, text = "Peri Peri Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_PPC2, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_PPC2 in expanding_pages.topping_peri_peri_chicken_list:
            Label(show_topping_name_frame, text = topping_PPC2, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_PPC2, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_PPC2, text = f"${13.50 + len(expanding_pages.topping_peri_peri_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_PPC(e):
        show_topping_frame_PPC2.place(x = 440, y= 40)
    def hide_topping_PPC(e):
        show_topping_frame_PPC2.place_forget()

    peri_peri_chicken_2.order_pizza_frame.bind('<Enter>', show_topping_PPC)
    peri_peri_chicken_2.order_pizza_frame.bind("<Leave>", hide_topping_PPC)

    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_2 = 1




# This where all types oe Peri peri chicken get add iwht it toppings
def adding_peri_peri_chicken_3():
    # setting a global variable so it can be updated and alos can be aPPCesded outsidr os this function to be updated
    global peri_peri_chicken_3, total_cost_for_all_pizzas, show_topping_frame_PPC3, length_PPC3, PPC_in_or_out_3, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aPPCurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_peri_peri_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)


    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_PPC3 = len(expanding_pages.topping_peri_peri_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    peri_peri_chicken_3 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Peri_Peri_chicken Resized order list.png", "Peri Peri\nChicken", f"{((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50):.2f}", removing_peri_peri_chicken_3)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_PPC3 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_PPC3, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_PPC3, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_PPC3, text = "Peri Peri Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_PPC3, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_PPC3 in expanding_pages.topping_peri_peri_chicken_list:
            Label(show_topping_name_frame, text = topping_PPC3, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_PPC3, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_PPC3, text = f"${13.50 + len(expanding_pages.topping_peri_peri_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_PPC(e):
        show_topping_frame_PPC3.place(x = 440, y= 40)
    def hide_topping_PPC(e):
        show_topping_frame_PPC3.place_forget()

    peri_peri_chicken_3.order_pizza_frame.bind('<Enter>', show_topping_PPC)
    peri_peri_chicken_3.order_pizza_frame.bind("<Leave>", hide_topping_PPC)

    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_3 = 1



# This where all types oe Peri peri chicken get add iwht it toppings
def adding_peri_peri_chicken_4():
    # setting a global variable so it can be updated and alos can be aPPCesded outsidr os this function to be updated
    global peri_peri_chicken_4, total_cost_for_all_pizzas, show_topping_frame_PPC4, length_PPC4, PPC_in_or_out_4, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aPPCurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_peri_peri_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)


    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_PPC4 = len(expanding_pages.topping_peri_peri_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    peri_peri_chicken_4 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Peri_Peri_chicken Resized order list.png", "Peri Peri\nChicken", f"{((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50):.2f}", removing_peri_peri_chicken_4)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_PPC4 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_PPC4, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_PPC4, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_PPC4, text = "Peri Peri Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_PPC4, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_PPC4 in expanding_pages.topping_peri_peri_chicken_list:
            Label(show_topping_name_frame, text = topping_PPC4, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_PPC4, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_PPC4, text = f"${13.50 + len(expanding_pages.topping_peri_peri_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of a certain when the cursor hover that specific pizza.
    def show_topping_PPC(e):
        show_topping_frame_PPC4.place(x = 440, y= 40)
    def hide_topping_PPC(e):
        show_topping_frame_PPC4.place_forget()

    peri_peri_chicken_4.order_pizza_frame.bind('<Enter>', show_topping_PPC)
    peri_peri_chicken_4.order_pizza_frame.bind("<Leave>", hide_topping_PPC)

    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_4 = 1


# This where all types oe Peri peri chicken get add iwht it toppings
def adding_peri_peri_chicken_5():
    # setting a global variable so it can be updated and alos can be aPPCesded outsidr os this function to be updated
    global peri_peri_chicken_5, total_cost_for_all_pizzas, show_topping_frame_PPC5, length_PPC5, PPC_in_or_out_5, total_cost_list

    # Heer is list that is collect all the topping that should not have charge and then displays them displays them separatlally. The topping that don't have charge they al get remove from the main list as they would give the aPPCurate price.
    no_charge_topping_list_length = len(expanding_pages.topping_peri_peri_chicken_list)
    no_charge_topping_list = []
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)
    if len(expanding_pages.topping_peri_peri_chicken_list) >= 1:
        no_charge_topping_list.append(expanding_pages.topping_peri_peri_chicken_list[0])
        expanding_pages.topping_peri_peri_chicken_list.pop(0)


    # All the cost that is added after the a option has been chosen from the delivery and pickup
    length_PPC5 = len(expanding_pages.topping_peri_peri_chicken_list)
    total_cost_for_all_pizzas += ((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50)
    total_cost_list.pop(0)
    total_cost_list.insert(0, total_cost_for_all_pizzas)
    Delivery_or_pickup.total_label.configure(text=f"Total Cost: ${sum(total_cost_list):.2f}")
    peri_peri_chicken_5 = Order_pizza_list(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Peri_Peri_chicken Resized order list.png", "Peri Peri\nChicken", f"{((len(expanding_pages.topping_peri_peri_chicken_list) * 0.50) + 13.50):.2f}", removing_peri_peri_chicken_5)

    # Display the toppings when teh user entre that specific pizza
    show_topping_frame_PPC5 = customtkinter.CTkFrame(Intro_Frames.order_list_frame, fg_color='white', bg_color= '#F2F2F2', corner_radius= 20)
    show_topping_name_frame = customtkinter.CTkFrame(show_topping_frame_PPC5, fg_color='white', border=0)
    show_topping_name_frame.grid(row=1, column=0, sticky='w')
    show_topping_price_frame = customtkinter.CTkFrame(show_topping_frame_PPC5, fg_color='white', border=0)
    show_topping_price_frame.grid(row=1, column=1, padx=(10,5))
    pizza_name_display = Label(show_topping_frame_PPC5, text = "Peri Peri Chicken", background='white', font=("Bahnschrift SemiBold", 12), border=0, pady = 5, padx=22, foreground='black')
    pizza_name_display.grid(column=0, row=0, sticky='nw')
    pizza_price_display = customtkinter.CTkLabel(show_topping_frame_PPC5, text = "$13.50", text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=30, fg_color='white', text_color='black')
    pizza_price_display.grid(row= 0, column=1, padx=(10,5), pady=5)
    # This parts count the topping for specific pizza and displays them it price.
    count_topping = 1
    if no_charge_topping_list_length == 0:
        show_topping_name_frame.grid_forget()
        show_topping_price_frame.grid_forget()
    else:
        for no_charge_topping in no_charge_topping_list:
            Label(show_topping_name_frame, text = no_charge_topping, background='white', font=("Bahnschrift SemiLight", 8),border=0, foreground='black').grid(row=count_topping, column=0, sticky='w', padx=(32, 10))
            Label(show_topping_price_frame, text='AWT', background='white', font=("Bahnschrift SemiBold", 8), border=0,foreground='black').grid(row=count_topping, column=1, padx=0, sticky='s', pady=0)
            count_topping += 1
        for topping_PPC5 in expanding_pages.topping_peri_peri_chicken_list:
            Label(show_topping_name_frame, text = topping_PPC5, background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black' ).grid(row = count_topping, column = 0, sticky='w', padx= (32,10))
            Label(show_topping_price_frame, text='$0.50', background='white', font=("Bahnschrift SemiLight", 8), border=0, foreground='black').grid(row=count_topping, column= 1, padx= 0, sticky='s', pady=0)
            count_topping += 1
    total_price_name_this_pizza = customtkinter.CTkLabel(show_topping_frame_PPC5, text = "Total Price:", fg_color='white', text_font=("Bahnschrift SemiBold", 12), corner_radius=20, width=5, text_color='black')
    total_price_name_this_pizza.grid(row=2, padx= (14,10), pady=(5,0), sticky='w', column=0)
    total_price_this_pizza = Label(show_topping_frame_PPC5, text = f"${13.50 + len(expanding_pages.topping_peri_peri_chicken_list)*0.50:.2f}", background='white', font=("Bahnschrift SemiBold", 12), border=0, width=10, foreground='black')
    total_price_this_pizza.grid(row=2, pady=(5,0), sticky='s', column=1)

    # This parts shows the topping of acertain when the cursor hover that specific pizza.
    def show_topping_PPC(e):
        show_topping_frame_PPC5.place(x = 440, y= 40)
    def hide_topping_PPC(e):
        show_topping_frame_PPC5.place_forget()

    peri_peri_chicken_5.order_pizza_frame.bind('<Enter>', show_topping_PPC)
    peri_peri_chicken_5.order_pizza_frame.bind("<Leave>", hide_topping_PPC)

    # updating the in and out Peri peri chicken pizza
    PPC_in_or_out_5 = 1



# This take of the Peri peri chicken adding in the order list
def peri_peri_chicken_add_order():
    global overall_PPC_counter, PPC_in_or_out_1, PPC_in_or_out_2, PPC_in_or_out_3, PPC_in_or_out_4, PPC_in_or_out_5

    # Telling the the counter thae Peri peri chicken has been added or display a number
    # This part add a number overall_PPC_counter when the Peri peri chicken add to cart button is clicked. Acorrding to the number the this function runs that sepcific function.
    Warning_message_box.storing_pizzas.append("Peri Peri Chicken")

    if PPC_in_or_out_1 == 2:
        PPC_in_or_out_1 = 0
        overall_PPC_counter = 1

    elif PPC_in_or_out_2 == 2:
        PPC_in_or_out_2 = 0
        overall_PPC_counter = 2

    elif PPC_in_or_out_3 == 2:
        PPC_in_or_out_3 = 0
        overall_PPC_counter = 3

    elif PPC_in_or_out_4 == 2:
        PPC_in_or_out_4 = 0
        overall_PPC_counter = 4

    elif PPC_in_or_out_5 == 2:
        PPC_in_or_out_5 = 0
        overall_PPC_counter = 5



    if overall_PPC_counter == 1:
        if PPC_in_or_out_1 == 0:
            adding_peri_peri_chicken_1()



    elif overall_PPC_counter == 2:
        if PPC_in_or_out_2 == 0:
            adding_peri_peri_chicken_2()


    elif overall_PPC_counter == 3:
        if PPC_in_or_out_3 == 0:
            adding_peri_peri_chicken_3()


    elif overall_PPC_counter== 4:
        if PPC_in_or_out_4 == 0:
            adding_peri_peri_chicken_4()


    elif overall_PPC_counter == 5:
        overall_PPC_counter = 0
        if PPC_in_or_out_5 == 0:
            adding_peri_peri_chicken_5()



    # This the counter for all five Peri peri chicken pizza
    overall_PPC_counter += 1


    # Running the delete topping function as it abl clear everything before any things blocked with avoids an error in the system
    expanding_pages.delete_topping_peri_peri_chicken()
    Warning_message_box.add()



# All the Moduels
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import Henderson_Pizza_Palace_Tkinter
import Menu_item


# Regular Range
# American Pepperion Animation
def hover_on_american_pepperion(e):
    different_picture_america_pepperion = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\American Pepperion zommed.png")
    Menu_item.american_pepperion_menu.packing_pizza_image.config(image=different_picture_america_pepperion)
    Menu_item.american_pepperion_menu.packing_pizza_image.image = different_picture_america_pepperion


def hover_off_american_pepperion(e):
    back_to_normal_america_pepperion = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\AMERICAN PEPPERONI.jpg")
    Menu_item.american_pepperion_menu.packing_pizza_image.config(image=back_to_normal_america_pepperion)
    Menu_item.american_pepperion_menu.packing_pizza_image.image = back_to_normal_america_pepperion


# Chessy Gralic Animation
def hover_on_chessy_gralic(e):
    different_picture_chessy_gralic = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\chessy gralic pizza zoomed.png")
    Menu_item.cheesy_gralic_menu.packing_pizza_image.config(image=different_picture_chessy_gralic)
    Menu_item.cheesy_gralic_menu.packing_pizza_image.image = different_picture_chessy_gralic


def hover_off_chessy_gralic(e):
    back_to_normal_chessy_gralic = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\CHEESY GARLIC PIZZA.jpg")
    Menu_item.cheesy_gralic_menu.packing_pizza_image.config(image=back_to_normal_chessy_gralic)
    Menu_item.cheesy_gralic_menu.packing_pizza_image.image = back_to_normal_chessy_gralic


# Chicken Supreme Animation
def hover_on_chicken_supreme(e):
    different_picture_chicken_supreme = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\chicken supreme zoomed.png")
    Menu_item.chicken_supreme_menu.packing_pizza_image.config(image=different_picture_chicken_supreme)
    Menu_item.chicken_supreme_menu.packing_pizza_image.image = different_picture_chicken_supreme


def hover_off_chicken_supreme(e):
    back_to_normal_chicken_supreme = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\CHICKEN SUPREME.jpg")
    Menu_item.chicken_supreme_menu.packing_pizza_image.config(image=back_to_normal_chicken_supreme)
    Menu_item.chicken_supreme_menu.packing_pizza_image.image = back_to_normal_chicken_supreme


# Ham and cheese Animation
def hover_on_ham_and_cheese(e):
    different_picture_ham_and_cheese = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\hame and cheese zoomed.png")
    Menu_item.ham_and_cheese_menu.packing_pizza_image.config(image=different_picture_ham_and_cheese)
    Menu_item.ham_and_cheese_menu.packing_pizza_image.image = different_picture_ham_and_cheese


def hover_off_ham_and_cheese(e):
    back_to_normal_ham_and_cheese = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\HAM & CHEESE.jpg")
    Menu_item.ham_and_cheese_menu.packing_pizza_image.config(image=back_to_normal_ham_and_cheese)
    Menu_item.ham_and_cheese_menu.packing_pizza_image.image = back_to_normal_ham_and_cheese


# Mr Wedge Animation
def hover_on_mr_wedge(e):
    different_picture_mr_wedge = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\mr wedge zoomed.png")
    Menu_item.mr_wedge_menu.packing_pizza_image.config(image=different_picture_mr_wedge)
    Menu_item.mr_wedge_menu.packing_pizza_image.image = different_picture_mr_wedge


def hover_off_mr_wedge(e):
    back_to_normal_mr_wedge = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\MR WEDGE.jpg")
    Menu_item.mr_wedge_menu.packing_pizza_image.config(image=back_to_normal_mr_wedge)
    Menu_item.mr_wedge_menu.packing_pizza_image.image = back_to_normal_mr_wedge


# Pepperion Animation
def hover_on_pepperion(e):
    different_picture_pepperion = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Pepperoni zoomed.png")
    Menu_item.pepperion_menu.packing_pizza_image.config(image=different_picture_pepperion)
    Menu_item.pepperion_menu.packing_pizza_image.image = different_picture_pepperion


def hover_off_pepperion(e):
    back_to_normal_pepperion = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\PEPPERONI.jpg")
    Menu_item.pepperion_menu.packing_pizza_image.config(image=back_to_normal_pepperion)
    Menu_item.pepperion_menu.packing_pizza_image.image = back_to_normal_pepperion


# Simply Cheese Animation
def hover_on_simply_cheese(e):
    different_picture_simply_cheese = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Simpy cheese zoomed.png")
    Menu_item.simply_cheese_menu.packing_pizza_image.config(image=different_picture_simply_cheese)
    Menu_item.simply_cheese_menu.packing_pizza_image.image = different_picture_simply_cheese


def hover_off_simply_cheese(e):
    back_to_normal_simply_cheese = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\SIMPLY CHEESE.jpg")
    Menu_item.simply_cheese_menu.packing_pizza_image.config(image=back_to_normal_simply_cheese)
    Menu_item.simply_cheese_menu.packing_pizza_image.image = back_to_normal_simply_cheese


# Supreme Animation
def hover_on_supreme(e):
    different_picture_supreme = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\supreme zoomed.png")
    Menu_item.supreme_menu.packing_pizza_image.config(image=different_picture_supreme)
    Menu_item.supreme_menu.packing_pizza_image.image = different_picture_supreme


def hover_off_supreme(e):
    back_to_normal_supreme = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\SUPREME.jpg")
    Menu_item.supreme_menu.packing_pizza_image.config(image=back_to_normal_supreme)
    Menu_item.supreme_menu.packing_pizza_image.image = back_to_normal_supreme


# Gourmet Range
# Apricot chicken
def hover_on_apricot_chicken(e):
    different_picture_apricot_chicken = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\apricot zoomed.png")
    Menu_item.apricot_chicken_menu.packing_pizza_image.config(image=different_picture_apricot_chicken)
    Menu_item.apricot_chicken_menu.packing_pizza_image.image = different_picture_apricot_chicken


def hover_off_apricot_chicken(e):
    back_to_normal_apricot_chicken = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\APRICOT CHICKEN.jpg")
    Menu_item.apricot_chicken_menu.packing_pizza_image.config(image=back_to_normal_apricot_chicken)
    Menu_item.apricot_chicken_menu.packing_pizza_image.image = back_to_normal_apricot_chicken


# Chicken, Bacon and Aiolo Animation
def hover_on_chicken_bacon_aioli(e):
    different_picture_chicken_bacon_aioli = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken, Bacon and Aloli zoomed.png")
    Menu_item.chicken_bacon_aiol_menu.packing_pizza_image.config(image=different_picture_chicken_bacon_aioli)
    Menu_item.chicken_bacon_aiol_menu.packing_pizza_image.image = different_picture_chicken_bacon_aioli


def hover_off_chicken_bacon_aioli(e):
    back_to_normal_chicken_bacon_aioli = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\CHICKEN, BACON & AIOLI Pizza.jpg")
    Menu_item.chicken_bacon_aiol_menu.packing_pizza_image.config(image=back_to_normal_chicken_bacon_aioli)
    Menu_item.chicken_bacon_aiol_menu.packing_pizza_image.image = back_to_normal_chicken_bacon_aioli


# Chicken and cheese Animation
def hover_on_chicken_cheese(e):
    different_picture_chicken_cheese = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\chicken and cheese  zoomed.png")
    Menu_item.chicken_cheese_menu.packing_pizza_image.config(image=different_picture_chicken_cheese)
    Menu_item.chicken_cheese_menu.packing_pizza_image.image = different_picture_chicken_cheese


def hover_off_chicken_cheese(e):
    back_to_normal_chicken_cheese = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\CHICKEN & CAMEMBERT.jpg")
    Menu_item.chicken_cheese_menu.packing_pizza_image.config(image=back_to_normal_chicken_cheese)
    Menu_item.chicken_cheese_menu.packing_pizza_image.image = back_to_normal_chicken_cheese


# Gralic and Prawn Animation
def hover_on_gralic_prawn(e):
    different_picture_gralic_prawn = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\GARLIC PRAWN zoomed.png")
    Menu_item.gralic_prawn_menu.packing_pizza_image.config(image=different_picture_gralic_prawn)
    Menu_item.gralic_prawn_menu.packing_pizza_image.image = different_picture_gralic_prawn


def hover_off_gralic_prawn(e):
    back_to_normal_gralic_prawn = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\GARLIC PRAWN.jpg")
    Menu_item.gralic_prawn_menu.packing_pizza_image.config(image=back_to_normal_gralic_prawn)
    Menu_item.gralic_prawn_menu.packing_pizza_image.image = back_to_normal_gralic_prawn


# Mega meatlover Animation
def hover_on_mega_meatlover(e):
    different_picture_mega_meatlover = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\MEGA MEATLOVERS zoomed.png")
    Menu_item.mega_meatlover_menu.packing_pizza_image.config(image=different_picture_mega_meatlover)
    Menu_item.mega_meatlover_menu.packing_pizza_image.image = different_picture_mega_meatlover


def hover_off_mega_meatlover(e):
    back_to_normal_mega_meatlover = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\MEGA MEATLOVERS.jpg")
    Menu_item.mega_meatlover_menu.packing_pizza_image.config(image=back_to_normal_mega_meatlover)
    Menu_item.mega_meatlover_menu.packing_pizza_image.image = back_to_normal_mega_meatlover


# Peri-peri chicken Animation
def hover_on_peri_peri_chicken(e):
    different_picture_peri_peri_chicken = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\PERI-PERI CHICKEN zoomed.png")
    Menu_item.peri_peri_chicken_menu.packing_pizza_image.config(image=different_picture_peri_peri_chicken)
    Menu_item.peri_peri_chicken_menu.packing_pizza_image.image = different_picture_peri_peri_chicken

def hover_off_peri_peri_chicken(e):
    back_to_normal_peri_peri_chicken = ImageTk.PhotoImage(file=r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\PERI-PERI CHICKEN.jpg")
    Menu_item.peri_peri_chicken_menu.packing_pizza_image.config(image=back_to_normal_peri_peri_chicken)
    Menu_item.peri_peri_chicken_menu.packing_pizza_image.image = back_to_normal_peri_peri_chicken





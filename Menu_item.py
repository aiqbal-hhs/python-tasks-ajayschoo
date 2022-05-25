# All the Moduels
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import Henderson_Pizza_Palace_Tkinter
import Intro_Frames
import Animation_menu
import expanding_pages

# All the meun items detail
# Regular Range
# American Pepperion meun detail
american_pepperion_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\AMERICAN PEPPERONI.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\8.50add_button_image.png",0,0,100,50,"American Pepperoni".upper(),
"Loaded with double the amount",
"of your favourite Domino's",
"pepperoni!",expanding_pages.expanding_American_pepperion)
american_pepperion_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_american_pepperion)
american_pepperion_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_american_pepperion)


# Cheesy Gralic Pizza meun detail
cheesy_gralic_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\CHEESY GARLIC PIZZA.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\8.50add_button_image.png",0,1,100,50,"Cheesy Garlic Pizza".upper(),
"Mozzarella & garlic sauce on",
"a crème fraiche base topped ",
"with oregano",expanding_pages.expanding_cheesy_gralic_pizza)
cheesy_gralic_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_chessy_gralic)
cheesy_gralic_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_chessy_gralic)


# Chicken Supreme menu detail
chicken_supreme_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\CHICKEN SUPREME.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\8.50add_button_image.png",0,2,100,50,"CHICKEN SUPREME",
"Seasoned chicken, pineapple,",
"mushrooms,capsicum & sliced",
"red onions,topped with spring onions",expanding_pages.expanding_chicken_supreme)
chicken_supreme_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_chicken_supreme)
chicken_supreme_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_chicken_supreme)


# Ham and cheese menu detail
ham_and_cheese_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\HAM & CHEESE.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\8.50add_button_image.png",1,0,35,50,"HAM & CHEESE",
"",
"Smokey ham & mozzarella",
"",expanding_pages.expanding_ham_cheese)
ham_and_cheese_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_ham_and_cheese)
ham_and_cheese_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_ham_and_cheese)


# Mr wedge menu detail
mr_wedge_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\MR WEDGE.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\8.50add_button_image.png",1,1,35,50,"MR WEDGE",
"Potato wedges, smokey Manukaham,",
"red onion & oregano on a BBQ",
" & garlic sauce base topped…",expanding_pages.expanding_mr_wedge)
mr_wedge_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_mr_wedge)
mr_wedge_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_mr_wedge)


# Pepperion menu detail
pepperion_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\PEPPERONI.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\8.50add_button_image.png",1,2,35,50,"PEPPERONI",
"",
"Lots of pepperoni & mozzarella",
"",expanding_pages.expanding_pepperion)
pepperion_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_pepperion)
pepperion_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_pepperion)


# Simply Cheese menu detail
simply_cheese_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\SIMPLY CHEESE.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\8.50add_button_image.png",2,0,35,50,"SIMPLY CHEESE",
"",
"Lots of mozzarella",
"", expanding_pages.expanding_simply_cheese)
simply_cheese_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_simply_cheese)
simply_cheese_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_simply_cheese)


# Supreme menu detail
supreme_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\SUPREME.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\8.50add_button_image.png",2,1,35,50,"SUPREME",
"Pepperoni, rasher bacon, capsicum,",
"ground beef, Italian sausage,",
"mushroom, pineapple, topped with…",expanding_pages.expanding_Supreme)
supreme_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_supreme)
supreme_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_supreme)


# Gourmet Range
# APRICOT CHICKEN menu detail
apricot_chicken_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\APRICOT CHICKEN.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50button_brighter_imroved_final.png",3,0,139,50,"APRICOT CHICKEN",
"Seasoned chicken, red onion",
"capsicum, & mozzarella topped",
"with Apricot sauce", expanding_pages.expanding_Apricot)
apricot_chicken_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_apricot_chicken)
apricot_chicken_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_apricot_chicken)


# CHICKEN, BACON & AIOLI menu detail
chicken_bacon_aiol_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\CHICKEN, BACON & AIOLI Pizza.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50button_brighter_imroved_final.png",3,1,139,50,"BACON & AIOLI",
"Tender chicken, crispy rasher",
"bacon, spinach and red onion,",
"topped with a creamy aioli", expanding_pages.expanding_chicken_bacon_aioli)
chicken_bacon_aiol_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_chicken_bacon_aioli)
chicken_bacon_aiol_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_chicken_bacon_aioli)


# CHICKEN & CHEESE menu detail
chicken_cheese_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\CHICKEN & CAMEMBERT.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50button_brighter_imroved_final.png",3,2,139,50,"CHICKEN & CHEESE",
"Seasoned chicken, camembert,",
"rasher bacon,baby spinach,",
"tomatoes, red onion..",expanding_pages.expand_chicken_cheese)
chicken_cheese_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_chicken_cheese)
chicken_cheese_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_chicken_cheese)


# GARLIC PRAWN menu detail
gralic_prawn_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\GARLIC PRAWN.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50button_brighter_imroved_final.png",4,0,35,50,"GRALIC PRAWN",
"Prawns, baby spinach, tomato",
"& oregano on a crème fraîche",
"& garlic sauce base",expanding_pages.expanding_gralic_prawn)
gralic_prawn_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_gralic_prawn)
gralic_prawn_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_gralic_prawn)


# MEGA MEATLOVERSmenu detail
mega_meatlover_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\MEGA MEATLOVERS.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50button_brighter_imroved_final.png",4,1,35,50,"MEGA MEATLOVER",
"Ground beef, Italian sausage,",
"crispy rasher bacon, succulent",
"chicken, smokey Manuka ham &...",expanding_pages.expanding_mega_meatlover)
mega_meatlover_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_mega_meatlover)
mega_meatlover_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_mega_meatlover)


# Peri-peri chicken menu detail
peri_peri_chicken_menu = Henderson_Pizza_Palace_Tkinter.Meun_item_geneartor(Intro_Frames.mini_menu_frame,r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\PERI-PERI CHICKEN.jpg",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50button_brighter_imroved_final.png",4,2,35,50,"PERI-PERI CHICKEN",
"Succulent chicken, tomato, baby",
"spinach & red onion, topped with",
"a peri peri sauce swirl",expanding_pages.expanding_peri_peri_chicken)
peri_peri_chicken_menu.mini_pizza_item_frame.bind('<Enter>',Animation_menu.hover_on_peri_peri_chicken)
peri_peri_chicken_menu.mini_pizza_item_frame.bind('<Leave>',Animation_menu.hover_off_peri_peri_chicken)
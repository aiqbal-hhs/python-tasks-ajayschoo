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
import pygame



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
American_pepperion_scroll_bar = ttk.Scrollbar(American_pepperion_canvas,orient=VERTICAL,command=American_pepperion_canvas.yview)
mini_American_pepperion_frame = Frame(American_pepperion_canvas, bg = '#14141D')


# Cheesy gralic scroll bar and mini frame
def expanding_cheesy_gralic_pizza():
    hiding_expanding_frames()
    Cheesy_gralic_pizza_frame.pack(expand=1,fill=BOTH)
    Cheesy_gralic_pizza_canvas.pack(side=LEFT,expand=1,fill=BOTH)
    Cheesy_gralic_pizza_scroll_bar.pack(side=RIGHT,fill=Y)
    Cheesy_gralic_pizza_canvas.configure(yscrollcommand=Cheesy_gralic_pizza_scroll_bar.set)
    Cheesy_gralic_pizza_canvas.bind("<Configure>",lambda e:Cheesy_gralic_pizza_canvas.configure(scrollregion=Cheesy_gralic_pizza_canvas.bbox('all')))
    Cheesy_gralic_pizza_canvas.create_window((0,0),window=mini_Cheesy_gralic_pizza_frame,width = 1066, height = 1550,anchor='nw')


Cheesy_gralic_pizza_frame = Frame(Intro_Frames.window)
Cheesy_gralic_pizza_canvas = Canvas(Cheesy_gralic_pizza_frame)
Cheesy_gralic_pizza_scroll_bar = ttk.Scrollbar(Cheesy_gralic_pizza_canvas, orient=VERTICAL,command=Cheesy_gralic_pizza_canvas.yview)
mini_Cheesy_gralic_pizza_frame = Frame(Cheesy_gralic_pizza_canvas, bg = '#14141D')


# Chicken supreme scroll bar and mini frame
def expanding_chicken_supreme():
    hiding_expanding_frames()
    Chicken_supreme_frame.pack(expand=1,fill=BOTH)
    Chicken_supreme_canvas.pack(side=LEFT,expand=1,fill=BOTH)
    Chicekn_supreme_scroll_bar.pack(side= RIGHT, fill=Y)
    Chicken_supreme_canvas.configure(yscrollcommand = Chicekn_supreme_scroll_bar.set)
    Chicken_supreme_canvas.bind("<Configure>",lambda e:Chicken_supreme_canvas.configure(scrollregion=Chicken_supreme_canvas.bbox('all')))
    Chicken_supreme_canvas.create_window((0,0),window=mini_chicken_supreme_frame,width = 1066, height = 1550,anchor='nw')


Chicken_supreme_frame = Frame(Intro_Frames.window)
Chicken_supreme_canvas = Canvas(Chicken_supreme_frame)
Chicekn_supreme_scroll_bar = ttk.Scrollbar(Chicken_supreme_canvas, orient=VERTICAL,command=Chicken_supreme_canvas.yview)
mini_chicken_supreme_frame = Frame(Chicken_supreme_canvas, bg = '#14141D')


# Ham and cheese scroll bar and frame
def expanding_ham_cheese():
    hiding_expanding_frames()
    Ham_and_cheese_frame.pack(expand=1,fill=BOTH)
    Ham_and_cheese_canvas.pack(expand=1,fill=BOTH,side=LEFT)
    Ham_and_cheese_scroll_bar.pack(side = RIGHT,fill=Y)
    Ham_and_cheese_canvas.configure(yscrollcommand=Ham_and_cheese_scroll_bar.set)
    Ham_and_cheese_canvas.bind("<Configure>",lambda e: Ham_and_cheese_canvas.configure(scrollregion=Ham_and_cheese_canvas.bbox('all')))
    Ham_and_cheese_canvas.create_window((0,0),window=mini_ham_and_cheese_frame,width = 1066, height = 1550,anchor='nw')


Ham_and_cheese_frame = Frame(Intro_Frames.window)
Ham_and_cheese_canvas = Canvas(Ham_and_cheese_frame)
Ham_and_cheese_scroll_bar = ttk.Scrollbar(Ham_and_cheese_canvas, orient=VERTICAL, command=Ham_and_cheese_canvas.yview)
mini_ham_and_cheese_frame = Frame(Ham_and_cheese_canvas, bg = '#14141D')


# Mr wedge frame and scroll
def expanding_mr_wedge():
    hiding_expanding_frames()
    Mr_wedge_frame.pack(expand=1,fill=BOTH)
    Mr_wedge_canvas.pack(fill=BOTH,side=LEFT,expand=1)
    Mr_wedge_scroll_bar.pack(side = RIGHT,fill=Y)
    Mr_wedge_canvas.configure(yscrollcommand=Mr_wedge_scroll_bar.set)
    Mr_wedge_canvas.bind("<Configure>", lambda e: Mr_wedge_canvas.configure(scrollregion=Mr_wedge_canvas.bbox('all')))
    Mr_wedge_canvas.create_window((0,0), window=mini_mr_wedge_frame,width = 1066, height = 1550,anchor='nw')


Mr_wedge_frame = Frame(Intro_Frames.window)
Mr_wedge_canvas = Canvas(Mr_wedge_frame)
Mr_wedge_scroll_bar = ttk.Scrollbar(Mr_wedge_canvas, orient=VERTICAL, command=Mr_wedge_canvas.yview)
mini_mr_wedge_frame = Frame(Mr_wedge_canvas, bg = '#14141D')


# Pepperion frame and scroll bar
def expanding_pepperion():
    hiding_expanding_frames()
    Pepperion_frame.pack(expand=1,fill=BOTH)
    Pepperion_canvas.pack(side=LEFT,expand=1,fill=BOTH)
    Pepperion_scroll_bar.pack(side=RIGHT,fill=Y)
    Pepperion_canvas.configure(yscrollcommand=Pepperion_scroll_bar.set)
    Pepperion_canvas.bind("<Configure>",lambda e: Pepperion_canvas.configure(scrollregion=Pepperion_canvas.bbox('all')))
    Pepperion_canvas.create_window((0,0),window=mini_Pepperion_frame,width = 1066, height = 1550,anchor='nw')


Pepperion_frame = Frame(Intro_Frames.window)
Pepperion_canvas = Canvas(Pepperion_frame)
Pepperion_scroll_bar = ttk.Scrollbar(Pepperion_canvas, orient=VERTICAL, command=Pepperion_canvas.yview)
mini_Pepperion_frame = Frame(Pepperion_canvas, bg = '#14141D')


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
Simply_cheese_scroll_bar = ttk.Scrollbar(Simply_cheese_canvas, orient=VERTICAL, command=Simply_cheese_canvas.yview)
mini_Simply_cheese_frame = Frame(Simply_cheese_canvas, bg = '#14141D')


# supreme frame and scroll bar
def expanding_Supreme():
    hiding_expanding_frames()
    Supreme_frame.pack(expand=1,fill=BOTH)
    Supreme_canvas.pack(side = LEFT, fill=BOTH, expand= 1)
    Supreme_scroll_bar.pack(side= RIGHT,fill=Y)
    Supreme_canvas.configure(yscrollcommand=Supreme_scroll_bar.set)
    Supreme_canvas.bind("<Configure>",lambda e: Supreme_canvas.configure(scrollregion= Supreme_canvas.bbox('all')))
    Supreme_canvas.create_window((0,0), window = mini_Supreme_frame, width = 1066, height = 1550,anchor='nw')


Supreme_frame = Frame(Intro_Frames.window)
Supreme_canvas = Canvas(Supreme_frame)
Supreme_scroll_bar = ttk.Scrollbar(Supreme_canvas, orient=VERTICAL, command=Supreme_canvas.yview)
mini_Supreme_frame = Frame(Supreme_canvas, bg = '#14141D')



# Gourmet Range
# Apricot frame and scroll bar
def expanding_Apricot():
    hiding_expanding_frames()
    Apricot_frame.pack(expand=1,fill=BOTH)
    Apricot_canvas.pack(side=LEFT,expand=1,fill=BOTH)
    Apricot_scrollbar.pack(fill=Y, side=RIGHT)
    Apricot_canvas.configure(yscrollcommand=Apricot_scrollbar.set)
    Apricot_canvas.bind("<Configure>",lambda e: Apricot_canvas.configure(scrollregion = Apricot_canvas.bbox('all')))
    Apricot_canvas.create_window((0,0),window=mini_Apricot_frame,width = 1066, height = 1550,anchor='nw')


Apricot_frame = Frame(Intro_Frames.window)
Apricot_canvas = Canvas(Apricot_frame)
Apricot_scrollbar = ttk.Scrollbar(Apricot_canvas,orient=VERTICAL,command=Apricot_canvas.yview)
mini_Apricot_frame = Frame(Apricot_canvas, bg = '#14141D')


# Chicken, Bacon and aioli scrollbar and frame
def expanding_chicken_bacon_aioli():
    hiding_expanding_frames()
    Chicken_bacon_aioli_frame.pack(fill=BOTH, expand=1)
    Chicken_bacon_aioli_canvas.pack(side=LEFT, expand=1, fill=BOTH)
    Chicken_bacon_aioli_scroll_bar.pack(side=RIGHT, fill= Y)
    Chicken_bacon_aioli_canvas.configure(yscrollcommand= Chicken_bacon_aioli_scroll_bar.set)
    Chicken_bacon_aioli_canvas.bind("<Configure>", lambda e: Chicken_bacon_aioli_canvas.configure(scrollregion= Chicken_bacon_aioli_canvas.bbox('all')))
    Chicken_bacon_aioli_canvas.create_window((0,0), window= mini_chicken_bacon_aioli, width = 1066, height = 1550,anchor='nw')


Chicken_bacon_aioli_frame = Frame(Intro_Frames.window)
Chicken_bacon_aioli_canvas = Canvas(Chicken_bacon_aioli_frame)
Chicken_bacon_aioli_scroll_bar = ttk.Scrollbar(Chicken_bacon_aioli_canvas, orient=VERTICAL,command=Chicken_bacon_aioli_canvas.yview)
mini_chicken_bacon_aioli = Frame(Chicken_bacon_aioli_canvas, bg = '#14141D')


# Chicken and cheese pizza scrollbar and frame
def expand_chicken_cheese():
    hiding_expanding_frames()
    Chicken_cheese_frame.pack(expand=1, fill=BOTH)
    Chicken_cheese_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    Chicken_cheese_scrollbar.pack(side= RIGHT, fill=Y)
    Chicken_cheese_canvas.configure(yscrollcommand = Chicken_cheese_scrollbar.set)
    Chicken_cheese_canvas.bind("<Configure>", lambda e: Chicken_cheese_canvas.configure(scrollregion=Chicken_cheese_canvas.bbox('all')))
    Chicken_cheese_canvas.create_window((0,0), window=mini_chicken_cheese_frame, width = 1066, height = 1550,anchor='nw')


Chicken_cheese_frame = Frame(Intro_Frames.window)
Chicken_cheese_canvas = Canvas(Chicken_cheese_frame)
Chicken_cheese_scrollbar = ttk.Scrollbar(Chicken_cheese_canvas, orient= VERTICAL, command= Chicken_cheese_canvas.yview)
mini_chicken_cheese_frame = Frame(Chicken_cheese_canvas, bg = '#14141D')

# Gralic prawn scrollbar and frame
def expanding_gralic_prawn():
    hiding_expanding_frames()
    Gralic_prawn_frame.pack(expand=1, fill= BOTH)
    Gralic_prawn_canvas.pack(side= LEFT, expand=1, fill=BOTH)
    Gralic_prawn_scrollbar.pack(side= RIGHT, fill=Y)
    Gralic_prawn_canvas.configure(yscrollcommand= Gralic_prawn_scrollbar.set)
    Gralic_prawn_canvas.bind("<Configure>", lambda e: Gralic_prawn_canvas.configure(scrollregion= Gralic_prawn_canvas.bbox("all")))
    Gralic_prawn_canvas.create_window((0,0), window=mini_gralic_prawn_frame, width = 1066, height = 1550,anchor='nw')


Gralic_prawn_frame = Frame(Intro_Frames.window)
Gralic_prawn_canvas = Canvas(Gralic_prawn_frame)
Gralic_prawn_scrollbar = ttk.Scrollbar(Gralic_prawn_canvas, orient=VERTICAL, command=Gralic_prawn_canvas.yview)
mini_gralic_prawn_frame = Frame(Gralic_prawn_canvas, bg = '#14141D')


# Mega meatlover frame and scroll bar
def expanding_mega_meatlover():
    hiding_expanding_frames()
    Mega_meatlover_frame.pack(expand=1, fill=BOTH)
    Mega_meatlover_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    Mega_meatlover_scrollbar.pack(side= RIGHT, fill=Y)
    Mega_meatlover_canvas.configure(yscrollcommand= Mega_meatlover_scrollbar.set)
    Mega_meatlover_canvas.bind("<Configure>", lambda e: Mega_meatlover_canvas.configure(scrollregion= Mega_meatlover_canvas.bbox('all')))
    Mega_meatlover_canvas.create_window((0,0), window=mini_Mega_meatlover_frame,width = 1066, height = 1550,anchor='nw')


Mega_meatlover_frame = Frame(Intro_Frames.window)
Mega_meatlover_canvas = Canvas(Mega_meatlover_frame)
Mega_meatlover_scrollbar = ttk.Scrollbar(Mega_meatlover_canvas,orient=VERTICAL, command=Mega_meatlover_canvas.yview)
mini_Mega_meatlover_frame = Frame(Mega_meatlover_canvas, bg = '#14141D')


# peri-peri chicken frame and scrollbar
def expanding_peri_peri_chicken():
    hiding_expanding_frames()
    Peri_peri_chicken_frame.pack(expand=1, fill= BOTH)
    Peri_peri_chicken_canvas.pack(side=LEFT, fill= BOTH, expand=1)
    Peri_peri_chicken_scrollbar.pack(side= RIGHT, fill=Y)
    Peri_peri_chicken_canvas.configure(yscrollcommand= Peri_peri_chicken_scrollbar.set)
    Peri_peri_chicken_canvas.bind("<Configure>", lambda e: Peri_peri_chicken_canvas.configure(scrollregion= Peri_peri_chicken_canvas.bbox('all')))
    Peri_peri_chicken_canvas.create_window((0,0),window= mini_Peri_peri_chicken, width = 1066, height = 1550,anchor='nw')


Peri_peri_chicken_frame = Frame(Intro_Frames.window)
Peri_peri_chicken_canvas = Canvas(Peri_peri_chicken_frame)
Peri_peri_chicken_scrollbar = ttk.Scrollbar(Peri_peri_chicken_canvas, orient=VERTICAL, command=Peri_peri_chicken_canvas.yview)
mini_Peri_peri_chicken = Frame(Peri_peri_chicken_canvas, bg = '#14141D')


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



def scroll_anywhere(event):
    global count_up, count_down, count_up_SC, count_down_SC, count_up_AM, count_down_AM, count_up_CS, count_down_CS, count_up_CIS, count_down_CIS, count_up_HC, count_down_HC, count_down_MW, count_up_MW, count_down_PE, count_up_PE, \
            count_down_SU, count_up_SU, count_down_AC, count_up_AC, count_down_CBA, count_up_CBA, count_down_CC, count_up_CC, count_down_GP, count_up_GP, count_down_MML, count_up_MML, count_down_PPC, count_up_PPC


    # Here, I put a method of checking if the scroll framw is aviable if so it will work else it will stop the whole scrolling.
    if Intro_Frames.menu_frame.winfo_ismapped() == True:
        # respond to Linux or Windows wheel event
        # This if statement makes the frame go down
        # The 5 and -120 indicate to the computer that the mousewheel is getting moved down
        if event.num == 5 or event.delta == -120:
            # resetting the value for count_up, so user can go back down perciously
            count_up = 0
            # Here, we will be counting positively to scroll down
            count_down += 1
            Intro_Frames.menu_canvas.yview_scroll(count_down, 'units')
            # Making the maximum value of scroll down to set equal to maximum valuw so no extra value be counted
            if count_down >= 9:
                count_down = 9
        # This if statement makes the frame goes up
        # The 4 and 120 indicate to the computer that the mousewheel is getting moved up
        if event.num == 4 or event.delta == 120:
            # resetting the value for count_down, so user can go back up perciously
            count_down = 0
            # Whereas, here we will be counting or subrating (negatively) to scroll up
            count_up -= 1
            Intro_Frames.menu_canvas.yview_scroll(count_up, 'units')
            # Making the maximum value of scroll up to set equal to maximum valuw so no extra value be counted
            if count_up <= -9:
                count_up = -9

    elif mini_Simply_cheese_frame.winfo_ismapped() == True:
        # This makes the pizza frmae scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_SC = 0
            count_up_SC += 1
            Simply_cheese_canvas.yview_scroll(count_up_SC, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_SC >= 7:
                count_up_SC = 7
        # This makes the pizza frmae scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_SC = 0
            count_down_SC -= 1
            Simply_cheese_canvas.yview_scroll(count_down_SC, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_SC <= -7:
                count_down_SC = -7

    elif mini_American_pepperion_frame.winfo_ismapped() == True:
        # This makes the pizza frmae scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_AM = 0
            count_up_AM += 1
            American_pepperion_canvas.yview_scroll(count_up_AM, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_AM >= 7:
                count_up_AM = 7
        # This makes the pizza frame scroll up
        if event.num == 4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_AM = 0
            count_down_AM -= 1
            American_pepperion_canvas.yview_scroll(count_down_AM, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_AM <= -7:
                count_down_AM = -7

    elif mini_Cheesy_gralic_pizza_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_CS = 0
            count_up_CS += 1
            Cheesy_gralic_pizza_canvas.yview_scroll(count_up_CS, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_CS >= 7:
                count_up_CS = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_CS = 0
            count_down_CS -= 1
            Cheesy_gralic_pizza_canvas.yview_scroll(count_down_CS, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_CS <= -7:
                count_down_CS = -7

    elif mini_mr_wedge_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_MW = 0
            count_up_MW += 1
            Mr_wedge_canvas.yview_scroll(count_up_MW, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_MW >= 7:
                count_up_MW = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_MW = 0
            count_down_MW -= 1
            Mr_wedge_canvas.yview_scroll(count_down_MW, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_MW <= -7:
                count_down_MW = -7


    elif mini_chicken_supreme_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_CIS = 0
            count_up_CIS += 1
            Chicken_supreme_canvas.yview_scroll(count_up_CIS, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_CIS >= 7:
                count_up_CIS = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_CIS = 0
            count_down_CIS -= 1
            Chicken_supreme_canvas.yview_scroll(count_down_CIS, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_CIS <= -7:
                count_down_CIS = -7

    elif mini_ham_and_cheese_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_HC = 0
            count_up_HC += 1
            Ham_and_cheese_canvas.yview_scroll(count_up_HC, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_HC >= 7:
                count_up_HC = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_HC = 0
            count_down_HC -= 1
            Ham_and_cheese_canvas.yview_scroll(count_down_HC, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_HC <= -7:
                count_down_HC = -7

    elif mini_Pepperion_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_PE = 0
            count_up_PE += 1
            Pepperion_canvas.yview_scroll(count_up_PE, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_PE >= 7:
                count_up_PE = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_PE = 0
            count_down_PE -= 1
            Pepperion_canvas.yview_scroll(count_down_PE, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_PE <= -7:
                count_down_PE = -7

    elif mini_Supreme_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_SU = 0
            count_up_SU += 1
            Supreme_canvas.yview_scroll(count_up_SU, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_SU >= 7:
                count_up_SU = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_SU = 0
            count_down_SU -= 1
            Supreme_canvas.yview_scroll(count_down_SU, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_SU <= -7:
                count_down_SU = -7

    elif mini_Apricot_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_AC = 0
            count_up_AC += 1
            Apricot_canvas.yview_scroll(count_up_AC, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_AC >= 7:
                count_up_AC = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_AC = 0
            count_down_AC -= 1
            Apricot_canvas.yview_scroll(count_down_AC, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_AC <= -7:
                count_down_AC = -7

    elif mini_chicken_bacon_aioli.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_CBA = 0
            count_up_CBA += 1
            Chicken_bacon_aioli_canvas.yview_scroll(count_up_CBA, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_CBA >= 7:
                count_up_CBA = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_CBA = 0
            count_down_CBA -= 1
            Chicken_bacon_aioli_canvas.yview_scroll(count_down_CBA, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_CBA <= -7:
                count_down_CBA = -7

    elif mini_chicken_cheese_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_CC = 0
            count_up_CC += 1
            Chicken_cheese_canvas.yview_scroll(count_up_CC, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_CC >= 7:
                count_up_CC = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_CC = 0
            count_down_CC -= 1
            Chicken_cheese_canvas.yview_scroll(count_down_CC, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_CC <= -7:
                count_down_CC = -7

    elif mini_gralic_prawn_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_GP = 0
            count_up_GP += 1
            Gralic_prawn_canvas.yview_scroll(count_up_GP, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_GP >= 7:
                count_up_GP = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_GP = 0
            count_down_GP -= 1
            Gralic_prawn_canvas.yview_scroll(count_down_GP, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_GP <= -7:
                count_down_GP = -7

    elif mini_Mega_meatlover_frame.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_MML = 0
            count_up_MML += 1
            Mega_meatlover_canvas.yview_scroll(count_up_MML, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_MML >= 7:
                count_up_MML = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_MML = 0
            count_down_MML -= 1
            Mega_meatlover_canvas.yview_scroll(count_down_MML, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_MML <= -7:
                count_down_MML = -7


    elif mini_Peri_peri_chicken.winfo_ismapped() == True:
        # This makes the pizza frame scroll down
        if event.num == 5 or event.delta == -120:
            # Resetting the value of the scroll up function
            count_down_PPC = 0
            count_up_PPC += 1
            Peri_peri_chicken_canvas.yview_scroll(count_up_PPC, 'units')
            # Fixing the max value to 7 so it doesn't count for extra numbers
            if count_up_PPC >= 7:
                count_up_PPC = 7
        # This makes the pizza frame scroll up
        if event.num ==4 or event.delta == 120:
            # Resetting the value of the scroll down function
            count_up_PPC = 0
            count_down_PPC -= 1
            Peri_peri_chicken_canvas.yview_scroll(count_down_PPC, 'units')
            # Fixing the max value to -7 so it doesn't subract any more extra numbers
            if count_down_PPC <= -7:
                count_down_PPC = -7

    else:
        return 'break'



# Pizza detail page generator
class Pizza_detail_generator:

    # This a funtion which checks if there is anything in the order list if so it will make the checkout button normal else keep it disabled.
    def allowed_to_checkout(self):
        try:
            if len(Intro_Frames.displaying_frame.winfo_children()) <= 0:
                Intro_Frames.checkout_button.configure(state=DISABLED)
            else:
                Intro_Frames.checkout_button.configure(state=NORMAL)
        except TclError:
            pass

    pygame.mixer.init()
    def added_teller(self):
        pygame.mixer.music.load(r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\synthesize.mp3")
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play(loops=0)

    def added_stop(self):
        pygame.mixer.music.stop()

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
        self.putting_price_image = Button(pizza_frame, image= self.taking_price_image, bg= "#14141D", border=0, activebackground= "#14141D", command = lambda : [adding_pizza(), self.allowed_to_checkout(), self.added_teller()], cursor = "hand2")
        self.putting_price_image.place(x = 660, y = 385)
        self.next_button = Button(pizza_frame, image=self.next_button_image,pady =5, padx =5,bg= "#14141D", border=0,activebackground= "#14141D",command =  lambda : [going_in_front(), self.added_stop()], cursor = "hand2")
        self.next_button.place(x = 905, y = 335.5)
        self.back_button = Button(pizza_frame, image=self.back_button_image,pady =5, padx =5,anchor='nw',bg= "#14141D", border=0, activebackground= "#14141D",command= lambda : [going_in_back(), self.added_stop()], cursor = "hand2")
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
        self.name_current_topping = Label(self.mini_labelframe, text = f"{current_topping_name}".title(), font=('Helvetica',8), bg = 'white', fg = 'black')
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
        self.add_on_topping_name = Label(self.mini_labelframe_add_on_topping, text = f"{add_on_topping_name}".title(),  font=('Helvetica',8), bg = 'white', fg = 'black')
        self.add_on_topping_name.grid(row = 1, column= 0,sticky='n')


# This all for regular range
# Simply cheese basic information
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def simply_cheese_going_order_list():
    global count_up_SC, count_down_SC
    count_up_SC = 0
    count_down_SC = 0

    Simply_cheese_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def simply_cheese_going_menu_page():
    global count_up_SC, count_down_SC
    count_up_SC = 0
    count_down_SC = 0

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
    global count_up_AM, count_down_AM
    count_up_AM = 0
    count_down_AM = 0

    American_pepperion_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def american_pepperion_going_menu_page():
    global count_up_AM, count_down_AM
    count_up_AM = 0
    count_down_AM = 0

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

# Cheesy Gralic Pizza information
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def cheesy_gralic_going_order_list():
    global count_up_CS, count_down_CS
    count_up_CS = 0
    count_down_CS = 0

    Cheesy_gralic_pizza_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def cheesy_gralic_going_menu_page():
    global count_up_CS, count_down_CS
    count_up_CS = 0
    count_down_CS = 0

    Cheesy_gralic_pizza_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


cheesy_gralic_page = Pizza_detail_generator(mini_Cheesy_gralic_pizza_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Cheesy Gralic Pizza Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\add_cart button_resized.png", "Cheesy Gralic Pizza", "Mozzarella & garlic sauce on a crème\nfraiche base topped with oregano", cheesy_gralic_going_order_list, cheesy_gralic_going_menu_page, lambda : Total_cost_order.cheesy_gralic_add_order())


# Moduel for putting mini current label frame in the moduel
from Cheesy_Gralic_PAGE import Cheesy_gralic_labelframe as chp
from Cheesy_Gralic_PAGE import Anchovies as pizza_2_1
from Cheesy_Gralic_PAGE import Baby_spinach as pizza_2_2
from Cheesy_Gralic_PAGE import Camembert_Cheese as pizza_2_3
from Cheesy_Gralic_PAGE import Cherry_tomato as pizza_2_4
from Cheesy_Gralic_PAGE import Cherry_wood_somked_leg_ham as pizza_2_5
from Cheesy_Gralic_PAGE import Chili_Flakes as pizza_2_6
from Cheesy_Gralic_PAGE import Capasicum as pizza_2_7
from Cheesy_Gralic_PAGE import Feta as pizza_2_8
from Cheesy_Gralic_PAGE import Franks_RedHot_Orginal_Hot_Sauce as pizza_2_9
from Cheesy_Gralic_PAGE import Fresh_Tomatos as pizza_2_10
from Cheesy_Gralic_PAGE import Gralic_base_sauce_swirl as pizza_2_11
from Cheesy_Gralic_PAGE import Gralic_Parmesan_Sauce as pizza_2_12
from Cheesy_Gralic_PAGE import Ground_beef as pizza_2_13
from Cheesy_Gralic_PAGE import Hickory_BBQ_Sauce as pizza_2_14
from Cheesy_Gralic_PAGE import Hollandaise_sauce_swirl as pizza_2_15
from Cheesy_Gralic_PAGE import Jalapenos as pizza_2_16
from Cheesy_Gralic_PAGE import Mayonnaise as pizza_2_17
from Cheesy_Gralic_PAGE import Mozzarella_topping as pizza_2_18
from Cheesy_Gralic_PAGE import Mushroom as pizza_2_19
from Cheesy_Gralic_PAGE import Olives as pizza_2_20
from Cheesy_Gralic_PAGE import Oregano as pizza_2_21
from Cheesy_Gralic_PAGE import Paneer_Cheese as pizza_2_22
from Cheesy_Gralic_PAGE import Pepperoni as pizza_2_23
from Cheesy_Gralic_PAGE import Peri_peri_sauce_swirl as pizza_2_24
from Cheesy_Gralic_PAGE import Pineapple as pizza_2_25
from Cheesy_Gralic_PAGE import Planet_based_Beef as pizza_2_26
from Cheesy_Gralic_PAGE import Prawns as pizza_2_27
from Cheesy_Gralic_PAGE import Rasher_Bacon as pizza_2_28
from Cheesy_Gralic_PAGE import Red_onion as pizza_2_29
from Cheesy_Gralic_PAGE import Seasoned_Chicken as pizza_2_30
from Cheesy_Gralic_PAGE import Spring_Onion as pizza_2_31
from Cheesy_Gralic_PAGE import Tomato_capsicum_sauce as pizza_2_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_toppings_cheesy_gralic():
    for topping_current in chp.current_labelframe_only.winfo_children():
        topping_current.destroy()
        chp.storing_current_toppings.clear()
    chp.storing_current_toppings.append("Mozzarella Cheese")
    chp.storing_current_toppings.append("Gralic Base Sauce Swirl")
    chp.storing_current_toppings.append("Oregano")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_2_1)
    importlib.reload(pizza_2_2)
    importlib.reload(pizza_2_3)
    importlib.reload(pizza_2_4)
    importlib.reload(pizza_2_5)
    importlib.reload(pizza_2_6)
    importlib.reload(pizza_2_7)
    importlib.reload(pizza_2_8)
    importlib.reload(pizza_2_9)
    importlib.reload(pizza_2_10)
    importlib.reload(pizza_2_11)
    importlib.reload(pizza_2_12)
    importlib.reload(pizza_2_13)
    importlib.reload(pizza_2_14)
    importlib.reload(pizza_2_15)
    importlib.reload(pizza_2_16)
    importlib.reload(pizza_2_17)
    importlib.reload(pizza_2_18)
    importlib.reload(pizza_2_19)
    importlib.reload(pizza_2_20)
    importlib.reload(pizza_2_21)
    importlib.reload(pizza_2_22)
    importlib.reload(pizza_2_23)
    importlib.reload(pizza_2_24)
    importlib.reload(pizza_2_25)
    importlib.reload(pizza_2_26)
    importlib.reload(pizza_2_27)
    importlib.reload(pizza_2_28)
    importlib.reload(pizza_2_29)
    importlib.reload(pizza_2_30)
    importlib.reload(pizza_2_31)
    importlib.reload(pizza_2_32)


# Creating a new varibale for the topping list for simlply cheese so it can be used in differnet moduels as the actual files causes import loop error
topping_cheesy_gralic_list = chp.storing_current_toppings


# All the information of topping of chicken Supreme
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def chicken_supreme_going_order_list():
    global count_up_CIS, count_down_CIS
    count_up_CIS = 0
    count_down_CIS = 0

    Chicken_supreme_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def chicken_supreme_going_menu_page():
    global count_up_CIS, count_down_CIS
    count_up_CIS = 0
    count_down_CIS = 0

    Chicken_supreme_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


chicken_supreme_page = Pizza_detail_generator(mini_chicken_supreme_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken Supreme Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\add_cart button_resized.png", "Chicken Supreme", "Seasoned chicken, pineapple,\nmushrooms,capsicum & sliced\nred onions, topped with\nspring onions", chicken_supreme_going_order_list, chicken_supreme_going_menu_page, lambda : Total_cost_order.chicken_supreme_add_order())

# Moduel for putting mini current label frame in the moduel
from Chicken_Supreme_PAGE import Chicken_supreme_labelframe as CS
from Chicken_Supreme_PAGE import Anchovies as pizza_3_1
from Chicken_Supreme_PAGE import Baby_spinach as pizza_3_2
from Chicken_Supreme_PAGE import Camembert_Cheese as pizza_3_3
from Chicken_Supreme_PAGE import Cherry_tomato as pizza_3_4
from Chicken_Supreme_PAGE import Cherry_wood_somked_leg_ham as pizza_3_5
from Chicken_Supreme_PAGE import Chili_Flakes as pizza_3_6
from Chicken_Supreme_PAGE import Capasicum as pizza_3_7
from Chicken_Supreme_PAGE import Feta as pizza_3_8
from Chicken_Supreme_PAGE import Franks_RedHot_Orginal_Hot_Sauce as pizza_3_9
from Chicken_Supreme_PAGE import Fresh_Tomatos as pizza_3_10
from Chicken_Supreme_PAGE import Gralic_base_sauce_swirl as pizza_3_11
from Chicken_Supreme_PAGE import Gralic_Parmesan_Sauce as pizza_3_12
from Chicken_Supreme_PAGE import Ground_beef as pizza_3_13
from Chicken_Supreme_PAGE import Hickory_BBQ_Sauce as pizza_3_14
from Chicken_Supreme_PAGE import Hollandaise_sauce_swirl as pizza_3_15
from Chicken_Supreme_PAGE import Jalapenos as pizza_3_16
from Chicken_Supreme_PAGE import Mayonnaise as pizza_3_17
from Chicken_Supreme_PAGE import Mozzarella_topping as pizza_3_18
from Chicken_Supreme_PAGE import Mushroom as pizza_3_19
from Chicken_Supreme_PAGE import Olives as pizza_3_20
from Chicken_Supreme_PAGE import Oregano as pizza_3_21
from Chicken_Supreme_PAGE import Paneer_Cheese as pizza_3_22
from Chicken_Supreme_PAGE import Pepperoni as pizza_3_23
from Chicken_Supreme_PAGE import Peri_peri_sauce_swirl as pizza_3_24
from Chicken_Supreme_PAGE import Pineapple as pizza_3_25
from Chicken_Supreme_PAGE import Planet_based_Beef as pizza_3_26
from Chicken_Supreme_PAGE import Prawns as pizza_3_27
from Chicken_Supreme_PAGE import Rasher_Bacon as pizza_3_28
from Chicken_Supreme_PAGE import Red_onion as pizza_3_29
from Chicken_Supreme_PAGE import Seasoned_Chicken as pizza_3_30
from Chicken_Supreme_PAGE import Spring_Onion as pizza_3_31
from Chicken_Supreme_PAGE import Tomato_capsicum_sauce as pizza_3_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_toppings_chicken_supreme():
    for topping_current in CS.current_labelframe_only.winfo_children():
        topping_current.destroy()
        CS.storing_current_toppings.clear()
    CS.storing_current_toppings.append("Mozzarella Cheese")
    CS.storing_current_toppings.append("Capsicum")
    CS.storing_current_toppings.append("Mushroom")
    CS.storing_current_toppings.append("Red Onions")
    CS.storing_current_toppings.append("Pineapple")
    CS.storing_current_toppings.append("Spring Onions")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_3_1)
    importlib.reload(pizza_3_2)
    importlib.reload(pizza_3_3)
    importlib.reload(pizza_3_4)
    importlib.reload(pizza_3_5)
    importlib.reload(pizza_3_6)
    importlib.reload(pizza_3_7)
    importlib.reload(pizza_3_8)
    importlib.reload(pizza_3_9)
    importlib.reload(pizza_3_10)
    importlib.reload(pizza_3_11)
    importlib.reload(pizza_3_12)
    importlib.reload(pizza_3_13)
    importlib.reload(pizza_3_14)
    importlib.reload(pizza_3_15)
    importlib.reload(pizza_3_16)
    importlib.reload(pizza_3_17)
    importlib.reload(pizza_3_18)
    importlib.reload(pizza_3_19)
    importlib.reload(pizza_3_20)
    importlib.reload(pizza_3_21)
    importlib.reload(pizza_3_22)
    importlib.reload(pizza_3_23)
    importlib.reload(pizza_3_24)
    importlib.reload(pizza_3_25)
    importlib.reload(pizza_3_26)
    importlib.reload(pizza_3_27)
    importlib.reload(pizza_3_28)
    importlib.reload(pizza_3_29)
    importlib.reload(pizza_3_30)
    importlib.reload(pizza_3_31)
    importlib.reload(pizza_3_32)

# Creating a new varibale for the topping list for simlply cheese so it can be used in differnet moduels as the actual files causes import loop error
topping_chicken_supreme_list = CS.storing_current_toppings

# All the information about Ham and cheese here
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def ham_cheese_going_order_list():
    global count_up_HC, count_down_HC
    count_up_HC = 0
    count_down_HC = 0

    Ham_and_cheese_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def ham_cheese_going_menu_page():
    global count_up_HC, count_down_HC
    count_up_HC = 0
    count_down_HC = 0

    Ham_and_cheese_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


ham_cheese_page = Pizza_detail_generator(mini_ham_and_cheese_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Ham and Cheese Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\add_cart button_resized.png", "Ham and Cheese", "Smokey ham & mozzarella", ham_cheese_going_order_list, ham_cheese_going_menu_page, lambda : Total_cost_order.ham_and_cheese_add_order())

# Moduel for putting mini current label frame in the moduel
from Ham_and_cheese_page import ham_and_cheese_intro_labelframes as HC
from Ham_and_cheese_page import Anchovies as pizza_4_1
from Ham_and_cheese_page import Baby_spinach as pizza_4_2
from Ham_and_cheese_page import Camembert_Cheese as pizza_4_3
from Ham_and_cheese_page import Cherry_tomato as pizza_4_4
from Ham_and_cheese_page import Cherry_wood_somked_leg_ham as pizza_4_5
from Ham_and_cheese_page import Chili_Flakes as pizza_4_6
from Ham_and_cheese_page import Capasicum as pizza_4_7
from Ham_and_cheese_page import Feta as pizza_4_8
from Ham_and_cheese_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_4_9
from Ham_and_cheese_page import Fresh_Tomatos as pizza_4_10
from Ham_and_cheese_page import Gralic_base_sauce_swirl as pizza_4_11
from Ham_and_cheese_page import Gralic_Parmesan_Sauce as pizza_4_12
from Ham_and_cheese_page import Ground_beef as pizza_4_13
from Ham_and_cheese_page import Hickory_BBQ_Sauce as pizza_4_14
from Ham_and_cheese_page import Hollandaise_sauce_swirl as pizza_4_15
from Ham_and_cheese_page import Jalapenos as pizza_4_16
from Ham_and_cheese_page import Mayonnaise as pizza_4_17
from Ham_and_cheese_page import Mozzarella_topping as pizza_4_18
from Ham_and_cheese_page import Mushroom as pizza_4_19
from Ham_and_cheese_page import Olives as pizza_4_20
from Ham_and_cheese_page import Oregano as pizza_4_21
from Ham_and_cheese_page import Paneer_Cheese as pizza_4_22
from Ham_and_cheese_page import Pepperoni as pizza_4_23
from Ham_and_cheese_page import Peri_peri_sauce_swirl as pizza_4_24
from Ham_and_cheese_page import Pineapple as pizza_4_25
from Ham_and_cheese_page import Planet_based_Beef as pizza_4_26
from Ham_and_cheese_page import Prawns as pizza_4_27
from Ham_and_cheese_page import Rasher_Bacon as pizza_4_28
from Ham_and_cheese_page import Red_onion as pizza_4_29
from Ham_and_cheese_page import Seasoned_Chicken as pizza_4_30
from Ham_and_cheese_page import Spring_Onion as pizza_4_31
from Ham_and_cheese_page import Tomato_capsicum_sauce as pizza_4_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_toppings_ham_and_cheese():
    for topping_current in HC.current_labelframe_only.winfo_children():
        topping_current.destroy()
        HC.storing_current_toppings.clear()
    HC.storing_current_toppings.append("Mozzarella Cheese")
    HC.storing_current_toppings.append("Cherry wood somked leg ham")


    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_4_1)
    importlib.reload(pizza_4_2)
    importlib.reload(pizza_4_3)
    importlib.reload(pizza_4_4)
    importlib.reload(pizza_4_5)
    importlib.reload(pizza_4_6)
    importlib.reload(pizza_4_7)
    importlib.reload(pizza_4_8)
    importlib.reload(pizza_4_9)
    importlib.reload(pizza_4_10)
    importlib.reload(pizza_4_11)
    importlib.reload(pizza_4_12)
    importlib.reload(pizza_4_13)
    importlib.reload(pizza_4_14)
    importlib.reload(pizza_4_15)
    importlib.reload(pizza_4_16)
    importlib.reload(pizza_4_17)
    importlib.reload(pizza_4_18)
    importlib.reload(pizza_4_19)
    importlib.reload(pizza_4_20)
    importlib.reload(pizza_4_21)
    importlib.reload(pizza_4_22)
    importlib.reload(pizza_4_23)
    importlib.reload(pizza_4_24)
    importlib.reload(pizza_4_25)
    importlib.reload(pizza_4_26)
    importlib.reload(pizza_4_27)
    importlib.reload(pizza_4_28)
    importlib.reload(pizza_4_29)
    importlib.reload(pizza_4_30)
    importlib.reload(pizza_4_31)
    importlib.reload(pizza_4_32)


topping_ham_and_cheese_list = HC.storing_current_toppings


# All the information about MR Wedge
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def mr_wedge_going_order_list():
    global count_up_MW, count_down_MW
    count_up_MW = 0
    count_down_MW = 0

    Mr_wedge_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def mr_wedge_going_menu_page():
    global count_up_MW, count_down_MW
    count_up_MW = 0
    count_down_MW = 0

    Mr_wedge_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


mr_wedge_page = Pizza_detail_generator(mini_mr_wedge_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mr Wedge Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\add_cart button_resized.png", "MR Wedge", "Potato wedges, smokey Manuka ham,\nred onion & oregano on a BBQ\n& garlic sauce base, topped\nwith a mayonnaise swirl", mr_wedge_going_order_list, mr_wedge_going_menu_page, lambda : Total_cost_order.mr_wedge_add_order())

# Moduel for putting mini current label frame in the moduel
from Mr_Wedge_page import mr_wedge_intro_labelframes as MW
from Mr_Wedge_page import Anchovies as pizza_5_1
from Mr_Wedge_page import Baby_spinach as pizza_5_2
from Mr_Wedge_page import Camembert_Cheese as pizza_5_3
from Mr_Wedge_page import Cherry_tomato as pizza_5_4
from Mr_Wedge_page import Cherry_wood_somked_leg_ham as pizza_5_5
from Mr_Wedge_page import Chili_Flakes as pizza_5_6
from Mr_Wedge_page import Capasicum as pizza_5_7
from Mr_Wedge_page import Feta as pizza_5_8
from Mr_Wedge_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_5_9
from Mr_Wedge_page import Fresh_Tomatos as pizza_5_10
from Mr_Wedge_page import Gralic_base_sauce_swirl as pizza_5_11
from Mr_Wedge_page import Gralic_Parmesan_Sauce as pizza_5_12
from Mr_Wedge_page import Ground_beef as pizza_5_13
from Mr_Wedge_page import Hickory_BBQ_Sauce as pizza_5_14
from Mr_Wedge_page import Hollandaise_sauce_swirl as pizza_5_15
from Mr_Wedge_page import Jalapenos as pizza_5_16
from Mr_Wedge_page import Mayonnaise as pizza_5_17
from Mr_Wedge_page import Mozzarella_topping as pizza_5_18
from Mr_Wedge_page import Mushroom as pizza_5_19
from Mr_Wedge_page import Olives as pizza_5_20
from Mr_Wedge_page import Oregano as pizza_5_21
from Mr_Wedge_page import Paneer_Cheese as pizza_5_22
from Mr_Wedge_page import Pepperoni as pizza_5_23
from Mr_Wedge_page import Peri_peri_sauce_swirl as pizza_5_24
from Mr_Wedge_page import Pineapple as pizza_5_25
from Mr_Wedge_page import Planet_based_Beef as pizza_5_26
from Mr_Wedge_page import Prawns as pizza_5_27
from Mr_Wedge_page import Rasher_Bacon as pizza_5_28
from Mr_Wedge_page import Red_onion as pizza_5_29
from Mr_Wedge_page import Seasoned_Chicken as pizza_5_30
from Mr_Wedge_page import Spring_Onion as pizza_5_31
from Mr_Wedge_page import Tomato_capsicum_sauce as pizza_5_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_topping_mr_wedge():
    for topping_current in MW.current_labelframe_only.winfo_children():
        topping_current.destroy()
        MW.storing_current_toppings.clear()
    MW.storing_current_toppings.append("Mozzarella Cheese")
    MW.storing_current_toppings.append("Gralic Base Sauce Swirl")
    MW.storing_current_toppings.append("Cherry wood somked leg ham")
    MW.storing_current_toppings.append("Mayonnaise")
    MW.storing_current_toppings.append("Red Onions")
    MW.storing_current_toppings.append("Oregano")


    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_5_1)
    importlib.reload(pizza_5_2)
    importlib.reload(pizza_5_3)
    importlib.reload(pizza_5_4)
    importlib.reload(pizza_5_5)
    importlib.reload(pizza_5_6)
    importlib.reload(pizza_5_7)
    importlib.reload(pizza_5_8)
    importlib.reload(pizza_5_9)
    importlib.reload(pizza_5_10)
    importlib.reload(pizza_5_11)
    importlib.reload(pizza_5_12)
    importlib.reload(pizza_5_13)
    importlib.reload(pizza_5_14)
    importlib.reload(pizza_5_15)
    importlib.reload(pizza_5_16)
    importlib.reload(pizza_5_17)
    importlib.reload(pizza_5_18)
    importlib.reload(pizza_5_19)
    importlib.reload(pizza_5_20)
    importlib.reload(pizza_5_21)
    importlib.reload(pizza_5_22)
    importlib.reload(pizza_5_23)
    importlib.reload(pizza_5_24)
    importlib.reload(pizza_5_25)
    importlib.reload(pizza_5_26)
    importlib.reload(pizza_5_27)
    importlib.reload(pizza_5_28)
    importlib.reload(pizza_5_29)
    importlib.reload(pizza_5_30)
    importlib.reload(pizza_5_31)
    importlib.reload(pizza_5_32)


topping_mr_wedge_list = MW.storing_current_toppings

# All the information about Pepperoni
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def pepperoni_going_order_list():
    global count_up_PE, count_down_PE
    count_up_PE = 0
    count_down_PE = 0

    Pepperion_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def pepperoni_going_menu_page():
    global count_up_PE, count_down_PE
    count_up_PE = 0
    count_down_PE = 0

    Pepperion_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


pepperoni_page = Pizza_detail_generator(mini_Pepperion_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Pepperion Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\add_cart button_resized.png", "Pepperoni", "Lots of pepperoni & mozzarella", pepperoni_going_order_list, pepperoni_going_menu_page, lambda : Total_cost_order.pepperoni_add_order())

# Moduel for putting mini current label frame in the moduel
from Pepperoni_page import pepperoni_intro_labelframes as Pe
from Pepperoni_page import Anchovies as pizza_6_1
from Pepperoni_page import Baby_spinach as pizza_6_2
from Pepperoni_page import Camembert_Cheese as pizza_6_3
from Pepperoni_page import Cherry_tomato as pizza_6_4
from Pepperoni_page import Cherry_wood_somked_leg_ham as pizza_6_5
from Pepperoni_page import Chili_Flakes as pizza_6_6
from Pepperoni_page import Capasicum as pizza_6_7
from Pepperoni_page import Feta as pizza_6_8
from Pepperoni_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_6_9
from Pepperoni_page import Fresh_Tomatos as pizza_6_10
from Pepperoni_page import Gralic_base_sauce_swirl as pizza_6_11
from Pepperoni_page import Gralic_Parmesan_Sauce as pizza_6_12
from Pepperoni_page import Ground_beef as pizza_6_13
from Pepperoni_page import Hickory_BBQ_Sauce as pizza_6_14
from Pepperoni_page import Hollandaise_sauce_swirl as pizza_6_15
from Pepperoni_page import Jalapenos as pizza_6_16
from Pepperoni_page import Mayonnaise as pizza_6_17
from Pepperoni_page import Mozzarella_topping as pizza_6_18
from Pepperoni_page import Mushroom as pizza_6_19
from Pepperoni_page import Olives as pizza_6_20
from Pepperoni_page import Oregano as pizza_6_21
from Pepperoni_page import Paneer_Cheese as pizza_6_22
from Pepperoni_page import Pepperoni as pizza_6_23
from Pepperoni_page import Peri_peri_sauce_swirl as pizza_6_24
from Pepperoni_page import Pineapple as pizza_6_25
from Pepperoni_page import Planet_based_Beef as pizza_6_26
from Pepperoni_page import Prawns as pizza_6_27
from Pepperoni_page import Rasher_Bacon as pizza_6_28
from Pepperoni_page import Red_onion as pizza_6_29
from Pepperoni_page import Seasoned_Chicken as pizza_6_30
from Pepperoni_page import Spring_Onion as pizza_6_31
from Pepperoni_page import Tomato_capsicum_sauce as pizza_6_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_topping_pepperoni():
    for topping_current in Pe.current_labelframe_only.winfo_children():
        topping_current.destroy()
        Pe.storing_current_toppings.clear()
    Pe.storing_current_toppings.append("Mozzarella Cheese")
    Pe.storing_current_toppings.append("Pepperoni")



    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_6_1)
    importlib.reload(pizza_6_2)
    importlib.reload(pizza_6_3)
    importlib.reload(pizza_6_4)
    importlib.reload(pizza_6_5)
    importlib.reload(pizza_6_6)
    importlib.reload(pizza_6_7)
    importlib.reload(pizza_6_8)
    importlib.reload(pizza_6_9)
    importlib.reload(pizza_6_10)
    importlib.reload(pizza_6_11)
    importlib.reload(pizza_6_12)
    importlib.reload(pizza_6_13)
    importlib.reload(pizza_6_14)
    importlib.reload(pizza_6_15)
    importlib.reload(pizza_6_16)
    importlib.reload(pizza_6_17)
    importlib.reload(pizza_6_18)
    importlib.reload(pizza_6_19)
    importlib.reload(pizza_6_20)
    importlib.reload(pizza_6_21)
    importlib.reload(pizza_6_22)
    importlib.reload(pizza_6_23)
    importlib.reload(pizza_6_24)
    importlib.reload(pizza_6_25)
    importlib.reload(pizza_6_26)
    importlib.reload(pizza_6_27)
    importlib.reload(pizza_6_28)
    importlib.reload(pizza_6_29)
    importlib.reload(pizza_6_30)
    importlib.reload(pizza_6_31)
    importlib.reload(pizza_6_32)


topping_pepperoni_list = Pe.storing_current_toppings

# All the information about Supreme
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def supreme_going_order_list():
    global count_up_SU, count_down_SU
    count_up_SU = 0
    count_down_SU = 0

    Supreme_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def supreme_going_menu_page():
    Supreme_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()



supreme_page = Pizza_detail_generator(mini_Supreme_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Supreme Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\add_cart button_resized.png", "Supreme", "Pepperoni, rasher bacon, capsicum,\nground beef, Italian sausage, mushroom,\npineapple, topped with oregano\n& spring onion", supreme_going_order_list, supreme_going_menu_page, lambda : Total_cost_order.Supreme_add_order())

# Moduel for putting mini current label frame in the moduel
from Supreme_page import supreme_intro_labelframes as Sp
from Supreme_page import Anchovies as pizza_7_1
from Supreme_page import Baby_spinach as pizza_7_2
from Supreme_page import Camembert_Cheese as pizza_7_3
from Supreme_page import Cherry_tomato as pizza_7_4
from Supreme_page import Cherry_wood_somked_leg_ham as pizza_7_5
from Supreme_page import Chili_Flakes as pizza_7_6
from Supreme_page import Capasicum as pizza_7_7
from Supreme_page import Feta as pizza_7_8
from Supreme_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_7_9
from Supreme_page import Fresh_Tomatos as pizza_7_10
from Supreme_page import Gralic_base_sauce_swirl as pizza_7_11
from Supreme_page import Gralic_Parmesan_Sauce as pizza_7_12
from Supreme_page import Ground_beef as pizza_7_13
from Supreme_page import Hickory_BBQ_Sauce as pizza_7_14
from Supreme_page import Hollandaise_sauce_swirl as pizza_7_15
from Supreme_page import Jalapenos as pizza_7_16
from Supreme_page import Mayonnaise as pizza_7_17
from Supreme_page import Mozzarella_topping as pizza_7_18
from Supreme_page import Mushroom as pizza_7_19
from Supreme_page import Olives as pizza_7_20
from Supreme_page import Oregano as pizza_7_21
from Supreme_page import Paneer_Cheese as pizza_7_22
from Supreme_page import Pepperoni as pizza_7_23
from Supreme_page import Peri_peri_sauce_swirl as pizza_7_24
from Supreme_page import Pineapple as pizza_7_25
from Supreme_page import Planet_based_Beef as pizza_7_26
from Supreme_page import Prawns as pizza_7_27
from Supreme_page import Rasher_Bacon as pizza_7_28
from Supreme_page import Red_onion as pizza_7_29
from Supreme_page import Seasoned_Chicken as pizza_7_30
from Supreme_page import Spring_Onion as pizza_7_31
from Supreme_page import Tomato_capsicum_sauce as pizza_7_32


# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_topping_supreme():
    for topping_current in Sp.current_labelframe_only.winfo_children():
        topping_current.destroy()
        Sp.storing_current_toppings.clear()

    Sp.storing_current_toppings.append("Mozzarella Cheese")
    Sp.storing_current_toppings.append("Rasher Bacon")
    Sp.storing_current_toppings.append("Ground Beef")
    Sp.storing_current_toppings.append("Capsicum")
    Sp.storing_current_toppings.append("Mushroom")
    Sp.storing_current_toppings.append("Oregano")
    Sp.storing_current_toppings.append("Pepperoni")
    Sp.storing_current_toppings.append("Pineapple")
    Sp.storing_current_toppings.append("Spring Onions")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_7_1)
    importlib.reload(pizza_7_2)
    importlib.reload(pizza_7_3)
    importlib.reload(pizza_7_4)
    importlib.reload(pizza_7_5)
    importlib.reload(pizza_7_6)
    importlib.reload(pizza_7_7)
    importlib.reload(pizza_7_8)
    importlib.reload(pizza_7_9)
    importlib.reload(pizza_7_10)
    importlib.reload(pizza_7_11)
    importlib.reload(pizza_7_12)
    importlib.reload(pizza_7_13)
    importlib.reload(pizza_7_14)
    importlib.reload(pizza_7_15)
    importlib.reload(pizza_7_16)
    importlib.reload(pizza_7_17)
    importlib.reload(pizza_7_18)
    importlib.reload(pizza_7_19)
    importlib.reload(pizza_7_20)
    importlib.reload(pizza_7_21)
    importlib.reload(pizza_7_22)
    importlib.reload(pizza_7_23)
    importlib.reload(pizza_7_24)
    importlib.reload(pizza_7_25)
    importlib.reload(pizza_7_26)
    importlib.reload(pizza_7_27)
    importlib.reload(pizza_7_28)
    importlib.reload(pizza_7_29)
    importlib.reload(pizza_7_30)
    importlib.reload(pizza_7_31)
    importlib.reload(pizza_7_32)

topping_supreme_list = Sp.storing_current_toppings

# This all for gourment Range:
# All the information about Apricot Chicken
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def apricot_chicken_going_order_list():
    global count_up_AC, count_down_AC
    count_up_AC = 0
    count_down_AC = 0

    Apricot_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def apricot_chicken_going_menu_page():
    global count_up_AC, count_down_AC
    count_up_AC = 0
    count_down_AC = 0

    Apricot_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


apricot_chicken_page = Pizza_detail_generator(mini_Apricot_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Apriot Chicken Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50 add to cart button.png", "Apricot Chicken", "Seasoned chicken, red onion, capsicum,\n& mozzarella topped with\nApricot sauce", apricot_chicken_going_order_list, apricot_chicken_going_menu_page, lambda : Total_cost_order.apricot_chicken_add_order())

# Moduel for putting mini current label frame in the moduel
from Apricot_pizza_page import apricot_pizza_intro_labelframes as AC
from Apricot_pizza_page import Anchovies as pizza_1_1_1
from Apricot_pizza_page import Baby_spinach as pizza_1_1_2
from Apricot_pizza_page import Camembert_Cheese as pizza_1_1_3
from Apricot_pizza_page import Cherry_tomato as pizza_1_1_4
from Apricot_pizza_page import Cherry_wood_somked_leg_ham as pizza_1_1_5
from Apricot_pizza_page import Chili_Flakes as pizza_1_1_6
from Apricot_pizza_page import Capasicum as pizza_1_1_7
from Apricot_pizza_page import Feta as pizza_1_1_8
from Apricot_pizza_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_1_1_9
from Apricot_pizza_page import Fresh_Tomatos as pizza_1_1_10
from Apricot_pizza_page import Gralic_base_sauce_swirl as pizza_1_1_11
from Apricot_pizza_page import Gralic_Parmesan_Sauce as pizza_1_1_12
from Apricot_pizza_page import Ground_beef as pizza_1_1_13
from Apricot_pizza_page import Hickory_BBQ_Sauce as pizza_1_1_14
from Apricot_pizza_page import Hollandaise_sauce_swirl as pizza_1_1_15
from Apricot_pizza_page import Jalapenos as pizza_1_1_16
from Apricot_pizza_page import Mayonnaise as pizza_1_1_17
from Apricot_pizza_page import Mozzarella_topping as pizza_1_1_18
from Apricot_pizza_page import Mushroom as pizza_1_1_19
from Apricot_pizza_page import Olives as pizza_1_1_20
from Apricot_pizza_page import Oregano as pizza_1_1_21
from Apricot_pizza_page import Paneer_Cheese as pizza_1_1_22
from Apricot_pizza_page import Pepperoni as pizza_1_1_23
from Apricot_pizza_page import Peri_peri_sauce_swirl as pizza_1_1_24
from Apricot_pizza_page import Pineapple as pizza_1_1_25
from Apricot_pizza_page import Planet_based_Beef as pizza_1_1_26
from Apricot_pizza_page import Prawns as pizza_1_1_27
from Apricot_pizza_page import Rasher_Bacon as pizza_1_1_28
from Apricot_pizza_page import Red_onion as pizza_1_1_29
from Apricot_pizza_page import Seasoned_Chicken as pizza_1_1_30
from Apricot_pizza_page import Spring_Onion as pizza_1_1_31
from Apricot_pizza_page import Tomato_capsicum_sauce as pizza_1_1_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_topping_aprciot_chicken():
    for topping_current in AC.current_labelframe_only.winfo_children():
        topping_current.destroy()
        AC.storing_current_toppings.clear()

    AC.storing_current_toppings.append("Mozzarella Cheese")
    AC.storing_current_toppings.append("Seasoned Chicken")
    AC.storing_current_toppings.append("Capsicum")
    AC.storing_current_toppings.append("Red Onions")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_1_1_1)
    importlib.reload(pizza_1_1_2)
    importlib.reload(pizza_1_1_3)
    importlib.reload(pizza_1_1_4)
    importlib.reload(pizza_1_1_5)
    importlib.reload(pizza_1_1_6)
    importlib.reload(pizza_1_1_7)
    importlib.reload(pizza_1_1_8)
    importlib.reload(pizza_1_1_9)
    importlib.reload(pizza_1_1_10)
    importlib.reload(pizza_1_1_11)
    importlib.reload(pizza_1_1_12)
    importlib.reload(pizza_1_1_13)
    importlib.reload(pizza_1_1_14)
    importlib.reload(pizza_1_1_15)
    importlib.reload(pizza_1_1_16)
    importlib.reload(pizza_1_1_17)
    importlib.reload(pizza_1_1_18)
    importlib.reload(pizza_1_1_19)
    importlib.reload(pizza_1_1_20)
    importlib.reload(pizza_1_1_21)
    importlib.reload(pizza_1_1_22)
    importlib.reload(pizza_1_1_23)
    importlib.reload(pizza_1_1_24)
    importlib.reload(pizza_1_1_25)
    importlib.reload(pizza_1_1_26)
    importlib.reload(pizza_1_1_27)
    importlib.reload(pizza_1_1_28)
    importlib.reload(pizza_1_1_29)
    importlib.reload(pizza_1_1_30)
    importlib.reload(pizza_1_1_31)
    importlib.reload(pizza_1_1_32)


topping_apricot_chicken_list = AC.storing_current_toppings

# All the information about Chicken Bacon and Alioli
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def chicken_bacon_alioli_going_order_list():
    global count_up_CBA, count_down_CBA
    count_up_CBA = 0
    count_down_CBA = 0

    Chicken_bacon_aioli_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def chicken_bacon_alioli_going_menu_page():
    global count_up_CBA, count_down_CBA
    count_up_CBA = 0
    count_down_CBA = 0

    Chicken_bacon_aioli_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


chicken_bacon_alioli_page = Pizza_detail_generator(mini_chicken_bacon_aioli, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken, Bacon and Aloli resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50 add to cart button.png", "Bacon & Alioli", "Tender chicken, crispy rasher bacon,\nspinach and red onion, topped with a creamy\naioli sauce and served on a pizza sauce\nbase with garlic sauce.", chicken_bacon_alioli_going_order_list, chicken_bacon_alioli_going_menu_page, lambda : Total_cost_order.bacon_aioli_add_order())

# Moduel for putting mini current label frame in the moduel
from Bacon_and_Aioli_page import bacon_and_aioli_intro_labelframes as CBA
from Bacon_and_Aioli_page import Anchovies as pizza_1_2_1
from Bacon_and_Aioli_page import Baby_spinach as pizza_1_2_2
from Bacon_and_Aioli_page import Camembert_Cheese as pizza_1_2_3
from Bacon_and_Aioli_page import Cherry_tomato as pizza_1_2_4
from Bacon_and_Aioli_page import Cherry_wood_somked_leg_ham as pizza_1_2_5
from Bacon_and_Aioli_page import Chili_Flakes as pizza_1_2_6
from Bacon_and_Aioli_page import Capasicum as pizza_1_2_7
from Bacon_and_Aioli_page import Feta as pizza_1_2_8
from Bacon_and_Aioli_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_1_2_9
from Bacon_and_Aioli_page import Fresh_Tomatos as pizza_1_2_10
from Bacon_and_Aioli_page import Gralic_base_sauce_swirl as pizza_1_2_11
from Bacon_and_Aioli_page import Gralic_Parmesan_Sauce as pizza_1_2_12
from Bacon_and_Aioli_page import Ground_beef as pizza_1_2_13
from Bacon_and_Aioli_page import Hickory_BBQ_Sauce as pizza_1_2_14
from Bacon_and_Aioli_page import Hollandaise_sauce_swirl as pizza_1_2_15
from Bacon_and_Aioli_page import Jalapenos as pizza_1_2_16
from Bacon_and_Aioli_page import Mayonnaise as pizza_1_2_17
from Bacon_and_Aioli_page import Mozzarella_topping as pizza_1_2_18
from Bacon_and_Aioli_page import Mushroom as pizza_1_2_19
from Bacon_and_Aioli_page import Olives as pizza_1_2_20
from Bacon_and_Aioli_page import Oregano as pizza_1_2_21
from Bacon_and_Aioli_page import Paneer_Cheese as pizza_1_2_22
from Bacon_and_Aioli_page import Pepperoni as pizza_1_2_23
from Bacon_and_Aioli_page import Peri_peri_sauce_swirl as pizza_1_2_24
from Bacon_and_Aioli_page import Pineapple as pizza_1_2_25
from Bacon_and_Aioli_page import Planet_based_Beef as pizza_1_2_26
from Bacon_and_Aioli_page import Prawns as pizza_1_2_27
from Bacon_and_Aioli_page import Rasher_Bacon as pizza_1_2_28
from Bacon_and_Aioli_page import Red_onion as pizza_1_2_29
from Bacon_and_Aioli_page import Seasoned_Chicken as pizza_1_2_30
from Bacon_and_Aioli_page import Spring_Onion as pizza_1_2_31
from Bacon_and_Aioli_page import Tomato_capsicum_sauce as pizza_1_2_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_topping_bacon_aioli():
    for topping_current in CBA.current_labelframe_only.winfo_children():
        topping_current.destroy()
        CBA.storing_current_toppings.clear()

    CBA.storing_current_toppings.append("Mozzarella Cheese")
    CBA.storing_current_toppings.append("Baby Spinach")
    CBA.storing_current_toppings.append("Gralic Base Sauce Swirl")
    CBA.storing_current_toppings.append("Rasher Bacon")
    CBA.storing_current_toppings.append("Red Onions")
    CBA.storing_current_toppings.append("Seasoned Chicken")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_1_2_1)
    importlib.reload(pizza_1_2_2)
    importlib.reload(pizza_1_2_3)
    importlib.reload(pizza_1_2_4)
    importlib.reload(pizza_1_2_5)
    importlib.reload(pizza_1_2_6)
    importlib.reload(pizza_1_2_7)
    importlib.reload(pizza_1_2_8)
    importlib.reload(pizza_1_2_9)
    importlib.reload(pizza_1_2_10)
    importlib.reload(pizza_1_2_11)
    importlib.reload(pizza_1_2_12)
    importlib.reload(pizza_1_2_13)
    importlib.reload(pizza_1_2_14)
    importlib.reload(pizza_1_2_15)
    importlib.reload(pizza_1_2_16)
    importlib.reload(pizza_1_2_17)
    importlib.reload(pizza_1_2_18)
    importlib.reload(pizza_1_2_19)
    importlib.reload(pizza_1_2_20)
    importlib.reload(pizza_1_2_21)
    importlib.reload(pizza_1_2_22)
    importlib.reload(pizza_1_2_23)
    importlib.reload(pizza_1_2_24)
    importlib.reload(pizza_1_2_25)
    importlib.reload(pizza_1_2_26)
    importlib.reload(pizza_1_2_27)
    importlib.reload(pizza_1_2_28)
    importlib.reload(pizza_1_2_29)
    importlib.reload(pizza_1_2_30)
    importlib.reload(pizza_1_2_31)
    importlib.reload(pizza_1_2_32)


topping_bacon_aioli_list = CBA.storing_current_toppings

# All the information about Chicken and Cheese
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def chicken_and_cheese_going_order_list():
    global count_up_CC, count_down_CC
    count_up_CC = 0
    count_down_CC = 0

    Chicken_cheese_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def chicken_and_cheese_going_menu_page():
    global count_up_CC, count_down_CC
    count_up_CC = 0
    count_down_CC = 0

    Chicken_cheese_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


chicken_and_cheese_page = Pizza_detail_generator(mini_chicken_cheese_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Chicken & Camembert Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50 add to cart button.png", "Chicken & Cheese", "Seasoned chicken, camembert, rasher bacon,\nbaby spinach, tomatoes, red onion & mozzarella,\ntopped with a hollandaise swirl", chicken_and_cheese_going_order_list, chicken_and_cheese_going_menu_page, lambda : Total_cost_order.chicken_cheese_add_order())

# Moduel for putting mini current label frame in the moduel
from Cheese_Chicken_page import chicken_cheese_intro_labelframes as CC
from Cheese_Chicken_page import Anchovies as pizza_1_3_1
from Cheese_Chicken_page import Baby_spinach as pizza_1_3_2
from Cheese_Chicken_page import Camembert_Cheese as pizza_1_3_3
from Cheese_Chicken_page import Cherry_tomato as pizza_1_3_4
from Cheese_Chicken_page import Cherry_wood_somked_leg_ham as pizza_1_3_5
from Cheese_Chicken_page import Chili_Flakes as pizza_1_3_6
from Cheese_Chicken_page import Capasicum as pizza_1_3_7
from Cheese_Chicken_page import Feta as pizza_1_3_8
from Cheese_Chicken_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_1_3_9
from Cheese_Chicken_page import Fresh_Tomatos as pizza_1_3_10
from Cheese_Chicken_page import Gralic_base_sauce_swirl as pizza_1_3_11
from Cheese_Chicken_page import Gralic_Parmesan_Sauce as pizza_1_3_12
from Cheese_Chicken_page import Ground_beef as pizza_1_3_13
from Cheese_Chicken_page import Hickory_BBQ_Sauce as pizza_1_3_14
from Cheese_Chicken_page import Hollandaise_sauce_swirl as pizza_1_3_15
from Cheese_Chicken_page import Jalapenos as pizza_1_3_16
from Cheese_Chicken_page import Mayonnaise as pizza_1_3_17
from Cheese_Chicken_page import Mozzarella_topping as pizza_1_3_18
from Cheese_Chicken_page import Mushroom as pizza_1_3_19
from Cheese_Chicken_page import Olives as pizza_1_3_20
from Cheese_Chicken_page import Oregano as pizza_1_3_21
from Cheese_Chicken_page import Paneer_Cheese as pizza_1_3_22
from Cheese_Chicken_page import Pepperoni as pizza_1_3_23
from Cheese_Chicken_page import Peri_peri_sauce_swirl as pizza_1_3_24
from Cheese_Chicken_page import Pineapple as pizza_1_3_25
from Cheese_Chicken_page import Planet_based_Beef as pizza_1_3_26
from Cheese_Chicken_page import Prawns as pizza_1_3_27
from Cheese_Chicken_page import Rasher_Bacon as pizza_1_3_28
from Cheese_Chicken_page import Red_onion as pizza_1_3_29
from Cheese_Chicken_page import Seasoned_Chicken as pizza_1_3_30
from Cheese_Chicken_page import Spring_Onion as pizza_1_3_31
from Cheese_Chicken_page import Tomato_capsicum_sauce as pizza_1_3_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_topping_chicken_cheese():
    for topping_current in CC.current_labelframe_only.winfo_children():
        topping_current.destroy()
        CC.storing_current_toppings.clear()

    CC.storing_current_toppings.append("Mozzarella Cheese")
    CC.storing_current_toppings.append("Baby Spinach")
    CC.storing_current_toppings.append("Camambert Cheese")
    CC.storing_current_toppings.append("Fresh Tomatos")
    CC.storing_current_toppings.append("Hollandaise Sauce Swirl")
    CC.storing_current_toppings.append("Rasher Bacon")
    CC.storing_current_toppings.append("Red Onions")
    CC.storing_current_toppings.append("Seasoned Chicken")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_1_3_1)
    importlib.reload(pizza_1_3_2)
    importlib.reload(pizza_1_3_3)
    importlib.reload(pizza_1_3_4)
    importlib.reload(pizza_1_3_5)
    importlib.reload(pizza_1_3_6)
    importlib.reload(pizza_1_3_7)
    importlib.reload(pizza_1_3_8)
    importlib.reload(pizza_1_3_9)
    importlib.reload(pizza_1_3_10)
    importlib.reload(pizza_1_3_11)
    importlib.reload(pizza_1_3_12)
    importlib.reload(pizza_1_3_13)
    importlib.reload(pizza_1_3_14)
    importlib.reload(pizza_1_3_15)
    importlib.reload(pizza_1_3_16)
    importlib.reload(pizza_1_3_17)
    importlib.reload(pizza_1_3_18)
    importlib.reload(pizza_1_3_19)
    importlib.reload(pizza_1_3_20)
    importlib.reload(pizza_1_3_21)
    importlib.reload(pizza_1_3_22)
    importlib.reload(pizza_1_3_23)
    importlib.reload(pizza_1_3_24)
    importlib.reload(pizza_1_3_25)
    importlib.reload(pizza_1_3_26)
    importlib.reload(pizza_1_3_27)
    importlib.reload(pizza_1_3_28)
    importlib.reload(pizza_1_3_29)
    importlib.reload(pizza_1_3_30)
    importlib.reload(pizza_1_3_31)
    importlib.reload(pizza_1_3_32)


topping_chicken_cheese_list = CC.storing_current_toppings

# All the information about Gralic Prawns
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def gralic_prawn_going_order_list():
    global count_up_GP, count_down_GP
    count_up_GP = 0
    count_down_GP = 0

    Gralic_prawn_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def gralic_prawn_going_menu_page():
    global count_up_GP, count_down_GP
    count_up_GP = 0
    count_down_GP = 0

    Gralic_prawn_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


gralic_prawn_page = Pizza_detail_generator(mini_gralic_prawn_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Gralice Prawn Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50 add to cart button.png", "Gralic Prawns", "Prawns, baby spinach, tomato & oregano on\na crème fraîche & garlic sauce base", gralic_prawn_going_order_list, gralic_prawn_going_menu_page, lambda : Total_cost_order.gralic_prawns_add_order())

# Moduel for putting mini current label frame in the moduel
from Gralic_Prawns_page import gralic_prawns_intro_labelframes as GP
from Gralic_Prawns_page import Anchovies as pizza_1_4_1
from Gralic_Prawns_page import Baby_spinach as pizza_1_4_2
from Gralic_Prawns_page import Camembert_Cheese as pizza_1_4_3
from Gralic_Prawns_page import Cherry_tomato as pizza_1_4_4
from Gralic_Prawns_page import Cherry_wood_somked_leg_ham as pizza_1_4_5
from Gralic_Prawns_page import Chili_Flakes as pizza_1_4_6
from Gralic_Prawns_page import Capasicum as pizza_1_4_7
from Gralic_Prawns_page import Feta as pizza_1_4_8
from Gralic_Prawns_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_1_4_9
from Gralic_Prawns_page import Fresh_Tomatos as pizza_1_4_10
from Gralic_Prawns_page import Gralic_base_sauce_swirl as pizza_1_4_11
from Gralic_Prawns_page import Gralic_Parmesan_Sauce as pizza_1_4_12
from Gralic_Prawns_page import Ground_beef as pizza_1_4_13
from Gralic_Prawns_page import Hickory_BBQ_Sauce as pizza_1_4_14
from Gralic_Prawns_page import Hollandaise_sauce_swirl as pizza_1_4_15
from Gralic_Prawns_page import Jalapenos as pizza_1_4_16
from Gralic_Prawns_page import Mayonnaise as pizza_1_4_17
from Gralic_Prawns_page import Mozzarella_topping as pizza_1_4_18
from Gralic_Prawns_page import Mushroom as pizza_1_4_19
from Gralic_Prawns_page import Olives as pizza_1_4_20
from Gralic_Prawns_page import Oregano as pizza_1_4_21
from Gralic_Prawns_page import Paneer_Cheese as pizza_1_4_22
from Gralic_Prawns_page import Pepperoni as pizza_1_4_23
from Gralic_Prawns_page import Peri_peri_sauce_swirl as pizza_1_4_24
from Gralic_Prawns_page import Pineapple as pizza_1_4_25
from Gralic_Prawns_page import Planet_based_Beef as pizza_1_4_26
from Gralic_Prawns_page import Prawns as pizza_1_4_27
from Gralic_Prawns_page import Rasher_Bacon as pizza_1_4_28
from Gralic_Prawns_page import Red_onion as pizza_1_4_29
from Gralic_Prawns_page import Seasoned_Chicken as pizza_1_4_30
from Gralic_Prawns_page import Spring_Onion as pizza_1_4_31
from Gralic_Prawns_page import Tomato_capsicum_sauce as pizza_1_4_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_topping_gralic_prawns():
    for topping_current in GP.current_labelframe_only.winfo_children():
        topping_current.destroy()
        GP.storing_current_toppings.clear()

    GP.storing_current_toppings.append("Mozzarella Cheese")
    GP.storing_current_toppings.append("Baby Spinach")
    GP.storing_current_toppings.append("Fresh Tomatos")
    GP.storing_current_toppings.append("Gralic Base Sauce Swirl")
    GP.storing_current_toppings.append("Oregano")
    GP.storing_current_toppings.append("Prawns")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_1_4_1)
    importlib.reload(pizza_1_4_2)
    importlib.reload(pizza_1_4_3)
    importlib.reload(pizza_1_4_4)
    importlib.reload(pizza_1_4_5)
    importlib.reload(pizza_1_4_6)
    importlib.reload(pizza_1_4_7)
    importlib.reload(pizza_1_4_8)
    importlib.reload(pizza_1_4_9)
    importlib.reload(pizza_1_4_10)
    importlib.reload(pizza_1_4_11)
    importlib.reload(pizza_1_4_12)
    importlib.reload(pizza_1_4_13)
    importlib.reload(pizza_1_4_14)
    importlib.reload(pizza_1_4_15)
    importlib.reload(pizza_1_4_16)
    importlib.reload(pizza_1_4_17)
    importlib.reload(pizza_1_4_18)
    importlib.reload(pizza_1_4_19)
    importlib.reload(pizza_1_4_20)
    importlib.reload(pizza_1_4_21)
    importlib.reload(pizza_1_4_22)
    importlib.reload(pizza_1_4_23)
    importlib.reload(pizza_1_4_24)
    importlib.reload(pizza_1_4_25)
    importlib.reload(pizza_1_4_26)
    importlib.reload(pizza_1_4_27)
    importlib.reload(pizza_1_4_28)
    importlib.reload(pizza_1_4_29)
    importlib.reload(pizza_1_4_30)
    importlib.reload(pizza_1_4_31)
    importlib.reload(pizza_1_4_32)


topping_gralic_prawns_list = GP.storing_current_toppings

# All the information about mega meatlover
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def mega_meatlover_going_order_list():
    global count_up_MML, count_down_MML
    count_up_MML = 0
    count_down_MML = 0

    Mega_meatlover_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def mega_meatlover_going_menu_page():
    global count_up_MML, count_down_MML
    count_up_MML = 0
    count_down_MML = 0

    Mega_meatlover_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


mega_meatlover_page = Pizza_detail_generator(mini_Mega_meatlover_frame, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Mega MeatLover Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50 add to cart button.png", "Mega MeatLover", "Ground beef, Italian sausage, crispy rasher bacon,\nsucculent chicken, smokey Manuka\nham & pepperoni,finished with\na BBQ sauce swirl", mega_meatlover_going_order_list, mega_meatlover_going_menu_page, lambda : Total_cost_order.mega_meatlover_add_order())

# Moduel for putting mini current label frame in the moduel
from Mega_MeatLover_page import mega_meatlover_intro_labelframes as MML
from Mega_MeatLover_page import Anchovies as pizza_1_5_1
from Mega_MeatLover_page import Baby_spinach as pizza_1_5_2
from Mega_MeatLover_page import Camembert_Cheese as pizza_1_5_3
from Mega_MeatLover_page import Cherry_tomato as pizza_1_5_4
from Mega_MeatLover_page import Cherry_wood_somked_leg_ham as pizza_1_5_5
from Mega_MeatLover_page import Chili_Flakes as pizza_1_5_6
from Mega_MeatLover_page import Capasicum as pizza_1_5_7
from Mega_MeatLover_page import Feta as pizza_1_5_8
from Mega_MeatLover_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_1_5_9
from Mega_MeatLover_page import Fresh_Tomatos as pizza_1_5_10
from Mega_MeatLover_page import Gralic_base_sauce_swirl as pizza_1_5_11
from Mega_MeatLover_page import Gralic_Parmesan_Sauce as pizza_1_5_12
from Mega_MeatLover_page import Ground_beef as pizza_1_5_13
from Mega_MeatLover_page import Hickory_BBQ_Sauce as pizza_1_5_14
from Mega_MeatLover_page import Hollandaise_sauce_swirl as pizza_1_5_15
from Mega_MeatLover_page import Jalapenos as pizza_1_5_16
from Mega_MeatLover_page import Mayonnaise as pizza_1_5_17
from Mega_MeatLover_page import Mozzarella_topping as pizza_1_5_18
from Mega_MeatLover_page import Mushroom as pizza_1_5_19
from Mega_MeatLover_page import Olives as pizza_1_5_20
from Mega_MeatLover_page import Oregano as pizza_1_5_21
from Mega_MeatLover_page import Paneer_Cheese as pizza_1_5_22
from Mega_MeatLover_page import Pepperoni as pizza_1_5_23
from Mega_MeatLover_page import Peri_peri_sauce_swirl as pizza_1_5_24
from Mega_MeatLover_page import Pineapple as pizza_1_5_25
from Mega_MeatLover_page import Planet_based_Beef as pizza_1_5_26
from Mega_MeatLover_page import Prawns as pizza_1_5_27
from Mega_MeatLover_page import Rasher_Bacon as pizza_1_5_28
from Mega_MeatLover_page import Red_onion as pizza_1_5_29
from Mega_MeatLover_page import Seasoned_Chicken as pizza_1_5_30
from Mega_MeatLover_page import Spring_Onion as pizza_1_5_31
from Mega_MeatLover_page import Tomato_capsicum_sauce as pizza_1_5_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_topping_mega_meatlover():
    for topping_current in MML.current_labelframe_only.winfo_children():
        topping_current.destroy()
        MML.storing_current_toppings.clear()

    MML.storing_current_toppings.append("Mozzarella Cheese")
    MML.storing_current_toppings.append("Cherry wood somked leg ham")
    MML.storing_current_toppings.append("Ground Beef")
    MML.storing_current_toppings.append("Hickory BBQ Sauce")
    MML.storing_current_toppings.append("Pepperoni")
    MML.storing_current_toppings.append("Rasher Bacon")
    MML.storing_current_toppings.append("Seasoned Chicken")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_1_5_1)
    importlib.reload(pizza_1_5_2)
    importlib.reload(pizza_1_5_3)
    importlib.reload(pizza_1_5_4)
    importlib.reload(pizza_1_5_5)
    importlib.reload(pizza_1_5_6)
    importlib.reload(pizza_1_5_7)
    importlib.reload(pizza_1_5_8)
    importlib.reload(pizza_1_5_9)
    importlib.reload(pizza_1_5_10)
    importlib.reload(pizza_1_5_11)
    importlib.reload(pizza_1_5_12)
    importlib.reload(pizza_1_5_13)
    importlib.reload(pizza_1_5_14)
    importlib.reload(pizza_1_5_15)
    importlib.reload(pizza_1_5_16)
    importlib.reload(pizza_1_5_17)
    importlib.reload(pizza_1_5_18)
    importlib.reload(pizza_1_5_19)
    importlib.reload(pizza_1_5_20)
    importlib.reload(pizza_1_5_21)
    importlib.reload(pizza_1_5_22)
    importlib.reload(pizza_1_5_23)
    importlib.reload(pizza_1_5_24)
    importlib.reload(pizza_1_5_25)
    importlib.reload(pizza_1_5_26)
    importlib.reload(pizza_1_5_27)
    importlib.reload(pizza_1_5_28)
    importlib.reload(pizza_1_5_29)
    importlib.reload(pizza_1_5_30)
    importlib.reload(pizza_1_5_31)
    importlib.reload(pizza_1_5_32)


topping_mega_meatlover_list = MML.storing_current_toppings

# All the information about Peri-peri Chicken
# Reseting the scroll bar for detail pages when going away from the detail pizza page
def peri_peri_chicken_going_order_list():
    global count_up_PPC, count_down_PPC
    count_up_PPC = 0
    count_down_PPC = 0

    Peri_peri_chicken_canvas.yview_moveto(0.0)
    Intro_Frames.order_list_page()


def peri_peri_chicken_going_menu_page():
    global count_up_PPC, count_down_PPC
    count_up_PPC = 0
    count_down_PPC = 0

    Peri_peri_chicken_canvas.yview_moveto(0.0)
    Intro_Frames.menu_page()


peri_peri_chicken_page = Pizza_detail_generator(mini_Peri_peri_chicken, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Menu_Items_Pictures\Peri_Peri_chicken Resized.png",
r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\button,background,etc\13.50 add to cart button.png", "Peri-Peri Chicken", "Succulent chicken, tomato, baby spinach &\nred onion, topped with a peri peri sauce swirl", peri_peri_chicken_going_order_list, peri_peri_chicken_going_menu_page, lambda : Total_cost_order.peri_peri_chicken_add_order())

# Moduel for putting mini current label frame in the moduel
from Peri_peri_chicken_page import peri_peri_chicken_intro_labelframes as PPC
from Peri_peri_chicken_page import Anchovies as pizza_1_6_1
from Peri_peri_chicken_page import Baby_spinach as pizza_1_6_2
from Peri_peri_chicken_page import Camembert_Cheese as pizza_1_6_3
from Peri_peri_chicken_page import Cherry_tomato as pizza_1_6_4
from Peri_peri_chicken_page import Cherry_wood_somked_leg_ham as pizza_1_6_5
from Peri_peri_chicken_page import Chili_Flakes as pizza_1_6_6
from Peri_peri_chicken_page import Capasicum as pizza_1_6_7
from Peri_peri_chicken_page import Feta as pizza_1_6_8
from Peri_peri_chicken_page import Franks_RedHot_Orginal_Hot_Sauce as pizza_1_6_9
from Peri_peri_chicken_page import Fresh_Tomatos as pizza_1_6_10
from Peri_peri_chicken_page import Gralic_base_sauce_swirl as pizza_1_6_11
from Peri_peri_chicken_page import Gralic_Parmesan_Sauce as pizza_1_6_12
from Peri_peri_chicken_page import Ground_beef as pizza_1_6_13
from Peri_peri_chicken_page import Hickory_BBQ_Sauce as pizza_1_6_14
from Peri_peri_chicken_page import Hollandaise_sauce_swirl as pizza_1_6_15
from Peri_peri_chicken_page import Jalapenos as pizza_1_6_16
from Peri_peri_chicken_page import Mayonnaise as pizza_1_6_17
from Peri_peri_chicken_page import Mozzarella_topping as pizza_1_6_18
from Peri_peri_chicken_page import Mushroom as pizza_1_6_19
from Peri_peri_chicken_page import Olives as pizza_1_6_20
from Peri_peri_chicken_page import Oregano as pizza_1_6_21
from Peri_peri_chicken_page import Paneer_Cheese as pizza_1_6_22
from Peri_peri_chicken_page import Pepperoni as pizza_1_6_23
from Peri_peri_chicken_page import Peri_peri_sauce_swirl as pizza_1_6_24
from Peri_peri_chicken_page import Pineapple as pizza_1_6_25
from Peri_peri_chicken_page import Planet_based_Beef as pizza_1_6_26
from Peri_peri_chicken_page import Prawns as pizza_1_6_27
from Peri_peri_chicken_page import Rasher_Bacon as pizza_1_6_28
from Peri_peri_chicken_page import Red_onion as pizza_1_6_29
from Peri_peri_chicken_page import Seasoned_Chicken as pizza_1_6_30
from Peri_peri_chicken_page import Spring_Onion as pizza_1_6_31
from Peri_peri_chicken_page import Tomato_capsicum_sauce as pizza_1_6_32



# Deleting all the toppings in current when user have added the pizza to their order list, so they could start on another one if they want
def delete_topping_peri_peri_chicken():
    for topping_current in PPC.current_labelframe_only.winfo_children():
        topping_current.destroy()
        PPC.storing_current_toppings.clear()

    PPC.storing_current_toppings.append("Mozzarella Cheese")
    PPC.storing_current_toppings.append("Baby Spinach")
    PPC.storing_current_toppings.append("Fresh Tomatos")
    PPC.storing_current_toppings.append("Peri Peri Sauce Swirl")
    PPC.storing_current_toppings.append("Red Onions")
    PPC.storing_current_toppings.append("Seasoned Chicken")

    # reimporting all the moduel so they become normal and clickable. This done as when tthe users clicks the add to cart it will destroy everything and bring it back to noraml
    importlib.reload(pizza_1_6_1)
    importlib.reload(pizza_1_6_2)
    importlib.reload(pizza_1_6_3)
    importlib.reload(pizza_1_6_4)
    importlib.reload(pizza_1_6_5)
    importlib.reload(pizza_1_6_6)
    importlib.reload(pizza_1_6_7)
    importlib.reload(pizza_1_6_8)
    importlib.reload(pizza_1_6_9)
    importlib.reload(pizza_1_6_10)
    importlib.reload(pizza_1_6_11)
    importlib.reload(pizza_1_6_12)
    importlib.reload(pizza_1_6_13)
    importlib.reload(pizza_1_6_14)
    importlib.reload(pizza_1_6_15)
    importlib.reload(pizza_1_6_16)
    importlib.reload(pizza_1_6_17)
    importlib.reload(pizza_1_6_18)
    importlib.reload(pizza_1_6_19)
    importlib.reload(pizza_1_6_20)
    importlib.reload(pizza_1_6_21)
    importlib.reload(pizza_1_6_22)
    importlib.reload(pizza_1_6_23)
    importlib.reload(pizza_1_6_24)
    importlib.reload(pizza_1_6_25)
    importlib.reload(pizza_1_6_26)
    importlib.reload(pizza_1_6_27)
    importlib.reload(pizza_1_6_28)
    importlib.reload(pizza_1_6_29)
    importlib.reload(pizza_1_6_30)
    importlib.reload(pizza_1_6_31)
    importlib.reload(pizza_1_6_32)


topping_peri_peri_chicken_list = PPC.storing_current_toppings



# Menu frame counter
# This a counter that counts that clicks in the mousewheel so it chnage the view of the menu page.
# Count up means it will take will the values for when the scroll get move to the towards
count_up = 0
# Whereas, count_down would take the values when mousewheel get moved backwards
count_down = 0

# Counter for simply Cheese
count_up_SC = 0
count_down_SC = 0

# Counter for American pepperion
count_up_AM = 0
count_down_AM = 0

# Counter for Cheesy gralic
count_up_CS = 0
count_down_CS = 0

# Counter for Chicken Supreme
count_up_CIS = 0
count_down_CIS = 0

# Ham and cheese counter
count_up_HC = 0
count_down_HC = 0

# Mr Wedge counter
count_up_MW = 0
count_down_MW = 0

# Counter for Pepperoni
count_up_PE = 0
count_down_PE = 0

# Counter for Supreme
count_up_SU = 0
count_down_SU = 0

# Aprciot Chicken counter
count_up_AC = 0
count_down_AC = 0

# CBA means Chicken Bacon Aioli counter
count_up_CBA = 0
count_down_CBA = 0

# CC chicken cheese counter
count_up_CC = 0
count_down_CC = 0

# Gralic Prawn counter
count_up_GP = 0
count_down_GP = 0

# Mega Meatlover counter
count_up_MML = 0
count_down_MML = 0

# peri-peri Chicken counter
count_up_PPC = 0
count_down_PPC = 0

Intro_Frames.window.bind_all('<MouseWheel>', scroll_anywhere)


# Importing the sotring pizza file
import Warning_message_box
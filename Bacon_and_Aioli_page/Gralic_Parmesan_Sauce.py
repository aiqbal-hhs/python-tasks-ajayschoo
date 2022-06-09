# All the Moduels
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import expanding_pages
from Bacon_and_Aioli_page import bacon_and_aioli_intro_labelframes as intro_pages


# Removing gralic_permesan_sauce cheese from current topping list if want to
def remove_gralic_permesan_sauce():
    gralic_permesan_sauce_current.mini_labelframe.destroy()
    intro_pages.storing_current_toppings.remove("Gralic Permesan Sauce")
    gralic_permesan_sauce_add_on.topping_button['state'] = NORMAL
    gralic_permesan_sauce_add_on.add_on_topping_name.configure(fg = 'black')
    intro_pages.reszing()


    if len(intro_pages.storing_current_toppings) < 10:
        Anchovies.anchovies_add_on.topping_button['state'] = NORMAL
        Anchovies.anchovies_add_on.add_on_topping_name.configure(fg='black')
        Baby_spinach.baby_spinach_add_on.topping_button['state'] = NORMAL
        Baby_spinach.baby_spinach_add_on.add_on_topping_name.configure(fg='black')
        Camembert_Cheese.camembert_cheese_add_on.topping_button['state'] = NORMAL
        Camembert_Cheese.camembert_cheese_add_on.add_on_topping_name.configure(fg= 'black')
        Cherry_tomato.cherry_tomatos_add_on.topping_button['state'] = NORMAL
        Cherry_tomato.cherry_tomatos_add_on.add_on_topping_name.configure(fg = 'Black')
        Cherry_wood_somked_leg_ham.cherry_wood_somked_leg_ham_add_on.topping_button['state'] = NORMAL
        Cherry_wood_somked_leg_ham.cherry_wood_somked_leg_ham_add_on.add_on_topping_name.configure(fg = 'black')
        Chili_Flakes.chili_flakes_add_on.topping_button['state'] = NORMAL
        Chili_Flakes.chili_flakes_add_on.add_on_topping_name.configure(fg = 'black')
        Capasicum.capsicum_add_on.topping_button['state'] = NORMAL
        Capasicum.capsicum_add_on.add_on_topping_name.configure(fg='black')
        Feta.feta_add_on.topping_button['state'] = NORMAL
        Feta.feta_add_on.add_on_topping_name.configure(fg= 'black')
        Franks_RedHot_Orginal_Hot_Sauce.frank_redhot_original_hot_sauce_add_on.topping_button['state'] = NORMAL
        Franks_RedHot_Orginal_Hot_Sauce.frank_redhot_original_hot_sauce_add_on.add_on_topping_name.configure(fg='black')
        Fresh_Tomatos.fresh_tomatos_add_on.topping_button['state'] = NORMAL
        Fresh_Tomatos.fresh_tomatos_add_on.add_on_topping_name.configure(fg='black')
        Gralic_base_sauce_swirl.gralic_base_sauce_swirl_add_on.topping_button['state'] = NORMAL
        Gralic_base_sauce_swirl.gralic_base_sauce_swirl_add_on.add_on_topping_name.configure(fg='black')
        Ground_beef.ground_beef_add_on.topping_button['state'] = NORMAL
        Ground_beef.ground_beef_add_on.add_on_topping_name.configure(fg='black')
        Hickory_BBQ_Sauce.hickory_bbq_sauce_add_on.topping_button['state'] = NORMAL
        Hickory_BBQ_Sauce.hickory_bbq_sauce_add_on.add_on_topping_name.configure(fg='black')
        Mozzarella_topping.mozzarella_cheese_add_on.topping_button['state'] = NORMAL
        Mozzarella_topping.mozzarella_cheese_add_on.add_on_topping_name.configure(fg='black')
        Paneer_Cheese.paneer_cheese_add_on.topping_button['state'] = NORMAL
        Paneer_Cheese.paneer_cheese_add_on.add_on_topping_name.configure(fg = 'black')
        Hollandaise_sauce_swirl.hollandaise_sauce_swirl_add_on.topping_button['state'] = NORMAL
        Hollandaise_sauce_swirl.hollandaise_sauce_swirl_add_on.add_on_topping_name.configure(fg = 'black')
        Jalapenos.jalapenos_add_on.topping_button['state'] = NORMAL
        Jalapenos.jalapenos_add_on.add_on_topping_name.configure(fg='black')
        Mayonnaise.mayonnaise_add_on.topping_button['state'] = NORMAL
        Mayonnaise.mayonnaise_add_on.add_on_topping_name.configure(fg='black')
        Mushroom.mushroom_add_on.topping_button['state'] = NORMAL
        Mushroom.mushroom_add_on.add_on_topping_name.configure(fg='black')
        Olives.olives_add_on.topping_button['state'] = NORMAL
        Olives.olives_add_on.add_on_topping_name.configure(fg='black')
        Oregano.oregano_add_on.topping_button['state'] = NORMAL
        Oregano.oregano_add_on.add_on_topping_name.configure(fg='black')
        Pepperoni.pepperoni_add_on.topping_button['state'] = NORMAL
        Pepperoni.pepperoni_add_on.add_on_topping_name.configure(fg='black')
        Peri_peri_sauce_swirl.peri_peri_sauce_swirl_add_on.topping_button['state'] = NORMAL
        Peri_peri_sauce_swirl.peri_peri_sauce_swirl_add_on.add_on_topping_name.configure(fg='black')
        Pineapple.pineapple_add_on.topping_button['state'] = NORMAL
        Pineapple.pineapple_add_on.add_on_topping_name.configure(fg='black')
        Planet_based_Beef.planet_based_beef_add_on.topping_button['state'] = NORMAL
        Planet_based_Beef.planet_based_beef_add_on.add_on_topping_name.configure(fg='black')
        Prawns.prawns_add_on.topping_button['state'] = NORMAL
        Prawns.prawns_add_on.add_on_topping_name.configure(fg='black')
        Rasher_Bacon.rasher_bacon_add_on.topping_button['state'] = NORMAL
        Rasher_Bacon.rasher_bacon_add_on.add_on_topping_name.configure(fg='black')
        Red_onion.red_onions_add_on.topping_button['state'] = NORMAL
        Red_onion.red_onions_add_on.add_on_topping_name.configure(fg='black')
        Seasoned_Chicken.seasoned_chicken_add_on.topping_button['state'] = NORMAL
        Seasoned_Chicken.seasoned_chicken_add_on.add_on_topping_name.configure(fg='black')
        Spring_Onion.spring_onions_add_on.topping_button['state'] = NORMAL
        Spring_Onion.spring_onions_add_on.add_on_topping_name.configure(fg='black')
        Tomato_capsicum_sauce.tomato_capsicum_sauce_add_on.topping_button['state'] = NORMAL
        Tomato_capsicum_sauce.tomato_capsicum_sauce_add_on.add_on_topping_name.configure(fg='black')


    # Adjusting the position of other topping if this topping has been deleted
    if 'Anchovies' in intro_pages.storing_current_toppings:
        anchovies_placement = intro_pages.storing_current_toppings.index('Anchovies')
        anchovies_row = 0
        if anchovies_placement >= 8:
            anchovies_row = 1
            anchovies_placement -= 8
        else:
            anchovies_row = 0
            anchovies_placement = anchovies_placement
        Anchovies.anchovies_current.mini_labelframe.grid(row=anchovies_row, column=anchovies_placement)
    else:
        pass
    if "Baby Spinach" in intro_pages.storing_current_toppings:
        baby_spinach_placement = intro_pages.storing_current_toppings.index('Baby Spinach')
        baby_spinach_row = 0
        if baby_spinach_placement >= 8:
            baby_spinach_row = 1
            baby_spinach_placement -= 8
        else:
            baby_spinach_row = 0
            baby_spinach_placement = baby_spinach_placement
        Baby_spinach.baby_spinach_current.mini_labelframe.grid(row=baby_spinach_row, column=baby_spinach_placement)
    else:
        pass
    if "Camambert Cheese" in intro_pages.storing_current_toppings:
        camembert_cheese_placement = intro_pages.storing_current_toppings.index('Camambert Cheese')
        camembert_cheese_row = 0
        if camembert_cheese_placement >= 8:
            camembert_cheese_row = 1
            camembert_cheese_placement -= 8
        else:
            camembert_cheese_row = 0
            camembert_cheese_placement = camembert_cheese_placement
        Camembert_Cheese.camembert_cheese_current.mini_labelframe.grid(row=camembert_cheese_row, column=camembert_cheese_placement)
    else:
        pass
    if "Cherry Tomatos" in intro_pages.storing_current_toppings:
        cherry_tomatos_placement = intro_pages.storing_current_toppings.index('Cherry Tomatos')
        cherry_tomatos_row = 0
        if cherry_tomatos_placement >= 8:
            cherry_tomatos_row = 1
            cherry_tomatos_placement -= 8
        else:
            cherry_tomatos_row = 0
            cherry_tomatos_placement = cherry_tomatos_placement
        Cherry_tomato.cherry_tomatos_current.mini_labelframe.grid(row=cherry_tomatos_row, column=cherry_tomatos_placement)
    else:
        pass
    if "Cherry wood somked leg ham" in intro_pages.storing_current_toppings:
        cherry_wood_somked_leg_ham_placement = intro_pages.storing_current_toppings.index('Cherry wood somked leg ham')
        cherry_wood_somked_leg_ham_row = 0
        if cherry_wood_somked_leg_ham_placement >= 8:
            cherry_wood_somked_leg_ham_row = 1
            cherry_wood_somked_leg_ham_placement -= 8
        else:
            cherry_wood_somked_leg_ham_row = 0
            cherry_wood_somked_leg_ham_placement = cherry_wood_somked_leg_ham_placement
        Cherry_wood_somked_leg_ham.cherry_wood_somked_leg_ham_current.mini_labelframe.grid(row=cherry_wood_somked_leg_ham_row,column=cherry_wood_somked_leg_ham_placement)
    else:
        pass
    if "Chili Flakes" in intro_pages.storing_current_toppings:
        chili_flakes_placement = intro_pages.storing_current_toppings.index('Chili Flakes')
        chili_flakes_row = 0
        if chili_flakes_placement >= 8:
            chili_flakes_row = 1
            chili_flakes_placement -= 8
        else:
            chili_flakes_row = 0
            chili_flakes_placement = chili_flakes_placement
        Chili_Flakes.chili_flakes_current.mini_labelframe.grid(row=chili_flakes_row, column=chili_flakes_placement)
    else:
        pass
    if "Capsicum" in intro_pages.storing_current_toppings:
        capsicum_placement = intro_pages.storing_current_toppings.index('Capsicum')
        capsicum_row = 0
        if capsicum_placement >= 8:
            capsicum_row = 1
            capsicum_placement -= 8
        else:
            capsicum_row = 0
            capsicum_placement = capsicum_placement
        Capasicum.capsicum_current.mini_labelframe.grid(row=capsicum_row, column=capsicum_placement)
    else:
        pass
    if "Feta" in intro_pages.storing_current_toppings:
        feta_placement = intro_pages.storing_current_toppings.index('Feta')
        feta_row = 0
        if feta_placement >= 8:
            feta_row = 1
            feta_placement -= 8
        else:
            feta_row = 0
            feta_placement = feta_placement
        Feta.feta_current.mini_labelframe.grid(row=feta_row, column=feta_placement)
    else:
        pass
    if "Frank RedHot Original Hot Sauce" in intro_pages.storing_current_toppings:
        frank_redhot_original_hot_sauce_placement = intro_pages.storing_current_toppings.index(
            'Frank RedHot Original Hot Sauce')
        frank_redhot_original_hot_sauce_row = 0
        if frank_redhot_original_hot_sauce_placement >= 8:
            frank_redhot_original_hot_sauce_row = 1
            frank_redhot_original_hot_sauce_placement -= 8
        else:
            frank_redhot_original_hot_sauce_row = 0
            frank_redhot_original_hot_sauce_placement = frank_redhot_original_hot_sauce_placement
        Franks_RedHot_Orginal_Hot_Sauce.frank_redhot_original_hot_sauce_current.mini_labelframe.grid(row=frank_redhot_original_hot_sauce_row,column=frank_redhot_original_hot_sauce_placement)
    else:
        pass
    if "Fresh Tomatos" in intro_pages.storing_current_toppings:
        fresh_tomatos_placement = intro_pages.storing_current_toppings.index('Fresh Tomatos')
        fresh_tomatos_row = 0
        if fresh_tomatos_placement >= 8:
            fresh_tomatos_row = 1
            fresh_tomatos_placement -= 8
        else:
            fresh_tomatos_row = 0
            fresh_tomatos_placement = fresh_tomatos_placement
        Fresh_Tomatos.fresh_tomatos_current.mini_labelframe.grid(row=fresh_tomatos_row, column=fresh_tomatos_placement)
    else:
        pass
    if "Gralic Base Sauce Swirl" in intro_pages.storing_current_toppings:
        gralic_base_sauce_swirl_placement = intro_pages.storing_current_toppings.index('Gralic Base Sauce Swirl')
        gralic_base_sauce_swirl_row = 0
        if gralic_base_sauce_swirl_placement >= 8:
            gralic_base_sauce_swirl_row = 1
            gralic_base_sauce_swirl_placement -= 8
        else:
            gralic_base_sauce_swirl_row = 0
            gralic_base_sauce_swirl_placement = gralic_base_sauce_swirl_placement
        Gralic_base_sauce_swirl.gralic_base_sauce_swirl_current.mini_labelframe.grid(row=gralic_base_sauce_swirl_row,column=gralic_base_sauce_swirl_placement)
    else:
        pass
    if "Ground Beef" in intro_pages.storing_current_toppings:
        ground_beef_placement = intro_pages.storing_current_toppings.index('Ground Beef')
        ground_beef_row = 0
        if ground_beef_placement >= 8:
            ground_beef_row = 1
            ground_beef_placement -= 8
        else:
            ground_beef_row = 0
            ground_beef_placement = ground_beef_placement
        Ground_beef.ground_beef_current.mini_labelframe.grid(row=ground_beef_row, column=ground_beef_placement)
    else:
        pass
    if "Hickory BBQ Sauce" in intro_pages.storing_current_toppings:
        hickory_bbq_sauce_placement = intro_pages.storing_current_toppings.index('Hickory BBQ Sauce')
        hickory_bbq_sauce_row = 0
        if hickory_bbq_sauce_placement >= 8:
            hickory_bbq_sauce_row = 1
            hickory_bbq_sauce_placement -= 8
        else:
            hickory_bbq_sauce_row = 0
            hickory_bbq_sauce_placement = hickory_bbq_sauce_placement
        Hickory_BBQ_Sauce.hickory_bbq_sauce_current.mini_labelframe.grid(row=hickory_bbq_sauce_row,column=hickory_bbq_sauce_placement)
    else:
        pass
    if "Mozzarella Cheese" in intro_pages.storing_current_toppings:
        mozzarella_placement = intro_pages.storing_current_toppings.index("Mozzarella Cheese")
        row_of_mozzarella = 0
        if mozzarella_placement >= 8:
            row_of_mozzarella = 1
            mozzarella_placement -= 8
        else:
            row_of_mozzarella = 0
            mozzarella_placement = mozzarella_placement
        Mozzarella_topping.mozzarella_cheese_current.mini_labelframe.grid(row=row_of_mozzarella, column=mozzarella_placement)
    else:
        pass
    if "Paneer Cheese" in intro_pages.storing_current_toppings:
        paneer_cheese_placement = intro_pages.storing_current_toppings.index('Paneer Cheese')
        paneer_row = 0
        if paneer_cheese_placement >= 8:
            paneer_row = 1
            paneer_cheese_placement -= 8
        else:
            paneer_row = 0
            paneer_cheese_placement = paneer_cheese_placement
        Paneer_Cheese.paneer_cheese_current.mini_labelframe.grid(row=paneer_row, column=paneer_cheese_placement)
    else:
        pass
    if "Hollandaise Sauce Swirl" in intro_pages.storing_current_toppings:
        hollandaise_sauce_swirl_placement = intro_pages.storing_current_toppings.index('Hollandaise Sauce Swirl')
        hollandaise_sauce_swirl_row = 0
        if hollandaise_sauce_swirl_placement >= 8:
            hollandaise_sauce_swirl_row = 1
            hollandaise_sauce_swirl_placement -= 8
        else:
            hollandaise_sauce_swirl_row = 0
            hollandaise_sauce_swirl_placement = hollandaise_sauce_swirl_placement
        Hollandaise_sauce_swirl.hollandaise_sauce_swirl_current.mini_labelframe.grid(row=hollandaise_sauce_swirl_row,
                                                                                     column=hollandaise_sauce_swirl_placement)
    else:
        pass
    if "Jalapenos" in intro_pages.storing_current_toppings:
        jalapenos_placement = intro_pages.storing_current_toppings.index('Jalapenos')
        jalapenos_row = 0
        if jalapenos_placement >= 8:
            jalapenos_row = 1
            jalapenos_placement -= 8
        else:
            jalapenos_row = 0
            jalapenos_placement = jalapenos_placement
        Jalapenos.jalapenos_current.mini_labelframe.grid(row=jalapenos_row, column=jalapenos_placement)
    else:
        pass

    if "Mayonnaise" in intro_pages.storing_current_toppings:
        mayonnaise_placement = intro_pages.storing_current_toppings.index('Mayonnaise')
        mayonnaise_row = 0
        if mayonnaise_placement >= 8:
            mayonnaise_row = 1
            mayonnaise_placement -= 8
        else:
            mayonnaise_row = 0
            mayonnaise_placement = mayonnaise_placement
        Mayonnaise.mayonnaise_current.mini_labelframe.grid(row=mayonnaise_row, column=mayonnaise_placement)
    else:
        pass

    if "Mushroom" in intro_pages.storing_current_toppings:
        mushroom_placement = intro_pages.storing_current_toppings.index('Mushroom')
        mushroom_row = 0
        if mushroom_placement >= 8:
            mushroom_row = 1
            mushroom_placement -= 8
        else:
            mushroom_row = 0
            mushroom_placement = mushroom_placement
        Mushroom.mushroom_current.mini_labelframe.grid(row=mushroom_row, column=mushroom_placement)
    else:
        pass
    if "Olives" in intro_pages.storing_current_toppings:
        olives_placement = intro_pages.storing_current_toppings.index('Olives')
        olives_row = 0
        if olives_placement >= 8:
            olives_row = 1
            olives_placement -= 8
        else:
            olives_row = 0
            olives_placement = olives_placement
        Olives.olives_current.mini_labelframe.grid(row=olives_row, column=olives_placement)
    else:
        pass
    if "Oregano" in intro_pages.storing_current_toppings:
        oregano_placement = intro_pages.storing_current_toppings.index('Oregano')
        oregano_row = 0
        if oregano_placement >= 8:
            oregano_row = 1
            oregano_placement -= 8
        else:
            oregano_row = 0
            oregano_placement = oregano_placement
        Oregano.oregano_current.mini_labelframe.grid(row=oregano_row, column=oregano_placement)
    else:
        pass

    if "Pepperoni" in intro_pages.storing_current_toppings:
        pepperoni_placement = intro_pages.storing_current_toppings.index('Pepperoni')
        pepperoni_row = 0
        if pepperoni_placement >= 8:
            pepperoni_row = 1
            pepperoni_placement -= 8
        else:
            pepperoni_row = 0
            pepperoni_placement = pepperoni_placement
        Pepperoni.pepperoni_current.mini_labelframe.grid(row=pepperoni_row, column=pepperoni_placement)
    else:
        pass

    if "Peri Peri Sauce Swirl" in intro_pages.storing_current_toppings:
        peri_peri_sauce_swirl_placement = intro_pages.storing_current_toppings.index('Peri Peri Sauce Swirl')
        peri_peri_sauce_swirl_row = 0
        if peri_peri_sauce_swirl_placement >= 8:
            peri_peri_sauce_swirl_row = 1
            peri_peri_sauce_swirl_placement -= 8
        else:
            peri_peri_sauce_swirl_row = 0
            peri_peri_sauce_swirl_placement = peri_peri_sauce_swirl_placement
        Peri_peri_sauce_swirl.peri_peri_sauce_swirl_current.mini_labelframe.grid(row=peri_peri_sauce_swirl_row,
                                                                                 column=peri_peri_sauce_swirl_placement)
    else:
        pass
    if "Pineapple" in intro_pages.storing_current_toppings:
        pineapple_placement = intro_pages.storing_current_toppings.index('Pineapple')
        pineapple_row = 0
        if pineapple_placement >= 8:
            pineapple_row = 1
            pineapple_placement -= 8
        else:
            pineapple_row = 0
            pineapple_placement = pineapple_placement
        Pineapple.pineapple_current.mini_labelframe.grid(row=pineapple_row, column=pineapple_placement)
    else:
        pass
    if "Planet Based Beef" in intro_pages.storing_current_toppings:
        planet_based_beef_placement = intro_pages.storing_current_toppings.index('Planet Based Beef')
        planet_based_beef_row = 0
        if planet_based_beef_placement >= 8:
            planet_based_beef_row = 1
            planet_based_beef_placement -= 8
        else:
            planet_based_beef_row = 0
            planet_based_beef_placement = planet_based_beef_placement
        Planet_based_Beef.planet_based_beef_current.mini_labelframe.grid(row=planet_based_beef_row,
                                                                         column=planet_based_beef_placement)
    else:
        pass
    if "Prawns" in intro_pages.storing_current_toppings:
        prawns_placement = intro_pages.storing_current_toppings.index('Prawns')
        prawns_row = 0
        if prawns_placement >= 8:
            prawns_row = 1
            prawns_placement -= 8
        else:
            prawns_row = 0
            prawns_placement = prawns_placement
        Prawns.prawns_current.mini_labelframe.grid(row=prawns_row, column=prawns_placement)
    else:
        pass
    if "Rasher Bacon" in intro_pages.storing_current_toppings:
        rasher_bacon_placement = intro_pages.storing_current_toppings.index('Rasher Bacon')
        rasher_bacon_row = 0
        if rasher_bacon_placement >= 8:
            rasher_bacon_row = 1
            rasher_bacon_placement -= 8
        else:
            rasher_bacon_row = 0
            rasher_bacon_placement = rasher_bacon_placement
        Rasher_Bacon.rasher_bacon_current.mini_labelframe.grid(row=rasher_bacon_row, column=rasher_bacon_placement)
    else:
        pass
    if "Red Onions" in intro_pages.storing_current_toppings:
        red_onions_placement = intro_pages.storing_current_toppings.index('Red Onions')
        red_onions_row = 0
        if red_onions_placement >= 8:
            red_onions_row = 1
            red_onions_placement -= 8
        else:
            red_onions_row = 0
            red_onions_placement = red_onions_placement
        Red_onion.red_onions_current.mini_labelframe.grid(row=red_onions_row, column=red_onions_placement)
    else:
        pass
    if "Seasoned Chicken" in intro_pages.storing_current_toppings:
        seasoned_chicken_placement = intro_pages.storing_current_toppings.index('Seasoned Chicken')
        seasoned_chicken_row = 0
        if seasoned_chicken_placement >= 8:
            seasoned_chicken_row = 1
            seasoned_chicken_placement -= 8
        else:
            seasoned_chicken_row = 0
            seasoned_chicken_placement = seasoned_chicken_placement
        Seasoned_Chicken.seasoned_chicken_current.mini_labelframe.grid(row=seasoned_chicken_row,
                                                                       column=seasoned_chicken_placement)
    else:
        pass
    if "Spring Onions" in intro_pages.storing_current_toppings:
        spring_onions_placement = intro_pages.storing_current_toppings.index('Spring Onions')
        spring_onions_row = 0
        if spring_onions_placement >= 8:
            spring_onions_row = 1
            spring_onions_placement -= 8
        else:
            spring_onions_row = 0
            spring_onions_placement = spring_onions_placement
        Spring_Onion.spring_onions_current.mini_labelframe.grid(row=spring_onions_row, column=spring_onions_placement)
    else:
        pass
    if "Tomato Capsicum Sauce" in intro_pages.storing_current_toppings:
        tomato_capsicum_sauce_placement = intro_pages.storing_current_toppings.index('Tomato Capsicum Sauce')
        tomato_capsicum_sauce_row = 0
        if tomato_capsicum_sauce_placement >= 8:
            tomato_capsicum_sauce_row = 1
            tomato_capsicum_sauce_placement -= 8
        else:
            tomato_capsicum_sauce_row = 0
            tomato_capsicum_sauce_placement = tomato_capsicum_sauce_placement
        Tomato_capsicum_sauce.tomato_capsicum_sauce_current.mini_labelframe.grid(row=tomato_capsicum_sauce_row,
                                                                                 column=tomato_capsicum_sauce_placement)
    else:
        pass


    # Making button disbale if there still in the current topping
    if 'Anchovies' in intro_pages.storing_current_toppings:
        Anchovies.anchovies_add_on.topping_button['state'] = DISABLED
        Anchovies.anchovies_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Baby Spinach" in intro_pages.storing_current_toppings:
        Baby_spinach.baby_spinach_add_on.topping_button['state'] = DISABLED
        Baby_spinach.baby_spinach_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Camambert Cheese" in intro_pages.storing_current_toppings:
        Camembert_Cheese.camembert_cheese_add_on.topping_button['state'] = DISABLED
        Camembert_Cheese.camembert_cheese_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Cherry Tomatos" in intro_pages.storing_current_toppings:
        Cherry_tomato.cherry_tomatos_add_on.topping_button['state'] = DISABLED
        Cherry_tomato.cherry_tomatos_add_on.add_on_topping_name.configure(fg = '#DADADA')
    if "Cherry wood somked leg ham" in intro_pages.storing_current_toppings:
        Cherry_wood_somked_leg_ham.cherry_wood_somked_leg_ham_add_on.topping_button['state'] = DISABLED
        Cherry_wood_somked_leg_ham.cherry_wood_somked_leg_ham_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Chili Flakes" in intro_pages.storing_current_toppings:
        Chili_Flakes.chili_flakes_add_on.topping_button['state'] = DISABLED
        Chili_Flakes.chili_flakes_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Capsicum" in intro_pages.storing_current_toppings:
        Capasicum.capsicum_add_on.topping_button['state'] = DISABLED
        Capasicum.capsicum_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Feta" in intro_pages.storing_current_toppings:
        Feta.feta_add_on.topping_button['state'] = DISABLED
        Feta.feta_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Frank RedHot Original Hot Sauce" in intro_pages.storing_current_toppings:
        Franks_RedHot_Orginal_Hot_Sauce.frank_redhot_original_hot_sauce_add_on.topping_button['state'] = DISABLED
        Franks_RedHot_Orginal_Hot_Sauce.frank_redhot_original_hot_sauce_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Fresh Tomatos" in intro_pages.storing_current_toppings:
        Fresh_Tomatos.fresh_tomatos_add_on.topping_button['state'] = DISABLED
        Fresh_Tomatos.fresh_tomatos_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Gralic Base Sauce Swirl" in intro_pages.storing_current_toppings:
        Gralic_base_sauce_swirl.gralic_base_sauce_swirl_add_on.topping_button['state'] = DISABLED
        Gralic_base_sauce_swirl.gralic_base_sauce_swirl_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Ground Beef" in intro_pages.storing_current_toppings:
        Ground_beef.ground_beef_add_on.topping_button['state'] = DISABLED
        Ground_beef.ground_beef_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Hickory BBQ Sauce" in intro_pages.storing_current_toppings:
        Hickory_BBQ_Sauce.hickory_bbq_sauce_add_on.topping_button['state'] = DISABLED
        Hickory_BBQ_Sauce.hickory_bbq_sauce_add_on.add_on_topping_name.configure(fg= '#DADADA')
    if "Mozzarella Cheese" in intro_pages.storing_current_toppings:
        Mozzarella_topping.mozzarella_cheese_add_on.topping_button['state'] = DISABLED
        Mozzarella_topping.mozzarella_cheese_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Paneer Cheese" in intro_pages.storing_current_toppings:
        Paneer_Cheese.paneer_cheese_add_on.topping_button['state'] = DISABLED
        Paneer_Cheese.paneer_cheese_add_on.add_on_topping_name.configure(fg = '#DADADA')
    if "Hollandaise Sauce Swirl" in intro_pages.storing_current_toppings:
        Hollandaise_sauce_swirl.hollandaise_sauce_swirl_add_on.topping_button['state'] = DISABLED
        Hollandaise_sauce_swirl.hollandaise_sauce_swirl_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Jalapenos" in intro_pages.storing_current_toppings:
        Jalapenos.jalapenos_add_on.topping_button['state'] = DISABLED
        Jalapenos.jalapenos_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Mayonnaise" in intro_pages.storing_current_toppings:
        Mayonnaise.mayonnaise_add_on.topping_button['state'] = DISABLED
        Mayonnaise.mayonnaise_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Mushroom" in intro_pages.storing_current_toppings:
        Mushroom.mushroom_add_on.topping_button['state'] = DISABLED
        Mushroom.mushroom_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Olives" in intro_pages.storing_current_toppings:
        Olives.olives_add_on.topping_button['state'] = DISABLED
        Olives.olives_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Oregano" in intro_pages.storing_current_toppings:
        Oregano.oregano_add_on.topping_button['state'] = DISABLED
        Oregano.oregano_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Pepperoni" in intro_pages.storing_current_toppings:
        Pepperoni.pepperoni_add_on.topping_button['state'] = DISABLED
        Pepperoni.pepperoni_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Peri Peri Sauce Swirl" in intro_pages.storing_current_toppings:
        Peri_peri_sauce_swirl.peri_peri_sauce_swirl_add_on.topping_button['state'] = DISABLED
        Peri_peri_sauce_swirl.peri_peri_sauce_swirl_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Pineapple" in intro_pages.storing_current_toppings:
        Pineapple.pineapple_add_on.topping_button['state'] = DISABLED
        Pineapple.pineapple_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Planet Based Beef" in intro_pages.storing_current_toppings:
        Planet_based_Beef.planet_based_beef_add_on.topping_button['state'] = DISABLED
        Planet_based_Beef.planet_based_beef_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Prawns" in intro_pages.storing_current_toppings:
        Prawns.prawns_add_on.topping_button['state'] = DISABLED
        Prawns.prawns_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Rasher Bacon" in intro_pages.storing_current_toppings:
        Rasher_Bacon.rasher_bacon_add_on.topping_button['state'] = DISABLED
        Rasher_Bacon.rasher_bacon_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Red Onions" in intro_pages.storing_current_toppings:
        Red_onion.red_onions_add_on.topping_button['state'] = DISABLED
        Red_onion.red_onions_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Seasoned Chicken" in intro_pages.storing_current_toppings:
        Seasoned_Chicken.seasoned_chicken_add_on.topping_button['state'] = DISABLED
        Seasoned_Chicken.seasoned_chicken_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Spring Onions" in intro_pages.storing_current_toppings:
        Spring_Onion.spring_onions_add_on.topping_button['state'] = DISABLED
        Spring_Onion.spring_onions_add_on.add_on_topping_name.configure(fg='#DADADA')
    if "Tomato Capsicum Sauce" in intro_pages.storing_current_toppings:
        Tomato_capsicum_sauce.tomato_capsicum_sauce_add_on.topping_button['state'] = DISABLED
        Tomato_capsicum_sauce.tomato_capsicum_sauce_add_on.add_on_topping_name.configure(fg='#DADADA')


# Converting gralic_permesan_sauce cheese into current topping
def gralic_permesan_sauce_becomes_current():
    global gralic_permesan_sauce_current
    intro_pages.storing_current_toppings.append('Gralic Permesan Sauce')
    gralic_permesan_sauce_current = expanding_pages.Current_topping_generator(intro_pages.current_labelframe_only, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Toppings\Gralic Parmesan suace.png",
    "Gralic\nPermesan\nSauce\n", remove_gralic_permesan_sauce,0,0)
    gralic_permesan_sauce_add_on.topping_button['state'] = DISABLED
    gralic_permesan_sauce_add_on.add_on_topping_name.configure(fg = '#DADADA')


    if len(intro_pages.storing_current_toppings) > 9:
        Anchovies.anchovies_add_on.topping_button['state'] = DISABLED
        Anchovies.anchovies_add_on.add_on_topping_name.configure(fg='#DADADA')
        Baby_spinach.baby_spinach_add_on.topping_button['state'] = DISABLED
        Baby_spinach.baby_spinach_add_on.add_on_topping_name.configure(fg= '#DADADA')
        Camembert_Cheese.camembert_cheese_add_on.topping_button['state'] = DISABLED
        Camembert_Cheese.camembert_cheese_add_on.add_on_topping_name.configure(fg= '#DADADA')
        Cherry_tomato.cherry_tomatos_add_on.topping_button['state'] = DISABLED
        Cherry_tomato.cherry_tomatos_add_on.add_on_topping_name.configure(fg = '#DADADA')
        Cherry_wood_somked_leg_ham.cherry_wood_somked_leg_ham_add_on.topping_button['state'] = DISABLED
        Cherry_wood_somked_leg_ham.cherry_wood_somked_leg_ham_add_on.add_on_topping_name.configure(fg='#DADADA')
        Chili_Flakes.chili_flakes_add_on.topping_button['state'] = DISABLED
        Chili_Flakes.chili_flakes_add_on.add_on_topping_name.configure(fg = '#DADADA')
        Capasicum.capsicum_add_on.topping_button['state'] = DISABLED
        Capasicum.capsicum_add_on.add_on_topping_name.configure(fg='#DADADA')
        Feta.feta_add_on.topping_button['state'] = DISABLED
        Feta.feta_add_on.add_on_topping_name.configure(fg= '#DADADA')
        Franks_RedHot_Orginal_Hot_Sauce.frank_redhot_original_hot_sauce_add_on.topping_button['state'] = DISABLED
        Franks_RedHot_Orginal_Hot_Sauce.frank_redhot_original_hot_sauce_add_on.add_on_topping_name.configure(fg='#DADADA')
        Fresh_Tomatos.fresh_tomatos_add_on.topping_button['state'] = DISABLED
        Fresh_Tomatos.fresh_tomatos_add_on.add_on_topping_name.configure(fg='#DADADA')
        Gralic_base_sauce_swirl.gralic_base_sauce_swirl_add_on.topping_button['state'] = DISABLED
        Gralic_base_sauce_swirl.gralic_base_sauce_swirl_add_on.add_on_topping_name.configure(fg='#DADADA')
        gralic_permesan_sauce_add_on.topping_button['state'] = DISABLED
        gralic_permesan_sauce_add_on.add_on_topping_name.configure(fg= '#DADADA')
        Ground_beef.ground_beef_add_on.topping_button['state'] = DISABLED
        Ground_beef.ground_beef_add_on.add_on_topping_name.configure(fg='#DADADA')
        Hickory_BBQ_Sauce.hickory_bbq_sauce_add_on.topping_button['state'] = DISABLED
        Hickory_BBQ_Sauce.hickory_bbq_sauce_add_on.add_on_topping_name.configure(fg= '#DADADA')
        Mozzarella_topping.mozzarella_cheese_add_on.topping_button['state'] = DISABLED
        Mozzarella_topping.mozzarella_cheese_add_on.add_on_topping_name.configure(fg='#DADADA')
        Paneer_Cheese.paneer_cheese_add_on.topping_button['state'] = DISABLED
        Paneer_Cheese.paneer_cheese_add_on.add_on_topping_name.configure(fg= '#DADADA')
        Hollandaise_sauce_swirl.hollandaise_sauce_swirl_add_on.topping_button['state'] = DISABLED
        Hollandaise_sauce_swirl.hollandaise_sauce_swirl_add_on.add_on_topping_name.configure(fg='#DADADA')
        Jalapenos.jalapenos_add_on.topping_button['state'] = DISABLED
        Jalapenos.jalapenos_add_on.add_on_topping_name.configure(fg='#DADADA')
        Mayonnaise.mayonnaise_add_on.topping_button['state'] = DISABLED
        Mayonnaise.mayonnaise_add_on.add_on_topping_name.configure(fg='#DADADA')
        Mushroom.mushroom_add_on.topping_button['state'] = DISABLED
        Mushroom.mushroom_add_on.add_on_topping_name.configure(fg='#DADADA')
        Olives.olives_add_on.topping_button['state'] = DISABLED
        Olives.olives_add_on.add_on_topping_name.configure(fg='#DADADA')
        Oregano.oregano_add_on.topping_button['state'] = DISABLED
        Oregano.oregano_add_on.add_on_topping_name.configure(fg='#DADADA')
        Pepperoni.pepperoni_add_on.topping_button['state'] = DISABLED
        Pepperoni.pepperoni_add_on.add_on_topping_name.configure(fg='#DADADA')
        Peri_peri_sauce_swirl.peri_peri_sauce_swirl_add_on.topping_button['state'] = DISABLED
        Peri_peri_sauce_swirl.peri_peri_sauce_swirl_add_on.add_on_topping_name.configure(fg='#DADADA')
        Pineapple.pineapple_add_on.topping_button['state'] = DISABLED
        Pineapple.pineapple_add_on.add_on_topping_name.configure(fg='#DADADA')
        Planet_based_Beef.planet_based_beef_add_on.topping_button['state'] = DISABLED
        Planet_based_Beef.planet_based_beef_add_on.add_on_topping_name.configure(fg='#DADADA')
        Prawns.prawns_add_on.topping_button['state'] = DISABLED
        Prawns.prawns_add_on.add_on_topping_name.configure(fg='#DADADA')
        Rasher_Bacon.rasher_bacon_add_on.topping_button['state'] = DISABLED
        Rasher_Bacon.rasher_bacon_add_on.add_on_topping_name.configure(fg='#DADADA')
        Red_onion.red_onions_add_on.topping_button['state'] = DISABLED
        Red_onion.red_onions_add_on.add_on_topping_name.configure(fg='#DADADA')
        Seasoned_Chicken.seasoned_chicken_add_on.topping_button['state'] = DISABLED
        Seasoned_Chicken.seasoned_chicken_add_on.add_on_topping_name.configure(fg='#DADADA')
        Spring_Onion.spring_onions_add_on.topping_button['state'] = DISABLED
        Spring_Onion.spring_onions_add_on.add_on_topping_name.configure(fg='#DADADA')
        Tomato_capsicum_sauce.tomato_capsicum_sauce_add_on.topping_button['state'] = DISABLED
        Tomato_capsicum_sauce.tomato_capsicum_sauce_add_on.add_on_topping_name.configure(fg='#DADADA')
    else:
        pass

    #Postion this topping using storing list indexs
    gralic_permesan_sauce_placement = intro_pages.storing_current_toppings.index('Gralic Permesan Sauce')
    gralic_permesan_sauce_row = 0
    if gralic_permesan_sauce_placement >= 8:
        gralic_permesan_sauce_row = 1
        gralic_permesan_sauce_placement -= 8
    else:
        gralic_permesan_sauce_row = 0
        gralic_permesan_sauce_placement = gralic_permesan_sauce_placement
    gralic_permesan_sauce_current.mini_labelframe.grid(row=gralic_permesan_sauce_row, column=gralic_permesan_sauce_placement)


# gralic_permesan_sauce cheese to add_on toppings
gralic_permesan_sauce_add_on = expanding_pages.Add_on_topping_generator(intro_pages.add_on_topping_labelframe_only, r"C:\Users\ajayb\PycharmProjects\Henderson_Pizza_Palace\Toppings\Gralic Parmesan suace.png"
,"Gralic\nPermesan\nSauce\n", 2,3, gralic_permesan_sauce_becomes_current)


# Importing all other toppings
from Bacon_and_Aioli_page import Mozzarella_topping, Paneer_Cheese, Anchovies, Baby_spinach, Camembert_Cheese, Cherry_tomato, Cherry_wood_somked_leg_ham, Chili_Flakes, Capasicum, Feta, Franks_RedHot_Orginal_Hot_Sauce, Fresh_Tomatos, Gralic_base_sauce_swirl, Ground_beef, Hickory_BBQ_Sauce,\
Hollandaise_sauce_swirl, Jalapenos, Mayonnaise, Mushroom, Olives, Oregano, Pepperoni, Peri_peri_sauce_swirl, Pineapple, Planet_based_Beef, Prawns, Rasher_Bacon, Red_onion, Seasoned_Chicken, Spring_Onion, Tomato_capsicum_sauce
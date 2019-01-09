#!/usr/bin/python

import string
import random


#character class

class enemy:
    name = ""
    description = ""
    health = 0
    damage = 0

class weapon:
    name = ""
    damage = 0
    value = 0

basic_stick = weapon()
basic_stick.name = "basic_stick"
basic_stick.damage = 1
basic_stick.value = 1

club = weapon()
club.name = "club"
club.damage = 5
club.value = 10

holder_spot = weapon()



class item:
    name = "empty"
    heal = 0
    value = 0

empty = item()

minor_health_potion = item()
minor_health_potion.name = "minor health potion"
minor_health_potion.heal = 5
minor_health_potion.value = 10

quartz_stone = item()
quartz_stone.name = "Quartz Stone"
quartz_stone.value = 30

class player:
    player_name = ""
    weapon = basic_stick
    item1 = empty
    item2 = empty
    item3 = empty
    health = 10
    money = 0
    max_health = 10
    holder = holder_spot

class chest:
    item1 = empty
    item2 = empty
    item3 = empty

class shopkeeper:
    item1 = empty
    item2 = empty
    item3 = empty
    item4 = empty

Earl = shopkeeper()
Earl.item1 = basic_stick
Earl.item2 = club
Earl.item3 = minor_health_potion
Earl.item4 = minor_health_potion

#Enemies #########################################

#Squawker
squawker = enemy()
squawker.name = "Squawker"
squawker.description = "Feisty Bird of the woods. Not overly powerful, but always willing to start a fight"
squawker.health = 6
squawker.damage = 2

#Bully
bully = enemy()
bully.name = "Bully"
bully.description = "Rough little creatures with bulging muscles and ferocious claws. Pack a hit but can't take one themselves"
bully.health = 1
bully.damage = 4

#Elfen
elfen = enemy()
elfen.name = "Elfen"
elfen.description = "A rare sight for those unlucky to come across them. They're cunning and quick and hate disturbances"
elfen.health = 5
elfen.damage = 3



#randoms
reg_crit = [-1,0,0,0,0,1]
enemies1 = [squawker,squawker, squawker, bully, bully, elfen]

    
#functions
def __init__(player,name, weapon, health):
    player.player_name = name
    player.weapon = weapon
    player.health  = health

def end_game():
    exit

def battle(enemy):
    global my_player
    print("You have come across a " + enemy.name + "!")
    done = False
    while done ==False:
        choice = input("Will you attack, use an item, or run? (1,2,3): ")
        if choice == "1":
            crit = random.choice(reg_crit)
            if crit == 0:
                enemy.health = enemy.health - my_player.weapon.damage
                print("Hit opponent for "+str(my_player.weapon.damage)+" damage!")
            elif crit == -1:
                print("Oh no, attack missed!")
            else:
                enemy.health = enemy.health - (my_player.weapon.damage * 2)
                print("Hit opponent for "+str(my_player.weapon.damage * 2)+" damage!")
            if enemy.health <= 0:
                print("Foe is down!")
                return
            print("Foe has " + str(enemy.health) + " health left")

            
        if choice == "2":
            print_inventory()
            print(" ")
            done2 = False
            while done2 == False:
                item_choice = input("What would you like to use? (1,2,3): ")
                if item_choice == "1":
                    if my_player.item1.heal > 0:
                        use_healable(my_player.item1)
                        done2 = True
                    else:
                        print("Cannot use that item!")
                if item_choice == "2":
                    if my_player.item2.heal > 0:
                        use_healable(my_player.item2)
                        done2 =True
                    else:
                        print("Cannot use that item!")
                if item_choice == "3":
                    if my_player.item3.heal > 0:
                        use_healable(my_player.item3)
                        done2 = True
                    else:
                        print("Cannot use that item!")
            

        if choice == "3":
            run = random.choice(reg_crit)
            if run == 0:
                print("ran away successfully!")
                return
            else:
                print("couldn't get away!")
        print("The enemy attacks!")
        my_player.health = my_player.health - enemy.damage
        print("Does "+str(enemy.damage)+" damage! Now have " + str(my_player.health) + " health!")
        if my_player.health <= 0:
            print("Oh no! you have died! Well done in your game play again soon")
            end_game()
        
        

def Oysterville():
    print("Your journey begins in the small coast town of Oysterville.")
    done = False
    while done == False:
        print("To your left, a small trade shop, and to your right is a the glistening ocean, sparkling in the warm sun")
        lr = input("Would you like to go to the shop, check out the ocean or venture onward? (press 4 to check inventory) (1,2,3,4): ")
        if lr == "1":
            print("You enter the quaint little shop")
            shopkeeper_iteraction(Earl)
            print("Upon leaving the shop you arrive back in the town square")
        if lr == "2":
            print("You approach the beach, and the wind picks up. It is quiet on the beach and to your surprise you find a small cache in the sand")
            chest_opening()
            print("You say goodbye to the beach and head back to town")
        if lr == "4":
            check_inventory()
        if lr == "3":
            road1()
            return



def road1():
    print("You're walking down the road, the sky is grim and the world is dimming as the sun sets")
    battle(random.choice(enemies1))
    return



def option():
    choice = input("Would you like to check inventory, or continue onward? (1,2): ")
    if choice == "1":
        #cue inventory function
        check_inventory()
    if choice == "2":
        #cue onward
        onward()
    else:
        option()

def item_user():
    print("holder")

def use_healable(item):
    global my_player
    my_player.health = my_player.health + item.heal
    if my_player.health > my_player.max_health:
        my_player.health = my_player.max_health

def check_weapon_data(weapon):
    print("Weapon name: " + str(weapon.name))
    print("Damage: " + str(weapon.damage))
    check_inventory()

def check_health_item_data(item):
    print("Healable name: " + item.name)
    print("Heals: " + str(item.heal) + " HP")
    print("Healable value: " + str(item.value))
    check_inventory()

def check_item_data(item):
    print("Item name: " + item.name)
    print("Item value: " + str(item.value))
    check_inventory()

def print_inventory():
    print(" ")
    print("Here is your current inventory")
    print("Primary weapon: " + my_player.weapon.name)
    print("Item 1: " + my_player.item1.name)
    print("Item 2: " + my_player.item2.name)
    print("Item 3: " + my_player.item3.name)
    print("Health: " + str(my_player.health))
    print("Money: " + str(my_player.money))

def check_inventory():
    print(" ")
    global my_player
    print("Here is your current inventory")
    print("Primary weapon: " + my_player.weapon.name)
    print("Item 1: " + my_player.item1.name)
    print("Item 2: " + my_player.item2.name)
    print("Item 3: " + my_player.item3.name)
    print("Health: " + str(my_player.health))
    print("Money: " + str(my_player.money))
    response = input("Would you like to change primary weapon/use an item, throw away an item, examine an item or exit inventory? (1,2,3,4): ")
    print(" ")
    if response == "1":
        item_choice = input("Which item? (1,2,3): ")
        if item_choice == "1":
            if isinstance(my_player.item1, weapon):
                my_player.holder = my_player.weapon
                my_player.weapon = my_player.item1
                my_player.item1 = my_player.holder
                my_player.holder = holder_spot
            if isinstance(my_player.item1, item):
                if my_player.item1.heal != 0:
                    use_healable(my_player.item1)
                else:
                    print("Cannot use this item")
                    check_inventory()
        if item_choice == "2":
            if isinstance(my_player.item2, weapon):
                my_player.holder = my_player.weapon
                my_player.weapon = my_player.item2
                my_player.item2 = my_player.holder
                my_player.holder = holder_spot
            if isinstance(my_player.item2, item):
                if my_player.item2.heal != 0:
                    use_healable(my_player.item2)
                else:
                    print("Cannot use this item")
                    check_inventory()
        if item_choice == "3":
            if isinstance(my_player.item3, weapon):
                my_player.holder = my_player.weapon
                my_player.weapon = my_player.item3
                my_player.item3 = my_player.holder
                my_player.holder = holder_spot
            if isinstance(my_player.item3, item):
                if my_player.item3.heal != 0:
                    use_healable(my_player.item3)
                else:
                    print("Cannot use this item")
                    check_inventory()
        else:
            check_inventory()

    if response == "2":
        delete_choice = input("Which item would you like to discard? (1,2,3): ")
        if delete_choice == "1":
            my_player.item1 = empty
        if delete_choice == "2":
            my_player.item2 = empty
        if delete_choice == "3":
            my_player.item3 = empty
        else:
            check_inventory()
        check_inventory()

    if response == "3":
        check_choice = input("Which item would you like to check? (1,2,3): ")
        if check_choice == "1":
            if isinstance(my_player.item1, weapon):
                check_weapon_data(my_player.item1)
            if isinstance(my_player.item1, item):
                if my_player.item1.heal != 0:
                     check_health_item_data(my_player.item1)
                else:
                    check_item_data(my_player.item1)
        if check_choice == "2":
            if isinstance(my_player.item2, weapon):
                check_weapon_data(my_player.item2)
            if isinstance(my_player.item2, item):
                if my_player.item2.heal != 0:
                     check_health_item_data(my_player.item2)
                else:
                    check_item_data(my_player.item2)
        if check_choice == "3":
            if isinstance(my_player.item3, weapon):
                check_weapon_data(my_player.item3)
            if isinstance(my_player.item3, item):
                if my_player.item3.heal != 0:
                     check_health_item_data(my_player.item3)
                else:
                    check_item_data(my_player.item3)
        else:
            check_inventory()
            
    if response == "4":
        print("exiting inventory")
        return

#Finding a chest
basic_chest_loot = [club, minor_health_potion, minor_health_potion, quartz_stone, empty,empty,empty]
def chest_opening():
    global my_player
    new_chest = chest()
    new_chest.item1 = random.choice(basic_chest_loot)
    new_chest.item2 = random.choice(basic_chest_loot)
    new_chest.item3 = random.choice(basic_chest_loot)
    print("You have found a basic chest! Inside is: ")
    print("Item 1: " + new_chest.item1.name)
    print("Item 2: " + new_chest.item2.name)
    print("Item 3: " + new_chest.item3.name)
    done = False
    while(done == False):
        take = input("Which item would you like to take?(1,2,3,4 = none): ")
        if take == "1":
            if my_player.item1 == empty:
                my_player.item1 = new_chest.item1
            elif my_player.item2 == empty:
                my_player.item2 = new_chest.item1               
            elif my_player.item3 == empty:
                my_player.item3 = new_chest.item1
            else:
                removal = input("Inventory full, choose a slot to discard or choose to keep inventory (1,2,3,4): ")
                if removal == "1":
                    my_player.item1 = new_chest.item1
                if removal == "2":
                    my_player.item2 = new_chest.item1
                if removal == "3":
                    my_player.item3 = new_chest.item1
        if take == "2":
            if my_player.item1 == empty:
                my_player.item1 = new_chest.item2
            elif my_player.item2 == empty:
                my_player.item2 = new_chest.item2               
            elif my_player.item3 == empty:
                my_player.item3 = new_chest.item2
            else:
                removal = input("Inventory full, choose a slot to discard or choose to keep inventory (1,2,3,4): ")
                if removal == "1":
                    my_player.item1 = new_chest.item2
                if removal == "2":
                    my_player.item2 = new_chest.item2
                if removal == "3":
                    my_player.item3 = new_chest.item2
        if take == "3":
            if my_player.item1 == empty:
                my_player.item1 = new_chest.item3
            elif my_player.item2 == empty:
                my_player.item2 = new_chest.item3              
            elif my_player.item3 == empty:
                my_player.item3 = new_chest.item3
            else:
                removal = input("Inventory full, choose a slot to discard or choose to keep inventory (1,2,3,4): ")
                if removal == "1":
                    my_player.item1 = new_chest.item3
                if removal == "2":
                    my_player.item2 = new_chest.item3
                if removal == "3":
                    my_player.item3 = new_chest.item3
        print_inventory()
        is_done = input("Finished search chest? (yes = 1, no = 2): ")
        if is_done == "1":
            done = True

def shopkeeper_iteraction(shopkeeper):
    global my_player
    done = False
    while done == False:
        bs = input("Welcome to the store! Would you like to buy or sell? (1,2): ")
        if bs == "1":
            print("Here is my inventory: ")
            print("Item1: " + shopkeeper.item1.name + " Cost: " + str(shopkeeper.item1.value))
            print("Item2: " + shopkeeper.item2.name + " Cost: " + str(shopkeeper.item2.value))
            print("Item3: " + shopkeeper.item3.name + " Cost: " + str(shopkeeper.item3.value))
            print("Item4: " + shopkeeper.item4.name + " Cost: " + str(shopkeeper.item4.value))
            purchase = input("Which would you like to buy? (1,2,3,4,5 = none): ")
            if purchase == "1":
                if my_player.money >= shopkeeper.item1.value:
                    my_player.money = my_player.money - shopkeeper.item1.value
                    print("Thank you, you now have " + str(my_player.money) + " dollars")
                    if my_player.item1 == empty:
                        my_player.item1 = shopkeeper.item1
                    elif my_player.item2 == empty:
                        my_player.item2 = shopkeeper.item1
                    elif my_player.item3 == empty:
                        my_player.item3 = shopkeeper.item1
                    else:
                        removal = input("Inventory full, choose a slot to discard or choose to keep inventory (1,2,3,4): ")
                        if removal == "1":
                            my_player.item1 = shopkeeper.item1
                        if removal == "2":
                            my_player.item2 = shopkeeper.item1
                        if removal == "3":
                            my_player.item3 = shopkeeper.item1                    
                else:
                    print("Sorry you do not have enough money to purchase this item")
                shopkeeper.item1 = empty
                    
            if purchase == "2":
                if my_player.money >= shopkeeper.item2.value:
                    my_player.money = my_player.money - shopkeeper.item2.value
                    print("Thank you, you now have " + str(my_player.money) + " dollars")
                    if my_player.item1 == empty:
                        my_player.item1 = shopkeeper.item2
                    elif my_player.item2 == empty:
                        my_player.item2 = shopkeeper.item2      
                    elif my_player.item3 == empty:
                        my_player.item3 = shopkeeper.item2
                    else:
                        removal = input("Inventory full, choose a slot to discard or choose to keep inventory (1,2,3,4): ")
                        if removal == "1":
                            my_player.item1 = shopkeeper.item2
                        if removal == "2":
                            my_player.item2 = shopkeeper.item2
                        if removal == "3":
                            my_player.item3 = shopkeeper.item2                   
                else:
                    print("Sorry you do not have enough money to purchase this item")
                shopkeeper.item2 = empty

            if purchase == "3":
                if my_player.money >= shopkeeper.item3.value:
                    my_player.money = my_player.money - shopkeeper.item3.value
                    print("Thank you, you now have " + str(my_player.money) + " dollars")
                    if my_player.item1 == empty:
                        my_player.item1 = shopkeeper.item3
                    elif my_player.item2 == empty:
                        my_player.item2 = shopkeeper.item3       
                    elif my_player.item3 == empty:
                        my_player.item3 = shopkeeper.item3
                    else:
                        removal = input("Inventory full, choose a slot to discard or choose to keep inventory (1,2,3,4): ")
                        if removal == "1":
                            my_player.item1 = shopkeeper.item3
                        if removal == "2":
                            my_player.item2 = shopkeeper.item3
                        if removal == "3":
                            my_player.item3 = shopkeeper.item3                
                else:
                    print("Sorry you do not have enough money to purchase this item")
                shopkeeper.item3 = empty

            if purchase == "4":
                if my_player.money >= shopkeeper.item4.value:
                    my_player.money = my_player.money - shopkeeper.item4.value
                    print("Thank you, you now have " + str(my_player.money) + " dollars")
                    if my_player.item1 == empty:
                        my_player.item1 = shopkeeper.item4
                    elif my_player.item2 == empty:
                        my_player.item2 = shopkeeper.item4     
                    elif my_player.item3 == empty:
                        my_player.item3 = shopkeeper.item4
                    else:
                        removal = input("Inventory full, choose a slot to discard or choose to keep inventory (1,2,3,4): ")
                        if removal == "1":
                            my_player.item1 = shopkeeper.item4
                        if removal == "2":
                            my_player.item2 = shopkeeper.item4
                        if removal == "3":
                            my_player.item3 = shopkeeper.item4                 
                else:
                    print("Sorry you do not have enough money to purchase this item")
                shopkeeper.item4 = empty
        if bs == "2":
            print_inventory()
            sell_choice = input("Which item would you like to sell?(1,2,3): ")
            if sell_choice == "1":
                print("Great, I can give " + str(int(my_player.item1.value * 0.5)) + " dollars for that")
                my_player.money = int(my_player.item1.value * 0.5) + my_player.money
                print("You now have " + str(my_player.money) + " dollars")
                my_player.item1  = empty
            if sell_choice == "2":
                print("Great, I can give " + str(int(my_player.item2.value * 0.5)) + " dollars for that")
                my_player.money = int(my_player.item2.value * 0.5) + my_player.money
                print("You now have " + str(my_player.money) + " dollars")
                my_player.item2  = empty
            if sell_choice == "3":
                print("Great, I can give " + str(int(my_player.item3.value * 0.5)) + " dollars for that")
                my_player.money = int(my_player.item3.value * 0.5) + my_player.money
                print("You now have " + str(my_player.money) + " dollars")
                my_player.item3  = empty
        print_inventory()
        is_done = input("Done shopping? (1 = yes, 2 = no): ")
        if is_done == "1":
             return
        
                    
    
        
    

#The game
print("Welcome to Azura")
my_name = input("What is your name?: ")
print(my_name + ", your journey is about to begin.")
print("Can you find your way to Mt. Colossus and claim your prize")
my_player = player()
my_player.player_name = my_name
my_player.weapon = basic_stick
my_player.health = 10.0
my_player.max_health = 10.0
my_player.item1 = club
my_player.item2 = minor_health_potion
my_player.item3 = quartz_stone
Oysterville()


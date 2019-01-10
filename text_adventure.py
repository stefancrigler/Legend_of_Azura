#!/usr/bin/env python3

import random


'''This is the world of Azura, a text based adventure game with enemy battles, quests, 
decision making, stores, looting and over 120 unique weapons to use. Enjoy the game! -Stefan'''


#enemies#################
class enemy:
    name = ""
    description = ""
    health = 0
    damage = 0
    exp = 0

#Squawker
squawker = enemy()
squawker.name = "Squawker"
squawker.description = "Feisty Bird of the woods. Not overly powerful, but always willing to start a fight"
squawker.health = 6
squawker.damage = 2
squawker.exp = 4

#Bully
bully = enemy()
bully.name = "Bully"
bully.description = "Rough little creatures with bulging muscles and ferocious claws. Pack a hit but can't take one themselves"
bully.health = 1
bully.damage = 4
bully.exp = 6

#Elfen
elfen = enemy()
elfen.name = "Elfen"
elfen.description = "A rare sight for those unlucky to come across them. They're cunning and quick and hate disturbances"
elfen.health = 5
elfen.damage = 3
elfen.exp = 11

#Clawer
clawer = enemy()
clawer.name = "Clawer"
clawer.description = "A dark and terrible being which lurks in the woods. 50 percent leapord 50 percent menace"
clawer.health = 12
clawer.damage = 4
clawer.exp = 20

#Sabre Stallion
sabre_stallion = enemy()
sabre_stallion.name = "Sabre Stallion"
sabre_stallion.description = "Majestic and quick, this beast rarely shows its fangs. Don't come to close though, or it will show you it's power"
sabre_stallion.health = 10
sabre_stallion.damage = 6
sabre_stallion.exp = 25

#Erupter
erupter = enemy()
erupter.name = "Erupter"
erupter.description = "This small fellows resemble gnomes, but where they lack size they have a fiery temper"
erupter.health = 5
erupter.damage = 10
erupter.exp = 18

#Ghoul
ghoul = enemy()
ghoul.name = "Ghoul"
ghoul.description = "Frightful and cunning, these foes lurk only in the shadows"
ghoul.health = 14
ghoul.damage = 7
ghoul.exp = 35

#Velmore soldier
velmore_soldier = enemy()
velmore_soldier.name = "Velmore soldier"
velmore_soldier.description = "Though just a grunt in the Velmore fleet, carries heavy armor and menacing sword"
velmore_soldier.health = 20
velmore_soldier.damage = 7
velmore_soldier.exp = 48


#weapons##############################

class weapon:
    name = ""
    damage = 0
    value = 0

#stick
basic_stick = weapon()
basic_stick.name = "stick"
basic_stick.damage = 1
basic_stick.value = 1

#club
club = weapon()
club.name = "club"
club.damage = 3
club.value = 10

#axe
axe = weapon()
axe.name = "axe"
axe.damage = 5
axe.value = 30

#flayer
flayer = weapon()
flayer.name = "flayer"
flayer.damage = 8
flayer.value = 80

#mage staff
mage_staff = weapon()
mage_staff.name = "mage staff"
mage_staff.damage = 15
mage_staff.value = 140

holder_spot = weapon()

#quests ################
class quest:
    done = 0
    name = ""
    exp = 0

#roark_mess
roark_mess = quest()
roark_mess.name = "roark mess"
roark_mess.exp = 30

roarkton_bartender_quest = quest()
roarkton_bartender_quest.name = "the birds of gold"
roarkton_bartender_quest.exp = 10

#items#######################
class item:
    name = "empty"
    heal = 0
    value = 0

empty = item()

#minor health potion
minor_health_potion = item()
minor_health_potion.name = "minor health potion"
minor_health_potion.heal = 5
minor_health_potion.value = 10

#health potion
health_potion = item()
health_potion.name = "health potion"
health_potion.heal = 11
health_potion.value = 20

#magical health potion
magical_health_potion = item()
magical_health_potion.name = "magical health potion"
magical_health_potion.heal = 30
magical_health_potion.value = 50

#max health potion
max_health_potion = item()
max_health_potion.name = "minor health potion"
max_health_potion.heal = 1000
max_health_potion.value = 120

#quartz stone
quartz_stone = item()
quartz_stone.name = "Quartz Stone"
quartz_stone.value = 30

#rare apple
rare_apple = item()
rare_apple.name = "Rare Apple"
rare_apple.heal = 5
rare_apple.value = 40

#ruby
ruby = item()
ruby.name = "Ruby"
ruby.value = 100

#rough diamond
rough_diamond = item()
rough_diamond.name = "Rough Diamond"
rough_diamond.value = 200

#diamond
diamond = item()
diamond.name = "Diamond"
diamond.value = 500


#THE PLAYER################
class player:
    player_name = ""
    weapon = basic_stick
    item1 = empty
    item2 = empty
    item3 = empty
    health = 10
    money = 0
    max_health = 10
    current_quest = ""
    exp = 0
    needed_exp = 10
    lvl = 1
    holder = holder_spot

#chest class

class chest:
    item1 = empty
    item2 = empty
    item3 = empty

####### shopkeeper class

class shopkeeper:
    item1 = empty
    item2 = empty
    item3 = empty
    item4 = empty


#prefixes
class ix:
    name = ""
    damage = 0
    value = 0

old = ix()
old.name = "old"
old.damage = 0
old.value = 0

worn = ix()
worn.name = "worn"
worn.damage = 1
worn.value = 5

basic = ix()
basic.name = "basic"
basic.damage = 3
basic.value = 10

mighty = ix()
mighty.name = "mighty"
mighty.damage = 7
mighty.value = 30

terrorizing = ix()
terrorizing.name = "terrorizing"
terrorizing.damage = 11
terrorizing.value = 100

nuisance = ix()
nuisance.name = "nuisance"
nuisance.damage = 0
nuisance.value = 0

slapper = ix()
slapper.name = "slapper"
slapper.damage = 1
slapper.value = 10

enforcer = ix()
enforcer.name = "enforcer"
enforcer.damage = 4
enforcer.value = 45

menace = ix()
menace.name = "menace"
menace.damage = 9
menace.value = 100

god = ix()
god.name = "god"
god.damage = 15
god.value = 300


#randoms
reg_crit = [-1,0,0,0,0,1]
enemies1 = [squawker,squawker, squawker, bully, bully, elfen]
battle_chance = [0,0,1]
weapon_prefix_all = [old,worn,basic,mighty,terrorizing]
weapon_prefix_early_game = [old,old,worn,worn,worn,basic]
weapon_prefix_mid_game = [old,worn,worn,worn,basic,basic,basic,basic,mighty,mighty]
weapon_prefix_end_game = [basic,basic,basic,mighty,mighty,terrorizing]
weapon_suffix_all = [nuisance,slapper,enforcer,menace,god]
weapon_suffix_early_game = [nuisance,nuisance,nuisance,slapper,slapper]
weapon_suffix_mid_game = [nuisance,slapper,slapper,slapper,enforcer,enforcer,enforcer,menace]
weapon_suffix_end_game = [enforcer,menace,menace,menace,menace,god]
weapons_all = [basic_stick, club, axe, flayer, mage_staff]
weapons_early_game = [basic_stick,basic_stick,basic_stick,basic_stick,basic_stick,basic_stick,club,club,club,club,axe,axe]
weapons_mid_game = [basic_stick,club,club,club,club,club,axe,axe,axe,axe,flayer,flayer]
weapons_end_game = [basic_stick,club,club,axe,axe,axe,flayer,flayer,flayer,mage_staff]

    
#functions
def __init__(player,name, weapon, health):
    player.player_name = name
    player.weapon = weapon
    player.health  = health

def end_game():
    exit

#weapon makers

def weapon_maker_early_game():
    prefix = random.choice(weapon_prefix_early_game)
    suffix = random.choice(weapon_suffix_early_game)
    weapon_choice = random.choice(weapons_early_game)
    new_weapon = weapon()
    new_weapon.name = prefix.name + " " + weapon_choice.name + " " + suffix.name
    new_weapon.damage = prefix.damage  + weapon_choice.damage  + suffix.damage
    new_weapon.value = prefix.value  + weapon_choice.value  + suffix.value
    return new_weapon

def weapon_maker_mid_game():
    prefix = random.choice(weapon_prefix_mid_game)
    suffix = random.choice(weapon_suffix_mid_game)
    weapon_choice = random.choice(weapons_mid_game)
    new_weapon = weapon()
    new_weapon.name = prefix.name + " " + weapon_choice.name + " " + suffix.name
    new_weapon.damage = prefix.damage  + weapon_choice.damage  + suffix.damage
    new_weapon.value = prefix.value  + weapon_choice.value  + suffix.value
    return new_weapon

def weapon_maker_end_game():
    prefix = random.choice(weapon_prefix_end_game)
    suffix = random.choice(weapon_suffix_end_game)
    weapon_choice = random.choice(weapons_end_game)
    new_weapon = weapon()
    new_weapon.name = prefix.name + " " + weapon_choice.name + " " + suffix.name
    new_weapon.damage = prefix.damage  + weapon_choice.damage  + suffix.damage
    new_weapon.value = prefix.value  + weapon_choice.value  + suffix.value
    return new_weapon

def weapon_maker_all():
    prefix = random.choice(weapon_prefix_all)
    suffix = random.choice(weapon_suffix_all)
    weapon_choice = random.choice(weapons_all)
    new_weapon = weapon()
    new_weapon.name = prefix.name + " " + weapon_choice.name + " " + suffix.name
    new_weapon.damage = prefix.damage  + weapon_choice.damage  + suffix.damage
    new_weapon.value = prefix.value  + weapon_choice.value  + suffix.value
    return new_weapon
    
#battle functions

def battle(enemy):
    enemy_health = enemy.health
    global my_player
    global roarkton_bartender_quest
    print("\033[1;31;47mYou have come across a " + enemy.name + "!")
    done = False
    while done ==False:
        choice = input("\033[1;31;47mWill you attack, use an item, or run? (1,2,3): ")
        if choice == "1":
            crit = random.choice(reg_crit)
            if crit == 0:
                enemy.health = enemy.health - my_player.weapon.damage
                print("Hit opponent for "+str(my_player.weapon.damage)+" damage!")
            elif crit == -1:
                print("Oh no, attack missed!")
            else:
                enemy.health = enemy.health - (my_player.weapon.damage * 2)
                print("Critical Hit! "+str(my_player.weapon.damage * 2)+" damage!")
            if enemy.health <= 0:
                print("\033[1;31;47mFoe is down!")
                print("You have earned " + str(enemy.exp) + " experience!")
                if roarkton_bartender_quest.done == 2:
                    print("The bartender was right! $50 fell out of the squawkers mouth")
                    print("You have completed: the birds of gold")
                    print("Gain 10 exp")
                    gain_exp(10)
                    my_player.money = my_player.money + 50
                    roarkton_bartender_quest.done = 1
                gain_exp(enemy.exp)
                enemy.health = enemy_health
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

def gain_exp(x):
    global my_player
    my_player.exp = my_player.exp + x
    while my_player.exp >= my_player.needed_exp:
        gained_hp = random.randint(1,4)
        print("Woohoo! Level up! You gained " + str(gained_hp) + " health!" )
        my_player.max_health = my_player.max_health + gained_hp
        my_player.health = my_player.max_health
        my_player.exp = my_player.exp - my_player.needed_exp
        new_needed = int(my_player.needed_exp * 1.5)
        my_player.needed_exp = new_needed
        
def random_battle1():
    x = random.choice(battle_chance)
    if x =="1":
        battle(random.choice(enemies1))



#map functions ################

def Oysterville():
    print("\033[1;34;47mYour journey begins in the small coast town of Oysterville.")
    done = False
    while done == False:
        print("\033[1;34;47mTo your left, a small trade shop, and to your right is a the glistening ocean, sparkling in the warm sun")
        lr = input("Would you like to go to the shop, check out the ocean or venture onward? (press 4 to check inventory) (1,2,3,4): ")
        if lr == "1":
            print("You enter the quaint little shop")
            shopkeeper_iteraction(Earl)
            print("Upon leaving the shop you arrive back in the town square")
        if lr == "2":
            print("You approach the beach, and the wind picks up. It is quiet on the beach and to your surprise you find a small cache in the sand")
            chest_opening(1)
            print("You say goodbye to the beach and head back to town")
        if lr == "4":
            check_inventory()
        if lr == "3":
            road1()
            return



def road1():
    print("\033[1;34;47m You're walking down the road, the sky is grim and the world is dimming as the sun sets")
    battle(random.choice(enemies1))
    print("A fork in the road appears, one side looks dark and wicked, while the other has a small village far in the distance")
    choice = input("Which way will you go? (1 = dark, 2 = village 3 = Oysterville 4 = check inventory): ")
    if choice == "1":
        gnarled_path()
    elif choice == "2":
        roarkton()
    elif choice == "4":
        check_inventory()
    else:
        Oysterville()

def gnarled_path():
    global my_player
    random_battle1()
    random_battle1()
    random_battle1()
    print("\033[1;34;47m The roots grow thicker, and despite the gloom you venture onward. Finally you reach a small, dim clearing")
    print("Standing in the center is a clawer!")
    battle(clawer)
    chest_choice = input("\033[1;34;47m With the clearing now empty, you notice a chest under the brush. Inspect? (1= yes, 2 = no): ")
    if chest_choice == "1":
        chest_opening(2)
    print("With no further to venture, you head back to the road")
    road1()
        


def roarkton():
    global roark_mess
    print("\033[1;34;47mAh the peaceful town of roarkton")
    if roark_mess.done == 0:
        print("But trouble is abrewing! You see a poor young woman being harrassed by two bullys!")
        choice = input("Do you help? (1 = yes, 2 = no): ")
        if choice == "1":
            roark_mess_quest()
        else:
            print("Not your problem you mutter, and walk away without another glance")
            roark_mess.done = 2
    print("There is a small shop tucked in the corner of the town, and a saloon to your right, straight ahead is a path that leads to an intersection")
    explore = input("1,2,3,4 = check inventory")
    if explore == "1":
        if roark_mess.done != 1:
            print("you enter the shop, but the lady who was being harassed is the owner. She tells you off, knowing you did not aid her")
            print("In a hurry, you run outside")
            roarkton()
        else:
            shopkeeper_interaction(Shelly)
    elif explore == "2":
        saloon_roarkton()
    elif explore == "3":
        roarkton_splits()
    else:
        check_inventory()

def saloon_roarkton():
    print("\033[1;34;47mYou enter the saloon, and a nice jangy paino tune is playing")
    print("The bartender beckons you over, but on the other side of the room a burly man gives you a wink")
    choice = input("Go to bartender, burly man, return outside or check inventory?(1,2,3,4): ")
    if choice == "1":
        bartender_roarkton()
    elif choice == "2":
        print("You walk up to the burly man, and he eyes you down")
        print("I run an underground fighting arena here. Think you can defeat five enemies in a row? I reward my champions handsomely")
        battler = input("1 = begin the rounds, 2 = no thanks: ")
        if battler == "1":
            battle(bully)
            print(" ")
            battle(bully)
            print(" ")
            battle(bully)
            print(" ")
            battle(elfen)
            print(" ")
            battle(elfen)
            print(" ")
            print("\033[1;34;47mCongrats, you lived, I'll pay you well")
            print("Recieved $20! come back anytime")
            saloon_roarkton()
        else:
            saloon_roarkton()

    elif choice == "3":
        roarkton()
    else:
        check_inventory()
        saloon_roarkton()

def bartender_roarkton():
    print("Welcome to the roarkton saloon")
    if roarkton_bartender_quest.done == 0: 
        print("Care for a drink? Or perhaps hear about a little rumor I heard?")
        rumor = input("1 = drink, 2 = rumor, 3 = see you later: ")
        if rumor == "1":
            buy_drink()
        elif rumor == "2":
            print("So I was told that a flock of squawker stole and ate a gold shipment recently. See if you can't go slay one and see if theres any gold to be had")
            print("New Quest: The birds of gold")
            roarkton_bartender_quest.done = 2
        saloonroarkton()
    else:
        response = input("Care for a drink? (1 = yes, 2 = no): ")
        if response == "1":
            buy_drink()
        saloon_roarkton()

def buy_drink():
    print("It's $10 for a pint")
    if my_player.money >= 10:
        my_player.money = my_player.money - 10
        my_player.health = my_player.max_health
        print("Delicious, health restored")
    else:
        print("Sorry, you don't seem to have enough money")
    saloon_roarkton()

def roarkton_splits():
    return

            

def roark_mess_quest():
    global roark_mess
    print("You run over to the lady, and fling yourself onto the baddies!")
    battle(bully)
    battle(bully)
    print("\033[1;34;47m With the last beating, the two bullys scramble away, and the lady smiles at you")
    print("Lady: thank you for aiding me in my time of need")
    print("You have gained " + str(roark_mess.exp) + " expeerience")
    gain_exp(roark_mess.exp)
    roark_mess.done = 1
    
        
        


    


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
    
#check data functions

def check_weapon_data(weapon):
    print("Weapon name: " + str(weapon.name))
    print("Damage: " + str(weapon.damage))
    print("Value: " + str(weapon.value))
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
    print("Exp: " + str(my_player.exp) + "/" + str(my_player.needed_exp))
    print("Money: " + str(my_player.money))

def check_inventory():
    print(" ")
    global my_player
    print("\033[1;32;47mHere is your current inventory")
    print("Primary weapon: " + my_player.weapon.name)
    print("Item 1: " + my_player.item1.name)
    print("Item 2: " + my_player.item2.name)
    print("Item 3: " + my_player.item3.name)
    print("Health: " + str(my_player.health))
    print("Exp: " + str(my_player.exp) + "/" + str(my_player.needed_exp))
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
                    my_player.item1 = empty
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
                    my_player.item2 = empty
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
                    my_player.item3 = empty
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
basic_chest_loot = [ minor_health_potion, minor_health_potion, quartz_stone, health_potion,empty,empty]
mid_chest_loot = [health_potion,health_potion,quartz_stone,rare_apple]
end_chest_loot = [magical_health_potion,magical_health_potion,magical_health_potion,magical_health_potion,max_health_potion,ruby,ruby,rough_diamond]
def chest_opening(x):
    global my_player
    new_chest = chest()
    if x == 1:
        new_chest.item1 = random.choice(basic_chest_loot)
        new_chest.item2 = random.choice(basic_chest_loot)
        new_chest.item3 = random.choice(basic_chest_loot)
        print("\033[1;36;47mYou have found a basic chest! Inside is: ")
    if x == 2:
        new_chest.item1 = weapon_maker_early_game()
        new_chest.item2 = random.choice(basic_chest_loot)
        new_chest.item3 = random.choice(basic_chest_loot)
        print("You have found a basic chest! Inside is: ")
    if x == 3:
        new_chest.item1 = weapon_maker_mid_game()
        new_chest.item2 = random.choice(mid_chest_loot)
        new_chest.item3 = random.choice(basic_chest_loot)
    if x == 4:
        new_chest.item1 = weapon_maker_end_game()
        new_chest.item2 = random.choice(end_chest_loot)
        new_chest.item3 = random.choice(mid_chest_loot)
        
    
    print("Item 1: " + new_chest.item1.name)
    print("Item 2: " + new_chest.item2.name)
    print("Item 3: " + new_chest.item3.name)
    done = False
    while(done == False):
        take = input("Which item would you like to take?(1,2,3,4 = none): ")
        removal = 0
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
                elif removal == "2":
                    my_player.item2 = new_chest.item1
                elif removal == "3":
                    my_player.item3 = new_chest.item1
            if removal != "4":
                new_chest.item1 = empty
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
                elif removal == "2":
                    my_player.item2 = new_chest.item2
                elif removal == "3":
                    my_player.item3 = new_chest.item2
                    
            if removal != "4":
                 new_chest.item2 = empty
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
                elif removal == "2":
                    my_player.item2 = new_chest.item3
                elif removal == "3":
                    my_player.item3 = new_chest.item3
            if removal != "4":
                new_chest.item3 = empty
        print_inventory()
        is_done = input("Finished search chest? (yes = 1, no = 2): ")
        if is_done == "1":
            done = True

def shopkeeper_iteraction(shopkeeper):
    global my_player
    done = False
    while done == False:
        bs = input("\033[1;33;47mWelcome to the store! Would you like to buy or sell? (1,2): ")
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
        
                    
    
Earl = shopkeeper()
Earl.item1 = random.choice(basic_chest_loot)
Earl.item2 = minor_health_potion
Earl.item3 = minor_health_potion
Earl.item4 = weapon_maker_early_game()

Shelly = shopkeeper()
Shelly.item1 = weapon_maker_early_game()
Shelly.item2 = weapon_maker_early_game()
Shelly.item3 = health_potion
Shelly.item4 = weapon_maker_mid_game()
    

#The game
print("\033[1;34;47mWelcome to Azura\n")
my_name = input("What is your name?: ")
print(my_name + ", your journey is about to begin.")
print("Can you find your way to Mt. Colossus and claim your prize\n")
my_player = player()
my_player.player_name = my_name
my_player.weapon = weapon_maker_end_game()
my_player.health = 10.0
my_player.max_health = 10.0
my_player.money = 10


Oysterville()



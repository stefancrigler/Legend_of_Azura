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

#Criminal
criminal = enemy()
criminal.name = "Criminal"
criminal.description = "part of the 'to save or not to save' quest, this villain wants to rob you"
criminal.health = 12
criminal.damage = 5
criminal.exp = 50

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

#Lt.Whilem
Lt_Whilem = enemy()
Lt_Whilem.name = "Lt. Whilem"
Lt_Whilem.description = "Lt. for the velmore, a mean large man with a punishing mace"
Lt_Whilem.health = 25
Lt_Whilem.damage = 9
Lt_Whilem.exp = 70

#commander herald
commander_herald = enemy()
commander_herald.name = "Commander Herald"
commander_herald.description = "Commander of the velmore, and cunning leader who inspires death"
commander_herald.health = 35
commander_herald.damage = 5
commander_herald.exp = 90

#rebel
rebel = enemy()
rebel.name = "Rebel"
rebel.description = "A fighter against the velmore, naive but brave"
rebel.health = 22
rebel.damage = 4
rebel.exp = 30

#old man
old_man = enemy()
old_man.name = "Old Man"
old_man.description = "Leader of the rebellion, old and willing to give his all for the cause"
old_man.health = 40
old_man.damage = 10
old_man.exp = 100

#elor
elor = enemy()
elor.name = "Elor"
elor.description = "A devastating bison, with the horns to kill and thick body to withstand the toughest blows"
elor.health = 21
elor.damage = 10
elor.exp = 60



######Slum enemies############
#Goon
goon = enemy()
goon.name = "Goon"
goon.description = "Not inherently evil, but will do anything to put food on the table"
goon.health = 7
goon.damage = 3
goon.exp = 13

#Hair Raiser
hair_raiser = enemy()
hair_raiser.name = "Hair Raiser"
hair_raiser.description = "A terrifying sight, the people of the slums pray he won't come knocking on their door."
hair_raiser.health = 13
hair_raiser.damage = 6
hair_raiser.exp = 27




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

sabre_savior = quest()
sabre_savior.name = "to save or not to save"
sabre_savior.exp = 0

first_time_opal_city = quest()

slum_lord_aid = quest()
slum_lord_aid.name = "saving the slums"
slum_lord_aid.exp = 50

chest_got = quest()

rebellion = quest()
rebellion.done = 0
rebellion.name = "The great velmore rebellion"


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
enemies2 = [elfen,elfen,elfen,clawer,sabre_stallion,sabre_stallion]
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

def random_battle2():
    x = random.choice(battle_chance)
    if x == "1":
        battle(random.choice(enemies2))



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
    global my_player
    random_battle1()
    print("You have come to a crossroads. Four lanes")
    roads = input("1 = Sabre Bluffs, 2 = long road, 3 = the Arena, 4 = roarkton")
    if roads == "1":
        print("The road is clear and safe on the way to the bluffs")
        Sabre_Bluffs()
    elif roads == "2":
        print("The long road is treacherous, but a safe village lies at the end")
        long_road()
    elif roads == "3":
        print("You turn right, heading towards the Arena")
        random_battle2()
        the_arena()
    else:
        roarkton()

def roark_mess_quest():
    global roark_mess
    global my_player
    print("You run over to the lady, and fling yourself onto the baddies!")
    battle(bully)
    battle(bully)
    print("\033[1;34;47m With the last beating, the two bullys scramble away, and the lady smiles at you")
    print("Lady: thank you for aiding me in my time of need")
    print("You have gained " + str(roark_mess.exp) + " experience")
    gain_exp(roark_mess.exp)
    roark_mess.done = 1

def Sabre_Bluffs():
    global sabre_savior
    global my_player
    print("You arrive at Sabre Bluffs. The wind is harsh, but the view out into the ocean is stellar")
    if sabre_savior.done == 0:
        print("You see a helpless soul, clutching to hold onto the cliffs edge")
        print("Man: Help me sir! I am stuck and need a hand up")
        choice = input("1 = help, 2 = walk away")
        if choice == "2":
            print("You will pay for this! I will kill you!")
            sabre_savior.done = 2
        else:
            print("Thank you for helping me up, now give me all your money or I swear I will kill you")
            choice2 = input("1 = fight 2 = give money")
            if choice2 == "2":
                print("Fine fine have my money")
                my_player.money = 0
                print("See, you made the right choice, I'll leave you in peace")
                sabre_savior.done = 1
            else:
                print("Really, you dare challenge me?!")
                battle(criminal)
                print("With the thief slain, you take his $30 he had on him")
                my_player.money = my_player.money + 30
                sabre_savior.done = 1
    if sabre_savior.done == 2:
        print("I'm still here! Now help me up")
        choice3 = input("1 = help, 2 = walk away")
        if choice3 == "2":
            print("You will pay for this! I will kill you!")
            sabre_savior.done = 2
        else:
            print("Thank you for helping me up, now give me all your money or I swear I will kill you")
            choice4 = input("1 = fight 2 = give money")
            if choice4 == "2":
                print("Fine fine have my money")
                my_player.money = 0
                print("See, you made the right choice, I'll leave you in peace")
                sabre_savior.done = 1
            else:
                print("Really, you dare challenge me?!")
                battle(criminal)
                print("With the thief slain, you take his $30 he had on him")
                my_player.money = my_player.money + 30
                sabre_savior.done = 1
    print("In front of you is a chest, but before you can react, a sabre stallion attacks!")
    battle(sabre_stallion)
    chest_opening(2)
    print("Though the view is nice, it is time to return to roarkton splits")
    roarkton_splits()

def long_road():
    print("You walk down the long road. Trees as tall as mountains grow on either side of you, and the hum of bugs echoes")
    random_battle1()
    random_battle2()
    print("You hit the middle of this long daunting journey")
    choice = input("To roarkton, or opal city? (1 = roarkton, 2 = opal city): ")
    if choice =="1":
        random_battle1()
        random_battle1()
        roarkton()
    else:
        opal_city()

def opal_city():
    global my_player
    global first_time_opal_city
    if first_time_opal_city.done == 0:
        print("As you arrive in Opal City, your first glimpse at Mt. Colossus appears, looming far in the distance")
        print("Though your goal is in sight, the road is still long, and ever dangerous")
        first_time_opal_city.done = 1
    print("Standing in the town square, you have many options on where to go. The slums stand gloomily to your right, whereas millionaire mansion stands centerfold, there is also a road that leads to the shopping center of the town.")
    choice = input("1 = slums, 2 = millionaire mansion, 3 = shopping center, 4 = roarkton: ")
    if choice == "1":
        opal_slums()
    elif choice == "2":
        millionaire_mansion()
    elif choice == "3":
        shopping_center()
    else:
        long_road()

def slums():
    global my_player
    global slum_lord_aid
    if slum_lord_aid.done == 0:
        print("As you enter the slums, a man, ragged clothes torn and covered in dirt, stumbles toward you.")
        print("Please, help me! My family, the boss is going to hurt them.")
        aid = input("1 = Go with man, 2 = ignore: ")
        if aid == "1":
            print("Thank you so much! Quickly, come with me I have a plan.")
            aid_poor()
            opal_city()
        else:
            print("Sad and alone, the man lets you be, and you walk away")
            print(" ")
            print(" ")
            print("A few blocks further, a man in a brilliant blue suit stops you.")
            print("Have you seen a beaten down man, he owes my boss money. Hey, if you can point him out to me, I can give you some money!")
            give_away = input("1 = give location, 2 = ignore: ")
            if give_away == "1":
                print("He went that way you say? Excellent, here is $100. Also, stop by my bosses bar anytime for a drink, on the house.")
                slum_lord_aid.done = 2
                gain_exp(slum_lord_aid.exp)
                print("You return to the town square")
                opal_city()
            else:
                print("See, I think you lying kid. I think you do know where the guy is, and I'm gunna get that info from you!")
                battle(hair_raiser)
                print("Ah fine, you win. Here is $100 bucks, its all I got. You better not come by these parts again.")
                slum_lord_aid.done = 3
                gain_exp(slum_lord_aid.exp)
                print("You return to the town square")
                opal_city()
    elif slum_lord_aid.done == 2:
        print("The slums are downtrodden, a mess of mud and stench. At the far end, there is a brilliant neon bar")
        bar = input("1 = go to bar, 2 = return to town square")
        if bar == "1":
            neon_bar()
        else:
            opal_city()
    elif slum_lord_aid.done == 3:
        print("Hey it's that kid, get him!")
        battle(goon)
        print("Nothing but sadness here, you return to the town square")
        opal_city()
    else:
        print("The man  you saved joyfully approaches you")
        print("Hey man thanks for saving my family again. Let me heal you up and send you on your way")
        my_player.health = my_player.max_health
        opal_city()

def neon_bar():
    global my_player
    print("Hey kid, thanks again for your help!")
    my_player.health = my_player.max_health
    print("Tell ya what, I want to see some enterntainment. Fight this goon and then we'll patch you up after")
    battle(goon)
    print("Hahah, thanks man, come again anytime")
    my_player.health = my_player.max_health
    opal_city()

def shopping_center():
    global my_player
    global slum_lord_aid
    if slum_lord_aid.done == 2:
        print("As you approach the shops, you notice the blinds being shut around you. Word that you helped the slum lord must have spread. The people do not want you.")
        print("Return to the town square")
        opal_city()
    print("There are two massive shops in the center. A weapons shop and healing shop")
    shop = input("1 = weapon shop, 2 = healing shop, 3 = return to square 4 = crevice peak")
    if shop =="1":
        shopkeeper_iteraction(opal_weapons)
        opal_city()
    elif shop == "2":
        shopkeeper_iteraction(opal_healers)
        opal_city()

    elif shop == "3":
        crevice_peak()

    else:
        opal_city()

def millionaire_mansion():
    global my_player
    global slum_lord_aid
    global chest_got
    if slum_lord_aid.done ==1 & chest_got == 0:
        print("A kind old man opens the door of his mansion, standing welcoming.")
        print("I heard what you did for the man from the slums. I normally don't like company but I want you to have this chest")
        chest_opening(3)
        print("Now get back out there and keep doing great stuff")
        chest_got = 1
        opal_city()
    elif slum_lord_aid.done == 2 & chest_got == 0:
        print("Get in quick! An old man pulls you into the large mansion")
        print("You scum! I heard what you did in the slums, now I will make you pay with my pets")
        battle(ghoul)
        battle(ghoul)
        print("Gah alright go! But never come back")
        chest_got = 1
        opal_city()
    else:
        print("The magnificent mansion is a beautiful bronze color in the sun. But the door is locked tight. So you return to the square")
        opal_city()

def aid_poor():
    global my_player 
    global slum_lord_aid
    print("Look there is my house. Go beat up those bad guys, and I will repay you however I can")
    battle(goon)
    check_inventory()
    battle(goon)
    check_inventory()
    battle(goon)
    print("Thank you so much! I do not have alot sadly. But I can give you $20.")
    slum_lord_aid.done = 1

crevice_peak_chest = False
come_from_crevice_peak = 0
def crevice_peak():
    global my_player
    global crevice_peak_chest
    print("Next to Opal City looms the daunting crevice peak, a mountain necessary to traverse to pass through the region.")
    random_battle2()
    random_battle2()
    random_battle2()
    print("Finally, at the peak. The view is incredible, with the sweeping ocean out in the distance and small specks of civilization below")
    if crevice_peak_chest == False:
        print("Nestled at the peak is a chest! You open it")
        chest_opening(3)
        crevice_peak_chest = True
    print("Here at the top, there are two ways down, to Opal city or to Velmenshire, the home of the legion of Velmore, a hostile people.")
    choice = input("1 = Opal City, 2 = Velmenshire pass 3 = check inventory")
    if choice == "1":
        print("Down to Opal City it is")
        random_battle2()
        random_battle2()
        opal_city()
    elif choice == "2":
        print("Down to the hostile region of Velmenshire")
        random_battle2()
        velmenshire_pass()
    else:
        check_inventory()
        crevice_peak()

def velmenshire_pass():
    global velmore_vanquish
    global my_player
    if come_from_crevice_peak == 0:
        print("The pass is hot, with lava peaking out of cracks in the earth. The land is run by the ferocious velmore")
        come_from_crevice_peak = 1
    print("Roars and screams can be heard in the distance. A velmore patrol approaches, attacking on sight")
    battle(velmore_soldier)
    choice = input("Would you like to go back to crevice peak or fight on to the small safe town of Hecten (1 = Hecten, 2 = Crevice peak 3 = check inventory): ")
    if choice == "1":
        battle(velmore_soldier)
        battle(velmore_soldier)
        Hecten()
    elif choice == "2":
        crevice_peak()
    else:
        check_inventory()

def hecten():
    global my_player
    global rebellion
    if rebellion.done == 0:
        print("The ramshackled town of Hecten, no open shops, but a few houses scattered about")
        print("A young boy approaches")
        rebel = input("Sir, come with me, please, the boy says (1 = go with, 2 = do not go with): ")
        if rebel == "2":
            rebel.done = 2 
            hecten()
        else:
            rebel_initiation()
    elif rebellion.done == 2:
        print("A velmore soldier appears from one of the worn down houses.")
        print("Hello sir, we have had reports of a rebellion forming here in Hecten, and would be willing to pay good money to those who assist in squashing it")
        legion = input("Would you be willing to hunt down rebels? (1 = yes, 2 = no): ")
        if legion == "1":
            print("excellent, find me here once you have defeated some rebels for a reward")
            rebellion.done = 3
        else:
            print("You will not help me? Fine then fight me!")
            battle(velmore_soldier)
    elif rebellion.done == 6:
        print("You find the solider and tell him the news")
        print("Wow, you have done us a great service! Have some money friend")
        print("You gain $400!")
        my_player.money = my_player.money + 400
    go = input("Two houses seem sturdy enough to enter, and there is a path leading out of Hecten towards the base of Mt. Colossus (1 = Whilem's House, 2 = Meek's House, 3 = road, 4 = Back to Pass, 5 = check_inventory")
    if go == "1":
        whilemhouse()
    elif go == "2":
        meekhouse()
    elif go == "3":
        colossus_range()
    elif go == "4":
        velmenshire_pass()
    else:
        check_inventory()
        hecten()

def meekhouse():
    global my_player
    global rebellion
    if rebellion.done == 5:
        print("Thank you for all your help, let me heal you fully.")
        my_player.health = my_player.max_health
        print("Now go on and be a hero")
        hecten()
    elif rebellion.done == 4:
        print("The house is dark, no signs of life")
        hecten()
    elif rebellion.done == 3:
        print("You walk inside, and come across a group of rebels")
        print("Time to fight!")
        battle(rebel)
        battle(rebel)
        print("The first room is cleared, and you drink a max health potion that was sitting on the table")
        my_player.health = my_player.max_health
        print("You enter the next room, and an old man is sitting in a chair, years of wisdom etched in his face")
        print("Ah, so you are the velmore's sell sword. You will not crush us!")
        battle(old_man)
        print("And with that, the leader of the rebellion is dead")
        print("You leave the house, but not before healing up")
        my_player.health = my_player.max_health
        rebellion.done = 6
        hecten()

    else:
        print("Meek, the town's medic, lives here")
        heal = input("I can heal you for $15 (1 = heal, 2 = no thanks): ")
        if heal == "1":
            if my_player.money >= 15:
                print("excellent, you are back to full health")
                my_player.money = my_player.money - 15
                hecten()
            else:
                print("Sorry you do not have enough money")
                hecten()

def whilemhouse():
    global my_player
    global rebellion
    if rebellion.done == 5:
        print("The house is dark, and it seems abandoned")
        hecten()
    elif rebellion.done == 4:
        print("Ah, hello young man. Appreciate what you did for the velmore. Now get out of here before I decied I dislike you")
        hecten()
    else:
        print("Whilem is not a man to approach lightly. You turn around at once")
        hecten()



def rebel_initiation():
    global my_player
    global rebellion
    print("You enter into a small cottage, and the boy leads you to an ancient looking man")
    print("The man, beard long and gray, stands up slowly")
    print("Thank you for coming to us. We need all the help we can get")
    print("We are the rebellion, and we stand to vanquish the core velmore dictatorship")
    join = input("Can we count on your help to bring down the velmore? (1 = yes, 2 = no): ")
    if join == "2":
        print("alright then now go be on your way")
        print("As you leave the house, the boy gives you a sad look, a tear dripping down his cheek")
        rebellion.done = 2
        hecten()
    else:
        print("Thank you, we are ready for our main assault now! Let me show you our plans")
        print("We are sending you into the velmore base in Hecten, an underground bunker guarded by a few soldiers")
        print("We need you to get rid of their leader, a man named Commander Herald. Once he is gone Hecten will be a safer place")
        print("We do not have any fit soldiers, but you can bring Meek, he is our healer. Now off you go")
        velmore_base()

def velmore_base():
    global my_player
    print("You enter the bunker, and the air is a putrid dry, burning the eyes")
    print("Suddenly, a velmore soldier appears!")
    battle(velmore_soldier)
    meek_heal()
    print("Walking down the corridor, you turn and two more soliders attack")
    battle(velmore_soldier)
    battle(velmore_soldier)
    meek_heal()
    print("After some exploring, a large door is visible on the far end of the corridor")
    print("However, standing in your way is a burly man, angry and fierce")
    print("You will not be reaching Commander Herald today mate, I will defeat you")
    battle(Lt_Whilem)
    meek_heal()
    print("With Whilem defeated, you push open the door, opening into a beautiful study")
    print("Mahogany wood and war plans dominate the room, and sitting at the desk is a small man with a cunning look of evil on his face")
    print("Ah, so you are the best the rebellion has to offer. No matter, you will see what true power is now")
    battle(commander_herald)
    print("Wow you did it, you really took down Herald! Let me heal you and we can report back")
    print("From the office, you acquire $300")
    my_player.money = my_player.money + 300
    meek_heal()
    print("Returning back to the house, the old man smiles at you. Thank you for your service to us. We will always be in your debt")
    print("You gained 100 exp")
    gain_exp(100)
    rebellion.done  = 5
    hecten()


def meek_heal():
    global my_player
    print("Excellent work, you are back at full health")
    my_player.health = my_player.max_health
    print("Check your inventory and let us continue")
    check_inventory()














def the_arena():
    global my_player
    print("Tucked away in the woods, this colossal building dominates the area. As you enter, the cheers of a crowd are heard")
    choice = input("Welcome to the arena! Would you like to enter, shop, or get out? (1 = battle, 2 = shop, 3 = leave, 4 = check_inventory): ")
    if choice == "1":
        print("Excellent! A fighter I see. We have special prizes at the end of this gauntlet, if you live of course. I will say, it is not for the faint of heart.")
        level_choice = input("Would you like teh regular or extreme challenge? (1 = regular, 2 = extreme): ")
        if level_choice == "2":
            print("Ah, few dare attempt our extreme gauntlet. Good luck to you and may a prize await you.")
            print("First round...Fight!")
            battle(erupter)
            battle(sabre_stallion)
            print("Excellent! round 2, but first a chance to heal")
            check_inventory()
            battle(ghoul)
            battle(ghoul)
            print("Unreal! But can you survive the final round")
            check_inventory()
            battle(erupter)
            battle(erupter)
            battle(elor)
            print("Amazing! A champion of the extreme challenge")
            print("You have earned your prize! $300 and anything inside this chest!")
            my_player.money = my_player.money + 300
            chest_opening(4)
            print("Before you go, we will heal you up of course.")
            my_player.health = my_player.max_health
            print("Now return to the splits")
            roarkton_splits()
        else:
            print("Ah, the standard challenge for you it is")
            print("First round... Fight!")
            battle(clawer)
            print("Well done. heal up before round 2")
            check_inventory()
            battle(sabre_stallion)
            battle(clawer)
            print("Excellent, now for the final round")
            check_inventory()
            battle(ghoul)
            print("A winner! Here is your prize: $50 and anything in this chest")
            my_player.health =  my_player.max_health
            my_player.money = my_player.money + 50
            chest_opening(2)
            roarkton_splits()
        if choice == "2":
            shopkeeper_iteraction(arena_shop)
            the_arena()
        else:
            roarkton_splits()




    

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
        new_chest.item1 = weapon_maker_early_game()
        new_chest.item2 = random.choice(basic_chest_loot)
        new_chest.item3 = random.choice(basic_chest_loot)
        print("\033[1;36;47mYou have found a basic chest! Inside is: ")
    if x == 2:
        new_chest.item1 = weapon_maker_mid_game()
        new_chest.item2 = random.choice(basic_chest_loot)
        new_chest.item3 = random.choice(basic_chest_loot)
        print("You have found a middle tier chest! Inside is: ")
    if x == 3:
        new_chest.item1 = weapon_maker_mid_game()
        new_chest.item2 = random.choice(mid_chest_loot)
        new_chest.item3 = random.choice(mid_chest_loot)
        print("You have found a great tier chest! Inside is: ")
    if x == 4:
        new_chest.item1 = weapon_maker_end_game()
        new_chest.item2 = random.choice(end_chest_loot)
        new_chest.item3 = random.choice(mid_chest_loot)
        print("You have found an incredible chest! Inside is: ")
        
    
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

def instructions():
    print(" ")
    print("In this game, you are an adventurer on a quest for fame and glory at Mt. Colossus")
    print("Choices are made by pressing a number and then enter when prompted")
    print("Each number corresponds to a choice which will be displayed for you while you pick")
    print("Your character has health, exp, and money. When exp reaches a certain point, you will level up and your possible max health will increase")
    print("Money is used to buy items and weapons. Your character can hold one primary weapon and 3 extra items or weapons")
    print("If you die in battle, you may respawn at certain check points, but will lose all your money")
    print("Goodluck and enjoy the game")
    print(" ")
        
                    
    
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

arena_shop = shopkeeper()
arena_shop.item1 = health_potion
arena_shop.item2 = weapon_maker_mid_game()
arena_shop.item3 = weapon_maker_mid_game()
arena_shop.item4 = health_potion

opal_weapons = shopkeeper()
opal_weapons.item1 = weapon_maker_mid_game()
opal_weapons.item2 = weapon_maker_all()
opal_weapons.item3 = weapon_maker_mid_game()
opal_weapons.item4 = weapon_maker_end_game()

opal_healers = shopkeeper()
opal_healers.item1 = health_potion
opal_healers.item2 = health_potion
opal_healers.item3 = max_health_potion
opal_healers.item4 = magical_health_potion
    

#The game
print("\033[1;34;47mWelcome to Azura\n")
loop = False
while(loop == False):
    begin = input("Type 1 and then enter to begin or anything else to see instructions: ")
    if begin == "1":
        loop = True   
    else:
        instructions()
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



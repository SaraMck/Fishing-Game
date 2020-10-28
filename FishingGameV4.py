import random as ran
import math

inventory = []      # Creates list to contain the objects in inventory

# GLOBAL VARIABLES
inventory_size = 5  # Will be used to set the max size of list
player_money = 1000
rod_upgrades = 0
rod_upgrades_counter = 0
money_charm = False
player_level = 1    # Player will start at level 1
current_xp = 0  # Player will start with 0 xp
xp_until_lvl_up = 250 * player_level  # Each level will need an extra 250 xp to level up (level 1: 250, Level 2:500 etc)


# CLASS
class Loot:     # Creates a class for the  objects that can be fished
    def __init__(self, loot_name, loot_price, loot_chance, loot_xp, level_unlocked):
        self.loot_name = loot_name
        self.loot_price = loot_price
        self.loot_chance = loot_chance
        self.loot_xp = loot_xp
        self.level_unlocked = level_unlocked


# FUNCTIONS
def sort_list_by_chance(list1):  # Creates function to sort lists by loot chance
    list1.sort(key=lambda x: x.loot_chance)


def check_length():  # Function to check if the inventory is full or not, and whether item can be added
    if len(inventory) >= inventory_size:
        print("Inventory is full. Dropping the fish.")
    else:
        inventory.append(catch_list[0])  # Adds the first element (the rarest fish) to your inventory
        inv_warning()


def inv_warning():  # Warns user when inventory is full
    if len(inventory) == inventory_size:
        print("Inventory full.")


def fish(fish_object, chance):  # Creates the fishing mechanic

    if chance < fish_object.loot_chance:
        catch_list.append(fish_object)


def help_menu():    # Displays the list of controls to the user
    print("""f - fish
    h - display help menu
    i - inventory
    s - enter store
    q- quit
    e - empty inventory
    p - display money
    u - check number of upgrades
    l - check level \n""")


def sell():     # sell system of store
    global player_money
    while True:
        sell_cmd = input("Enter the name of what you want to sell, or type e to exit \n>").title()
        if sell_cmd == "E":
            print("Leaving sell menu...")
            break
        elif sell_cmd == "P":
            print(f" You have {player_money} money.")
        for item in inventory:
            if sell_cmd == item.loot_name:  # if the name of the item is in inventory list
                quantity = int(input("How many do you want to sell? "))
                if inventory.count(item) >= quantity:
                    for i in range(quantity):   # Will repeat this process for the number of that item you want to sell
                        player_money += item.loot_price     # Adds item price to player money
                        inventory.remove(item)      # Removes item from player inventory
                        print(f"{item.loot_name} sold!")
                else:
                    print("You do not have that quantity.")
                break


def buy():      # buy system of store
    global player_money
    global inventory_size
    global rod_upgrades
    global rod_upgrades_counter
    global money_charm
    while True:
        buy_cmd = input("""Enter name of item to buy, or press e to exit.
inventory upgrade - 500 money
rod upgrade - 2000 money
money charm - 1000 money 
\n""").lower()
        if buy_cmd == "inventory upgrade":
            if player_money >= 500:
                player_money -= 500
                inventory_size += 5
                print("Inventory upgrade bought!")
            else:
                print("Insufficient funds.")
        elif buy_cmd == "rod upgrade":
            if player_money >= 2000:
                player_money -= 2000
                rod_upgrades += 0.001
                rod_upgrades_counter += 1
                print("Rod upgrade bought!")
            else:
                print("Insufficient funds.")
        elif buy_cmd == "money charm":
            if not money_charm:
                if player_money >= 1000:
                    player_money -= 1000
                    money_charm = True
                    print("Money Charm bought! ")
                    for item in all_loot:
                        item.loot_price = math.ceil(item.loot_price * 1.2)
                else:
                    print("Insufficient funds. ")
            else:
                print("Money Charm already bought! ")
        elif buy_cmd == "e":
            print("Leaving buy menu...")
        elif buy_cmd == "p":
            print(f" You have {player_money} money.")
        else:
            print("Invalid command. ")


def store():
    global player_money
    while True:
        str_cmd = input("Do you want to buy (b) or sell? (s), or press e to exit ").lower()
        if str_cmd == "b":
            buy()
        elif str_cmd == "s":
            sell()
        elif str_cmd == "e":
            print("Leaving store...")
            break
        elif str_cmd == "p":
            print(f" You have {player_money} money.")
        else:
            print("Invalid command.")


def new_fish():
    for item in all_loot:
        if player_level >= item.level_unlocked and loot_list.count(item) == 0:
            loot_list.append(item)
            print(f"{item.loot_name} can now be caught!")
    for item in loot_list:
        print(item.loot_name)


def level_up():
    global player_level
    global xp_until_lvl_up
    global current_xp
    if current_xp >= xp_until_lvl_up:   # Checks if the current xp is greater than the xp needed for the level up
        player_level += 1   # Increases the player level
        current_xp = 0  # Resets current xp
        xp_until_lvl_up = 250 * player_level    # Increases the xp needed for next level up by 250 each time
        print(f"Level up! You are now Level {player_level}")    # Displays the new level to the player
        new_fish()


# Creates the individual objects that can be fished
carp = Loot("Carp", 45, 0.15, 70, 0)
tuna = Loot("Tuna", 40, 0.2, 50, 0)
trout = Loot("Trout", 50, 0.1, 100, 0)
old_boot = Loot("Old Boot", 2, 0.6, 10, 0)
shark = Loot("Shark", 200, 0.05, 500, 5)
whale = Loot("Whale", 500, 0.01, 800, 6)
loch_ness_monster = Loot("Loch Ness Monster", 10000, 0.0005, 5000, 10)
all_loot = [tuna, carp, trout, old_boot, shark, whale, loch_ness_monster]   # Adds the objects to a list
loot_list = [tuna, carp, trout, old_boot]    # Adds the unlocked objects to a list
sort_list_by_chance(loot_list)  # Sorts loot list by rarity
#    for element in loot_list:
#        print(element.loot_name)


# MAIN CODE
print("Welcome to the fishing game! Press h to view controls.")
while True:
    command = input(">").lower()
    if command == "f":
        catch_list = []    # Creates an empty list for the potential caught fish
        percentage_chance = (ran.random() - rod_upgrades)    # Calculates catch percentage chance
        print(percentage_chance)
        for element in loot_list:   # Loops through each of the fish objects in loot list
            fish(element, percentage_chance)    # Calls the fish function
        sort_list_by_chance(catch_list)    # Sorts the caught list so that the rarest fish will be first
        if catch_list:     # If the catch list is True (which means its not empty) , this will happen
            print(f"Wow! {catch_list[0].loot_name} caught!")   # Prints a message which says the name of caught fish
            print(f"You gained: {catch_list[0].loot_xp} XP!")
            current_xp += catch_list[0].loot_xp  # Adds the xp for the fish to current xp variable
            level_up()  # Runs the level up function
            check_length()  # Calls the check length function to see if inventory is full or not
        else:
            print("Nothing caught this time!")  # If nothing was caught, prints message to tell user
    elif command == "i":
        print("Inventory: ")
        for element in inventory:
            print(element.loot_name)    # Displays the name of each object in the inventory
        print(f"Inventory Space: {len(inventory)}/{inventory_size}")
    elif command == "q":
        break   # Exits the while statement if q is typed, exiting the game
    elif command == "e":
        print("Inventory emptied!")
        inventory.clear()   # Empties all elements from the inventory list
    elif command == "h":
        help_menu()
    elif command == "s":
        print("Entering store...")
        store()
    elif command == "p":
        print(f" You have {player_money} money.")
    elif command == "u":
        print(f"You have {rod_upgrades_counter} upgrades!")
    elif command == "l":
        print(f"Player Level: {player_level} \n"    # Displays current player level
              f"{current_xp} / {xp_until_lvl_up}")  # Displays the progress towards next level up
    else:
        print("Invalid Command.")   # If any other keys are input, tells the user it is invalid

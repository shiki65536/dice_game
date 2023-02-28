###################################
# Created by
# Name: Shih-Chi Wen
# Student ID: 32977271,
# Creation date: 15/Aug/2022
# Last modified date: 26/Aug/2022
##################################

#TODO: Number of dice, if only one then one
#TODO: Rule
#TODO: ascii
#TODO: [0]exit

# show main menu and ask for user's input
def main_menu():

    main_banner = """
     _____  _             _____ 
    |  __ \(_)           / ____|
    | |  | |_  ___ ___  | |  __  __ _ _ __ ___   ___ 
    | |  | | |/ __/ _ \ | | |_ |/ _` | '_ ` _ \ / _ \   
    | |__| | | (_|  __/ | |__| | (_| | | | | | |  __/
    |_____/|_|\___\___|  \_____|\__,_|_| |_| |_|\___|

    """
    main_greeting = """
    Please select the number between 1 ~ 3.

    [1] Start Game
    [2] Show Game History
    [3] Exit Program
    """
    
    print(main_banner, main_greeting)
    
    main_input = input(">>> Your choice: ")
    
    return main_input

# show game menu and ask for user's input
def game_menu(dice_type, dice_number): 
    
    game_banner = """
     ____ ____ ____ ____ _________ ____ ____ ____ ____ 
    ||G |||A |||M |||E |||       |||M |||E |||N |||U ||
    ||__|||__|||__|||__|||_______|||__|||__|||__|||__||
    |/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|"""
    
    print(game_banner)
    
    game_greeting = f"""
    Your dice type is {dice_type}, your dice number is {dice_number}.

    Please select:
    [1] Select the type of Dice. **ONLY ONCE per game**
    [2] Select the number of Dice.
    [3] Roll dice with selected type and number.
    [4] Check if median value equals to mean value.
    [5] Exit game.
    """

    print(game_greeting)

    game_input = input(">>> Your game choice: ")

               
    return game_input

# select dice type
def select_type():
    
    select_type_flag = True
    
    select_type_greeting = """
    You have only one chance to change your dice type in a game.
    [6] the dice will have values 1, 2, 3, 4, 5, 6.
    [8] the dice will have values 2, 2, 3, 3, 4, 8.
    [9] the dice will have values 1, 1, 1, 1, 5, 9.

    """
    
    print(select_type_greeting)
    
    while select_type_flag:
        select_type_input = input(">>> Your dice type choice: ")
        validation(select_type_input, [6, 8, 9])
        
        if select_type_input == "6":
            return [1, 2, 3, 4, 5, 6]

        elif select_type_input == "8":
            return [2, 2, 3, 3, 4, 8]

        elif select_type_input == "9":
            return [1, 1, 1, 1, 5, 9]
        
#         else:
#             print("\n<<< Please enter one of the folowering numbers: [6, 8, 9] >>>\n")

# select dice number
def select_number():
    
    select_number_flag = True
      
    select_number_greeting = """
    Choose the number of your dice.
    [2] 2 dices.
    [3] 3 dices.
    [4] 4 dices.
    [5] 5 dices.
    [6] 6 dices.
    """
    
    print(select_number_greeting)
    
    while select_number_flag:
        select_number_input = input(">>> Your dice number choice: ")
        validation(select_number_input, [2, 3, 4, 5, 6])
    
        if select_number_input == "2":
            return 2
        elif select_number_input == "3":
            return 3
        elif select_number_input == "4":
            return 4
        elif select_number_input == "5":
            return 5
        elif select_number_input == "6":
            return 6
#         else:
#             print("\n<<< Please select one of the following numbers: [2, 3, 4, 5, 6] >>>\n")

import random

# roll random numbers depend on dice type and dice number
def roll_dice(selected_type, selected_number):
    result = ()
    tmp = ""
    
    # select random number based by dice type whith in dice number times
    for i in range(selected_number):
        rolled_dice = random.choice(selected_type)
        result += (rolled_dice,)
        
    
        
    return result

def dice_pic(num_array):
    dice_array = [
"""
""",
"""---------
|       |
|   o   |
|       |
---------\n""",
"""---------
|       |
| o   o |
|       |
---------\n""",
"""---------
| o     |
|   o   |
|     o |
---------\n""",
"""---------
| o   o |
|       |
| o   o |
---------\n""",
"""---------
| o   o |
|   o   |
| o   o |
---------\n""",
"""---------
| o   o |
| o   o |
| o   o |
---------\n""",
"""
""",
"""---------
| o o o |
| o   o |
| o o o |
---------\n""",
"""---------
| o o o |
| o o o |
| o o o |
---------\n"""
    ]
    
    dice_array_copy = []
    
    for i in dice_array:
        dice_array_copy.append(i.replace("\n", ""))
            
    
    for i in range(5):
        for j in num_array:
            for k in range(9):
                print(dice_array_copy[j][ i*9 + k], end="")
            print(" ", end="")
        print("")

# check mean and median value of list
def check(roll_array, mode=1 ):
    win = """
     ____ ____ ____ _________ ____ ____ ____ 
    ||Y |||O |||U |||       |||W |||I |||N ||
    ||__|||__|||__|||_______|||__|||__|||__||
    |/__\|/__\|/__\|/_______\|/__\|/__\|/__\|                                               
    """
    lose = """
     ____ ____ ____ _________ ____ ____ ____ ____ 
    ||Y |||O |||U |||       |||L |||O |||S |||E ||
    ||__|||__|||__|||_______|||__|||__|||__|||__||
    |/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|                                                    
    """

    # initialization
    result = []
    count = 0
    dice_number_count = 0
    dice_number_list = []
    median = 0
    mean = 0
    
    # sort dice history
    for i in range(len(roll_array)):
        for j in range(len(roll_array[i])):
            count += 1
            dice_number_count += 1
            result.append(roll_array[i][j])
        dice_number_list.append(dice_number_count)
        dice_number_count = 0
    
    # ascending dice roll history list
    result.sort()
    
    # calculate median value
    if count % 2 == 0:
        median = int((result[int(len(result)/2) - 1] + result[int(len(result)/2)]) / 2)
    else:
        median = result[int(len(result)/2)]

    # calculate mean value
    mean = sum(result) / count
    
    # check win/lose by mode
    # mode 1: check in game
    # mode 2: check in history    
    if mode == 1:
        if len(roll_array)> 10:
            print(lose)

        elif int(mean) == int(median):
            print(win)

        else:
            print(lose)
            
    else:
        if len(roll_array)> 10:
            return (len(roll_array), dice_number_list, "lose")

        elif int(mean) == int(median):
            return (len(roll_array), dice_number_list, "win")

        else:
            return (len(roll_array), dice_number_list, "lose")


# show game history 
def game_history(games_result_list):
    game_history_greeting = """
     ____ ____ ____ ____ ____ ____ ____ 
    ||H |||I |||S |||T |||O |||R |||Y ||
    ||__|||__|||__|||__|||__|||__|||__||
    |/__\|/__\|/__\|/__\|/__\|/__\|/__\|
    """
    print(game_history_greeting)
    
    
    # if user played the game more than one time, sort result based on length
    if len(games_result_list) == 0:
        print(">>> You didn't play game, yet.\n")
        
    else:
        games_result_list.sort(key = lambda order: len(order))
        
        for game in games_result_list:
            tmp_result = check(game, 2)
            print(f">>> Dice rolling times: {tmp_result[0]}, Number of dice: {tmp_result[1]}, Result: {tmp_result[2]}")


# control flow
def main():
    goodbye = """
       _____                 _ _                
      / ____|               | | |               
     | |  __  ___   ___   __| | |__  _   _  ___ 
     | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ 
     | |__| | (_) | (_) | (_| | |_) | |_| |  __/  
      \_____|\___/ \___/ \__,_|_.__/ \__, |\___|  
                                      __/ |     
                                     |___/      
    """ 
    
    main_menu_flag = True
    game_menu_flag = False
    dice_type_flag = True
    dice_type = "<Please Select>"
    dice_number = "<Please Select>"
    roll_history = []
    all_history = [] 
    
    # get main menu input
    while main_menu_flag:
        main_input = main_menu()
        
        validation(main_input, [1, 2, 3])
        
        if main_input == "1":
            game_menu_flag = True

        elif main_input == "2":
            game_history(all_history)

        elif main_input == "3":
            print(goodbye)
            print(">>> Thank you for playing.")
            break

            
        # get game menu input    
        while game_menu_flag:
            game_input = game_menu(dice_type, dice_number)
            
            validation(game_input, [1, 2, 3, 4, 5])
            
            if game_input == "1":
                if dice_type_flag:
                    dice_type_flag = False
                    dice_type = select_type()
                else:
                    print("\n<<< You can only change dice type once per game. >>>")

            elif game_input == "2":
                dice_number = select_number()

            elif game_input == "3":
                if type(dice_type) == str:
                    print("\n<<< Please select dice type! >>>")

                elif type(dice_number) == str:
                    print("\n<<< Please select dice number! >>>")

                else:
                    result = roll_dice(dice_type, dice_number)
                    print("\n<<< Your roll dice result: >>>")
                    dice_pic(result)
                    roll_history.append(result)

            elif game_input == "4":
                if len(roll_history) == 0:
                    print("\n<<< You have to roll dice at first. >>>")

                else:
                    roll_result = check(roll_history)

            elif  game_input == "5":
                # pevent null return
                if len(roll_history) == 0:
                    print("\n<<< Please roll dice >>>")

                else:
                    all_history.append(roll_history)
                    game_menu_flag = False
                    roll_history = []
                    dice_type_flag = True
                    dice_type = "<Please Select>"
                    dice_number = "<Please Select>"            


# check if input letter match expected number list
def validation(user_input, number_list):
    if not user_input.isdigit():
        print("\n<<< Please enter one number from: ", number_list, " >>>")
    elif not int(user_input) in number_list:
        print("\n<<< Please enter one number from: ", number_list, " >>>")
    else:
        return True

main()
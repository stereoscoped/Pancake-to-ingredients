"""
Pancake to ingredients 1.1
2/24/2024
created by stereoscoped
"""

repeat_program = True

while repeat_program:

    # Makeshift version of cookies
    cookie_file = open("saves\cookies.txt", "r")
    if cookie_file.read() == "True":
        cookies = True
    else:
        cookies = False

    # Asks the first question - tries if it is a number or not
    while True:
        try:
            pancake_amount = float(input("\033[37mHow many pancakes are you baking? "))
            break
        except:
            print("\033[31mThat is not a number.\033[37m")

    # Conversion calculation
    cups_of_flour = pancake_amount * 1
    cups_of_milk = pancake_amount * 1
    tablespoons_of_sugar = pancake_amount * 2
    tablespoons_of_oil = pancake_amount * 2
    teaspoons_of_baking_powder = pancake_amount * 2
    teaspoons_of_salt = pancake_amount * 1
    eggs = pancake_amount * 1

    # Output
    # if-else statements are for plurals in grammar
    print("You will need:")
    if cups_of_flour == 1: print(cups_of_flour,"cup of flour")
    else: print(cups_of_flour,"cups of flour")

    if tablespoons_of_sugar == 1: print(tablespoons_of_sugar,"tablespoon of sugar")
    else: print(tablespoons_of_sugar,"tablespoons of sugar")

    if tablespoons_of_oil == 1: print(tablespoons_of_oil,"tablespoon of oil")
    else: print(tablespoons_of_oil,"tablespoons of oil")

    if teaspoons_of_baking_powder == 1: print(teaspoons_of_baking_powder, "teaspoon of baking powder")
    else: print(teaspoons_of_baking_powder, "teaspoons of baking powder")

    if teaspoons_of_salt == 1: print(teaspoons_of_salt, "teaspoon of salt")
    else: print(teaspoons_of_salt, "teaspoons of salt")

    if cups_of_milk == 1: print(cups_of_milk, "cup of milk")
    else: print(cups_of_milk, "cups of milk")

    if eggs == 1: print(eggs, "egg")
    else: print(eggs, "eggs")

    # Checks to repeat program or not, which is influenced by cookies
    if cookies == True:
        while True:

            # Asks if another cake is going to be baked
            repeat_program_question = input("\033[37mAre you baking another cake? (y/n) ")
            if repeat_program_question == "n" or repeat_program_question == "N":
                repeat_program = False
                break

            if repeat_program_question == "y" or repeat_program_question == "Y":
                # Asks if program wants to be repeated again

                while True:
                    repeat_program = True
                    cookie_question = input("\033[37mDo you want this message to show again? (y/n) ")
                    if cookie_question == "n":
                        # Changes the cookies file
                        cookie_file = open("saves\cookies.txt", "w")  # write mode
                        cookie_file.write("False")
                        cookie_file.close()
                        break
                    if cookie_question == "y" or cookie_question == "Y":
                        break
                    else:
                        print("\033[31mPlease type y or n. \033[37m")
                break
            else:
                print("\033[31mPlease type y or n. \033[37m")


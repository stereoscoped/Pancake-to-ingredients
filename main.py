"""
Pancake to ingredients
2/23/2024
created by stereoscoped
"""

repeat_program = True

while repeat_program:
    cookie_file = open("saves\cookies.txt", "r")
    if cookie_file.read() == "True":
        cookies = True
    else:
        cookies = False

    while True:
        try:
            pancake_amount = float(input("How many pancakes are you baking? "))
            break
        except:
            print("That is not a number.")

    # Conversion calculation
    cups_of_flour = pancake_amount * 1
    cups_of_milk = pancake_amount * 1
    tablespoons_of_sugar = pancake_amount * 2
    tablespoons_of_oil = pancake_amount * 2
    teaspoons_of_baking_powder = pancake_amount * 2
    teaspoons_of_salt = pancake_amount * 1
    eggs = pancake_amount * 1

    # Output
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

    if cookies == True:
        while True:
            repeat_program_question = input("Are you baking another cake? (y/n) ")
            if repeat_program_question == "n" or repeat_program_question == "N":
                repeat_program = False
                break
            if repeat_program_question == "y" or repeat_program_question == "Y":
                while True:
                    repeat_program = True
                    cookie_question = input("Do you want this message to show again? (y/n) ")
                    if cookie_question == "n":
                        cookie_file = open("saves\cookies.txt", "w")  # write mode
                        cookie_file.write("False")
                        cookie_file.close()
                        break
                    if cookie_question == "y" or cookie_question == "Y":
                        break
                    else:
                        print("Please type y or n. ")
                break
            else:
                print("Please type y or n. ")


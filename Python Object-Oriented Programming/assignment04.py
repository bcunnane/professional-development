"""
CS3A, Lab Assignment 4 - Free Frozen Yogurt
Brandon Cunnane
Free frozen yogurt stamp accounting program.
"""

FREE_YOG_NUM = 7

stamps = 0
while True:
    print("Menu:\n"
          "   P (process Purchase)\n"
          "   S (Shut down)")
    choice = input("Your Choice: ")
    if len(choice) > 0:
        choice = choice[0].lower()
    else:
        print('\n*** Enter a response, please. ***\n')
        continue
    if choice == 's':
        break
    elif choice == 'p':
        # award transaction
        if stamps >= FREE_YOG_NUM:
            use_free = input("You qualify for a free yogurt. "
                             "Would you like to use your stamps? (Y or N): ")
            if len(use_free) > 0:
                use_free = use_free[0].lower()
            else:
                print('\n*** Enter a response, please. ***\n')
                continue
            if use_free == 'y':
                stamps = stamps - FREE_YOG_NUM
                print(f'You have just used {FREE_YOG_NUM} stamps'
                      f' and have {stamps} left.\n'
                      f'Enjoy your free yogurt. \n')
                continue
            elif use_free == 'n':
                pass
            else:
                print('\n*** Use Y or N, please. ***\n')
                continue
        # normal transaction
        yogurts = int(input("How many yogurts would you like to buy?: "))
        if not 0 < yogurts:
            print("\n*** Invalid # yogurts. ***\n")
            continue
        stamps = stamps + yogurts
        print(f"You just earned {yogurts} stamps "
              f"and have a total of {stamps} to use.\n")
    else:
        print('\n*** Use P or S, please. ***\n')
        continue
print("Thank you. Please come again!")

"""
Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: p
How many yogurts would you like to buy?: 5
You just earned 5 stamps and have a total of 5 to use.

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: purchase
How many yogurts would you like to buy?: -4

*** Invalid # yogurts. ***

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: 6

*** Use P or S, please. ***

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: p
How many yogurts would you like to buy?: 6
You just earned 6 stamps and have a total of 11 to use.

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: purchase
You qualify for a free yogurt. Would you like to use your stamps? (Y or N): nope
How many yogurts would you like to buy?: 3
You just earned 3 stamps and have a total of 14 to use.

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: p
You qualify for a free yogurt. Would you like to use your stamps? (Y or N): y
You have just used 7 stamps and have 7 left.
Enjoy your free yogurt. 

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: s
Thank you. Please come again!

Process finished with exit code 0
"""

"""
Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: 

*** Enter a response, please. ***

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: PURCHASE PLEASE
How many yogurts would you like to buy?: 4
You just earned 4 stamps and have a total of 4 to use.

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: p
How many yogurts would you like to buy?: -10

*** Invalid # yogurts. ***

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: p
How many yogurts would you like to buy?: 9
You just earned 9 stamps and have a total of 13 to use.

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: p
You qualify for a free yogurt. Would you like to use your stamps? (Y or N): 

*** Enter a response, please. ***

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: p
You qualify for a free yogurt. Would you like to use your stamps? (Y or N): not today
How many yogurts would you like to buy?: 1
You just earned 1 stamps and have a total of 14 to use.

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: p
You qualify for a free yogurt. Would you like to use your stamps? (Y or N): YSS PLS
You have just used 7 stamps and have 7 left.
Enjoy your free yogurt. 

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: P
You qualify for a free yogurt. Would you like to use your stamps? (Y or N): y
You have just used 7 stamps and have 0 left.
Enjoy your free yogurt. 

Menu:
   P (process Purchase)
   S (Shut down)
Your Choice: SHUT IT DOWN
Thank you. Please come again!

Process finished with exit code 0
"""
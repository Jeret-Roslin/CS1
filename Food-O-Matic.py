# Author: Jeret Roslin
# Sources: Ms. Marciano, CS Google Classroom
# Description: This code uses parallel arrays to randomly generate a food with a side with a price
# Date: 4/4/25
# Challenges: Domain has been changed, prices for flairs have been added, valueError added, total cost of items added.
# Bugs: May bug on number of items slighlty but not common

import random                                                                                                           # random library is imported

mains = ['nachos','cheesesteak','BE&C','Pepperoni Pizza','Hot Chicken Sandwich','poutine']                              # list of mains
main_prices = [12, 15, 10, 16, 20, 17]                                                                                  # list of main prices
flairs = ['with salsa','with truffle fries','with coffee','with garlic knots',' with side vegetables','with butter']    # list of flairs
flair_prices =[2,7,3,5,8,1]                                                                                             # prices with flairs

print("Welcome to Jeret's Food Shack")                                                                                  # displays message 

while True:                                                                                                             # forever loop
    num_items = int(input("How many items will you like? "))                                                            # ask the user for a number of items
    if num_items > 6:                                                                                                   # says if total number of items is over amount
        print  ("To many items please try again")                                                                       # displays message 
        continue                                                                                                        # goes back to previous message
    print("you entered:", num_items)                                                                                    # displays message 
    total = 0                                                                                                           # sets total to 0

    for i in range(num_items):                                                                                          # displays the number of items user wants
        main = random.choice(mains)                                                                                     #randomly generate a main from mains
        flair = random.choice(flairs)                                                                                   #randomly generate a flair from flairs 
        price = main_prices[mains.index(main)]
        flair_price = flair_prices [flairs.index(flair)]                                                                # generates index from prices and flairs
        print (f'{main} {flair}, ${price+flair_price} ')                                                                # prints price of items
        total += price                                                                                                  # adds up total price of items
    print("Your total is:", total)                                                                                      # prints total price of items
        

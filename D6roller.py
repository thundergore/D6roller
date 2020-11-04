import numpy as np
import pandas as pd

#The following is used for Davis Ford's session history roll average idea
historic_rolls = []

#Setting up userinput to roll again once done
roll_dice = 'y'
while roll_dice == 'y':

    #We don't want non-integers being input so try block to eliminate ValueError
    d6 = 0
    is_int = False

    answer = input("\n How many d6s will you roll brother?: ")

    while not is_int:
        try:
            answer = int(answer)
            is_int = True
            d6 = answer
        except ValueError:
            answer = input("\n Halt in the Emperor's name! Input a number only: ")

    #using random.randint from numpy to get 'd6' sized range of numbers between 1 and 6, then printing them
    dice_result = np.random.randint(1,7,size=(d6,))
    print("\n Excellent! May the Emperor bless these dice rolls! \n", dice_result)

    #counting unique dice values in the range and then printing them
    unique_dice, counts = np.unique(dice_result, return_counts=True)
    unique_dice = dict(zip(unique_dice, counts))
    print("\n You can see how many of each you rolled below brother: \n", unique_dice)

    #Stats
    print("\n By the Emperor's will the mean for this rolling spree was: ", round(dice_result.mean(), 3))
    #Saving the mean to a list
    historic_rolls.append(round(dice_result.mean(), 3))

    print("Here are the average value(s) of previous rolls brother:", historic_rolls)

    #The input to set roll_dice to y or n
    roll_dice = input("\n Are the filty Xenos still standing? (y or n) ")

if roll_dice is not 'y':
    #Return historic stats for session with historic roll list
    historic_mean = round(sum(historic_rolls) / len(historic_rolls), 3)
    print("\nGlory to the Emperor! The inquisition wills that I share the average of your last {} dice rolls: {}".format(len(historic_rolls), historic_mean))

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

    answer = input("\n How many d6s will you roll?: ")

    while not is_int:
        try:
            answer = int(answer)
            is_int = True
            d6 = answer
        except ValueError:
            answer = input("\n Input a number: ")

    #using random.randint from numpy to get 'd6' sized range of numbers between 1 and 6, then printing them
    dice_result = np.random.randint(1,7,size=(d6,))
    print("\n", dice_result)

    #counting unique dice values in the range as 2xseries in a dataframe
    unique_dice, counts = np.unique(dice_result, return_counts=True)
    series_dice = {'No. of dice':pd.Series(counts), 'results': pd.Series(unique_dice)}
    df_dice = pd.DataFrame(series_dice)
    #hide index during print
    print("\n", df_dice.to_string(index=False), "\n")


    #Stats
    print("\n Mean: ", round(dice_result.mean(), 3))
    #Saving the mean to a list
    historic_rolls.append(round(dice_result.mean(), 3))

    print("\n Average value(s) of previous rolls:", historic_rolls)

    #The input to set roll_dice to y or n
    roll_dice = input("\n Again? (y or n) ")

if roll_dice == 'n':
    #Return historic stats for user selected end of session with historic roll list
    historic_mean = round(sum(historic_rolls) / len(historic_rolls), 3)
    print("\n The average of your last {} dice rolls: {}".format(len(historic_rolls), historic_mean), "\n")
    quit()
else:
    #Return historic stats for forced end of session with historic roll list
    historic_mean = round(sum(historic_rolls) / len(historic_rolls), 3)
    print("\n Input y or n only ... Ending session.")
    print("\n The average of your last {} dice rolls: {}".format(len(historic_rolls), historic_mean), "\n")
    quit()

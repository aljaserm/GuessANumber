# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:49:59 2019

@author: aljaser

Number Guessing Game
"""

import random
#print(random.randint(1,100))

lstGuess=[]
appNumberPicker=random.randint(1,100)
userGuess=int(input("Guess a number (1-100):"))
lstGuess.append(userGuess)
while userGuess!=appNumberPicker:
    if userGuess>appNumberPicker:
        print("Higer than my pick")
    else:
        print("Lower than my pick")
    userGuess=int(input("Guess a number (1-100):"))
    lstGuess.append(userGuess)
else:
    if len(lstGuess)==1:
        print("Wow you got it")
    elif len(lstGuess) < 5:
        print("Impressive, it took you {} guess to get it".format(len(userGuess)))
    else:
        print("I felt asleep until you got my guess :( ")

print("here is your guesses:")
print(lstGuess)


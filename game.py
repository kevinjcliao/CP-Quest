import random
import sys
import time
import chambers/chamber_one

class Game: 
    def __init__(self, gamePlayerName): 
        print "New game created! " + "Hi, " + gamePlayerName
    
    def newGame (self): 
        chamber_one = 
        
        self.slowPrint(
    def slowPrint(self, s): 
        for c in s + '\n': 
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.01)

    def printAcceptableInputs(self, acceptableInputs): 
        self.slowPrint("Current acceptable inputs: ")
        print acceptableInputs

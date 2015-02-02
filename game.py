import random
import sys
import time

class Game: 
    def __init__(self, gamePlayerName): 
        print "New game created! " + "Hi, " + gamePlayerName
    
    def firstRun (self): 
        self.slowPrint("You awake in the dark flickering lights of Lunt Basement.")

    def slowPrint(self, s): 
        for c in s + '\n': 
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.01)

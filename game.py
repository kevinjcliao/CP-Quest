import random
import sys
import time

sys.path.append('chambers/')
import chamber_one


class Game: 
    def __init__(self, gamePlayerName): 
        print "New game created! " + "Hi, " + gamePlayerName

    def run(self): 
        self.slowPrint("Let's get started...")
        current_chamber = chamber_one.chamber_one(self)

    def slowPrint(self, s): 
        for c in s + '\n': 
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)

    def printAcceptableInputs(acceptableInputs): 
        slowPrint("Current acceptable inputs: ")
        print acceptableInputs

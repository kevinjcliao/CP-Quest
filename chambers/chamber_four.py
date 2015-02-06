# -*- coding: utf-8 -*-
import sys

sys.path.append("../")


class chamber_four: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = [
            "0: Confront their CPs",
            "1: Go on a tirade in their hall, stomping around and destroying everything"+\
                "and laying waste to the speakers that play that awful music.",
            "2: Gather your hall to make equal to greater noise in order to annoy the other hall",
            "3: Ignore it"
            ]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint(
            "The workload is really picking up,"+\
            "and the courses are getting really difficult."+\
            "Your customs group is located down the hall from another,"+\
            "and every night they play very loud music"+\
            "that makes it impossible to study anywhere on the hall."+\
            "While you have grown used to the noise,"+\
            "some freshmen express their irritance to you."+\
            "What do you do? ")
        self.theCurrentGame.slowPrint("!")
        self.printAcceptableInputs(acceptable_inputs)

    def printAcceptableInputs(self, acceptable_inputs): 
        for line in acceptable_inputs: 
            print line 

    def getUserInput(self, acceptable_inputs): 
        input = raw_input("Choose an answer: ")
        
        correctInput = False 

        for i in range(0,len(self.acceptable_inputs)): 
            
            if int(input) == i:
                correctInput = True
                print "You chose: " + input
                
                if i==0: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   -= 1
                    self.theCurrentGame.slowPrint(
                        "You confront their CPs respectfully,"+\
                        "but instead of respecting your confrontation,"+\
                        "they tell you that this is how they want to live"+\
                        "and expect you to live with it."
                        )

                elif i==1: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "You go on a tirade in their hall and destroy absolutely everything."+\
                        "You have to compensate them for all damages")
                    sys.exit()
                    

                elif i==2: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Your hall succeeds in making more noise than the other hall,"+\
                        "but this causes a competition between halls"+\
                        "and eventually everyone becomes deaf."
                        )
                elif i==3: 
                    self.theCurrentGame.aura -= 2
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "You ignore you halls complaints"+\
                        "and as a result the other hall continues to make loud noises"+\
                        "and your hall becomes distraught."
                        ) 
                break
  
        if not correctInput:  
            print "Error! Perhaps you made a typo somewhere? "
            self.getUserInput(acceptable_inputs)

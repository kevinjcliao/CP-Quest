# -*- coding: utf-8 -*-
import sys

sys.path.append("../")


class chamber_three: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = [
                "0: Pull him aside respectfully and confront him in private.", 
                "1: In the middle of the photo, point at his costume, bounce" +\
                        " up and down and yell 'NO. NO. NO. NO. NO.", 
                "2: Ignore the problem. There is no problem.", 
                "3: Match the outfit to make sure they don't feel out of place."
                ]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("Episode 2: Mid-October")
        self.theCurrentGame.slowPrint(
                "It’s time for the Halloween party! You’ve spent a lot of" +\
                " time decorating the hall with your freshmen and picking" +\
                " out your costume. On the night of Halloween your freshmen" +\
                " are all costumed, excited and ready to have a blast. You" +\
                " notice, however, that one of your freshmen is dressed up" +\
                " in blackface. He has clearly spent hours on his costume,"+\
                " but it is (probably unintentionally) offensive and racist."+\
                " What do you do?"
                )

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
                print "Great! You chose: " + input
                
                if i==0: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("")

                elif i==1: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("Some Answer")
                    print "I'd put you in the apartments!"
                elif i==2: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("Some Answer")
                elif i==3: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("Unbelievable. You are " +\
                            " no longer the CP of this hall. ")
                    sys.exit()
                    
                break
  
        if not correctInput:  
            print "Error! Perhaps you made a typo somewhere? "
            self.getUserInput(acceptable_inputs)

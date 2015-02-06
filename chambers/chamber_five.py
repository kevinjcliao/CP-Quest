# -*- coding: utf-8 -*-
import sys

sys.path.append("../")


class chamber_five: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = [
            "0:Implement martial law. Set a curfew"+\
                "and confine people to their rooms to study.",
            "1: Pressure people to study, and remind them that"+\
                "finals are coming, but they can drink and"+\
                    "party all though winter break.",
            "2: Do nothing. You have your own finals to worry about.",
            "3: Join them. Drinking is cool,"+\
                "therefore you drinking with them must make you cool."
            ]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint(
            "Finals are right around the corner,"+\
            "but you begin to notice that your freshmen"+\
            "have not been studying. Instead all they do is party,"+\
            "and they have stopped doing homework in general."+\
            "What do you do? ")
        self.theCurrentGame.slowPrint("!")
        print acceptable_inputs

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
                    self.theCurrentGame.slowPrint(
                        "This causes more stress during finals week,"+\
                        "and eventually people stop coming back home"+\
                        "and instead become refugees all around campus.")


                elif i==1: 
                    self.theCurrentGame.aura += 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Most of your hall follow your plan and begin to study,"+\
                        "though there are still the group of partiers,"+\
                        "the majority are now taking finals serious.")

                elif i==2: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Are you sure you want to be a CP?")

                elif i==3: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Your freshmen get too wasted and many end up failing their finals."+\
                        "Dean Martinez and President Dan Weiss personally"+\
                        "escort you from your hall"+\
                        "Sorry you are no longer CP of this hall”
                        )
                    sys.exit()
                
                break
  
        if not correctInput:  
            print "Error! Perhaps you made a typo somewhere? "
            self.getUserInput(acceptable_inputs)

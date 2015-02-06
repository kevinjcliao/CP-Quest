# -*- coding: utf-8 -*-
import sys

sys.path.append("../")


class chamber_seven: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = [
            "0: Well for Christmas we had a Secret Snowflake,"+\
                " how about Valentine's Day we have a Secret Valentine.",
            "1: It's not my job to play match maker,"+\
                " plus I already have plans of my own.",
            "2: Even though I shouldn't play match maker,"+\
                " I should at least through a customs get together.",
            "3: I myself do not have anyone,"+\
                " so I will just sleep through valentine's day"+\
                " and avoid this whole mess."
            ]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("Episode Six: Mid-February")
        self.theCurrentGame.slowPrint(
            "After dealing with the previous hall relationship problem,"+\
            " you realize that valentines day is right around the corner "+\
            " and half of your hall has no one to be their valentine."+\
            " What do you do?")
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
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Ehh bad choice. Customs incest runs amok."+\
                        " Leading to your whole hall breaking up.")
                    sys.exit()


                elif i==1: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   -= 1
                    self.theCurrentGame.slowPrint(
                        "As you sit with your valentine, eating the wonderful"+\
                        " food of the DC, your valentine sees your freshmen"+\
                        " eating alone and sad."+\
                        " He/she promtly invites them to your table"+\
                        " essentially killing the mood")

                elif i==2: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Your freshmen are very happy by your choice!" )

                elif i==3: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "You wake up to a Zombie apocalypse."+\
                        " As it turns out, since your freshmen did not have dates"+\
                        " they decied to play in the KINSC and ultimataly"+\
                        " contracted something while they were in there."+\
                        " Zombie Dean Martinez informs you that"+\
                        " you are no longer CP of this hall!")
                    sys.exit()
                break
  
        if not correctInput:  
            print "Error! Perhaps you made a typo somewhere? "
            self.getUserInput(acceptable_inputs)

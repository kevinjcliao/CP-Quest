# -*- coding: utf-8 -*-
import sys

sys.path.append("../")

class chamber_two: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = [
            "0: Do nothing. Respect their personal space." +\
                " What business do you have poking around when they've told" +\
                " you to stop?", 
            "1: Perhaps ask some of their friends to see" +\
                " if they're alright. ",
            "2: Go out to eat with them"+\
                "give them a space for them to open up.",
            "3: Hold a PAF session and leave it to them to solve."
            ]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("Episode 1: Mid-September")
        self.theCurrentGame.slowPrint(
            "Customs week is over. From getting" +\
            " soaked and covered in mud during primal" +\
            " scream, to gaining a bit of emotional intimacy" +\
            " during pluralism, its clear that" +\
            " your freshmen had a blast. Now, as the monotony of the semester" +\
            " begins to sink in, two of your freshmen become withdrawn from most"+\
            " activities. You ask them what's up and they insist they're fine." +\
            " What do you do? "
        )
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
                print "Great! You chose: " + acceptable_inputs[i]
                
                if i==0: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("Gradually, the two freshmen become completely" +\
                            " uninvolved in any hall activities. It seems" +\
                            " as if they're always on the hall but never" +\
                            " visible. Their class attendance drops.")

                elif i==1: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Good choice! You find out that they are just"+\
                        " homesick and feeling out of place. "+\
                        "This allows you to better approach them later")
                elif i==2: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Good choice! By having an open space,"+\
                        " they tell you about their homesickness"+\
                        " and you are able to help them out.")
                elif i==3:      
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Pushing your dilemas to others is not a good thing. "+\
                        "Without knowing exactly what to cover in the PAF session,"+\
                        " the PAFs find that holding a session becomes a waste of time, and the"+\
                        " freshmen writhdraw more.")
                break
                
           
  
        if not correctInput:  
            print "Error! Perhaps you made a typo somewhere? "
            self.getUserInput(acceptable_inputs)

       


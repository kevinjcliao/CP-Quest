import sys

sys.path.append("../")


class chamber_eight: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = [
            "0: Wear hazmat suits in your common room"+\
            "and convince the intruders that there was a chemical leak in the room.",
            "1: Play loud music in the common room to scare them away.",
            "2: Leave it be, unless they become a nuisance in which case intervene.",
            "3: Barricade your common room in a 300 style phalanx formation"+\
            "and prepare for the worse.]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint(
            "Your common room has been overrun by people not from your hall!"
            )
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
                        "Though this would be funny to see"+\
                        "You freshmen,not knowing your trick,"+\
                        "call safety and security who calls homeland security"+\
                        "You are arrested for a false alarm,"+\
                        "And Dean Martinez visits you in jail to tell you"+\
                        "That you are no longer CP of this hall.")
                    sys.exit()


                elif i==1: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Though this works for a little,"+\
                        "they eventualy think it is a paryt"+\
                        "and invite more people.")

                elif i==2: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "This is the best choice."+\
                        "These 'invaders' are friends of someone on your hall"+\
                        "and they have the right to spend time with her/him"+\
                        "Only intervene if things get too rowdy.")

                elif i==3: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "Seeing your hall is composed of less then 300 people,"+\
                        "This plan fails".)
                
                break
  
        if not correctInput:  
            print "Error! Perhaps you made a typo somewhere? "
            self.getUserInput(acceptable_inputs)

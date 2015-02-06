import sys

sys.path.append("../")


class chamber_three: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = ["Confront their CPs"]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("The workload is really picking up,"+\
        "and the courses are getting really difficult."+\
        "Your customs group is located down the hall from another,"+\
        "and every night they play very loud music"+\
        "that makes it impossible to study anywhere on the hall."+\ 
        "While you have grown used to the noise, some freshmen express their irritance to you."+
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
                print "Great! You chose: " + input
                
                if i==0: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("Some Answer")


                elif i==1: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("Some Answer")

                elif i==2: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("Some Answer")

                elif i==3: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("Some Answer")
                
                break
  
        if not correctInput:  
            print "Error! Perhaps you made a typo somewhere? "
            self.getUserInput(acceptable_inputs)

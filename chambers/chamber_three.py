import sys

sys.path.append("../")


class chamber_three: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = []
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("FILL IN Scenario")
        self.theCurrentGame.slowPrint("!")
        self.printAcceptableInputs(acceptable_inputs)

    def printAcceptableInputs(self, acceptable_inputs): 
        for line in acceptable_inputs: 
            print line

    def getUserInput(self, acceptable_inputs): 
        input = raw_input("Choose an answer: ")
        print "Great! You chose: " + input
        
        for i in range(0,len(self.acceptable_inputs)): 

            if input == self.acceptable_inputs[i]: 
                if i==0: 
                    self.gamePlayer.user_something = "Fill in Answer"
                    print "response"
                elif i==1: 
                    self.gamePlayer.user_something = "Fill in Answer"
                    print "response"
                elif i==2: 
                    self.gamePlayer.user_something = "Fill in Answer"
                    print "response"
                elif i==3: 
                    self.gamePlayer.user_something = "Fill in Answer"
                    print "response"
                    
                break
  
            else: 
                print "Error"
                self.getUserInput(acceptable_inputs)

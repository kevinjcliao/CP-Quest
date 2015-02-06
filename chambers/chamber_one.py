import sys

sys.path.append("../")


class chamber_one: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = [
                "0: Hearing exactly what's going on next door.", 
                "1: Being so far off campus you can never engage in campus life.", 
                "2: Getting attacked by bats, mice, and insects.", 
                "3: Living in a disgusting wasteland of bodily fluids."
            ]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)
        self.theCurrentGame.slowPrint("Alright then... Let's get started...")        
    
    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("What kind of hall do you like? ")
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
                    self.gamePlayer.user_hall = "Tritton"
                    print "Tritton Hall sounds like a good fit for you!"
                elif i==1: 
                    self.gamePlayer.user_hall = "HCA"
                    print "I'd put you in the apartments!"
                elif i==2: 
                    self.gamePlayer.user_hall = "Barclay"
                    print "Barclay's your hall!"
                elif i==3: 
                    self.gamePlayer.user_hall = "Gunmere"
                    print "Really?! I'm surprised. Gunmere it is, then!!"
                
                break
  
        if not correctInput:  
            print "Error! Perhaps you made a typo somewhere? "
            self.getUserInput(acceptable_inputs)

       


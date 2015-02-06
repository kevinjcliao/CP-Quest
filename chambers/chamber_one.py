import sys

sys.path.append("../")


class chamber_one: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = [
                "Hearing exactly what's going on next door.", 
                "Being so far off campus you can never engage in campus life.", 
                "Getting attacked by bats, mice, and insects.", 
                "Living in a disgusting wasteland of bodily fluids."
            ]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)
        self.theCurrentGame.slowPrint("Alright then... Let's get started...")        
    
    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("What kind of hall do you like? ")
        print acceptable_inputs

    def getUserInput(self, acceptable_inputs):
        input = raw_input("Choose an answer: ")
        print "Great! You chose: " + input

        for i in range(0,len(self.acceptable_inputs)): 
            if input == self.acceptable_inputs[i]: 
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
  
            else: 
                print "Error"
                self.getUserInput(acceptable_inputs)

       


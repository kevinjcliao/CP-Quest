import sys

sys.path.append("../")

class chamber_two: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = []
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("Customs week is over. From getting " + 
        " soaked and covered in mud during primal" + 
        " scream, to gaining a bit of emotional intimacy" + 
        " during pluralism, its clear that" + 
        " your freshmen had a blast. Now, as the monotony of the semester" +   
        " begins to sink in, two of your freshmen become withdrawn from most activities.")
        self.theCurrentGame.slowPrint("!")

    def getUserInput(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("Hello World!")


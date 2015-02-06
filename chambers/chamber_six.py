import sys

sys.path.append("../")


class chamber_six: 
    def __init__(self, currentGame, currentPlayer): 
        self.gamePlayer = currentPlayer
        self.theCurrentGame = currentGame
        self.acceptable_inputs = ["0: WOW. I do NOT"+\
            " want to deal with this right now." +\
            " Their personal affairs are their" +\
            " business.", 
            "1: I need to promote more hall activities so that they" +\
            " do not feel excluded.", 
            "2: Give them space and see if they want to come for me" +\
            " for help.", 
            "3: Hold a PAF session and announce their troubles to the" +\
            " customs group. After all, customs is about building a" +\
            " family. What family doesn't want to know about all the" +\
            " troubles of its members?"]
        self.printQuestion(self.acceptable_inputs)
        self.getUserInput(self.acceptable_inputs)

    def printQuestion(self, acceptable_inputs): 
        self.theCurrentGame.slowPrint("Episode 5: Post-Winter Break")
        self.theCurrentGame.slowPrint(
                "Winter break has come to an end and your customs" +\
                " group is back on the hall. You notice that two" +\
                " freshmen who were close before are no longer" +\
                " talking to each other and instead are avoiding" +\
                " you. Upon investigation you find out that they" +\
                " were previously in a relationship and just broke" +\
                " up over break! How do you respond?" 
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
                print "You chose: " + input
                
                if i==0: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                        "While your decision may have been driven" +\
                        " by a well-intentioned desire to give them" +\
                        " personal autonomy, their relationship begins" +\
                        " to take a negative toll on the customs group."+\
                        " Individual autonomy is very important, but" +\
                        " sometimes it's important to intervene when the" +\
                        " wellbeing of the hall is at stake."
                        )


                elif i==1: 
                    self.theCurrentGame.aura += 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                            "You decide to hold a movie night in order" +\
                            " to promote hall cohesion. You set up the" +\
                            " schedule in such a way that it allows" +\
                            " both of the former lovers to attend."+\
                            " Although it's very awkward and tense" +\
                            " at times, it provides an opportunity" +\
                            " for them to reintegrate themselves with" +\
                            " other members of the hall. It wasn't the" +\
                            " greatest of your hall experiences, but" +\
                            " your hall is on the path to recovery again."
                        )

                elif i==2: 
                    self.theCurrentGame.aura += 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint(
                            "Rather than ignore your responsibilities" +\
                            " you choose to tell each freshman individually" +\
                            " that you are here as a support person if" +\
                            " necessary. Some time passes, and you are" +\
                            " called upon to mediate conversations every" +\
                            " now and then, but the situation begins to" +\
                            " improve."
                        )

                elif i==3: 
                    self.theCurrentGame.aura -= 1
                    self.gamePlayer.sanity   += 1
                    self.theCurrentGame.slowPrint("Unbelievable. You're"+\
                            " no longer the CP of this hall.")
                    sys.exit()
                
                break
  
        if not correctInput:  
            print "Error! Perhaps you made a typo somewhere? "
            self.getUserInput(acceptable_inputs)

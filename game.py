import random
import sys
import time

sys.path.append('chambers/')
import chamber_one
import chamber_two
import chamber_three
import chamber_four
import chamber_five
import chamber_six
import chamber_seven
import chamber_eight
import chamber_nine


class Game: 
    def __init__(self, player): 
        print "New game created! " + "Hi, " + player.user_name 
        self.gamePlayer = player
        self.aura = 5
        self.academicScore = 5
        self.honorCodeAwareness = 5

    def run(self): 
        self.slowPrint("Let's get started...")
        current_chamber = chamber_one.chamber_one(self, self.gamePlayer)
        current_chamber = chamber_two.chamber_two(self, self.gamePlayer)
        self.inBetweenChambers()
        current_chamber = chamber_three.chamber_three(self, self.gamePlayer)
        self.inBetweenChambers()
        current_chamber = chamber_four.chamber_four(self, self.gamePlayer)
        self.inBetweenChambers()
        current_chamber = chamber_five.chamber_five(self, self.gamePlayer)
        self.inBetweenChambers()
        current_chamber = chamber_six.chamber_six(self, self.gamePlayer)
        self.inBetweenChambers()
        current_chamber = chamber_seven.chamber_seven(self, self.gamePlayer)
        self.inBetweenChambers()
        current_chamber = chamber_eight.chamber_eight(self, self.gamePlayer)
        self.inBetweenChambers()
        current_chamber = chamber_nine.chamber_nine(self, self.gamePlayer)
        self.endGame()

    def slowPrint(self, s): 
        for c in s + '\n': 
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.0005)
        print ""


    def inBetweenChambers(self): 
        self.slowPrint("You hold a PAF Session.")
        if self.aura >= 4: 
            self.slowPrint("It is attended by all freshmen.")
        else: 
            self.slowPrint("Attendance is limited...")


        self.slowPrint("You hold a HCO Session.")
        if self.aura >= 4: 
            self.slowPrint("It is attended by all freshmen.")
            self.honorCodeAwareness+=1
        else: 
            self.slowPrint("Attendance is limited...")
            self.honorCodeAwareness-=1

    def endGame(self): 
        self.slowPrint("Congratulations! You survived a year as a Customs" +\
                " Person at Haverford College! It isn't an easy job, but" +\
                " you made it.")
        if self.honorCodeAwareness >=3: 
            self.slowPrint("Your freshmen demonstrated good understanding" +\
                    " of the honor code through participation in HCO" +\
                    " discussions."
                    )
        else: 
            self.slowPrint("Your freshmen did not demonstrate good" +\
                    " understanding of the honor code through" +\
                    " participation in HCO discussions."
                    )
        if self.aura >= 3: 
            self.slowPrint("Overall, your hall had a good customs experience.")
        else: 
            self.slowPrint("Your hall had an awful customs experience.")

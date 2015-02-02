import users
import game

def main(): 
    player_name = raw_input("What is your name? ")
    player = users.User(player_name)
    print("Hi " + player.user_name+  ", shall we play a game?")
    newGame = game.Game(player.user_name)
    newGame.run()
    print "I get this far"


if __name__ =="__main__":  
    main()

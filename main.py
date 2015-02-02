import users
import game

def main(): 
    player_name = raw_input("What is your name? ")
    player = users.User(player_name)
    print("Hi " + player.user_name+  ", shall we play a game?")
    newGame = game.Game(player)
    newGame.run()
    print "Game Over! "

if __name__ =="__main__":  
    main()

import Player
import menu
import Intro
import globale
import Map

"""
def checkDone(player):
    count = 0

    for i in globale.schiff_Codierung.keys():
        k = player.ownMap.checkSunkShip(i)
        if k[0]:
            count +=1
    if count == 5:
        return True, "Spieler 1" if Player.amZug else "Spieler 2"
"""

def ScoreScreen():
    print(f"Sorry, but {loser} lost.")
    print(f'{"Player 1" if loser != "Player 1" else "Player 2"}, You win!')
    Intro.asciiIntro()

def gameLoop():
    global done
    done = False
    global loser
    loser = ""

    menu.menu()
    
    player1 = Player.Player()
    player1.setOwnMap()
    player1.setEnemyMap()

    player2 = Player.Player()
    player2.setOwnMap()
    player2.setEnemyMap()

    player1.askCheckPlaceShips()
    player1.ownMap.printMap()

    player2.askCheckPlaceShips()
    player2.ownMap.printMap()
    
    while not done:
        while player1.shoot(player2):
            player1.shoot(player2)
            if checkDone():
                done = True
                break

        while player2.shoot(player1):
            player2.shoot(player1)
            if checkDone():
                done = True
                break
  
    
    scoreScreen()
    end()

gameLoop()
import Player
import menu

def gameLoop():
    global done
    done = False

    #menu.menu()
    
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
        while player2.shoot(player1):
            player2.shoot(player1)
        
        if checkDone():
            done == True
    
    scoreScreen()
    end()

gameLoop()
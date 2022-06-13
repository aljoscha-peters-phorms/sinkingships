import Player
import menu

def gameLoop():
    global done
    done = False

    #menu.menu()
    
    p1 = Player.Player()
    p1.setOwnMap()
    p1.setEnemyMap()

    p2 = Player.Player()
    p2.setOwnMap()
    p2.setEnemyMap()

    print("Player 1: Place your ships!")
    p1.askCheckPlaceShips()
    p1.ownMap.printMap()

    print("Player 2: Place your ships!")
    p2.askCheckPlaceShips()
    p2.ownMap.printMap()
    
    while not done:
        while p1.shoot(p2):
            p1.shoot(p2)
        while p2.shoot(p1):
            p2.shoot(p1)
        
        if checkDone():
            done == True
    
    scoreScreen()
    end()

gameLoop()
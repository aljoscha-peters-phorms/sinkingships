import Player
import menu

def gameLoop():
    global done
    done = False

    menu.main()
    
    p1 = Player.Player()
    p1.setOwnMap()
    p1.setEnemyMap()

    p2 = Player.Player()
    p2.setOwnMap()
    p2.setEnemyMap()

    p1.askCheckPlaceShips()
    p2.askCheckPlaceShips()
    
    while not done:
        while p1.shoot():
            p1.shoot()
        while p2.shoot():
            p2.shoot()
        
        if checkDone():
            done == True
    
    scoreScreen()
    end()

gameLoop()
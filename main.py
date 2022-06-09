import Player

def gameLoop():
    done = False
    p1 = Player.Player()
    p1.setOwnMap()
    p1.setEnemyMap()

    p2 = Player.Player()
    p2.setOwnMap()
    p2.setEnemyMap()

    p1.askCheckPlaceShips()
    p2.askCheckPlaceShips()

    while not done: 
        p1.shoot(p2)
        p1.ownMap.printMap()

        p2.shoot(p1)
        p2.ownMap.printMap()


gameLoop()
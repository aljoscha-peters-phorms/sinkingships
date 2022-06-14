from numpy import False_
from Map import Map, clearScreen
from time import sleep
import globale

class Player():

    def __init__(self):
        self.name = ""
        self.ownMap = Map()
        self.enemyMap = Map()
        self.shipPositions = []
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setOwnMap(self):
        self.ownMap.mapDictInit()
    
    def setEnemyMap(self):
        self.enemyMap.mapDictInit()

    def askCheckPlaceShips(self):
        done = False

        while not done:
            self.ownMap.printMap()
            
            print(f"Setz deine Schiffe!")
            for i, j in globale.schiff_Typen.items():
                placementCoord = input(f'Wo willst du {i} (Länge: {j}) setzen: (Antwortformat(a1,b1,c1...h10,i10,j10):bsp: a5)')
                placementOrient = input(f'Wie willst du {i} (Länge: {j}) setzen: (Antwortformat (v: vertikal, h: horizontal): bsp. v)')
            
                if self.ownMap.schiffeSetzen(i, placementCoord, placementOrient):
                    print("Schiff richtig gesetzt")
                    if i == "Carrier":
                        done = True
                        break
                else:
                    print("Schiff falsch gesetzt")
                    sleep(3)
                    clearScreen()
                    self.setOwnMap()
                    done = False
                    break

    def shoot(self, player):
        self.enemyMap.printMap()
        shootPos = input(f"Auf welches Feld willst du schießen: (Antwortformat(a1,b1,c1...h10,i10,j10):bsp: g5)")
        if len(str(player.ownMap.map_dict[shootPos])) > 1:
            print("You already shot there.")
            z = ""
        
        elif player.ownMap.map_dict[shootPos] != 0 or player.ownMap.map_dict[shootPos] != "+" or player.ownMap.map_dict[shootPos] != "-":
            z = "+"
            print("Getroffen!")
            if int(player.ownMap.map_dict[shootPos]) != 0:
                shipType = str(list(globale.schiff_Codierung.keys())[list(globale.schiff_Codierung.values()).index(int(player.ownMap.map_dict[shootPos]))])
                cSS = player.ownMap.checkSunkShip(shipType)
                if cSS[-1][1] == int(player.ownMap.map_dict[shootPos]):
                    print(f"Versenkt, {cSS[-1][1]}")
        else:
            z = "-"
            print("Nicht getroffen.")
        
        self.enemyMap.changeStellen(shootPos, z)
        player.ownMap.appendStellen(shootPos, z)

        if z == "+":
            return True
        return False
    
    def checkSunkShips(self, player):
        sunkShips = []

        for i in globale.schiff_Codierung.keys():
            sunkShips.append(player.ownMap.checkSunkShip(i))

        return sunkShips


"""
p1 = Player()
p1.setOwnMap()
p1.setEnemyMap()

p2 = Player()
p2.setOwnMap()
p2.setEnemyMap()

p1.askCheckPlaceShips()
p1.ownMap.printMap()

p2.askCheckPlaceShips()
p2.ownMap.printMap()

while True:
    while p1.shoot(p2):
        p1.shoot(p2)
    while p2.shoot(p1):
        p2.shoot(p1)
"""
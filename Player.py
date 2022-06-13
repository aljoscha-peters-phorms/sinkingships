from numpy import False_
from Map import Map, clearScreen
from time import sleep
import globale

class Player():
    
    amZug = True

    def __init__(self):
        self.name = ""
        self.ownMap = Map()
        self.enemyMap = Map()
    
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
            p = "Spieler 1" if amZug else "Spieler 2"
            print(f"{p}, Setz deine Schiffe!")
            for i, j in globale.schiff_Typen.items():
                placementCoord = input(f'Wo willst du {i} (Länge: {j}) setzen: (Antwortformat(a1,b1,c1...h10,i10,j10):bsp: a5)')
                placementOrient = input(f'Wie willst du {i} (Länge: {j}) setzen: (Antwortformat (v: vertikal, h: horizontal): bsp. v)')
            
                if self.ownMap.schiffeSetzen(i, placementCoord, placementOrient):
                    print("Schiff richtig gesetzt")
                    if i == "Carrier":
                        amZug = False
                        done = True
                else:
                    print("Schiff falsch gesetzt")
                    sleep(3)
                    clearScreen()
                    self.setOwnMap()
    
    def shoot(self, player):
        self.enemyMap.printMap()
        shootPos = input(f"Auf welches Feld willst du ({p}))schießen: (Antwortformat(a1,b1,c1...h10,i10,j10):bsp: g5)")
        if int(player.ownMap.map_dict[shootPos]) > 0:
            z = "+"
            print("Getroffen!")
        else:
            z = "-"
            print("Nicht getroffen.")
        
        self.enemyMap.changeStellen(shootPos, z)
        player.ownMap.appendStellen(shootPos, z)
        p = True if p == False else True
        
        if z == "+":
            return True
        return False
    
    def checkSunkShips(self):
        pass


"""
p1 = Player()
p1.setOwnMap()
p1.setEnemyMap()

p1.askCheckPlaceShips()
p1.ownMap.printMap()
"""
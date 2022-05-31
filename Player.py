from Map import ownMap, enemyMap, Map, clearScreen
from time import sleep
import globale

class Player():
   
    def __init__(self):
        self.name = ""
        self.ownMap = ownMap()
        self.enemyMap = enemyMap()
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setOwnMap(self):
        self.ownMap.mapDictInit()
    
    def getOwnMap(self):
        self.ownMap.printMap()
    
    def setEnemyMap(self):
        self.enemyMap.mapDictInit()
    
    def getEnemyMap(self):
        self.enemyMap.printMap()
    
    def askCheckPlaceShips(self):
        done = False

        while not done:
            self.ownMap.printMap()
            for i, j in globale.schiff_Typen.items():
                placementCoord = input(f'Wo willst du {i} (Länge: {j}) setzen: (Antwortformat(a1,b1,c1...h10,i10,j10):bsp: a5)')
                placementOrient = input(f'Wie willst du {i} (Länge: {j}) setzen: (Antwortformat (v: vertikal, h: horizontal): bsp. v)')
            
                if self.ownMap.schiffeSetzen(i, placementCoord, placementOrient):
                    print("Schiff richtig gesetzt")
                    if i == "Carrier":
                        done = True
                else:
                    print("Schiff falsch gesetzt")
                    break
                    sleep(3)
                    clearScreen()
                    self.setOwnMap()
                    done = False
    
    def shoot(self, player):
        self.enemyMap.printMap()
        shootPos = input("Auf welches Feld willst du schießen: (Antwortformat(a1,b1,c1...h10,i10,j10):bsp: g5)")
        if self.enemyMap[shootPos] > 0:
            z = "+"
            print("Getroffen!")
        else:
            z = "-"
            print("Nicht getroffen.")
        
        self.enemyMap.changeStellen(shootPos, z)
        player.ownMap.appendStellen(shootPos, z)

class Player1(Player):
    pass

class Player2(Player):
    pass

p1 = Player1()
p1.setOwnMap()
p1.setEnemyMap()

p1.askCheckPlaceShips()
print(p1.ownMap.printMap())
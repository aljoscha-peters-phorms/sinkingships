from Map import ownMap, enemyMap, Map, clearScreen
from time import sleep
import globale

class Player():
   
    def __init__(self):
        self.score = 0
        self.name = ""
        self.ownMap = ownMap()
        self.enemyMap = enemyMap()
    
    def setScore(self, score):
        self.score = score
    
    def getScore(self):
        return self.score
    
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

p1 = Player()
p1.setOwnMap()

p1.askCheckPlaceShips()
print(p1.ownMap.printMap())